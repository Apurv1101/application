# buildozer.spec
# This file specifies the configuration for building your Kivy Android application
# using Buildozer. Place it in the root directory of your project.

[app]

# (str) Title of your application
title = Face Attendance App

# (str) Package name
package.name = com.example.faceattendanceapp

# (str) Package domain (needed for android/ios packaging)
package.domain = example.com

# (str) Application versioning (usually auto incremented by buildozer)
version = 1.0.0

# (list) Application requirements
# Add all Python packages your app depends on.
# opencv-python-headless is crucial for mobile deployments as it's smaller.
requirements = python3,kivy,opencv-python-headless,numpy,requests,pillow

# (str) Main application file relative to the project root
# If your main file is named 'main.py', Buildozer will find it automatically.
source.dir = .

# (list) List of target machine hardware for which the application is being built
# Currently 'android' is supported.
# For iOS: add 'ios' to the list.
# For desktop: add 'linux', 'win', 'osx'
target.api = 21
min.api = 21 # Minimum Android API level
android.api = 33 # Target Android API level

# (list) Android permissions to request
# CAMERA is essential for your app. INTERNET for Google Forms/email.
# WRITE_EXTERNAL_STORAGE for saving known_faces and emails (though internal storage is better).
# READ_EXTERNAL_STORAGE is often paired with WRITE.
android.permissions = \
    android.permission.CAMERA,\
    android.permission.INTERNET,\
    android.permission.WRITE_EXTERNAL_STORAGE,\
    android.permission.READ_EXTERNAL_STORAGE

# (str) Presplash image (optional)
# This image will be shown briefly when the app starts.
# Place it in your project root, e.g., 'data/presplash.png'
# android.presplash_image = %(source.dir)s/data/presplash.png
# Default presplash is a Kivy logo. You should create your own.
# A simple placeholder:
android.presplash_str = <string>
android.presplash_bg = #000000

# (str) Application icon (optional)
# Place it in your project root, e.g., 'data/icon.png'
# android.icon = %(source.dir)s/data/icon.png
# Default icon is a Kivy logo. You should create your own.

# (list) Exclude folders from packaging.
# Buildozer will include everything by default if not specified.
exclude_dirs = bin, build, dist, .buildozer, venv, __pycache__

# (bool) If set to 1, Buildozer will automatically sign the APK with a debug key.
# For release builds, you'll want to use your own keystore.
debug = 1

# (bool) If set to 1, Buildozer will try to upload the APK to a connected device.
# Not relevant for GitHub Actions.
# android.run = 0

# (str) Release keystore details (for release builds only, replace with your own)
# android.release_keystore = path/to/your/release.keystore
# android.release_keystore_pass = your_keystore_password

# (list) Add any non-Python files (e.g., images, sounds) that your app needs.
# These will be copied into the APK.
# Your app uses 'thank_you.mp3' and 'tick.png'. Ensure these are in your project root
# or adjust the paths here.
source.include_exts = py,png,jpg,mp3,xml

# (str) Full path to the Android SDK directory.
# Not typically needed for GitHub Actions as the runner usually has it pre-configured.
# android.sdk_path = /path/to/android-sdk

# (int) The version of the NDK to use.
# Buildozer usually picks a compatible one, but you can specify.
# android.ndk = 25b

# (bool) Enable AndroidX support. Recommended for modern Android apps.
android.enable_androidx = 1

# (bool) If set to 1, will enable the Android network access in your application.
# Important for `requests` and `smtplib`.
android.internet = 1

# (list) Android features (optional)
# For example: android.features = accelerometer

# (str) Log level for buildozer operations.
log_level = 2

# (bool) If set to 1, forces a clean build. Useful for debugging build issues.
# Do NOT enable this for every build in CI, it slows things down.
# force_build = 0

# (bool) If set to 1, will package the application only as a python package
# (without Android specific stuff).
# Only for advanced use cases where you distribute just the Python code.
# python_only = 0

[buildozer]
# (str) The directory where buildozer stores its internal files.
# Usually '.buildozer' in the project root.
build_dir = .buildozer

# (str) The directory where the final APK/AAB files will be placed.
# Usually 'bin' in the project root.
dist_dir = bin

