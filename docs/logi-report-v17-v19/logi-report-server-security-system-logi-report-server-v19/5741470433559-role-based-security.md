---
title: "Role Based Security"
id: 5741470433559
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741470433559-Role-Based-Security
updated_at: 2022-10-31T17:18:28Z
---

# Role Based Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741475703063-Security-Cache-System)

# Role Based Security

In addition to the security system based on users, groups, and roles, Logi Report Server also supports a role-based security system in which you define permissions on roles only, and map users and groups to roles. This topic describes how you can turn on the role-based security system.

To switch to the role-based security system, you can use either of the following two methods:

* On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Advanced**. Then select **Role Based Authorization**.

  By default, Server does not select the option and applies the security mechanism of setting permissions for users, groups, and roles. If you select the option, Server hides **Permission Setting UI Displays** automatically, since it controls UI display and is of no use in the role-based security environment.
* In the **server.properties** file, set **server.rolebased.authorization** to **true**.

  In this case, the following three properties will not take effect since they control UI display of setting user/group/role permissions:

  + server.ui.set\_permissions.group
  + server.ui.set\_permissions.role
  + server.ui.set\_permissions.user

If you enable the role based security system, when you [set permissions for a resource](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on the Server Console, Server displays only roles. Role only based security is similar to Java EE security, where the developer assigns roles and during deployment users and groups can be mapped to the roles. So, if you are already using Java EE security, this would be the best method.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741475703063-Security-Cache-System)
