---
title: "Server Security System"
id: 1500009692622
section: "Server Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692622-Server-Security-System
updated_at: 2021-11-03T06:56:33Z
---

# Server Security System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692602-Dynamic-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718821-Security-System-Data-Model)

# Server Security System

All of the [resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009717721-Managing-Resources) (objects in the resource tree or version tables, such as folders, resources and archive versions) on Logi JReport Server are protected by the Logi JReport Server security system. This system is based on maintaining a registered set of users and setting permissions on each resource for each user.

The Logi JReport Server runtime security checking system is implemented based on a standard set of Security Service method calls. The default implementation provided in Logi JReport Server is based on the data set of users and resources that is stored in Logi JReport Server.

For integration with an existing application that already has a system for managing users and permissions, Logi JReport Server defines the Security Service as a Java interface and allows for an application developer to supply a customized version to replace the default implementation. This allows an existing application to provide a custom version of the Security Service that supports Logi JReport Server runtime security checking based on user data and permissions that are stored outside of Logi JReport Server. In this configuration, the Logi JReport Server admin section for managing users and permissions is not used.

Logi JReport Server also can integrate with an existing application that uses an LDAP system for managing user and group information. Logi JReport Server can be configured to interact with the LDAP system so that edit of information about users and groups can be done only in the LDAP system. Information about permissions for resources is not part of the LDAP data model. That information continues to be maintained by Logi JReport Server.

Accessing user and permission data by database lookup on each service request may result in many time-consuming IO operations. As a result, the performance of the server security system may be lowered. In order to promote performance, a cache system exists just above the Security Service. The cache system is used to store security objects including users, groups, roles and access control lists obtained from making calls to the Security Service. This cached data will be used when the same information is needed later.

The following is a diagram of the Logi JReport Server security system structure:

![Security System Structure](https://devnet.logianalytics.com/hc/article_attachments/4412131408919/scrty_rsc_srv.gif)

This section contains the following topics about the server security system:

* [Security System Data Model](https://devnet.logianalytics.com/hc/en-us/articles/1500009718821-Security-System-Data-Model)
* [Multi-tenancy Supported via Organizations](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)
* [Role Based Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009718981-Role-Based-Security)
* [Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/1500009692642-Security-Cache-System)
* [Using an LDAP Server's Security System](https://devnet.logianalytics.com/hc/en-us/articles/1500009692702-Using-an-LDAP-Server-s-Security-System)

See also [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009712201-Customized-Implementation-of-the-Security-API) for details about using the Security API to build your preferred security system. For information about security in an integrated environment, see [Seamless Integrated Security Solution](https://devnet.logianalytics.com/hc/en-us/articles/1500009717541-Seamless-Integrated-Security-Solution).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692602-Dynamic-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718821-Security-System-Data-Model)
