---
title: "Role Based Security"
id: 1500009751381
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751381-Role-Based-Security
updated_at: 2021-07-25T07:18:36Z
---

# Role Based Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751221-Security-Cache-System)

# Role Based Security

In addition to the security system based on users, groups and roles, Logi Report Server also supports a role based security system in which permissions are defined on roles only, and users and groups are mapped to roles.

To switch to the role based security system, you can use either of the following two methods:

* In the Logi Report Server console, point to **Administration** on the system toolbar, select **Configuration** > **Advanced** on the system toolbar, then select the **Role Based Authorization** option.

  By default, the option is unselected and the security mechanism of setting permissions for users, groups and roles is applied. If the option is selected, the Permission Setting UI Displays option will be hidden automatically, since it is used to control UI display and is of no use in the role based security environment.
* In the server.properties file, set server.rolebased.authorization to **true**.

  In this case, the following three properties will not take effect since they control UI display of setting user/group/role permissions:

  + server.ui.set\_permissions.group
  + server.ui.set\_permissions.role
  + server.ui.set\_permissions.user

If the role based security system is used, when you [set permissions for a resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) in the server console, there are only roles displayed. Role only based security is similar to Java EE security where the developer assigns roles and during deployment users and groups can be mapped to the roles so if you are already using Java EE security, this would be the best method.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751221-Security-Cache-System)
