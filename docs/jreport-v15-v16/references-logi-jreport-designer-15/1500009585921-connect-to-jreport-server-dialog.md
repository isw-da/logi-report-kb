---
title: "Connect to JReport Server Dialog"
id: 1500009585921
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog
updated_at: 2021-07-24T05:55:34Z
---

# Connect to JReport Server Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585901-Conditional-Formatting-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564762-Connect-to-MySQL-Dialog)

# Connect to JReport Server Dialog

The Connect to JReport Server dialog helps you to connect to Logi JReport Server in order to [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely) to the server, [download resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009592621-Downloading-Resources-from-Logi-JReport-Server) from the server, [get global NLS resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009568562-Creating-NLS-Property-Files) defined on the server, or [import users, groups and roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security#Server) from the server. [See the dialog](javascript:%20void(null)).

![Connect to Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893818519/connect.gif)

The following are details about options in the dialog:

**Connection Information**

Specifies information for connecting to the server.

* **Host**  
   Specifies the host of the remote web server. You can use the host name or the IP address.
* **Port**  
   Specifies the port that the web server listens to. The default is 8888 for the standard server port. It is not the administration port.
* **Servlet Path**  
   It is /jrserver when using the Logi JReport standalone server, and is used in the URL to access the servlet. If you are using an embedded server, for example Logi JReport.jar the servlet path would be /jreport/jrserver.
* **SSL**  
   Abbreviation of Security Socket Layer. Check this option to specify whether to create an SSL connection when the server you are using is integrated with another web server which supports SSL.
* **Remember connection information**  
   If checked, the connection information will be remembered by Logi JReport Designer, and next time when you open this dialog, the connection information you have specified will be automatically displayed in the dialog.

**Login**

Specifies the user name and password for login to the server.

* **User Name**  
   Specifies the user name used to access Logi JReport Server.
* **Password**  
   Specifies the password of the user name.

**Connect**

Connects to Logi JReport Server.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585901-Conditional-Formatting-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564762-Connect-to-MySQL-Dialog)
