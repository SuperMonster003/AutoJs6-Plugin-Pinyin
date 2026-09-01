package io.github.supermonster003.autojs6.plugin.pinyin

import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.os.Bundle
import android.os.Debug
import android.os.IBinder
import android.os.SystemClock
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.autojs.plugin.pinyin.api.IPinyinPlugin
import org.autojs.plugin.pinyin.api.PinyinPluginActions
import org.autojs.plugin.pinyin.api.PinyinPluginIds
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import java.util.concurrent.CountDownLatch
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicReference

/** Manual evidence harness; CI runs the deterministic service test instead. */
@RunWith(AndroidJUnit4::class)
class PinyinSegmenterBenchmarkTest {

    private val instrumentation = InstrumentationRegistry.getInstrumentation()
    private val context = instrumentation.targetContext

    @Test
    fun reportColdAndWarmSegmentConversionCost() {
        withBoundPlugin { plugin ->
            val input = "音乐重要，重庆银行行长，长孙无忌。".repeat(2)
            val pssBeforeKb = Debug.getPss()
            val heapBefore = usedHeapBytes()

            val coldNanos = measureNanos {
                assertTrue(plugin.simple(input, false, true).isNotEmpty())
            }
            val pssAfterColdKb = Debug.getPss()
            val heapAfterCold = usedHeapBytes()

            val warmNanos = LongArray(WARM_ITERATIONS) {
                measureNanos {
                    assertTrue(plugin.simple(input, false, true).isNotEmpty())
                }
            }.sortedArray()
            val pssAfterWarmKb = Debug.getPss()
            val heapAfterWarm = usedHeapBytes()

            val report = buildString {
                append("SEGMENT_BENCHMARK ")
                append("cold_ms=${coldNanos.toMillis()} ")
                append("warm_median_ms=${warmNanos[WARM_ITERATIONS / 2].toMillis()} ")
                append("warm_min_ms=${warmNanos.first().toMillis()} ")
                append("warm_max_ms=${warmNanos.last().toMillis()} ")
                append("pss_before_kb=$pssBeforeKb ")
                append("pss_after_cold_kb=$pssAfterColdKb ")
                append("pss_after_warm_kb=$pssAfterWarmKb ")
                append("heap_before_bytes=$heapBefore ")
                append("heap_after_cold_bytes=$heapAfterCold ")
                append("heap_after_warm_bytes=$heapAfterWarm ")
                append("input_chars=${input.length} iterations=$WARM_ITERATIONS")
            }
            instrumentation.sendStatus(
                2,
                Bundle().apply { putString("stream", "\n$report\n") },
            )
        }
    }

    private fun measureNanos(block: () -> Unit): Long {
        val start = SystemClock.elapsedRealtimeNanos()
        block()
        return SystemClock.elapsedRealtimeNanos() - start
    }

    private fun usedHeapBytes(): Long {
        val runtime = Runtime.getRuntime()
        return runtime.totalMemory() - runtime.freeMemory()
    }

    private fun Long.toMillis(): String = "%.3f".format(this / 1_000_000.0)

    private fun withBoundPlugin(block: (IPinyinPlugin) -> Unit) {
        val discoveryIntent = Intent(PinyinPluginActions.PINYIN)
            .addCategory(PinyinPluginIds.ID)
            .setPackage(context.packageName)
        @Suppress("DEPRECATION")
        val matches = context.packageManager.queryIntentServices(discoveryIntent, 0)
        assertEquals(1, matches.size)
        val serviceInfo = matches.single().serviceInfo
        val intent = Intent(discoveryIntent).setComponent(ComponentName(serviceInfo.packageName, serviceInfo.name))
        val latch = CountDownLatch(1)
        val binder = AtomicReference<IBinder?>()
        val connection = object : ServiceConnection {
            override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
                binder.set(service)
                latch.countDown()
            }

            override fun onServiceDisconnected(name: ComponentName?) = Unit
        }

        assertTrue(context.bindService(intent, connection, Context.BIND_AUTO_CREATE))
        try {
            assertTrue(latch.await(15, TimeUnit.SECONDS))
            val rawBinder = binder.get()
            assertNotNull(rawBinder)
            block(IPinyinPlugin.Stub.asInterface(rawBinder))
        } finally {
            context.unbindService(connection)
        }
    }

    private companion object {
        const val WARM_ITERATIONS = 9
    }
}
