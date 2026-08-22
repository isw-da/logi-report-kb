---
title: "Import from Logi Report Server Dialog Box"
id: 5735551708695
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735551708695-Import-from-Logi-Report-Server-Dialog-Box
updated_at: 2022-11-02T04:37:45Z
---

# Import from Logi Report Server Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735566493591-Image-Button-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735551697943-Imported-SQL-Editor-Dialog-Box)

# Import from Logi Report Server Dialog Box

You can use the Import from Logi Report Server dialog box to [import users, groups, and roles from a started Server](https://devnet.logianalytics.com/hc/en-us/articles/5735527007767-Working-with-RLS-and-CLS-at-Data-Source-Scope#Create) to use in a security policy. This topic describes the options in the dialog box.

Designer displays the Import from Logi Report Server dialog box when you select Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) and select Import from Logi Report Server from the drop-down menu in the Users/Groups/Roles panel of the [Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524608407-Security-Dialog-Box).

![Import from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898479292823/imptfrmsrv.gif)

Designer displays these options:

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735566493591-Image-Button-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735551697943-Imported-SQL-Editor-Dialog-Box)
