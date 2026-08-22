---
title: "Server Security System"
id: 5741483732759
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741483732759-Server-Security-System
updated_at: 2022-10-31T17:18:24Z
---

# Server Security System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483705367-Dynamic-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741463552151-Security-System-Data-Model)

# Server Security System

Logi Report Server protects all of the [resources](https://devnet.logianalytics.com/hc/en-us/articles/5741438016279-Managing-Resources) (objects in the resource tree or version tables, such as folders, resources, and archive versions) using a security system. This system maintains a registered set of users and sets permissions on each resource for each user. This topic describes the server security system.

The Logi Report Server implements its runtime security checking system based on a standard set of Security Service method calls. The default implementation is based on the data set of users and resources in Logi Report Server.

For integration with an existing application that already has a system for managing users and permissions, Logi Report Server defines the Security Service as a Java interface and enables a developer to supply a customized version to replace the default implementation. This enables an existing application to provide a custom version of the Security Service that supports Logi Report Server runtime security checking based on user data and permissions that are stored outside Logi Report Server. In this configuration, the Logi Report Server admin section for managing users and permissions is not used.

Logi Report Server also can integrate with an existing application that uses an LDAP system for managing user and group information. Logi Report Server can be configured to interact with the LDAP system so that edit of information about users and groups can be done only in the LDAP system. Information about permissions for resources is not part of the LDAP data model. That information continues to be maintained by Logi Report Server.

Accessing user and permission data by database look-up on each service request may result in many time-consuming IO operations. As a result, the performance of the server security system may be lowered. In order to promote performance, a cache system exists just above the Security Service. The cache system is used to store security objects including users, groups, roles, and access control lists obtained from making calls to the Security Service. This cached data will be used when the same information is needed later.

The following diagram illustrates the Logi Report Server security system structure:

![Security System Structure](https://devnet.logianalytics.com/hc/article_attachments/9905658166551/scrty_rsc_srv.gif)

Select the following links to view the topics:

* [Security System Data Model](https://devnet.logianalytics.com/hc/en-us/articles/5741463552151-Security-System-Data-Model)
* [Multitenancy Supported via Organizations](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations)
* [Role Based Security](https://devnet.logianalytics.com/hc/en-us/articles/5741470433559-Role-Based-Security)
* [Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/5741475703063-Security-Cache-System)
* [Using an LDAP Server's Security System](https://devnet.logianalytics.com/hc/en-us/articles/5741439835159-Using-an-LDAP-Server-s-Security-System)

For more information, see [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/5741363965079-Customized-Implementation-of-the-Security-API) and [Seamless Integrated Security Solution](https://devnet.logianalytics.com/hc/en-us/articles/5741461315351-Seamless-Integrated-Security-Solution).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483705367-Dynamic-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741463552151-Security-System-Data-Model)
