---
title: "Connect to Logi Report Server Dialog"
id: 1500009607442
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog
updated_at: 2021-07-24T16:04:57Z
---

# Connect to Logi Report Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630061-Conditional-Formatting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630101-Connect-to-MySQL-Dialog)

# Connect to Logi Report Server Dialog

The Connect to Logi Report Server dialog helps you to specify the connection and user information in order to [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#Remotely) to the server, [download resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#DownReport) from the server, [get global NLS resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files) defined on the server, or import users, groups and roles from the server when editing [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security#Configure). It appears when you want to publish or get resources from a started Logi Report Server but Logi Report Designer cannot set up the connection and log you in automatically.

![Connect to Logi Report Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904386071/cnnct.gif)

The following are details about options in the dialog:

**Connection Information**

Specifies information for connecting to the server.

* **Host**  
   Specifies the host of the remote web server. You can use the host name or the IP address.
* **Port**  
   Specifies the port that the web server listens to. The default is 8888 for the standard server port.
* **Servlet Path**  
   It is /jrserver when using the Logi Report standalone server, and is used in the URL to access the servlet. If you are using an embedded server, for example jreport.jar the servlet path would be /jreport/jrserver.
* **SSL**  
   Abbreviation of Security Socket Layer. Select this option to specify whether to create an SSL connection when the server you are using is integrated with another web server which supports SSL.
* **Remember connection information**  
  Specifies whether or not to allow Logi Report Designer to remember the connection information, so that it can set up the connection automatically when you want to connect to Logi Report Server.

**Login**

Specifies the user name and password for login to the server.

* **User Name**  
   Specifies the user name used to access Logi Report Server. When the Organization feature is enabled on the server and the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.
* **Password**  
   Specifies the password of the user name.
* **Remember login account and password**  
   Specifies whether or not to allow Logi Report Designer to remember the user information, so that it can log you onto the connected server automatically. You cannot use this checkbox if Remember connection information is unselected.

When both the connection and user information is remembered by Logi Report Designer, when you want to connect to the specified Logi Report Server to publish or get resources, Logi Report Designer will set up the connection and log you in automatically. If you want to change the connection and user information to connect to another started server or login using a different user account, you can edit it in the [Server category](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Server) of the Options dialog.

**Connect**

Connects to Logi Report Server.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630061-Conditional-Formatting-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630101-Connect-to-MySQL-Dialog)
