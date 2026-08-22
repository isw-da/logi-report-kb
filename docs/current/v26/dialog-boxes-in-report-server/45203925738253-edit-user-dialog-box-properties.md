---
title: "Edit User Dialog Box Properties"
id: 45203925738253
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203925738253-Edit-User-Dialog-Box-Properties
updated_at: 2026-06-29T20:08:29Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Edit User Dialog Box Properties

This topic describes how you can use the Edit User dialog box to edit a user. 

Server displays the dialog box when an administrator selects a username in the User Name column of the Administration > Security > User page on the Server Console.

Selected Realm

Realm in which the user is.

User Name

Name of the user.

Full Name

Full name for the user.

Description

Specify the description for the user.

E-mail

Specify the email address of the user.

Account Disabled

Select if you want to disable the user account for the time being.

Password Life

Specify the validity period of the password.

- 
Never Expires
 Select if you don't want the password to expire.

- 
Expires in N days
  Specify the number of days during which the password is valid.

Password Length

Specify the length of the password.

- 
Permit Blank
  Select if the password can be blank.

- 
Minimum Length
  Specify the minimum number of characters in the password. The number should be between 0 and 20.

Ask user to change the password after expired

Select if you want to prompt the user to change the password when the user signs in with an expired password.

Ask user to change the password after reset by administrator 

Select if you want to prompt the user to change the password when the user signs in with the password for the first time after the administrator resets it. 

Privileges

Select the privileges you want the user to have:

- 
Publish
  The privilege of publishing resources to Report Server.

- 
Advanced Properties
  The privilege of viewing advanced version properties information, such as catalog connections and report related resources.

- 
Enable Multiple Logins Using the Same Username
 Allows multiple users to log in using this username. Premise: advance-setting - Enable Multiple Users to Login Using the Same User Name is true.

OK

Select to apply any changes you made here and exit the dialog box.

Cancel

Select to close the dialog box without saving any changes.
