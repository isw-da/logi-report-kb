---
title: "Logi JReport Server Security System"
id: 1500011463661
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463661-Logi-JReport-Server-Security-System
updated_at: 2021-07-24T10:39:44Z
---

# Logi JReport Server Security System

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431882-Logi-JReport-Server-Monitor) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463841-Links-in-Report)

# Logi JReport Server Security System

The current users and resources on Logi JReport Server are hosted in an active realm. A user identifies a particular user of Logi JReport Server. Users can be arranged in groups and added with roles so that they can inherit permissions from their parent groups and their roles. The registered users can log onto Logi JReport Server to work with the reports. User accessibility to server resources can be defined using the following models:

* **Privilege**  
   Logi JReport Server offers two types of privileges for users: Publish and Advanced Properties. They allow users to publish resources to Logi JReport Server and view advanced resource properties. When a user/group/role is created, the privileges can be granted to it. Privileges can also be assigned to multiple users/groups/roles at a time.
* **Alias**  
   Logi JReport Server organizes report resources into a resource tree. Aliases are used to provide different resource trees of the Public Reports folder to different users and allow them to see only the resources that they are permitted to see.
* **Permission**  
   Different permissions allows users to perform different operations on the public resources, such as viewing, running, and editing resources, scheduling report running tasks, updating resource status, and granting permissions to other users. Permissions are specified on folders or resources to users/groups/roles. Administrators and the users that have been given the Grant permission can assign permissions to other users.

![Set Permission for New User](https://devnet.logianalytics.com/hc/article_attachments/4404901355159/serversecurity_user.gif)

**LDAP support.** Users and groups from an LDAP system can be imported into the Logi JReport Server security system. In this way, the edition of information about users and groups can be done only in the LDAP system. Information about permissions for resources is not part of the LDAP data model and continues to be maintained by Logi JReport Server.

We will configure the LDAP server in advance to make the following process more efficient.

![Configure LDAP](https://devnet.logianalytics.com/hc/article_attachments/4404901355543/serversecurity_ldap.gif)

**Single Sign On** **(SSO)** is for Logi JReport Server to work with an existing web application more easily. Users only need to login to the web application in order to access Logi JReport Server web pages. Logi JReport Server is able to receive the login information and will not prompt another login dialog to the users and will allow them access to Logi JReport Server web pages.

For more information, see Logi JReport Security System in the *Logi JReport Server User's Guide*.

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431882-Logi-JReport-Server-Monitor) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463841-Links-in-Report)
