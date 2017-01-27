# CLIPUSH

Send push notifications to Android devices via the command line.

## Requirements
- Android device or emulator
- Python 2.7

## Usage

1. Android
From the project root, enter into the `PushAndroid` directory and run `./gradlew installDebug` to install the APK on your device. Launch the *Push Me* app on your device and note your __device\_id__. Your __device\_id__ will be shown on screen and printed to the logcat: `adb logcat | grep "device token"`
Your device is now registered to receive push notifications.

2. cli-push
From the project root, enter into the `cli-push` directory and run `python setup.py install`. Now run `cli-push DEVICE_ID "MESSAGE"` - substituting DEVICE\_ID with your __device\_id__ from Step 1 and "MESSAGE" with "Your message to send surrounded in quotes"
