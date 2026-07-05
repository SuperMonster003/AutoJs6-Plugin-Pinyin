package io.github.supermonster003.autojs6.plugin.pinyin

import android.app.Service
import android.content.Intent
import android.os.Bundle
import android.os.IBinder
import com.huaban.analysis.jieba.CharsDictionaryDatabase
import com.huaban.analysis.jieba.JiebaSegmenter
import com.huaban.analysis.jieba.PhrasesDictionaryDatabase
import org.autojs.autojs.runtime.api.augment.pinyin.Dict
import org.autojs.plugin.common.api.PluginInfo
import org.autojs.plugin.pinyin.api.IPinyinPlugin
import org.autojs.plugin.pinyin.api.PinyinOptionKeys
import org.json.JSONArray
import java.util.regex.Pattern

class PinyinPluginService : Service() {

    private val charsDictDatabase by lazy { CharsDictionaryDatabase.getInstance(applicationContext).database }
    private val phrasesDictDatabase by lazy { PhrasesDictionaryDatabase.getInstance(applicationContext).database }

    override fun onBind(intent: Intent?): IBinder = binder

    override fun onDestroy() {
        runCatching { charsDictDatabase.close() }
        runCatching { phrasesDictDatabase.close() }
        super.onDestroy()
    }

    private val binder = object : IPinyinPlugin.Stub() {
        override fun getInfo(): PluginInfo {
            return pluginInfo(
                name = "Pinyin",
                description = "Pinyin conversion and Jieba segmentation provider for AutoJs6.",
            )
        }

        override fun convert(text: String?, options: Bundle?): String {
            return convertInternal(text.orEmpty(), PinyinOptions.from(options)).toJson()
        }

        override fun simple(text: String?, enableNumericTone: Boolean, enableSegment: Boolean): String {
            val style = if (enableNumericTone) PinyinStyle.TONE2.value else PinyinStyle.NORMAL.value
            return convertInternal(
                hans = text.orEmpty(),
                options = PinyinOptions(style = style, segment = enableSegment),
            ).joinToString("") { row -> row.firstOrNull().orEmpty() }
        }

        override fun fromCodePoint(codePoint: Int): String {
            return fromCodePointInternal(codePoint).orEmpty()
        }

        override fun fromPhrase(phrase: String?): String {
            return fromPhraseInternal(phrase.orEmpty()).toJson()
        }
    }

    private fun convertInternal(hans: String, options: PinyinOptions): List<List<String>> = when {
        hans.isEmpty() -> emptyList()
        options.mode == PinyinMode.SURNAME.value -> surnamePinyin(hans, options)
        else -> {
            val phrases = if (options.segment) segment(hans) else groupChineseAndNonChinese(hans)
            val pinyinList = mutableListOf<List<String>>()
            var nonHans = ""
            for (words in phrases) {
                val firstCharCode = words.codePointAt(0)
                if (fromCodePointInternal(firstCharCode) != null) {
                    if (nonHans.isNotEmpty()) {
                        pinyinList.add(listOf(nonHans))
                        nonHans = ""
                    }
                    val next = when (words.length) {
                        1 -> listOf(singlePinyin(words, options))
                        else -> phrasePinyin(words, options)
                    }
                    if (options.group) {
                        pinyinList.add(groupPhrases(next))
                    } else {
                        pinyinList.addAll(next)
                    }
                } else {
                    nonHans += words
                }
            }
            if (nonHans.isNotEmpty()) {
                pinyinList.add(listOf(nonHans))
            }
            pinyinList
        }
    }

    private fun fromCodePointInternal(codePoint: Int): String? {
        return charsDictDatabase.query(
            "Dict",
            arrayOf("Pinyin"),
            "CodePoint = ?",
            arrayOf(codePoint.toString()),
            null,
            null,
            null,
        ).use { cursor ->
            when {
                cursor.moveToFirst() -> cursor.getString(cursor.getColumnIndexOrThrow("Pinyin"))
                else -> null
            }
        }
    }

    private fun fromPhraseInternal(phrase: String): List<List<String>> {
        val result = mutableListOf<MutableList<String>>()
        phrasesDictDatabase.query(
            "PhrasesDict",
            arrayOf("Pinyin", "OrderIndex"),
            "Word = ?",
            arrayOf(phrase),
            null,
            null,
            "OrderIndex ASC",
        ).use { cursor ->
            while (cursor.moveToNext()) {
                val pinyin = cursor.getString(cursor.getColumnIndexOrThrow("Pinyin"))
                val orderIndex = cursor.getInt(cursor.getColumnIndexOrThrow("OrderIndex"))
                while (result.size < orderIndex) {
                    result.add(mutableListOf())
                }
                result[orderIndex - 1].add(pinyin)
            }
        }
        return result
    }

    private fun segment(hans: String): List<String> {
        return JiebaSegmenter(applicationContext).cutSmall(hans, 4)
    }

    private fun phrasePinyin(phrase: String, options: PinyinOptions): List<List<String>> {
        val phrasePinyinList = fromPhraseInternal(phrase)
        return when {
            phrasePinyinList.isNotEmpty() -> phrasePinyinList.map { item ->
                if (options.heteronym) {
                    item.map { pyItem -> toFixed(pyItem, options.style) }.toMutableList()
                } else {
                    mutableListOf(toFixed(item[0], options.style))
                }
            }.toMutableList()
            else -> phrase.map { ch -> singlePinyin(ch.toString(), options) }
        }
    }

    private fun singlePinyin(han: String, options: PinyinOptions): List<String> {
        require(han.isNotEmpty()) { "Argument han must not be empty" }
        val consulted = fromCodePointInternal(han.codePointAt(0))
        val pinyinList = consulted?.split(",") ?: return listOf(han.first().toString())
        return if (options.heteronym) {
            pinyinList.map { toFixed(it, options.style) }.distinct()
        } else {
            listOf(toFixed(pinyinList.first(), options.style))
        }
    }

    private fun surnamePinyin(hans: String, options: PinyinOptions): List<List<String>> {
        val len = hans.length
        var prefixIndex = 0
        val result = mutableListOf<List<String>>()
        var i = 0
        while (i < len) {
            val twoWords = hans.substring(i, (i + 2).coerceAtMost(len))
            if (!Dict.COMPOUND_SURNAME.containsKey(twoWords)) {
                i++
                continue
            }
            if (prefixIndex < i) {
                result.addAll(singleSurname(hans.substring(prefixIndex, i), options))
            }
            Dict.COMPOUND_SURNAME[twoWords]?.map { toFixedList(it, options) }?.let(result::addAll)
            i += 2
            prefixIndex = i
        }
        if (prefixIndex < len) {
            result.addAll(singleSurname(hans.substring(prefixIndex, len), options))
        }
        return result
    }

    private fun singleSurname(hans: String, options: PinyinOptions): List<List<String>> {
        val result = mutableListOf<List<String>>()
        hans.forEach { char ->
            val word = char.toString()
            Dict.SURNAME[word]?.map { toFixedList(it, options) }?.let {
                result.addAll(it)
            } ?: result.add(singlePinyin(word, options))
        }
        return result
    }

    private fun toFixedList(items: List<String>, options: PinyinOptions): List<String> {
        return items.map { toFixed(it, options.style) }
    }

    private fun toFixed(pinyin: String, style: Int): String = when (style) {
        PinyinStyle.NORMAL.value -> pinyin.replace(RE_PHONETIC_SYMBOL) { match ->
            PHONETIC_SYMBOL[match.groupValues[1]]?.replace(RE_TONE2, "$1") ?: match.value
        }
        PinyinStyle.INITIALS.value -> initials(pinyin)
        PinyinStyle.FIRST_LETTER.value -> pinyin.first().toString()
        PinyinStyle.TONE.value -> pinyin
        PinyinStyle.TONE2.value -> {
            var tone = ""
            val py = pinyin.replace(RE_PHONETIC_SYMBOL) { match ->
                PHONETIC_SYMBOL[match.groupValues[1]]?.let { s ->
                    s.replace(RE_TONE2, "$2").also { tone = it }
                    s.replace(RE_TONE2, "$1")
                } ?: match.value
            }
            py + tone
        }
        PinyinStyle.TO3NE.value -> pinyin.replace(RE_PHONETIC_SYMBOL) { match ->
            PHONETIC_SYMBOL[match.groupValues[1]] ?: match.value
        }
        else -> pinyin
    }

    private fun initials(pinyin: String): String = INITIALS.find { pinyin.startsWith(it) } ?: ""

    private fun groupPhrases(phrases: List<List<String>>): List<String> = when (phrases.size) {
        1 -> phrases[0]
        else -> combo(phrases)
    }

    private fun combo(arr: List<List<String>>): List<String> {
        if (arr.size <= 1) return arr.firstOrNull() ?: emptyList()
        var result = combo2array(arr[0], arr[1])
        for (i in 2 until arr.size) {
            result = combo2array(result, arr[i])
        }
        return result
    }

    private fun combo2array(a1: List<String>, a2: List<String>): List<String> = when {
        a1.isEmpty() -> a2
        a2.isEmpty() -> a1
        else -> a1.flatMap { item1 -> a2.map { item2 -> item1 + item2 } }
    }

    private fun groupChineseAndNonChinese(input: String): List<String> {
        if (input.isEmpty()) return emptyList()
        val result = mutableListOf<String>()
        val chineseRegex = "\\p{IsHan}".toRegex()
        var tempGroup = StringBuilder()
        var isLastChinese = chineseRegex.matches(input[0].toString())
        for (char in input) {
            val isChinese = chineseRegex.matches(char.toString())
            if (isChinese != isLastChinese) {
                result.add(tempGroup.toString())
                tempGroup = StringBuilder()
            }
            tempGroup.append(char)
            isLastChinese = isChinese
        }
        if (tempGroup.isNotEmpty()) {
            result.add(tempGroup.toString())
        }
        return result
    }

    private fun List<List<String>>.toJson(): String {
        val rows = JSONArray()
        forEach { row ->
            rows.put(JSONArray().apply {
                row.forEach(::put)
            })
        }
        return rows.toString()
    }

    private data class PinyinOptions(
        val mode: Int = PinyinMode.NORMAL.value,
        val style: Int = PinyinStyle.TONE.value,
        val segment: Boolean = false,
        val heteronym: Boolean = false,
        val group: Boolean = false,
    ) {
        companion object {
            fun from(bundle: Bundle?): PinyinOptions {
                return PinyinOptions(
                    mode = bundle?.getInt(PinyinOptionKeys.MODE, PinyinMode.NORMAL.value) ?: PinyinMode.NORMAL.value,
                    style = bundle?.getInt(PinyinOptionKeys.STYLE, PinyinStyle.TONE.value) ?: PinyinStyle.TONE.value,
                    segment = bundle?.getBoolean(PinyinOptionKeys.SEGMENT, false) ?: false,
                    heteronym = bundle?.getBoolean(PinyinOptionKeys.HETERONYM, false) ?: false,
                    group = bundle?.getBoolean(PinyinOptionKeys.GROUP, false) ?: false,
                )
            }
        }
    }

    private enum class PinyinStyle(val value: Int) {
        NORMAL(0),
        TONE(1),
        TONE2(2),
        TO3NE(5),
        INITIALS(3),
        FIRST_LETTER(4),
    }

    private enum class PinyinMode(val value: Int) {
        NORMAL(0),
        SURNAME(1),
        PLACE_NAME(2),
        PLACENAME(2),
    }

    private companion object {
        val INITIALS = arrayOf(
            "b", "p", "m", "f", "d", "t", "n", "l",
            "g", "k", "h", "j", "q", "x",
            "zh", "ch", "sh", "r", "z", "c", "s",
        )
        val PHONETIC_SYMBOL = Dict.PHONETIC_SYMBOL
        val RE_PHONETIC_SYMBOL = Pattern.compile("([${PHONETIC_SYMBOL.keys.joinToString("")}])").toRegex()
        val RE_TONE2 = Regex("([aeoiuvnm])([0-4])$")
    }
}
