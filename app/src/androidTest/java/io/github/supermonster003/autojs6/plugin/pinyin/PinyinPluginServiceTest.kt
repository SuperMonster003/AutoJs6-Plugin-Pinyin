package io.github.supermonster003.autojs6.plugin.pinyin

import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.content.pm.PackageInfo
import android.os.Build
import android.os.Bundle
import android.os.IBinder
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.autojs.plugin.common.api.PluginCapabilityKeys
import org.autojs.plugin.pinyin.api.IPinyinPlugin
import org.autojs.plugin.pinyin.api.PinyinOptionKeys
import org.autojs.plugin.pinyin.api.PinyinPluginActions
import org.autojs.plugin.pinyin.api.PinyinPluginIds
import org.autojs.plugin.pinyin.api.PinyinPluginCapabilityKeys
import org.json.JSONObject
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Assert.assertThrows
import org.junit.Test
import org.junit.runner.RunWith
import java.util.concurrent.CountDownLatch
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicReference

@RunWith(AndroidJUnit4::class)
class PinyinPluginServiceTest {

    private val context = InstrumentationRegistry.getInstrumentation().targetContext

    @Test
    fun discoveryBindingMetadataAndEveryBinderMethodRoundTrip() {
        withBoundPlugin { plugin ->
            assertRuntimeInfo(plugin)
            assertStyleMatrix(plugin)

            assertEquals("[[\"zhōng\"],[\"xīn\"]]", plugin.convert("中心", null))
            assertEquals(
                "[[\"zhòng\",\"chóng\"]]",
                plugin.convert("重", options(heteronym = true)),
            )
            assertEquals(
                "[[\"yīnyuè\"],[\"zhòngyào\"]]",
                plugin.convert("音乐重要", options(segment = true, group = true)),
            )
            assertEquals(
                "[[\"shàn\"],[\"tián\"],[\"fāng\"]]",
                plugin.convert("单田芳", options(mode = MODE_SURNAME)),
            )
            assertEquals(
                "[[\"liù\"],[\"ān\"]]",
                plugin.convert("六安", null),
            )
            assertEquals(
                "[[\"lù\"],[\"ān\"]]",
                plugin.convert("六安", options(mode = MODE_PLACE_NAME)),
            )
            assertEquals(
                "[[\"yan2\"],[\"shan1\"]]",
                plugin.convert(
                    "铅山",
                    options(mode = MODE_PLACE_NAME, style = STYLE_TONE2, heteronym = true),
                ),
            )
            assertEquals(
                "[[\"lùān\"],[\"shì\"]]",
                plugin.convert("六安市", options(mode = MODE_PLACE_NAME, group = true)),
            )
            assertEquals(
                plugin.convert("中心", null),
                plugin.convert("中心", options(mode = MODE_PLACE_NAME)),
            )
            assertEquals(
                "[[\"liu2\"],[\"an1\"],[\"shi4\"]]",
                plugin.convert(
                    "六安市",
                    options(
                        mode = MODE_PLACE_NAME,
                        style = STYLE_TONE2,
                        customDictionaryJson = """{"六安":[["liú"],["ān"]],"市":[["shì"]]}""",
                    ),
                ),
            )
            assertEquals(
                "[[\"zhong4xing2\",\"zhong4hang2\",\"chong2xing2\",\"chong2hang2\"]]",
                plugin.convert(
                    "重行",
                    options(
                        style = STYLE_TONE2,
                        heteronym = true,
                        group = true,
                        customDictionaryJson = """{"重行":[["zhòng","chóng"],["xíng","háng"]]}""",
                    ),
                ),
            )
            assertThrows(IllegalArgumentException::class.java) {
                plugin.convert(
                    "重",
                    options(customDictionaryJson = """{"重":[["ZHONG"]]}"""),
                )
            }

            assertEquals("zhong1xin1", plugin.simple("中心", true, false))
            assertEquals("yinyuezhongyao", plugin.simple("音乐重要", false, true))
            assertEquals("zhōng,zhòng", plugin.fromCodePoint("中".codePointAt(0)))
            assertEquals("[[\"chóng\"],[\"qìng\"]]", plugin.fromPhrase("重庆"))

            assertEquals("[]", plugin.convert(null, null))
            assertEquals("", plugin.simple(null, false, false))
            assertEquals("", plugin.fromCodePoint(-1))
            assertEquals("[]", plugin.fromPhrase(null))
            assertEquals("[[\"Auto 😀 \"],[\"zhōng\"],[\"!\"]]", plugin.convert("Auto 😀 中!", null))
        }
    }

    @Test
    fun polyphoneQualityBaselineMatchesExactBinderOutput() {
        val testContext = InstrumentationRegistry.getInstrumentation().context
        val corpus = testContext.assets.open("polyphone-baseline.json")
            .bufferedReader(Charsets.UTF_8)
            .use { reader -> JSONObject(reader.readText()) }
        assertEquals(1, corpus.getInt("schemaVersion"))
        val cases = corpus.getJSONArray("cases")
        assertEquals(15, cases.length())

        withBoundPlugin { plugin ->
            for (index in 0 until cases.length()) {
                val case = cases.getJSONObject(index)
                val actual = plugin.convert(
                    case.getString("input"),
                    options(
                        mode = case.optInt("mode", MODE_NORMAL),
                        segment = case.optBoolean("segment", false),
                        heteronym = case.optBoolean("heteronym", false),
                    ),
                )
                assertEquals(
                    "Polyphone baseline mismatch for ${case.getString("id")}",
                    case.getJSONArray("expected").toString(),
                    actual,
                )
            }
        }
    }

    private fun assertStyleMatrix(plugin: IPinyinPlugin) {
        val expected = linkedMapOf(
            STYLE_TONE to "zhōng",
            STYLE_TONE2 to "zhong1",
            STYLE_TO3NE to "zho1ng",
            STYLE_NORMAL to "zhong",
            STYLE_INITIALS to "zh",
            STYLE_FIRST_LETTER to "z",
        )
        for ((style, output) in expected) {
            assertEquals(
                "Unexpected Binder output for style=$style",
                "[[\"$output\"]]",
                plugin.convert("中", options(style = style)),
            )
        }
    }

    private fun assertRuntimeInfo(plugin: IPinyinPlugin) {
        val info = plugin.info
        val packageInfo = context.packageManager.getPackageInfo(context.packageName, 0)

        assertEquals("Pinyin", info.name)
        assertTrue(info.description?.isNotBlank() == true)
        assertEquals("@raw/plugin_instruction", info.instruction)
        assertEquals("SuperMonster003", info.author)
        assertEquals(PinyinPluginIds.ID, info.id)
        assertEquals(PinyinPluginIds.ENGINE, info.engine)
        assertEquals(PinyinPluginIds.VARIANT_DEFAULT, info.variant)
        assertEquals(packageInfo.versionName.orEmpty(), info.versionName)
        assertEquals(packageInfo.versionCodeCompat(), info.versionCode)
        assertTrue(info.versionDate?.isNotBlank() == true)
        assertTrue(info.supportedAbis.orEmpty().isEmpty())

        val capabilities = requireNotNull(info.capabilities) { "Plugin capabilities are missing" }
        assertEquals(3923, capabilities.getInt(PluginCapabilityKeys.REQUIRES_HOST_VERSION))
        assertTrue(capabilities.getBoolean(PinyinPluginCapabilityKeys.CUSTOM_DICTIONARY_V1))
    }

    private fun options(
        mode: Int = MODE_NORMAL,
        style: Int = STYLE_TONE,
        segment: Boolean = false,
        heteronym: Boolean = false,
        group: Boolean = false,
        customDictionaryJson: String? = null,
    ): Bundle = Bundle().apply {
        putInt(PinyinOptionKeys.MODE, mode)
        putInt(PinyinOptionKeys.STYLE, style)
        putBoolean(PinyinOptionKeys.SEGMENT, segment)
        putBoolean(PinyinOptionKeys.HETERONYM, heteronym)
        putBoolean(PinyinOptionKeys.GROUP, group)
        customDictionaryJson?.let { putString(PinyinOptionKeys.CUSTOM_DICTIONARY_JSON, it) }
    }

    private fun withBoundPlugin(block: (IPinyinPlugin) -> Unit) {
        val discoveryIntent = Intent(PinyinPluginActions.PINYIN)
            .addCategory(PinyinPluginIds.ID)
            .setPackage(context.packageName)
        @Suppress("DEPRECATION")
        val matches = context.packageManager.queryIntentServices(discoveryIntent, 0)
        assertEquals("Pinyin discovery must resolve exactly one service", 1, matches.size)

        val serviceInfo = matches.single().serviceInfo
        val explicitIntent = Intent(discoveryIntent).setComponent(
            ComponentName(serviceInfo.packageName, serviceInfo.name),
        )
        val latch = CountDownLatch(1)
        val binder = AtomicReference<IBinder?>()
        val connection = object : ServiceConnection {
            override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
                binder.set(service)
                latch.countDown()
            }

            override fun onServiceDisconnected(name: ComponentName?) = Unit

            override fun onNullBinding(name: ComponentName?) {
                latch.countDown()
            }

            override fun onBindingDied(name: ComponentName?) {
                latch.countDown()
            }
        }

        assertTrue(
            "Unable to bind the discovered Pinyin service",
            context.bindService(explicitIntent, connection, Context.BIND_AUTO_CREATE),
        )
        try {
            assertTrue("Timed out binding the Pinyin service", latch.await(15, TimeUnit.SECONDS))
            val rawBinder = binder.get()
            assertNotNull("Pinyin service returned a null Binder", rawBinder)
            block(IPinyinPlugin.Stub.asInterface(rawBinder))
        } finally {
            context.unbindService(connection)
        }
    }

    private fun PackageInfo.versionCodeCompat(): Long {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) return longVersionCode
        @Suppress("DEPRECATION")
        return versionCode.toLong()
    }

    private companion object {
        const val STYLE_NORMAL = 0
        const val STYLE_TONE = 1
        const val STYLE_TONE2 = 2
        const val STYLE_INITIALS = 3
        const val STYLE_FIRST_LETTER = 4
        const val STYLE_TO3NE = 5

        const val MODE_NORMAL = 0
        const val MODE_SURNAME = 1
        const val MODE_PLACE_NAME = 2
    }
}
