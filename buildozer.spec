[app]

title = EurApp

package.name = eurApk
package.domain = org.novfensec

# مجلد المشروع (ليس ملف)
source.dir = .

# الملف الرئيسي
source.main = main.py

source.include_exts = py,png,jpg,kv,atlas

# ❌ حذفنا images بالكامل
# source.include_patterns = images/*.png

version = 0.2

requirements = python3, kivy==2.3.1, kivymd, exceptiongroup, asynckivy, asyncgui, materialyoucolor, materialshapes

icon.filename =  %(source.dir)s/images/logo.png

presplash.filename = %(source.dir)s/images/splesh.png

orientation = portrait

android.api = 36
android.minapi = 30
android.archs = arm64-v8a

android.accept_sdk_license = True

android.release_artifact = aab
android.debug_artifact = apk

p4a.branch = develop


[buildozer]
log_level = 2
warn_on_root = 1
