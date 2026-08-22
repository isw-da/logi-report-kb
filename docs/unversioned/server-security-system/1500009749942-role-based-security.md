---
title: "Role Based Security"
id: 1500009749942
section: "Server Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749942-Role-Based-Security
updated_at: 2021-07-24T00:47:34Z
---

# Role Based Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778561-Security-Cache-System)

# Role Based Security

In addition to the security system based on users, groups, and roles, Logi Report Server also supports a role-based security system in which you define permissions on roles only, and map users and groups to roles. This topic describes how you can turn on the role-based security system.

To switch to the role-based security system, you can use either of the following two methods:

* In the Server Console, point to **Administration** on the system toolbar, select **Configuration** > **Advanced** on the system toolbar, then select the **Role Based Authorization** option.

  By default, Server does not select the option and applies the security mechanism of setting permissions for users, groups, and roles. If you select the option, Server hides the **Permission Setting UI Displays** option automatically, since it controls UI display and is of no use in the role-based security environment.
* In the **server.properties** file, set **server.rolebased.authorization** to **true**.

  In this case, the following three properties will not take effect since they control UI display of setting user/group/role permissions:

  + server.ui.set\_permissions.group
  + server.ui.set\_permissions.role
  + server.ui.set\_permissions.user

If you enable the role based security system, when you [set permissions for a resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) in the Server Console, Server displays only roles. Role only based security is similar to Java EE security, where the developer assigns roles and during deployment users and groups can be mapped to the roles. So, if you are already using Java EE security, this would be the best method.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778561-Security-Cache-System)
