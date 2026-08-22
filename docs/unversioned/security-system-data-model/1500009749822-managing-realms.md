---
title: "Managing Realms"
id: 1500009749822
section: "Security System Data Model"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749822-Managing-Realms
updated_at: 2021-07-24T00:47:35Z
---

# Managing Realms

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778581-Security-System-Data-Model)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749862-Managing-User-Accounts)

# Managing Realms

This topic describes how you can create realms, set a realm as the active realm of Logi Report Server, and manage the users, groups, and roles in a realm. Only administrators can perform these realm management tasks.

To manage realms, in the Server Console, point to **Administration** on the system toolbar and select **Security** > **Realm** from the drop-down menu to go to the Realm page.

![Security - Realm page](https://devnet.logianalytics.com/hc/article_attachments/4404880218775/scrty_rsc_srv_dtmdl_realm.gif)

This topic contains the following sections:

* [Creating a New Realm](#Create)
* [Activating a Realm](#Activate)
* [Managing the Users, Groups, and Roles in an Inactive Realm](#Select)
* [Deleting a Realm](#Delete)

## Creating a New Realm

1. Select **New Realm** on the task bar. Server displays the [New Realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009774201-New-Realm-Dialog-Box-Properties) dialog box.

   ![New Realm dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880219031/nwrealm.gif)
2. In the **Realm Name** text box, type a name for the realm.
3. Select an authentication mode as the scheme.
   * **Basic Authentication** uses the base64 encryption method as defined by RFC 1945. It provides lower security but is usually what is used on intranets.
   * **Digest Authentication** uses the MD5 encryption method as defined by RFC 2069. It provides much higher security and usually works with SSL in a highly secure environment.
4. Select **OK** to create the realm.

Server adds the new realm in the realm table, which contains the following columns:

| Column Name | Description |
| --- | --- |
| Name | Names of the existing realms. |
| State | States of the existing realms: **Active Realm** or **Selected Realm**, or none. If a realm is both active and selected, Server marks it as Active Realm. A Selected Realm is the current editing realm in the Security page. |
| Control | You can control the realms using the following options:  * **Select**  Select to set a realm to be the current editing realm. * **Delete**  Select to delete a realm. |

When you created a new realm, Server assigns it with built-in users, groups, and the default resource tree. Remember to activate the correct realm before allowing clients to visit.

## Activating a Realm

You need to activate a realm before the client users can access the resources, users, groups, and roles in it. There can be only one active realm at any time.

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** > **Service** from the drop-down menu.
2. Select the realm you want to activate from the **Active Realm** drop-down list.
3. Select **Save** to apply the change.
4. Restart Server so that the change can take effect.

## Managing the Users, Groups, and Roles in an Inactive Realm

Users, groups, and roles are only available when the realm they belong to is active. However, you can still manage the users, groups, and roles in an inactive realm. To do this:

1. In the realm table, select the **Select** link in the Control column to select the realm you want to manage.
2. Select **Administration** > **Security** and then **User**, **Group**, or **Role** from the drop-down menu to display the corresponding page.
3. Manage the [users](https://devnet.logianalytics.com/hc/en-us/articles/1500009749862-Managing-User-Accounts), [groups,](https://devnet.logianalytics.com/hc/en-us/articles/1500009778621-Managing-Groups) and [roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009749842-Managing-Roles) in the selected realm.

## Deleting a Realm

If you no longer need a realm, you can delete it by selecting the corresponding Delete link in the Control column of the realm table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778581-Security-System-Data-Model)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749862-Managing-User-Accounts)
