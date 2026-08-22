---
title: "Import from Logi Report Server Dialog Box"
id: 4405661621911
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661621911-Import-from-Logi-Report-Server-Dialog-Box
updated_at: 2022-01-27T20:35:58Z
---

# Import from Logi Report Server Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661619223-Image-Button-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661620887-Imported-SQL-Editor-Dialog-Box)

# Import from Logi Report Server Dialog Box

You can use the Import from Logi Report Server dialog box to [import users, groups, and roles from a started Server](https://devnet.logianalytics.com/hc/en-us/articles/4405661342359-Working-with-RLS-and-CLS-at-Data-Source-Scope#Create) to use in a security policy. This topic describes the options in the dialog box.

Designer displays the Import from Logi Report Server dialog box when you select Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) and select Import from Logi Report Server from the drop-down menu in the Users/Groups/Roles panel of the [Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661696919-Security-Dialog-Box).

![Import from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556154007/imptfrmsrv.gif)

You see the following options in the dialog box:

**Logi Report Server**

Specify the information to connect with the started Server.

* **Host**  
  Specify the host of the Server. You can use the host name or the IP address.
* **Port**  
  Specify the port that the Server listens to. By default, it is 8888.
* **Full Path**  
  It is "/jrserver" if the Server runs in a standalone environment. If the Server is integrated with another application server using jreport.jar for example, the servlet path is "/jreport/jrserver".

**Login**

Specify the user information for signing in to the Server.

* **User Name**  
  Specify the user name to access the Server. When the Organization feature is enabled on the Server and the user is an organization user, User Name should include the organization name. Use "\" to separate the organization name and the user name, for example, "org1\user1".
* **Password**  
  Specify the password of the user name.

**Replace**

If you select this option, when there are users, groups, and roles on the Server with the same names as those on Designer, Designer applies the settings from Server to replace those on Designer. If the names of the users/roles are the same on both Server and Designer, you can use the Server users/roles to override any user-defined ones. You lose the permission settings for user-defined users or roles once they are replaced.

**Merge**

If you select this option, when there are users, groups, and roles on the Server with the same names as those on Designer, Designer maintains the settings from Server and integrates them with the permissions on Designer.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661619223-Image-Button-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661620887-Imported-SQL-Editor-Dialog-Box)
