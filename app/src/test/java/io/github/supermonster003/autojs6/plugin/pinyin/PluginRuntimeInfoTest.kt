package io.github.supermonster003.autojs6.plugin.pinyin

import org.autojs.plugin.pinyin.api.PinyinPluginIds
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PluginRuntimeInfoTest {

    @Test
    fun runtimeFieldsPreservePackageMetadataAndCompatibilityContract() {
        val fields = pluginRuntimeFields(
            name = "Pinyin",
            description = "Pinyin test description",
            author = "SuperMonster003",
            id = PinyinPluginIds.ID,
            engine = PinyinPluginIds.ENGINE,
            variant = PinyinPluginIds.VARIANT_DEFAULT,
            versionName = "1.0.1",
            versionCode = 10,
            versionDate = "Sep 1, 2026",
        )

        assertEquals("Pinyin", fields.name)
        assertEquals("Pinyin test description", fields.description)
        assertEquals("@raw/plugin_instruction", fields.instruction)
        assertEquals("SuperMonster003", fields.author)
        assertEquals(PinyinPluginIds.ID, fields.id)
        assertEquals(PinyinPluginIds.ENGINE, fields.engine)
        assertEquals(PinyinPluginIds.VARIANT_DEFAULT, fields.variant)
        assertEquals("1.0.1", fields.versionName)
        assertEquals(10, fields.versionCode)
        assertEquals("Sep 1, 2026", fields.versionDate)
        assertTrue(fields.supportedAbis.isEmpty())
        assertEquals(3923, fields.requiredHostVersion)
    }
}
