---
title: "Role Based Security"
id: 1500009718981
section: "Server Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718981-Role-Based-Security
updated_at: 2021-11-03T06:56:30Z
---

# Role Based Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692642-Security-Cache-System)

# Role Based Security

In addition to the security system based on users, groups and roles, Logi JReport Server also supports a role based security system in which permissions are defined on roles only, and users and groups are mapped to roles.

To switch to the role based security system, you can use either of the following two methods:

* In the Logi JReport Server console, point to **Administration** on the system toolbar, select **Configuration** > **Advanced** on the system toolbar, then check the **Role Based Authorization** option.

  By default, the option is unchecked and the security mechanism of setting permissions for users, groups and roles is applied. If the option is checked, the Permission Setting UI Displays option will be hidden automatically, since it is used to control UI display and is of no use in the role based security environment.
* In the server.properties file, set server.rolebased.authorization to **true**.

  In this case, the following three properties will not take effect since they control UI display of setting user/group/role permissions:

  + server.ui.set\_permissions.group
  + server.ui.set\_permissions.role
  + server.ui.set\_permissions.user

If the role based security system is used, when you [set permissions for a resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) in the server console, there are only roles displayed. Role only based security is similar to Java EE security where the developer assigns roles and during deployment users and groups can be mapped to the roles so if you are already using Java EE security, this would be the best method.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692642-Security-Cache-System)
