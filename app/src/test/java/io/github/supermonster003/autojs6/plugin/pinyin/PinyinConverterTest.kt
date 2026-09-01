package io.github.supermonster003.autojs6.plugin.pinyin

import org.autojs.plugin.pinyin.api.PinyinOptionKeys
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class PinyinConverterTest {

    private val segmentCalls = mutableListOf<String>()

    private val dictionary = FakeDictionary(
        characters = mapOf(
            "中" to "zhōng,zhòng",
            "心" to "xīn",
            "重" to "zhòng,chóng",
            "庆" to "qìng",
            "吕" to "lǚ",
            "阿" to "ā",
            "六" to "liù",
            "安" to "ān",
            "铅" to "qiān,yán",
            "山" to "shān",
            "台" to "tái,tāi",
            "州" to "zhōu",
            "市" to "shì",
            "民" to "mín",
        ),
        phrases = mapOf(
            "中心" to listOf(listOf("zhōng"), listOf("xīn")),
            "重庆" to listOf(listOf("chóng", "zhòng"), listOf("qìng")),
        ),
    )

    private val converter = PinyinConverter(
        dictionary = dictionary,
        segmenter = PinyinSegmenter { hans ->
            segmentCalls += hans
            when (hans) {
                "重庆" -> listOf("重庆")
                "重庆中心" -> listOf("重庆", "中心")
                else -> listOf(hans)
            }
        },
    )

    @Test
    fun sixStylesProduceTheDocumentedOutput() {
        val expected = linkedMapOf(
            PinyinStyle.TONE to "zhōng",
            PinyinStyle.TONE2 to "zhong1",
            PinyinStyle.TO3NE to "zho1ng",
            PinyinStyle.NORMAL to "zhong",
            PinyinStyle.INITIALS to "zh",
            PinyinStyle.FIRST_LETTER to "z",
        )

        for ((style, output) in expected) {
            assertEquals(
                "Unexpected output for $style",
                listOf(listOf(output)),
                converter.convert("中", PinyinOptions(style = style.value)),
            )
        }

        assertEquals(listOf(listOf("")), converter.convert("阿", PinyinOptions(style = PinyinStyle.INITIALS.value)))
        assertEquals(listOf(listOf("lv3")), converter.convert("吕", PinyinOptions(style = PinyinStyle.TO3NE.value)))
    }

    @Test
    fun optionParsingPreservesBundleKeysOverridesAndDefaults() {
        val defaults = PinyinOptions.fromValues(
            intValue = { _, defaultValue -> defaultValue },
            booleanValue = { _, defaultValue -> defaultValue },
        )
        assertEquals(PinyinOptions(), defaults)

        val integers = mapOf(
            PinyinOptionKeys.MODE to PinyinMode.SURNAME.value,
            PinyinOptionKeys.STYLE to PinyinStyle.TONE2.value,
        )
        val booleans = mapOf(
            PinyinOptionKeys.SEGMENT to true,
            PinyinOptionKeys.HETERONYM to true,
            PinyinOptionKeys.GROUP to true,
        )
        val parsed = PinyinOptions.fromValues(
            intValue = { key, defaultValue -> integers[key] ?: defaultValue },
            booleanValue = { key, defaultValue -> booleans[key] ?: defaultValue },
        )

        assertEquals(PinyinMode.SURNAME.value, parsed.mode)
        assertEquals(PinyinStyle.TONE2.value, parsed.style)
        assertTrue(parsed.segment)
        assertTrue(parsed.heteronym)
        assertTrue(parsed.group)
    }

    @Test
    fun heteronymSegmentAndGroupComposePhraseCandidates() {
        val result = converter.convert(
            "重庆",
            PinyinOptions(
                segment = true,
                heteronym = true,
                group = true,
            ),
        )

        assertEquals(listOf("重庆"), segmentCalls)
        assertEquals(listOf(listOf("chóngqìng", "zhòngqìng")), result)
    }

    @Test
    fun segmentCanReturnMultipleWordsWithoutGroupingThemTogether() {
        val result = converter.convert(
            "重庆中心",
            PinyinOptions(
                style = PinyinStyle.NORMAL.value,
                segment = true,
            ),
        )

        assertEquals(listOf(listOf("chong"), listOf("qing"), listOf("zhong"), listOf("xin")), result)
        assertEquals(listOf("重庆中心"), segmentCalls)
    }

    @Test
    fun mixedTextAndUnknownCharactersArePreservedInStableRows() {
        val result = converter.convert("Auto 😀中心!")

        assertEquals(
            listOf(
                listOf("Auto 😀"),
                listOf("zhōng"),
                listOf("xīn"),
                listOf("!"),
            ),
            result,
        )
        assertTrue(segmentCalls.isEmpty())
    }

    @Test
    fun surnameAndSimpleModesUseTheirDedicatedFormattingRules() {
        assertEquals(
            listOf(listOf("ou1"), listOf("yang2")),
            converter.convert(
                "欧阳",
                PinyinOptions(
                    mode = PinyinMode.SURNAME.value,
                    style = PinyinStyle.TONE2.value,
                ),
            ),
        )
        assertEquals("zhong1", converter.simple("中", enableNumericTone = true, enableSegment = false))
        assertEquals("zhong", converter.simple("中", enableNumericTone = false, enableSegment = false))
        assertFalse(segmentCalls.isNotEmpty())
    }

    @Test
    fun directDictionaryQueriesAndEmptyInputHaveStableResults() {
        assertEquals("zhōng,zhòng", converter.fromCodePoint("中".codePointAt(0)))
        assertEquals(listOf(listOf("chóng", "zhòng"), listOf("qìng")), converter.fromPhrase("重庆"))
        assertEquals(emptyList<List<String>>(), converter.fromPhrase("未收录"))
        assertEquals(emptyList<List<String>>(), converter.convert(""))
    }

    @Test
    fun placeNameModeOverridesCuratedReadingsAndFallsBackToNormalText() {
        assertEquals(
            listOf(listOf("liù"), listOf("ān")),
            converter.convert("六安"),
        )
        assertEquals(
            listOf(listOf("lù"), listOf("ān")),
            converter.convert("六安", PinyinOptions(mode = PinyinMode.PLACE_NAME.value)),
        )
        assertEquals(
            listOf(listOf("yan2"), listOf("shan1")),
            converter.convert(
                "铅山",
                PinyinOptions(
                    mode = PinyinMode.PLACE_NAME.value,
                    style = PinyinStyle.TONE2.value,
                    heteronym = true,
                ),
            ),
        )
        assertEquals(
            converter.convert("中心"),
            converter.convert("中心", PinyinOptions(mode = PinyinMode.PLACE_NAME.value)),
        )
        assertEquals(
            listOf(listOf("lùān"), listOf("shì")),
            converter.convert(
                "六安市",
                PinyinOptions(mode = PinyinMode.PLACE_NAME.value, group = true),
            ),
        )
    }

    @Test
    fun placeNameModeUsesLongestMatchBeforeNormalFallback() {
        val longestMatchConverter = PinyinConverter(
            dictionary = dictionary,
            segmenter = PinyinSegmenter { listOf(it) },
            placeNameReadings = linkedMapOf(
                "台州" to listOf("tāi", "zhōu"),
                "台州市" to listOf("tāi", "zhōu", "shì"),
            ),
        )

        assertEquals(
            listOf(listOf("tāizhōushì"), listOf("mín")),
            longestMatchConverter.convert(
                "台州市民",
                PinyinOptions(mode = PinyinMode.PLACE_NAME.value, group = true),
            ),
        )
    }

    @Test
    fun customDictionaryUsesLongestMatchBeforeEveryBuiltInModeAndDoesNotPersist() {
        val customDictionary = linkedMapOf(
            "六" to listOf(listOf("liù")),
            "六安" to listOf(listOf("liú"), listOf("ān")),
            "市" to listOf(listOf("shì")),
        )
        assertEquals(
            listOf(listOf("liu2"), listOf("an1"), listOf("shi4")),
            converter.convert(
                "六安市",
                PinyinOptions(
                    mode = PinyinMode.PLACE_NAME.value,
                    style = PinyinStyle.TONE2.value,
                    customDictionary = customDictionary,
                ),
            ),
        )
        assertEquals(
            listOf(listOf("lù"), listOf("ān")),
            converter.convert("六安", PinyinOptions(mode = PinyinMode.PLACE_NAME.value)),
        )
    }

    @Test
    fun customDictionaryComposesHeteronymsGroupingAndStyleFormatting() {
        val result = converter.convert(
            "重行",
            PinyinOptions(
                style = PinyinStyle.TONE2.value,
                heteronym = true,
                group = true,
                customDictionary = mapOf(
                    "重行" to listOf(
                        listOf("zhòng", "chóng"),
                        listOf("xíng", "háng"),
                    ),
                ),
            ),
        )

        assertEquals(
            listOf(listOf("zhong4xing2", "zhong4hang2", "chong2xing2", "chong2hang2")),
            result,
        )
        assertEquals(
            listOf(listOf("a")),
            converter.convert(
                "阿",
                PinyinOptions(
                    style = PinyinStyle.FIRST_LETTER.value,
                    customDictionary = mapOf("阿" to listOf(listOf("ā"))),
                ),
            ),
        )
    }

    private class FakeDictionary(
        characters: Map<String, String>,
        private val phrases: Map<String, List<List<String>>>,
    ) : PinyinDictionary {

        private val codePoints = characters.mapKeys { (character, _) -> character.codePointAt(0) }

        override fun fromCodePoint(codePoint: Int): String? = codePoints[codePoint]

        override fun fromPhrase(phrase: String): List<List<String>> = phrases[phrase].orEmpty()
    }
}
