---
title: "Managing Realms"
id: 1500009718901
section: "Security System Data Model"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718901-Managing-Realms
updated_at: 2021-11-03T06:56:32Z
---

# Managing Realms

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718821-Security-System-Data-Model)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718921-Managing-User-Accounts)

# Managing Realms

To manage realms, you must be a member of the administrator role in order to access the Administration menu in the Logi JReport Server console. Then in the server console, point to **Administration** on the system toolbar and select **Security** > **Realm** from the drop-down menu to go to the Realm page.

![Security - Realm page](https://devnet.logianalytics.com/hc/article_attachments/4412131405335/scrty_rsc_srv_dtmdl_realm.gif)

The following lists the realm management tasks:

* **Creating a new realm**  
  1. Select **New Realm** on the task bar. The [New Realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009714821-New-Realm) dialog appears.

     ![New Realm dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131405591/nwrealm.gif)
  2. In the Realm Name text box, type a name for the realm.
  3. Select an authentication mode as the scheme.

     Basic Authentication uses the base64 encryption method as defined by RFC 1945. Digest Authentication uses the MD5 encryption method as defined by RFC 2069. Basic Authentication provides lower security but is usually what is used on intranets. Digest Authentication provides much higher security and is usually used with SSL in a highly secure environment.
  4. Select **OK** to create the realm.

  The new realm is now added in the realm table, which contains the following columns:

  | Column Name | Description |
  | --- | --- |
  | Name | Displays the names of the existing realms. |
  | State | Displays the states of the existing realms: Active Realm or Selected Realm. If a realm is both active and selected, it is marked as Active Realm. A Selected Realm is the current editing realm in the Security page. |
  | Control | Controls the realms. + **Select**  Sets the specified realm to be the current editing realm. + **Delete**  Deletes the specified realm. |

  When a new realm is created, it is assigned with built-in users, groups, and the default resource tree. Remember to activate the correct realm before allowing clients to visit.
* **Activating a realm**  
   The realm must be activated before the resources, users, groups, and roles in it can be accessed by the client users. There can be only one active realm at any time.
  1. In the server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Service** from the drop-down menu.
  2. Select the realm you want to activate from the Active Realm drop-down list.
  3. Select **Save** to apply the change.
  4. Restart Logi JReport Server so that the change can take effect.
* **Managing the users, groups and roles in an inactive realm**  
   Users, groups and roles are only available when the realm they belong to is active. However, users, groups and roles in an inactive realm can still be managed by users in the administrator role. To do this:
  1. In the realm table, select the **Select** link in the Control column to select the realm you want to manage.
  2. Select **Administration** > **Security** and then **User**, **Group** or **Role** from the drop-down menu to display the corresponding page.
  3. Manage the [users](https://devnet.logianalytics.com/hc/en-us/articles/1500009718921-Managing-User-Accounts), [groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009718841-Managing-Groups) and [roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009692682-Managing-Roles) in the selected realm.
* **Deleting a realm**  
   If you find a realm is no longer required, you can delete it by selecting the corresponding Delete link in the Control column of the realm table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718821-Security-System-Data-Model)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718921-Managing-User-Accounts)
