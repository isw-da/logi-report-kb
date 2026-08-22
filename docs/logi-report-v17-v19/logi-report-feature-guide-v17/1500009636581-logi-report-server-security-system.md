---
title: "Logi Report Server Security System"
id: 1500009636581
section: "Logi Report Feature Guide v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009636581-Logi-Report-Server-Security-System
updated_at: 2021-07-24T16:05:41Z
---

# Logi Report Server Security System

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636321-Logi-Report-Server-Monitor) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636301-Links-in-Report)

# Logi Report Server Security System

Logi Report Server protects all of the resources (objects in the resource tree or version tables, such as folders, resources, and archive versions) using a security system. This system is based on maintaining a registered set of users, group, and roles, and setting permissions for them on the resources. This involves administrative operations to register users, group, and roles in the security system, and manage their permissions on different resources.

In the following example, we create the user Jack and assign him the Execute permission on the Public Report\SampleReports folder as a server administrator. When the user Jack logs onto the server, he is able to run reports in the folder.

![Set Permission for New User](https://devnet.logianalytics.com/hc/article_attachments/4404904152087/serversecurity_user.gif)

**LDAP Support**

Logi Report Server also can integrate with an existing application that uses an LDAP system for managing user and group information. Logi Report Server can be configured to interact with the LDAP system so that edit of information about users and groups can be done only in the LDAP system. Information about permissions for resources is not part of the LDAP data model. That information continues to be maintained by Logi Report Server.

In the following example, we configure the LDAP server in advance to make the process more efficient.

![Configure LDAP](https://devnet.logianalytics.com/hc/article_attachments/4404911570583/serversecurity_ldap.gif)

**Single Sign On (SSO)**

SSO is for Logi Report Server to work with an existing web application more easily. Users only need to log onto the web application in order to access Logi Report Server web pages. Logi Report Server is able to receive the login information and will not prompt another login dialog to the users and will allow them access to Logi Report Server web pages.

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636321-Logi-Report-Server-Monitor) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636301-Links-in-Report)
