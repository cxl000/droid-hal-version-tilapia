# rpm_device is the name of the ported device
%define rpm_device tilapia
# rpm_vendor is used in the rpm space
%define rpm_vendor asus
# Manufacturer and device name to be shown in UI
%define vendor_pretty ASUS
%define device_pretty Nexus 7 GSM (2012)
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 0
%define have_led 1
%include droid-hal-version/droid-hal-version.inc
