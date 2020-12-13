import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

###################
## MOVE CALENDAR ##
###################

print "dragging calendar down"
print " "

# drag down to up
device.drag((530, 1460), (609, 132), 0.5, 50)
time.sleep(3)

########################
## MOVE BACK TO TODAY ##
########################

print "go back to today's date"
print " "

# hit on today
device.touch(886, 122, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

########################
## DROP DOWN CALENDAR ##
########################

print "drop down calendar"
print " "

# hit on month name
device.touch(357, 119, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on month name
device.touch(357, 119, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

print "select a date"
print " "

# hit on a date
device.touch(542, 528, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on today
device.touch(886, 122, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

############################
## CHANGING VIEW TO MONTH ##
############################

print "changing view to month"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Month
device.touch(238, 663, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

######################
## UNMARK BIRTHDAYS ##
######################

print "unmarking birthdays"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit birthday checkbox
device.touch(260, 1517, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on right side of screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

####################
## MARK BIRTHDAYS ##
####################

print "marking birthdays"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit birthday checkbox
device.touch(260, 1517, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on right side of screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#####################
## UNMARK HOLIDAYS ##
#####################

print "unmarking holidays"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit birthday checkbox
device.touch(287, 1640, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on right side of screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

###################
## MARK HOLIDAYS ##
###################

print "marking holidays"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit birthday checkbox
device.touch(287, 1640, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on right side of screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Schedule
device.touch(238, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d >> log.txt", shell=True)
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_other.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)