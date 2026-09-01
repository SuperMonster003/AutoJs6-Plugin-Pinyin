package io.github.supermonster003.autojs6.plugin.pinyin

import org.autojs.plugin.pinyin.api.PinyinCustomDictionaryContract
import org.json.JSONObject
import java.nio.charset.StandardCharsets

internal object PinyinCustomDictionary {

    fun parse(json: String?): Map<String, List<List<String>>> {
        if (json == null) return emptyMap()
        require(json.toByteArray(StandardCharsets.UTF_8).size <= PinyinCustomDictionaryContract.MAX_JSON_BYTES) {
            "pinyin customDictionary exceeds ${PinyinCustomDictionaryContract.MAX_JSON_BYTES} UTF-8 bytes"
        }
        if (json.isBlank()) return emptyMap()
        val source = runCatching { JSONObject(json) }.getOrElse { error ->
            throw IllegalArgumentException("pinyin customDictionary JSON is malformed", error)
        }
        require(source.length() <= PinyinCustomDictionaryContract.MAX_ENTRIES) {
            "pinyin customDictionary exceeds ${PinyinCustomDictionaryContract.MAX_ENTRIES} entries"
        }

        return source.keys().asSequence().toList().sorted().associateWith { key ->
            val rows = source.optJSONArray(key)
                ?: throw IllegalArgumentException("pinyin customDictionary[$key] must be an array of candidate arrays")
            val codePointCount = key.codePointCount(0, key.length)
            require(codePointCount in 1..PinyinCustomDictionaryContract.MAX_KEY_CODE_POINTS) {
                "pinyin customDictionary key length must be between 1 and ${PinyinCustomDictionaryContract.MAX_KEY_CODE_POINTS} code points"
            }
            require(PinyinCustomDictionaryContract.isHanKey(key)) {
                "pinyin customDictionary key must contain Han characters only: $key"
            }
            require(rows.length() == codePointCount) {
                "pinyin customDictionary[$key] must contain exactly $codePointCount rows"
            }

            var combinations = 1
            (0 until rows.length()).map { rowIndex ->
                val candidates = rows.optJSONArray(rowIndex)
                    ?: throw IllegalArgumentException("pinyin customDictionary[$key][$rowIndex] must be an array")
                require(candidates.length() in 1..PinyinCustomDictionaryContract.MAX_CANDIDATES_PER_CODE_POINT) {
                    "pinyin customDictionary[$key][$rowIndex] must contain between 1 and ${PinyinCustomDictionaryContract.MAX_CANDIDATES_PER_CODE_POINT} candidates"
                }
                val parsed = (0 until candidates.length()).map { candidateIndex ->
                    val candidate = candidates.opt(candidateIndex) as? String
                        ?: throw IllegalArgumentException(
                            "pinyin customDictionary[$key][$rowIndex][$candidateIndex] must be a string",
                        )
                    require(PinyinCustomDictionaryContract.isCanonicalSyllable(candidate)) {
                        "pinyin customDictionary[$key][$rowIndex][$candidateIndex] is not a canonical lowercase pinyin syllable"
                    }
                    candidate
                }
                require(parsed.distinct().size == parsed.size) {
                    "pinyin customDictionary[$key][$rowIndex] contains duplicate candidates"
                }
                combinations *= parsed.size
                require(combinations <= PinyinCustomDictionaryContract.MAX_COMBINATIONS_PER_ENTRY) {
                    "pinyin customDictionary[$key] exceeds ${PinyinCustomDictionaryContract.MAX_COMBINATIONS_PER_ENTRY} combinations"
                }
                parsed
            }
        }
    }
}
