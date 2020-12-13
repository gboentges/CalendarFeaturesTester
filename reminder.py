import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

#######################
## CREATE A REMINDER ##
#######################

print "creating a reminder"
print " "

# hit on + button
device.touch(978, 1702, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on reminder button
device.touch(978, 1513, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down reminder
device.type('read')
time.sleep(2)

# select possible name
device.touch(307, 798, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# select possible name
device.touch(363, 549, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Done button
device.touch(969, 140, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Save button
device.touch(969, 140, MonkeyDevice.DOWN_AND_UP)
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

########################
## REMOVING REMINDERS ##
########################

print "unmarking reminders"
print " "

# hit on nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Reminders checkbox
device.touch(238, 1226, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on right side of screen
device.touch(951, 1149, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

print "marking reminders"
print " "

# hit on nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Reminders checkbox
device.touch(238, 1226, MonkeyDevice.DOWN_AND_UP)
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

############################
## SEARCHING FOR REMINDER ##
############################

print "searching for reminder"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('read')
time.sleep(2)

# hit on submitt
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## EDITING A REMINDER ##
########################

print "editing a reminder"
print " "

# hit on reminder
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on edit button
device.touch(78, 392, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Does Not Repeat option
device.touch(278, 689, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on an option
device.touch(250, 852, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Save button
device.touch(990, 137, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

############################
## SEARCHING FOR REMINDER ##
############################

print "searching for reminder"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('read')
time.sleep(2)

# hit on submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

#####################
## MARKING AS DONE ##
#####################

print "mark a reminder as done"
print " "

# hit on reminder
device.touch(467, 413, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on MARK AS DONE button
device.touch(877, 1715, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit the back button
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

############################
## SEARCHING FOR REMINDER ##
############################

print "searching for reminder"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('read')
time.sleep(2)

# hit on submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

#########################
## MARKING AS NOT DONE ##
#########################

print "mark a reminder as not done"
print " "

# hit on reminder
device.touch(467, 413, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on MARK AS NOT DONE button
device.touch(877, 1715, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit the back button
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## SEARCHING REMINDER ##
########################

print "searching reminder"
print " "

# hit the nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit the search button
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type the name of reminder
device.type('read')
time.sleep(2)

# hit the submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#######################
## DELETING REMINDER ##
#######################

print "deleting all future reminder"
print " "

# hit a reminder
device.touch(409, 661, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit the Options button
device.touch(1008, 104, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Delete button
device.touch(667, 127, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Delete All Reminders button
device.touch(415, 991, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on OK button
device.touch(904, 1128, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

print "deleting current reminder"
print " "

# hit a reminder
device.touch(427, 404, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit the Options button
device.touch(999, 138, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit the Delete button
device.touch(696, 123, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit the OK button
device.touch(911, 984, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit the back button
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d >> log.txt", shell=True)
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_reminder.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)