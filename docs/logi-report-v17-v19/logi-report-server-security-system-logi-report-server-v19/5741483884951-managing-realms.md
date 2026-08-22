---
title: "Managing Realms"
id: 5741483884951
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741483884951-Managing-Realms
updated_at: 2022-10-31T17:18:25Z
---

# Managing Realms

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463552151-Security-System-Data-Model)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts)

# Managing Realms

This topic describes how you can create realms, set a realm as the active realm of Logi Report Server, and manage the users, groups, and roles in a realm.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) You need to be an administrator to perform realm management tasks.

To manage realms, on the system toolbar of the Server Console, navigate to **Administration** > **Security** > **Realm** to go to the Realm page.

![Security - Realm page](https://devnet.logianalytics.com/hc/article_attachments/9905657658135/scrty_rsc_srv_dtmdl_realm.gif)

This topic contains the following sections:

* [Creating a New Realm](#Create)
* [Activating a Realm](#Activate)
* [Managing the Users, Groups, and Roles in an Inactive Realm](#Select)
* [Deleting a Realm](#Delete)

## Creating a New Realm

1. Select **New Realm** on the task bar. Server displays the [New Realm dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741414197783-New-Realm-Dialog-Box-Properties).

   ![New Realm dialog](https://devnet.logianalytics.com/hc/article_attachments/9905657699223/nwrealm.gif)
2. In the **Realm Name** text box, type a name for the realm.
3. Select **Basic Authentication** to encrypt passwords using the SHA-384 algorithm.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)Or, select **Digest Authentication** if you are using a Server version earlier than v18.3.
4. Select **OK** to create the realm.

Server adds the new realm in the realm table, which contains the following columns:

| Column Name | Description |
| --- | --- |
| Name | Names of the existing realms. |
| State | States of the existing realms: **Active Realm** or **Selected Realm**, or none. If a realm is both active and selected, Server marks it as Active Realm. A Selected Realm is the current editing realm in the Security page. |
| Control | You can control the realms using the following options:  * **Select**  Select to set a realm to be the current editing realm. * **Delete**  Select to delete a realm. |

When you created a new realm, Server assigns it with built-in users, groups, and the default resource tree. Remember to activate the correct realm before allowing clients to visit.

## Activating a Realm

You need to activate a realm before the client users can access the resources, users, groups, and roles in it. You can set only one active realm at any time.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Service**.
2. Select the realm you want to activate from the **Active Realm** drop-down list.
3. Select **Save** to apply the change.
4. Restart Server so that the change can take effect.

## Managing the Users, Groups, and Roles in an Inactive Realm

Users, groups, and roles are only available when the realm they belong to is active. However, you can still manage the users, groups, and roles in an inactive realm. To do this:

1. In the realm table, select **Select** in the Control column to select the realm you want to manage.
2. Navigate to **Administration** > **Security** and then select **User**, **Group**, or **Role** to display the corresponding page.
3. Manage the [users](https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts), [groups,](https://devnet.logianalytics.com/hc/en-us/articles/5741475829015-Managing-Groups) and [roles](https://devnet.logianalytics.com/hc/en-us/articles/5741439782039-Managing-Roles) in the selected realm.

## Deleting a Realm

If you no longer need a realm, you can delete it by selecting **Delete** in the Control column of the realm table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463552151-Security-System-Data-Model)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts)
