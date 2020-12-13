import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

###################
## CREATE A GOAL ##
###################

print "create a goal"
print " "

# hit on + button
device.touch(978, 1702, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit the goal button
device.touch(978, 1365, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on exercise
device.touch(554, 691, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on work out
device.touch(283, 499, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Once a Week
device.touch(292, 493, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on 30 minutes
device.touch(267, 614, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Evening
device.touch(289, 754, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on submit button
device.touch(983, 421, MonkeyDevice.DOWN_AND_UP)
time.sleep(10)

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
time.sleep(3)

# hit nav bar
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Schedule
device.touch(238, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## SEARCHING FOR GOAL ##
########################

print "searching for goal"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('work')
time.sleep(2)

# hit on submitt
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#################
## EDIT A GOAL ##
#################

print "edit a goal"
print " "

# hit on goal
device.touch(409, 445, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on edit button
device.touch(63, 610, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on goal
device.touch(383, 810, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on 2 sessions
device.touch(267, 676, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on default color
device.touch(223, 1619, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on grape color
device.touch(260, 1228, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on nav bar
device.touch(983, 117, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## SEARCHING FOR GOAL ##
########################

print "searching for goal"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('work')
time.sleep(2)

# hit on submitt
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

##################
## DEFER A GOAL ##
##################

print "defer a goal"
print " "

# hit on goal
device.touch(409, 445, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on DEFER
device.touch(630, 1724, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## SEARCHING FOR GOAL ##
########################

print "searching for goal"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('work')
time.sleep(2)

# hit on submitt
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

##################
## MARK AS DONE ##
##################

print "mark a goal as done"
print " "

# hit on goal
device.touch(409, 445, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on MARK AS DONE
device.touch(893, 1724, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## SEARCHING FOR GOAL ##
########################

print "searching for goal"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('work')
time.sleep(2)

# hit on submitt
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

######################
## MARK AS NOT DONE ##
######################

print "mark a goal as not done"
print " "

# hit on goal
device.touch(409, 445, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on MARK AS DONE
device.touch(893, 1724, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## SEARCHING FOR GOAL ##
########################

print "searching for goal"
print " "

# hit on nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search option
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of reminder
device.type('work')
time.sleep(2)

# hit on submitt
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

###################
## DELETING GOAL ##
###################

print "deleting goal"
print " "

# hit on goal
device.touch(409, 445, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on options
device.touch(1008, 143, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on delete button
device.touch(667, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on options
device.touch(338, 965, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on OK button
device.touch(899, 1128, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d >> log.txt", shell=True)
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_goal.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)