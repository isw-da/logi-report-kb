---
title: "Import from Logi JReport Server Dialog"
id: 1500009566382
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566382-Import-from-Logi-JReport-Server-Dialog
updated_at: 2021-07-24T05:55:08Z
---

# Import from Logi JReport Server Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587541-Image-Button-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566402-Incremental-Condition-Dialog)

# Import from Logi JReport Server Dialog

The Import from Logi JReport Server dialog appears when you select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and then select **Import from Logi JReport Server** from the drop-down menu in the Users/Groups/Roles panel of the [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009588521-Security-Dialog) dialog. It helps you to [import users, groups and roles from Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope) to use in the security policy. [See the dialog](javascript:%20void(null)).

![Import from Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893875351/imptfrmsrv.gif)

The following are details about options in the dialog:

**Host**

Specifies the host of the remote web server. You can use the host name or the IP address.

**Port**

Specifies the port that the web server listens to, by default it is 8888. Do not use the Administration port.

**Full path**

If you are using a standalone server it is /jrserver, which is used in the URL to access the servlet. If you are using a server embedded in a Java application it will be the name of the jar file plus jrserver such as /Logi JReport/jrserver.

**User Name**

Specifies the user name used to access Logi JReport Server. When the Organization feature is enabled and when the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.

**Password**

Specifies the password of the user name.

**Replace**

If checked, when there are users, groups and roles on the server with the same names as those on Logi JReport Designer, the setting from the server will replace those on Logi JReport Designer. If the names of the user/role are the same on both the server and Logi JReport Designer, you can use the server users/roles to override any user defined ones. Permission settings for user defined users or roles will be lost once they are replaced.

**Merge**

If checked, when there are users, groups and roles on the server with the same names as those on Logi JReport Designer, the settings from the server will be maintained while being integrated with the permissions from Logi JReport Designer.

**OK**

Imports users, groups and roles from Logi JReport Server and closes the dialog.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587541-Image-Button-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566402-Incremental-Condition-Dialog)
