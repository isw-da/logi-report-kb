---
title: "Managing Privileges"
id: 1500009718861
section: "Security System Data Model"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718861-Managing-Privileges
updated_at: 2021-11-03T06:56:30Z
---

# Managing Privileges

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692682-Managing-Roles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692662-Managing-Aliases)

# Managing Privileges

Logi JReport Server offers these types of privileges for users, groups, and roles: Publish and Advanced Properties. Users that are granted the Publish privilege will be able to publish resources to Logi JReport Server, while users that have the privilege of Advanced Properties are allowed to view advanced information of version properties such as catalog connections and report related resources. In order to publish resources, users must at the same time have both Publish privilege and [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions). By default, only the role "administrators" and the user account "admin" have the Publish and Advanced Properties privileges.

To manage privileges, you must be a member of the administrator role in order to access the Administration menu in the Logi JReport Server console.

Before managing privileges, you need to first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009718901-Managing-Realms#Select)  which contains the roles/groups/users you want to grant privilege for, then in the server console, point to **Administration** on the system toolbar and select **Security** > **Privilege** from the drop-down menu to display the Privilege page.

![Security - Privilege page](https://devnet.logianalytics.com/hc/article_attachments/4412131405975/scrty_rsc_srv_dtmdl_privlg.gif)

The following lists the privilege management tasks:

* **Searching for roles/groups/users in the Available/Selected table**  
   In the corresponing Search box, type in the text of the principal names you want to search for and the principals containing the matched text will be listed. After entering text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4412139498007/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case and Match Whole Word**.** To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112483991/btn_dltobj.gif).
* **Granting role/group/user privileges**

+ **For roles/groups/users that already have privileges**  
   Roles/groups/users that already have privileges are listed in the Selected table. To assign privileges to them, select a role/group/user in the table, then check the checkbox beside the type of privilege you want to grant. Select **OK** to apply the changes.
+ **For roles/groups/users that have neither of the privileges**
  1. Select the **Role**/**Group**/**User** radio button below the Available box.
  2. Select the role/group/user in the Available table and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif) to add it to the Selected table.
  3. The newly added role/group/user is selected by default. Check the type of privilege you want to grant.
  4. Select the **OK** button to apply the changes.

* **Removing privileges from a role/group/user**
  + To remove a privilege from a role/group/user, select the role/group/user in the Selected table, uncheck the checkbox beside the privilege, then select **OK** to apply the changes.
  + To remove all privileges from a role/group/user, first select the role/group/user in the Selected table, then select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif). By doing this, the role/group/user will be deleted from the Selected table.

  You can also remove privileges from a role, group or user when editing the role, group or user.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692682-Managing-Roles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692662-Managing-Aliases)
