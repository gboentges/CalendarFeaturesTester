import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

######################################
## CLOSING CALENDAR AND LOGGING OFF ##
######################################

print "closing calendar"
print " "

# hit HOME button
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit square button
device.touch(852, 1859, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#hit CLEAR ALL button
device.touch(928, 147, MonkeyDevice.DOWN_AND_UP)
time.sleep(1)

#hit HOME button
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

print "removing account"
print " "

# open settings
device.startActivity(component='com.android.settings/.Settings$AccountSettingsActivity')
time.sleep(4)

# hit search button
device.touch(1028, 128, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#type down accounts
device.type('accounts')
time.sleep(4)

#hit on Accounts button
device.touch(258, 434, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

# hit on Google account
device.touch(277, 263, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Options button
device.touch(1016, 147, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on REMOVE ACCOUNT button
device.touch(732, 260, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on REMOVE ACCOUNT button
device.touch(742, 1071, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

print "closing settings"
print " "

# hit on HOME button
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on square button
device.touch(852, 1859, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on CLEAR ALL button
device.touch(928, 147, MonkeyDevice.DOWN_AND_UP)
time.sleep(1)

# hit on HOME button
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

print "finished!"

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d >> log.txt", shell=True)
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_close.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)