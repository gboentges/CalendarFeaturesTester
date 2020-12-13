import sys
import os
import time
import commands
import subprocess
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

subprocess.call("..\\..\\platform-tools\\adb.exe logcat -c", shell=True)
device = MonkeyRunner.waitForConnection()

##############################
## SEARCHING FOR INVITATION ##
##############################

print "searching for invitation"
print " "

# hit nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of invitation
device.type('invitation')
time.sleep(2)

# hit submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## VIEWING INVITATION ##
########################

# hit on invitation
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

print "clicking on guest of invitation"
print " "

# hit on guests of invitation
device.touch(475, 1383, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

# hit on back button
device.touch(233, 1839, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

########################
## EDITING INVITATION ##
########################

print "editing an invitation"
print " "

# hit on invitation
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on editing
device.touch(63, 380, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on color
device.touch(193, 728, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on flamingo color
device.touch(278, 1352, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on on Save button
device.touch(978, 137, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on X button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

##############################
## SEARCHING FOR INVITATION ##
##############################

print "searching for invitation"
print " "

# hit nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of invitation
device.type('invitation')
time.sleep(2)

# hit submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

########################
## EDITING INVITATION ##
########################

print "RSVPing MAYBE to invitation"
print " "

# hit on invitation
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on MAYBE button
device.touch(970, 1722, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on X button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

##############################
## CHANGING INVITATION BACK ##
##############################

print "changing invitation back"
print " "

# hit nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of invitation
device.type('invitation')
time.sleep(2)

# hit submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

# hit on invitation
device.touch(298, 271, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on NO button
device.touch(805, 1722, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on editing
device.touch(63, 380, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on color
device.touch(193, 728, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on default color
device.touch(313, 1622, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on on Save button
device.touch(978, 137, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on X button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# hit on back button
device.touch(65, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

############################
## CREATING AN INVITATION ##
############################

print "creating an invitation"
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
device.type('invite')
time.sleep(2)

# hit submit button
device.touch(1001, 1704, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit the Invite People
device.touch(263, 1447, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# type name of event
device.type('gboentges@gmail.com')
time.sleep(3)

# hit submit button
device.touch(1001, 1704, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Add Hangout button
device.touch(978, 1188, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit Save button
device.touch(978, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

##############################
## SEARCHING FOR INVITATION ##
##############################

print "searching for invitation"
print " "

# hit nav bar
device.touch(88, 132, MonkeyDevice.DOWN_AND_UP)
time.sleep(2)

# hit on Search
device.touch(245, 769, MonkeyDevice.DOWN_AND_UP)
time.sleep(4)

# type down name of invitation
device.type('invite')
time.sleep(2)

# hit submit button
device.touch(998, 1692, MonkeyDevice.DOWN_AND_UP)
time.sleep(5)

#########################
## DELETING INVITATION ##
#########################

print "deleting invitation"
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
subprocess.call("..\\..\\platform-tools\\adb.exe logcat -d > log_invitation.txt", shell=True)
#subprocess.call("taskkill /f /im adb.exe", shell=True)