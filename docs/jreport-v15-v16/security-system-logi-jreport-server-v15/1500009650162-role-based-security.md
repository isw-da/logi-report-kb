---
title: "Role Based Security"
id: 1500009650162
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650162-Role-Based-Security
updated_at: 2021-07-24T20:53:38Z
---

# Role Based Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650042-Security-Cache-System)

# Role-Based Security

In addition to the security system based on users, groups and roles, Logi JReport Server also supports a role based security system in which permissions are defined on roles only, and users and groups are mapped to roles.

To switch to the role based security system, you can use either of the following two methods:

* Check the **Role Based Authorization** option on the Logi JReport Administration > Configuration > Advanced page.

  By default, the option is unchecked and the security mechanism of setting permissions for users, groups and roles is applied. If the option is checked, the Permission Setting UI Displays option will be hidden automatically, since it is used to control UI display and is of no use in the role based security environment.
* In the server.properties file, set server.rolebased.authorization to **true**.

  In this case, the following three properties will not take effect since they control UI display of setting user/group/role permissions:

  server.ui.set\_permissions.group

  server.ui.set\_permissions.role

  server.ui.set\_permissions.user

If the role based security system is used, in both the Logi JReport Administration page and Console page, when you [set permissions for a resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions), there are only roles displayed. Role only based security is similar to Java EE security where the developer assigns roles and during deployment users and groups can be mapped to the roles so if you are already using Java EE security, this would be the best method.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650042-Security-Cache-System)
