# buildozer.spec
# This file specifies the configuration for building your Kivy Android application
# using Buildozer. Place it in the root directory of your project.

[app]

# (str) Title of your application
title = Face Attendance App

# (str) Package name (should be unique for your app)
package.name = com.faceapp.attendance

# (str) Package domain (e.g., your company's domain in reverse)
package.domain = example.com

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
# Added mp3 for 'thank_you.mp3' and xml for 'haarcascade_frontalface_default.xml'
source.include_exts = py,png,jpg,kv,atlas,mp3,xml

# (list) List of exclusions for directories (bin, build, .buildozer, venv, __pycache__)
source.exclude_dirs = bin, build, .buildozer, venv, __pycache__

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Added necessary packages for your app: opencv-python-headless, numpy, requests, pillow.
# opencv-python-headless is crucial for mobile builds as it's smaller.
requirements = python3,kivy,opencv-python-headless,numpy,requests,pillow

# (str) Presplash image (optional, path relative to source.dir)
# If you have one, uncomment and specify path, e.g., presplash.filename = data/presplash.png
# For now, using a black background with a generic string.
android.presplash_str = Welcome to FaceApp
android.presplash_bg = #000000

# (str) Icon of the application (optional, path relative to source.dir)
# If you have one, uncomment and specify path, e.g., icon.filename = data/icon.png
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions your app needs. Crucial for camera, internet, storage.
# android.permission.CAMERA: For accessing the device's camera.
# android.permission.INTERNET: For submitting data to Google Forms and sending OTP emails.
# android.permission.WRITE_EXTERNAL_STORAGE: For saving known faces and email data (though Kivy's user_data_dir is internal,
# this permission is still sometimes required for broader file system interactions or older Android versions).
# android.permission.READ_EXTERNAL_STORAGE: Paired with WRITE for general file access.
android.permissions = \
    android.permission.CAMERA,\
    android.permission.INTERNET,\
    android.permission.WRITE_EXTERNAL_STORAGE,\
    android.permission.READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# API 33 is a common recent target.
android.api = 33

# (int) Minimum API your APK / AAB will support.
# API 21 (Android 5.0 Lollipop) is a common minimum for modern apps.
android.minapi = 21

# (bool) Enable AndroidX support. Recommended for modern Android apps.
android.enable_androidx = True

# (list) The Android architectures to build for, supporting both 64-bit and 32-bit ARM.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable Android network access for your application (redundant with INTERNET permission but good for clarity).
android.internet = 1

# (bool) If set to 1, Buildozer will automatically sign the APK with a debug key.
# Change to 0 for release builds and use your own keystore.
debug = 1

#
# Buildozer specific
#

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer (default)

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin (default)
