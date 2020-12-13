import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

print "starting calendar testing..."
print " "

#####################################
## OPENING CALENDAR AND LOGGING IN ##
#####################################

print "opening calendar"
print " "

# open Calendar App
device.startActivity(component='com.google.android.calendar/com.android.calendar.AllInOneActivity')
time.sleep(20)

# hit on account name
device.touch(136, 649, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

#hit on account name
device.touch(136, 649, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

print "writing down account"
print " "

# writing down account
device.type('ctj784@gmail.com')
time.sleep(4)

# hit on Next button
device.touch(916, 996, MonkeyDevice.DOWN_AND_UP)
time.sleep(7)

# writing down password
device.type('T35t1ng1234')
time.sleep(4)

# hit on Next button
device.touch(901, 1003, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

print "accepting terms and conditions"
print " "

# hit on accept terms and conditions
device.touch(946, 1680, MonkeyDevice.DOWN_AND_UP)
time.sleep(10)

# hit on remove Google Drive sync
device.touch(981, 927, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on ACCEPT
device.touch(946, 1680, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Schedule
device.touch(238, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

print "syncing"
print " "

# hit on options
device.touch(1016, 147, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Refresh button
device.touch(732, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(20)

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log.txt", shell=True)
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_open.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)