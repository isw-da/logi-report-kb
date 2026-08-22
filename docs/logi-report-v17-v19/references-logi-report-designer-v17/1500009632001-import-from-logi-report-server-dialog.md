---
title: "Import from Logi Report Server Dialog"
id: 1500009632001
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009632001-Import-from-Logi-Report-Server-Dialog
updated_at: 2021-07-24T16:04:28Z
---

# Import from Logi Report Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608782-Image-Button-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631981-Imported-SQL-Editor-Dialog)

# Import from Logi Report Server Dialog

This Import from Logi Report Server dialog helps you to [import users, groups and roles from Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security#Create) to use in a security policy. It appears when you select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) and select Import from Logi Report Server from the drop-down menu in the Users/Groups/Roles panel of the [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009633321-Security-Dialog) dialog.

![Import from Logi Report Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904268055/imptfrmsrv.gif)

The following are details about options in the dialog:

**Host**

Specifies the host of the remote web server. You can use the host name or the IP address.

**Port**

Specifies the port that the web server listens to, by default it is 8888.

**Full path**

If you are using a standalone server it is /jrserver, which is used in the URL to access the servlet. If you are using a server embedded in a Java application it will be the name of the jar file plus jrserver such as /jreport/jrserver.

**User Name**

Specifies the user name used to access Logi Report Server. When the Organization feature is enabled on the server and the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.

**Password**

Specifies the password of the user name.

**Replace**

If the option is selected, when there are users, groups and roles on the server with the same names as those on Logi Report Designer, the setting from the server will replace those on Logi Report Designer. If the names of the user/role are the same on both the server and Logi Report Designer, you can use the server users/roles to override any user defined ones. Permission settings for user defined users or roles will be lost once they are replaced.

**Merge**

If the option is selected, when there are users, groups and roles on the server with the same names as those on Logi Report Designer, the settings from the server will be maintained while being integrated with the permissions from Logi Report Designer.

**OK**

Imports users, groups and roles from Logi Report Server and closes the dialog.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608782-Image-Button-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631981-Imported-SQL-Editor-Dialog)
