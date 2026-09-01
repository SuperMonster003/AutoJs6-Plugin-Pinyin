package io.github.supermonster003.autojs6.plugin.pinyin

import androidx.test.ext.junit.runners.AndroidJUnit4
import org.autojs.plugin.pinyin.api.PinyinCustomDictionaryContract
import org.junit.Assert.assertEquals
import org.junit.Assert.assertThrows
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class PinyinCustomDictionaryTest {

    @Test
    fun parserAcceptsCanonicalBoundedDictionary() {
        assertEquals(
            mapOf(
                "重行" to listOf(
                    listOf("zhòng", "chóng"),
                    listOf("xíng", "háng"),
                ),
            ),
            PinyinCustomDictionary.parse(
                """{"重行":[["zhòng","chóng"],["xíng","háng"]]}""",
            ),
        )
    }

    @Test
    fun parserRejectsMalformedStructureAndNonCanonicalSyllables() {
        listOf(
            "{",
            """{"A":[["a"]]}""",
            """{"重":[["ZHONG"]]}""",
            """{"重":[["zhong2"]]}""",
            """{"重":[["zhòng","zhòng"]]}""",
            """{"重庆":[["chóng"]]}""",
        ).forEach { json ->
            assertThrows("Expected rejection for $json", IllegalArgumentException::class.java) {
                PinyinCustomDictionary.parse(json)
            }
        }
    }

    @Test
    fun parserRejectsCombinationAndUtf8Budgets() {
        val rows = (0 until 3).joinToString(",") {
            "[\"a\",\"b\",\"c\",\"d\",\"e\",\"f\",\"g\"]"
        }
        assertThrows(IllegalArgumentException::class.java) {
            PinyinCustomDictionary.parse("{\"重庆市\":[$rows]}")
        }
        assertThrows(IllegalArgumentException::class.java) {
            PinyinCustomDictionary.parse(
                " ".repeat(PinyinCustomDictionaryContract.MAX_JSON_BYTES + 1),
            )
        }
    }

    @Test
    fun parserRejectsEntryKeyAndCandidateCountBudgets() {
        val tooManyEntries = buildString {
            append('{')
            repeat(PinyinCustomDictionaryContract.MAX_ENTRIES + 1) { index ->
                if (index > 0) append(',')
                append('"')
                appendCodePoint(0x4E00 + index)
                append("\":[[\"a\"]]")
            }
            append('}')
        }
        assertThrows(IllegalArgumentException::class.java) {
            PinyinCustomDictionary.parse(tooManyEntries)
        }

        val tooLongKey = "重".repeat(PinyinCustomDictionaryContract.MAX_KEY_CODE_POINTS + 1)
        val tooManyRows = List(PinyinCustomDictionaryContract.MAX_KEY_CODE_POINTS + 1) { "[\"a\"]" }
            .joinToString(",")
        assertThrows(IllegalArgumentException::class.java) {
            PinyinCustomDictionary.parse("{\"$tooLongKey\":[$tooManyRows]}")
        }

        val tooManyCandidates = List(PinyinCustomDictionaryContract.MAX_CANDIDATES_PER_CODE_POINT + 1) { index ->
            "\"a${('a'.code + index).toChar()}\""
        }.joinToString(",")
        assertThrows(IllegalArgumentException::class.java) {
            PinyinCustomDictionary.parse("{\"重\":[[$tooManyCandidates]]}")
        }
    }
}
