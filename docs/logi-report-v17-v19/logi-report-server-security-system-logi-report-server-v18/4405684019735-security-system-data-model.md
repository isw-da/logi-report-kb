---
title: "Security System Data Model"
id: 4405684019735
section: "Logi Report Server Security System Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684019735-Security-System-Data-Model
updated_at: 2022-01-27T07:59:49Z
---

# Security System Data Model

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684017687-Server-Security-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690680727-Managing-Realms)

# Security System Data Model

Logi Report Server provides a database to hold registered users and permissions on report resources.
The Server Security Service uses the database to control access at runtime.
This topic describes the basic concepts in the server security system including realm, user, group, role, privilege, permission, and alias.

The following diagram illustrates the data model that the Server Security Service uses:

![Data Model](https://devnet.logianalytics.com/hc/article_attachments/4420453463575/scrty_rsc_srv_dtmdl1.gif)

This shows the inherited relationship among User, Group, and Role.

![Inherited Relationship](https://devnet.logianalytics.com/hc/article_attachments/4420461530775/scrty_rsc_srv_dtmdl2.gif)

**User data model**

The user data model defines users, as well as their membership in groups and roles. By having groups and roles, the system can apply permissions for a set of users with one transaction.

Server defines these entities in the user model:

* **Realm**  
  Realm is an abstract security concept, which hosts the resources and authentication entities on Server. There can be more than one realm on the server and each realm is independent from others. The resources and authentication entities that reside in different realms are different.

  At runtime, only one realm can be active and only the users and resources in the active realm are accessible. A realm is identified by a unique name, which can contain any characters other than forward slash (/) and backward slash (\).

  The authentication entities consist of user accounts, group accounts, and role accounts.
* **User**  
  The user is the primary element of the database. It is a unique name that identifies a particular user of Logi Report Server.

  The Logi Report Server web pages are not accessible until a servlet session is established based on verification and signing in of a registered Logi Report Server user.
  All activity done during the web session will use that user identity when the Security Service is considering access privileges to report resources.

  Logi Report Server comes with two built-in users: admin and guest. Both accounts cannot be deleted, and the "admin" user account cannot be disabled either.
* **Group**  
   The principal group, which represents an organization of user accounts, is available for managing users. Users or groups can be added into a group as its child members, and therefore inherit the resource and folder permissions from the group.
* **Role**  
  Users must have certain user rights and permissions in order to perform tasks on resources. Roles, which represent an aggregate of permissions, help you to efficiently assign the appropriate user rights and permissions to users. Assigning roles to users gives the users all the user rights and permissions of the roles to perform their jobs with. A role can also be assigned to other groups or roles, and thus groups or roles can inherit the permissions of other roles.
  Logi Report Server comes with two built-in role accounts, *administrators* and *everyone*.
  The built-in role accounts cannot be deleted, and the administrators role account cannot be disabled either. Users who have the administrators role are generally referred to as administrators.

**Access control data model**

Access control to report resources is based on this data model:

* **Privilege**  
  Privilege is a mode for managing permissions. It can be used to manage different access permissions unrelated with nodes. Logi Report Server offers these types of privileges for users: Publish and Advanced Properties. Users that are granted the Publish privilege will be able to publish resources to Logi Report Server, while users that have the privilege of Advanced Properties are allowed to view advanced information of version properties such as catalog connections and report related resources.
* **Permission**  
  Permissions, associated with resources that are saved in public folders, are the rules that are granted to users to control their access to the resources.
* **Alias**  
  Logi Report Server organizes file and directories into a Resource Tree. Aliases are used to provide different "views" of a tree for different users to enter the Resource Tree. For example, you may set an alias resource tree (based on the resource tree) for Tanya, so that she can only see the market resource node and thus can directly walk into the report file she is interested in. In summary, an alias is a combination of users and resource nodes.

Select the following links to view the topics:

* [Managing Realms](https://devnet.logianalytics.com/hc/en-us/articles/4405690680727-Managing-Realms)
* [Managing User Accounts](https://devnet.logianalytics.com/hc/en-us/articles/4405684026007-Managing-User-Accounts)
* [Managing Groups](https://devnet.logianalytics.com/hc/en-us/articles/4405684021783-Managing-Groups)
* [Managing Roles](https://devnet.logianalytics.com/hc/en-us/articles/4405684024983-Managing-Roles)
* [Managing Privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405684022807-Managing-Privileges)
* [Managing Aliases](https://devnet.logianalytics.com/hc/en-us/articles/4405684020759-Managing-Aliases)
* [Managing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684017687-Server-Security-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690680727-Managing-Realms)
