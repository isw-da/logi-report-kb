---
title: "Import from Report Server Dialog Box"
id: 45190512096013
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190512096013-Import-from-Report-Server-Dialog-Box
updated_at: 2026-04-30T15:13:45Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Import from Report Server Dialog Box

You can use the Import from Report Server dialog box to import users, groups, and roles from a started Server to use in a security policy. This topic describes the options in the dialog box.
    

Designer displays the Import from Report Server dialog box when you select Add  and select Import from Report Server from the drop-down menu in the Users/Groups/Roles panel of the Security dialog box.

Designer displays these options:

Report Server

Specify the information to connect with the started Server.

- 
Host
Specify the host of the Server. You can use the host name or the IP address.

- 
Port
Specify the port that the Server listens to. By default, it is 8888.

- 
Full Path
It is "/jrserver" if the Server runs in a standalone environment. If the Server is integrated with another application server using jreport.jar for example, the servlet path is "/jreport/jrserver". 

Login

Specify the user information for signing in to the Server.

- 
User Name
Specify the user name to access the Server. When the Organization feature is enabled on the Server and the user is an organization user, User Name should include the organization name. Use "\" to separate the organization name and the user name, for example, "org1\user1".

- 
Password
Specify the password of the user name.

Replace

If you select this option, when there are users, groups, and roles on the Server with the same names as those on Designer, Designer applies the settings from Server to replace those on Designer. If the names of the users/roles are the same on both Server and Designer, you can use the Server users/roles to override any user-defined ones. You lose the permission settings for user-defined users or roles once they are replaced.

Merge

If you select this option, when there are users, groups, and roles on the Server with the same names as those on Designer, Designer maintains the settings from Server and integrates them with the permissions on Designer.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
