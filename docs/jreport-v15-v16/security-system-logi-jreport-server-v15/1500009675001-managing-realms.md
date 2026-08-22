---
title: "Managing Realms"
id: 1500009675001
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms
updated_at: 2021-07-24T20:53:40Z
---

# Managing Realms

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650062-Security-System-Data-Model)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts)

# Managing Realms

To manage realms, you must be a member of the administrator role in order to access the Logi JReport Administration page. Then on the Logi JReport Administration page, select **Security** on the system toolbar and select **Realm** from the drop-down menu to go to the Security - Realm page, where you can manage the realms as required.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920418071/scrty_rsc_srv_dtmdl_realm.gif)

The following lists the realm management tasks:

* **Creating a new realm**  
  1. Select the **New Realm** link.
  2. In the [New Realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009670901-New-Realm) dialog, type a name for the realm, and select an authentication mode as the scheme.

     Basic Authentication uses the base64 encryption method as defined by RFC 1945. Digest Authentication uses the MD5 encryption method as defined by RFC 2069. Basic Authentication is lower security but is usually what is used on intranets. Digest Authentication provides much higher security and is usually used with SSL in a highly secure environment.
  3. Select **OK**, the new realm is then added to the realm table, which consists of the following columns.

     | Column Name | Description |
     | --- | --- |
     | Name | Displays the names of the existing realms. |
     | State | Displays the states of the existing realms: + **Active Realm**  An active realm is marked as Active Realm. It means that the realm is the current active realm. If a realm is both active and selected, it is marked as Active Realm. + **Selected Realm**  A selected realm is marked as Selected Realm. It means that the realm is the current editing realm in the Security panel. |
     | Control | Controls the realms. + **Select**  Sets the specified realm to be the current editing realm. + **Delete**  Deletes the specified realm. |

  When a new realm is created, it is assigned with built-in users, groups, and the default resource tree. Remember to activate the correct realm before allowing clients to visit.
* **Activating a realm**  
   The realm must be activated before the resources, users, groups, and roles in it can be accessed by the client users. There can be only one active realm at any time.
  1. On the Logi JReport Administration page, select **Configuration** on the system toolbar, and then select **Service** from the drop-down menu.
  2. Select the realm you want to activate from the Active Realm drop-down list.
  3. Select **Save** to apply the change.
  4. Restart Logi JReport Server so that the change can take effect.
* **Managing the users, groups and roles in an inactive realm**  
   Users, groups and roles are only available when the realm they belong to is active. However, users, groups and roles in an inactive realm can still be managed by users in the administrator role. To do this:
  1. In the realm table, select the **Select** link in the Control column to select the realm you want to manage.
  2. Select **Security** and then **User**, **Group** or **Role** from the drop-down menu to display the corresponding page.
  3. Manage the [users](https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts), [groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009674961-Managing-Groups) and [roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009675021-Managing-Roles) in the selected realm.
* **Deleting a realm**  
   If you find a realm is no longer required, you can delete it by selecting the corresponding Delete link in the Control column of the realm table.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650062-Security-System-Data-Model)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts)
