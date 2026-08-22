---
title: "Import from JReport Server Dialog"
id: 1500010066841
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066841-Import-from-JReport-Server-Dialog
updated_at: 2021-07-24T10:38:40Z
---

# Import from JReport Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031362-Image-Button-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031382-Incremental-Condition-Dialog)

# Import from JReport Server Dialog

This Import from JReport Server dialog helps you to [import users, groups and roles from Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security#Create) to use in a security policy. It appears when you select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) and select Import from JReport Server from the drop-down menu in the Users/Groups/Roles panel of the [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010067681-Security-Dialog) dialog.

![Import from JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901206679/imptfrmsrv.gif)

The following are details about options in the dialog:

**Host**

Specifies the host of the remote web server. You can use the host name or the IP address.

**Port**

Specifies the port that the web server listens to, by default it is 8888.

**Full path**

If you are using a standalone server it is /jrserver, which is used in the URL to access the servlet. If you are using a server embedded in a Java application it will be the name of the jar file plus jrserver such as /jreport/jrserver.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031362-Image-Button-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031382-Incremental-Condition-Dialog)
