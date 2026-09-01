package io.github.supermonster003.autojs6.plugin.pinyin

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicInteger

class PinyinSegmenterReuseTest {

    @Test
    fun concurrentCallsInitializeOneDelegateAndPreserveEveryResult() {
        val factoryCalls = AtomicInteger()
        val segmentCalls = AtomicInteger()
        val segmenter = ReusablePinyinSegmenter {
            factoryCalls.incrementAndGet()
            PinyinSegmenter { hans ->
                segmentCalls.incrementAndGet()
                listOf(hans.take(2), hans.drop(2))
            }
        }
        val executor = Executors.newFixedThreadPool(8)
        try {
            val results = (0 until 64).map { index ->
                executor.submit<List<String>> {
                    segmenter.segment("音乐$index")
                }
            }
            results.forEachIndexed { index, result ->
                assertEquals(listOf("音乐", index.toString()), result.get(10, TimeUnit.SECONDS))
            }
        } finally {
            executor.shutdownNow()
            assertTrue(executor.awaitTermination(5, TimeUnit.SECONDS))
        }

        assertEquals(1, factoryCalls.get())
        assertEquals(64, segmentCalls.get())
    }
}
