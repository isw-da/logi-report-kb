---
title: "Connect to Report Server Dialog Box"
id: 28897951263117
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897951263117-Connect-to-Report-Server-Dialog-Box
updated_at: 2024-09-30T09:09:19Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Connect to Report Server Dialog Box

You can use the Connect to Report Server dialog box to specify the information to connect and sign in to a started Server, in order to publish resources, download resources, get global NLS resources, or import users, groups, and roles when editing business view security from the Server. This topic describes the options in the dialog box.
    

Designer displays the Connect to Report Server dialog box when you want to publish or get resources from a started Server but Designer cannot set up the connection and sign you in automatically.

Designer displays these options:

Connection Information

You can specify the information for connecting to the Server in this box.

- 
Host
Specify the host of the Server. You can use the host name or the IP address.

- 
Port
Specify the port that the Server listens to. By default, it is 8888.

- 
Servlet Path
It is "/jrserver" if the Server runs in a standalone environment. If the Server is integrated with another application server using jreport.jar for example, the servlet path is "/jreport/jrserver". 

- 
SSL
Abbreviation of Security Socket Layer. Select this option to  create an SSL connection when the Server is integrated with another application server which supports SSL.

- 
Remember connection information
Select to allow Designer to remember the connection information, so that it can set up the connection automatically when you want to connect to the Server the next time. 

Login

You can specify the user name and password for signing in to the Server in this box.

- 
User Name
Specify the user name for accessing the Server. When the Organization feature is enabled on the Server and the user is an organization user, User Name should include the organization name. Use "\" to separate the organization name and the user name, for example, "org1\user1".

- 
Password
Specify the password of the user name.

- 
Remember login account and password
Select to allow Designer to remember the user information, so that it can sign you in to the Server automatically the next time. You cannot select this option if you do not select "Remember connection information".

When both the connection and user information is remembered by Designer, when you want to connect to the specified Server to publish or get resources later, Designer sets up the connection and signs you in automatically. If you want to change the connection and user information to connect to another started Server or signing in using a different user account, you can edit it in the Server category of the Options dialog box. 

Connect

Select to connect and sign in to the specified Server.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
