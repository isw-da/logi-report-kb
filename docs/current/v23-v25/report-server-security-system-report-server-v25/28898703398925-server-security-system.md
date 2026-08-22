---
title: "Server Security System"
id: 28898703398925
section: "Report Server Security System Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898703398925-Server-Security-System
updated_at: 2026-02-26T02:13:50Z
source_host: docs-report.zendesk.com
---
# 
Server Security System

Report Server protects all of the resources (objects in the resource tree or version tables, such as folders, resources, and archive versions) using a security system. This system maintains a registered set of users and sets permissions on each resource for each user. This topic describes the server security system.

The Report Server implements its runtime security checking system based on a standard set of Security Service method calls. The default implementation is based on the data set of users and resources in Report Server.

For integration with an existing application that already has a system for managing users and permissions, Report Server defines the Security Service as a Java interface and enables a developer to supply a customized version to replace the default implementation. This enables an existing application to provide a custom version of the Security Service that supports Report Server runtime security checking based on user data and permissions that are stored outside Report Server. In this configuration, the Report Server admin section for managing users and permissions is not used.

Report Server also can integrate with an existing application that uses an LDAP system for managing user and group information. Report Server can be configured to interact with the LDAP system so that edit of information about users and groups can be done only in the LDAP system. Information about permissions for resources is not part of the LDAP data model. That information continues to be maintained by Report Server.

Accessing user and permission data by database look-up on each service request may result in many time-consuming IO operations. As a result, the performance of the server security system may be lowered. In order to promote performance, a cache system exists just above the Security Service. The cache system is used to store security objects including users, groups, roles, and access control lists obtained from making calls to the Security Service. This cached data will be used when the same information is needed later.

The following diagram illustrates the Report Server security system structure:

Select the following links to view the topics:

- 
                    Security System Data Model
                

- 
                    Multitenancy Supported via Organizations
                

- 
                    Role Based Security
                

- 
                    Security Cache System
                

- 
                    Using an LDAP Server's Security System
                

For more information, see Customized Implementation of the Security API and Seamless Integrated Security Solution.
