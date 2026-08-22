---
title: "Server Security System"
id: 5741491720087
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741491720087-Server-Security-System
updated_at: 2022-10-31T17:18:47Z
---

# Server Security System

![](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741491347863-Server-Monitor)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741471985431-Web-Controls)

# Server Security System

Server protects all of the resources (objects in the resource tree or version tables, such as folders, resources, and archive versions) using a security system. This system is based on maintaining a registered set of users, group, and roles, and setting permissions for them on the resources. This involves administrative operations to register users, group, and roles in the security system, and manage their permissions on different resources.

In the following example, we create the user Jack and assign him the Execute permission on the Public Report\SampleReports folder as a Server administrator. When the user Jack logs onto the Server Console, he is able to run reports in the folder.

![Set Permission for New User](https://devnet.logianalytics.com/hc/article_attachments/9905614485399/serversecurity_user.gif)

**LDAP Support**

Server also can integrate with an existing application that uses an LDAP system for managing user and group information. You can configure Server to interact with the LDAP system so that you can edit information about users and groups only in the LDAP system. While information about permissions for resources is not part of the LDAP data model. Server maintains this information.

In the following example, we configure the LDAP server in advance to make the process more efficient.

![Configure LDAP](https://devnet.logianalytics.com/hc/article_attachments/9905576498455/serversecurity_ldap.gif)

**Single Sign-on (SSO)**

SSO is for Server to work with an existing web application more easily. Users only need to sign in to the web application in order to access the Server web pages. Server is able to receive the user information and does not prompt another dialog box to the users for signing in again. Server grants the users access to its web pages.

![](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741491347863-Server-Monitor)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741471985431-Web-Controls)
