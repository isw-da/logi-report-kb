---
title: "Connect to JReport Server Dialog"
id: 1500010029982
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog
updated_at: 2021-07-24T10:39:06Z
---

# Connect to JReport Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064981-Conditional-Formatting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065021-Connect-to-MySQL-Dialog)

# Connect to JReport Server Dialog

The Connect to JReport Server dialog helps you to specify the connection and user information in order to [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely) to the server, [download resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#DownReport) from the server, [get global NLS resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010068941-Creating-NLS-Property-Files) defined on the server, or import users, groups and roles from the server when editing [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security#Configure). It appears when you want to publish or get resources from a started Logi JReport Server but Logi JReport Designer cannot set up the connection and log you in automatically.

![Connect to JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901288215/cnnct.gif)

The following are details about options in the dialog:

**Connection Information**

Specifies information for connecting to the server.

* **Host**  
   Specifies the host of the remote web server. You can use the host name or the IP address.
* **Port**  
   Specifies the port that the web server listens to. The default is 8888 for the standard server port.
* **Servlet Path**  
   It is /jrserver when using the Logi JReport standalone server, and is used in the URL to access the servlet. If you are using an embedded server, for example jreport.jar the servlet path would be /jreport/jrserver.
* **SSL**  
   Abbreviation of Security Socket Layer. Check this option to specify whether to create an SSL connection when the server you are using is integrated with another web server which supports SSL.
* **Remember connection information**  
  Specifies whether or not to allow Logi JReport Designer to remember the connection information, so that it can set up the connection automatically when you want to connect to Logi JReport Server.

**Login**

Specifies the user name and password for login to the server.

* **User Name**  
   Specifies the user name used to access Logi JReport Server. When the Organization feature is enabled and when the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.
* **Password**  
   Specifies the password of the user name.
* **Remember login account and password**  
   Specifies whether or not to allow Logi JReport Designer to remember the user information, so that it can log you onto the connected server automatically. You cannot use this checkbox if Remember connection information is unchecked.

When both the connection and user information is remembered by Logi JReport Designer, when you want to connect to the specified Logi JReport Server to publish or get resources, Logi JReport Designer will set up the connection and log you in automatically. If you want to change the connection and user information to connect to another started server or login using a different user account, you can edit it in the [Server category](https://devnet.logianalytics.com/hc/en-us/articles/1500010031962-Options-Dialog#Server) of the Options dialog.

**Connect**

Connects to Logi JReport Server.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064981-Conditional-Formatting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065021-Connect-to-MySQL-Dialog)
