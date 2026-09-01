package io.github.supermonster003.autojs6.plugin.pinyin

import android.app.Service
import android.content.Intent
import android.os.Bundle
import android.os.IBinder
import com.huaban.analysis.jieba.CharsDictionaryDatabase
import com.huaban.analysis.jieba.JiebaSegmenter
import com.huaban.analysis.jieba.PhrasesDictionaryDatabase
import org.autojs.plugin.common.api.PluginInfo
import org.autojs.plugin.pinyin.api.IPinyinPlugin
import org.json.JSONArray

class PinyinPluginService : Service() {

    // These database helpers are process-wide singletons, so their connections must
    // outlive an individual bound-service lifecycle and remain valid across rebinds.
    private val charsDictDatabase by lazy { CharsDictionaryDatabase.getInstance(applicationContext).database }
    private val phrasesDictDatabase by lazy { PhrasesDictionaryDatabase.getInstance(applicationContext).database }

    private val converter by lazy {
        PinyinConverter(
            dictionary = object : PinyinDictionary {
                override fun fromCodePoint(codePoint: Int): String? {
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

                override fun fromPhrase(phrase: String): List<List<String>> {
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
            },
            segmenter = ReusablePinyinSegmenter {
                val jiebaSegmenter = JiebaSegmenter(applicationContext)
                PinyinSegmenter { hans -> jiebaSegmenter.cutSmall(hans, 4) }
            },
        )
    }

    override fun onBind(intent: Intent?): IBinder = binder

    private val binder = object : IPinyinPlugin.Stub() {
        override fun getInfo(): PluginInfo {
            return pluginInfo(
                name = getString(R.string.app_name),
                description = getString(R.string.plugin_description),
            )
        }

        override fun convert(text: String?, options: Bundle?): String {
            return converter.convert(text.orEmpty(), PinyinOptions.from(options)).toJson()
        }

        override fun simple(text: String?, enableNumericTone: Boolean, enableSegment: Boolean): String {
            return converter.simple(text.orEmpty(), enableNumericTone, enableSegment)
        }

        override fun fromCodePoint(codePoint: Int): String {
            return converter.fromCodePoint(codePoint).orEmpty()
        }

        override fun fromPhrase(phrase: String?): String {
            return converter.fromPhrase(phrase.orEmpty()).toJson()
        }
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
}
