import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

#######################
## CREATING AN EVENT ##
#######################

print "creating an event"
print " "

# Hit the + sign
device.touch(978, 1702, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# Hit the event button
device.touch(978, 1702, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# hit the text option
device.touch(220, 275, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type name of event
device.type('final_exam')
time.sleep(2)

# hit submit button
device.touch(975, 142, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit All-Day option
device.touch(970, 407, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit calendar option
device.touch(410, 524, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# select date
device.touch(637, 1053, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit OK button
device.touch(801, 1485, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Save button
device.touch(978, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

###############################
## CHANGING VIEW OF CALENDAR ##
###############################

print "changing view of calendar:"

print "day"

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Day
device.touch(238, 267, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

print "3 day"

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit 3 Days
device.touch(238, 413, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

print "week"

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Week
device.touch(247, 517, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

print "month"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Month
device.touch(238, 663, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#####################
## REMOVING EVENTS ##
#####################

print "unmarking events"
print " "

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Events checkbox
device.touch(238, 1092, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# click on right side of screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

print "marking events"
print " "

# ht nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Events checkbox
device.touch(238, 1092, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on right hand screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Schedule
device.touch(238, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#########################
## SEARCHING FOR EVENT ##
#########################

print "searching for event"
print " "

# hit nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of event
device.type('final_exam')
time.sleep(2)

# hit submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

######################
## EDITING AN EVENT ##
######################

print "editing an event"
print " "

# hit on event
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on edit button
device.touch(78, 392, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on All Day option
device.touch(970, 407, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Save button
device.touch(990, 137, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on exit button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#########################
## SEARCHING FOR EVENT ##
#########################

print "searching for an event"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of event
device.type('final_exam')
time.sleep(2)

# hit submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

####################
## DELETING EVENT ##
####################

print "deleting event"
print " "

# hit on event
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on Options
device.touch(993, 130, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Delete button
device.touch(635, 140, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on OK button
device.touch(919, 999, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 140, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d >> log.txt", shell=True)
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_event.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)