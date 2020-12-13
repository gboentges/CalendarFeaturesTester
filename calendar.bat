echo off
title Testing Features of Google Calendar
:: Gabriela Boentges
:: ctj784
:: Project II

:: Open Calendar and sign in with account
call monkeyrunner.bat open.py

:: Test small features of Calendar
call monkeyrunner.bat other.py

:: Test events of Calendar
call monkeyrunner.bat event.py

:: Test event invitations of Calendar
call monkeyrunner.bat invitation.py

:: Test reminders of Calendar
call monkeyrunner.bat reminder.py

:: Test goals of Calendar
call monkeyrunner.bat goal.py

:: Closing Calendar and removing account
call monkeyrunner.bat close.py