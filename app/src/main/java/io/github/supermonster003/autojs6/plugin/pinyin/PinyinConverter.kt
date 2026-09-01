package io.github.supermonster003.autojs6.plugin.pinyin

import android.os.Bundle
import org.autojs.autojs.runtime.api.augment.pinyin.Dict
import org.autojs.plugin.pinyin.api.PinyinOptionKeys
import java.util.regex.Pattern

internal interface PinyinDictionary {
    fun fromCodePoint(codePoint: Int): String?
    fun fromPhrase(phrase: String): List<List<String>>
}

internal fun interface PinyinSegmenter {
    fun segment(hans: String): List<String>
}

internal class ReusablePinyinSegmenter(
    factory: () -> PinyinSegmenter,
) : PinyinSegmenter {

    private val delegate by lazy(LazyThreadSafetyMode.SYNCHRONIZED, factory)

    override fun segment(hans: String): List<String> = delegate.segment(hans)
}

internal data class PinyinOptions(
    val mode: Int = PinyinMode.NORMAL.value,
    val style: Int = PinyinStyle.TONE.value,
    val segment: Boolean = false,
    val heteronym: Boolean = false,
    val group: Boolean = false,
) {
    companion object {
        fun from(bundle: Bundle?): PinyinOptions {
            return fromValues(
                intValue = { key, defaultValue -> bundle?.getInt(key, defaultValue) ?: defaultValue },
                booleanValue = { key, defaultValue -> bundle?.getBoolean(key, defaultValue) ?: defaultValue },
            )
        }

        internal fun fromValues(
            intValue: (key: String, defaultValue: Int) -> Int,
            booleanValue: (key: String, defaultValue: Boolean) -> Boolean,
        ): PinyinOptions {
            return PinyinOptions(
                mode = intValue(PinyinOptionKeys.MODE, PinyinMode.NORMAL.value),
                style = intValue(PinyinOptionKeys.STYLE, PinyinStyle.TONE.value),
                segment = booleanValue(PinyinOptionKeys.SEGMENT, false),
                heteronym = booleanValue(PinyinOptionKeys.HETERONYM, false),
                group = booleanValue(PinyinOptionKeys.GROUP, false),
            )
        }
    }
}

internal enum class PinyinStyle(val value: Int) {
    NORMAL(0),
    TONE(1),
    TONE2(2),
    TO3NE(5),
    INITIALS(3),
    FIRST_LETTER(4),
}

internal enum class PinyinMode(val value: Int) {
    NORMAL(0),
    SURNAME(1),
    PLACE_NAME(2),
}

internal class PinyinConverter(
    private val dictionary: PinyinDictionary,
    private val segmenter: PinyinSegmenter,
    placeNameReadings: Map<String, List<String>> = PlaceNameReadings.ALL,
) {

    private val placeNamesByFirstCodePoint = placeNameReadings.entries
        .groupBy { (name, _) -> name.codePointAt(0) }
        .mapValues { (_, entries) ->
            entries.sortedWith(
                compareByDescending<Map.Entry<String, List<String>>> { it.key.length }
                    .thenBy { it.key },
            )
        }

    fun convert(hans: String, options: PinyinOptions = PinyinOptions()): List<List<String>> = when {
        hans.isEmpty() -> emptyList()
        options.mode == PinyinMode.SURNAME.value -> surnamePinyin(hans, options)
        options.mode == PinyinMode.PLACE_NAME.value -> placeNamePinyin(hans, options)
        else -> normalPinyin(hans, options)
    }

    private fun normalPinyin(hans: String, options: PinyinOptions): List<List<String>> {
        val phrases = if (options.segment) segmenter.segment(hans) else groupChineseAndNonChinese(hans)
        val pinyinList = mutableListOf<List<String>>()
        var nonHans = ""
        for (words in phrases) {
            if (words.isEmpty()) continue
            val firstCharCode = words.codePointAt(0)
            if (fromCodePoint(firstCharCode) != null) {
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
        return pinyinList
    }

    private fun placeNamePinyin(hans: String, options: PinyinOptions): List<List<String>> {
        val result = mutableListOf<List<String>>()
        val fallbackOptions = options.copy(mode = PinyinMode.NORMAL.value)
        var unmatchedStart = 0
        var index = 0
        while (index < hans.length) {
            val matched = longestPlaceNameAt(hans, index)
            if (matched == null) {
                index += Character.charCount(hans.codePointAt(index))
                continue
            }

            if (unmatchedStart < index) {
                result.addAll(normalPinyin(hans.substring(unmatchedStart, index), fallbackOptions))
            }
            val fixed = matched.value.map { syllable -> listOf(toFixed(syllable, options.style)) }
            if (options.group) {
                result.add(groupPhrases(fixed))
            } else {
                result.addAll(fixed)
            }
            index += matched.key.length
            unmatchedStart = index
        }
        if (unmatchedStart < hans.length) {
            result.addAll(normalPinyin(hans.substring(unmatchedStart), fallbackOptions))
        }
        return result
    }

    private fun longestPlaceNameAt(hans: String, index: Int): Map.Entry<String, List<String>>? {
        val firstCodePoint = hans.codePointAt(index)
        return placeNamesByFirstCodePoint[firstCodePoint]
            ?.firstOrNull { (name, _) -> hans.startsWith(name, index) }
    }

    fun simple(hans: String, enableNumericTone: Boolean, enableSegment: Boolean): String {
        val style = if (enableNumericTone) PinyinStyle.TONE2.value else PinyinStyle.NORMAL.value
        return convert(
            hans = hans,
            options = PinyinOptions(style = style, segment = enableSegment),
        ).joinToString("") { row -> row.firstOrNull().orEmpty() }
    }

    fun fromCodePoint(codePoint: Int): String? = dictionary.fromCodePoint(codePoint)

    fun fromPhrase(phrase: String): List<List<String>> = dictionary.fromPhrase(phrase)

    private fun phrasePinyin(phrase: String, options: PinyinOptions): List<List<String>> {
        val phrasePinyinList = fromPhrase(phrase)
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
        val consulted = fromCodePoint(han.codePointAt(0))
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
                PHONETIC_SYMBOL[match.groupValues[1]]?.let { symbol ->
                    symbol.replace(RE_TONE2, "$2").also { tone = it }
                    symbol.replace(RE_TONE2, "$1")
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
