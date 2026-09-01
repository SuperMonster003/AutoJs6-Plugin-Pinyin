#!/bin/sh

set -eu

target_package="io.github.supermonster003.autojs6.plugin.pinyin"
test_package="${target_package}.test"
target_apk="ci-apks/debug/app-debug.apk"
test_apk="ci-apks/androidTest/debug/app-debug-androidTest.apk"

cleanup() {
  adb uninstall "${test_package}" >/dev/null 2>&1 || true
  adb uninstall "${target_package}" >/dev/null 2>&1 || true
}
trap cleanup 0

test -f "${target_apk}"
test -f "${test_apk}"
adb install -r -t "${target_apk}"
adb install -r -t "${test_apk}"

output="$(adb shell am instrument -w -r \
  -e class io.github.supermonster003.autojs6.plugin.pinyin.PinyinPluginServiceTest \
  "${test_package}/androidx.test.runner.AndroidJUnitRunner")"
printf '%s\n' "${output}"
printf '%s\n' "${output}" | grep -F "OK (2 tests)"
