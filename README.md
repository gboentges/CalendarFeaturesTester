# CalendarFeaturesTester
This is the Google Calendar Features tester. To setup the testing of Google Calendar, you simple place all files currently in folder 
in the same path as monkeyrunner.
To start the testing, you simply execute the command of calendar.bat on the Home Page of Pixel 2 emulator.
The script will be printing out lines in the Command Prompt of the different tests it is performing on the emulator, 
while at the same time writing the log of system messages on individual in different files.
You will find individual log files written for each python script being performed in calendar.bat and a log.txt file that will
have the system messages from all the scripts together in chronological order.

The testing is done with the assumption that no other accounts are currently open and/or active on the phone. 
Besides that, all Apps currently open need to be closed before the testing starts. 
The Calendar App also needs to have turned on both Calendar and Contacts permissions, and the Location and Phone permissions are to 
be turned off. These are all located in the Apps section of Phone Settings.

The testing will be in charge of connecting to an account in Google, testing out all the features of Google Calendar, and the cleaning 
out everything in the aftermath of the testing. This way the script can be executed multitple times with little to no changes 
in the emulator.