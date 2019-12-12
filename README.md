# BuildAndroid

A handy tool for those who either want to be a build bot, or those who want a hassle free method of learning to build.

* What this is:
  - A way of learning the fundamentals of compiling Android.
  - A glimpse of what it is like to compile an Android ROM.
  - A way of simplifying builds for those who already know how to compile Android.

* What this is not:
  - A start-to-finish automatic build script.
    - You will need to do some inital configuration. This means the process is not automatic from the word go. You can NOT just install Linux, run this script and expect it to compile Android. This README.md contains all the steps required to achieve a compilation.
  - An in-depth guide to mastering Android, and becoming a ROM wizard.
  - The be-all or end-all of Android ROM compilation.

### Table of Contents
1. [Introduction](#Introduction)
2. [Recommended System Requirements](#RecSysReq)
3. [Enabling CCACHE](#EnableCCACHE)

## Introduction <a name="Introduction"></a>

To keep things simple, I will refer to LineageOS as LOS in certain places.

BuildAndroid has been developed to teach people how to build android, while also doubling up as a simple script that can be edited, to automate the android build process.

For the sake of simplicity on my part, this script will build [LineageOS v17](https://lineageos.org/) (formally CyanogenMOD) from the repo located [here](https://github.com/lineageos). It will use the manifest branch `lineage-17.0` which is LOS's Android 10. It will try to stay as LineageOS based as possible, requiring 3rd party `trees` where necessary. The device it will build for is Blueline (Google Pixel 3). You may notice references to Crosshatch (Google Pixel 3 XL), this is because Blueline and Crosshatch are `unified trees`.

For reference of what will be cloned to your drive, see:
1. [Blueline Device Tree](https://github.com/LineageOS/android_device_google_blueline) (cloned to device/google/blueline)
2. [Crosshatch Device Tree](https://github.com/LineageOS/android_device_google_crosshatch) (cloned to device/google/crosshatch)
3. [Crosshatch-sepolicy](https://android.googlesource.com/device/google/crosshatch-sepolicy) (cloned to device/google/crosshatch-sepolicy)
4. [Kernel](https://github.com/LineageOS/android_kernel_google_msm-4.9) (cloned to kernel/google/msm-4.9)
5. [Google Vendor](https://github.com/themuppets/proprietary_vendor_google) (cloned to vendor/google)
6. [Google Apps](https://gitlab.com/shagbag913/vendor_gapps) (cloned to vendor/gapps)
7. [Audio](https://github.com/LineageOS/android_hardware_qcom_audio) (cloned to hardware/qcom/audio)
8. [ipacfg-mgr](https://android.googlesource.com/platform/hardware/qcom/sdm845/data/ipacfg-mgr) (cloned to hardware/qcom/data/ipacfg-mgr)

## Recommended System Requirements <a name="RecSysReq"></a>

* RAM
  - 16GB for new devices / Android 10.
  - 8GB for modern devices / Android 9.
* DISK SPACE
  - 200GB to be safe.
  - This is dependent on the amount of ROMs you are building. Head for around 200GB +- each ROM.
* CPU
  - MINIMUM quad core - that goes without saying. More cores = more threads = faster build times.
* SWAP
  - MINIMUM 30GB.
  
You should also ensure that CCACHE is enabled. CCACHE makes subsequent build times so much shorter. We're talking... 5 hours down to 1 hour. It's worth it, if you can spare the disk space. See [Enabling CCACHE](#EnableCCACHE).

## Enabling CCACHE <a name="EnableCCACHE"></a>

`export USE_CCACHE=1` and listen to some music. If you like dubstep, I recommend [this playlist](https://open.spotify.com/playlist/5f3M8DsWZG5IuuOuu9ws3u?si=x1T0F25KR7KimbBNM0qA7w)
