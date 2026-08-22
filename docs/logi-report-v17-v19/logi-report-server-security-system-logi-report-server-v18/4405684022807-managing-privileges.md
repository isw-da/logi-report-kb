---
title: "Managing Privileges"
id: 4405684022807
section: "Logi Report Server Security System Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684022807-Managing-Privileges
updated_at: 2022-01-27T07:59:49Z
---

# Managing Privileges

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684024983-Managing-Roles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684020759-Managing-Aliases)

# Managing Privileges

Logi Report Server offers two types of privileges for users, groups, and roles: **Publish** and **Advanced Properties**. This topic describes how you can grant and remove the privileges for users, groups, and roles, as an administrator.

You need to have the corresponding privilege before you can perform certain task on the server. When you have the Publish privilege and at the same time the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions) on a folder on the server resource tree, you are able to [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources) to the folder. When you have the privilege of Advanced Properties, you can view advanced information about version properties such as catalog connections and report related resources. By default, only the role "administrators" and the user account "admin" have the Publish and Advanced Properties privileges.

To manage privileges, first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/4405690680727-Managing-Realms#Select) which contains the users, groups, or roles you want to grant privilege for, then on the system toolbar of the Server Console, navigate to **Administration** > **Security** > **Privilege** to display the Privilege page.

![Security - Privilege page](https://devnet.logianalytics.com/hc/article_attachments/4420461527575/scrty_rsc_srv_dtmdl_privlg.gif)

**To managing the privileges for users, groups, and roles:**

1. Select the **Role**, **User**, or **Group** radio button.
2. Select a role, user, or group in the Selected box, then select or clear the required privileges.

   If a role, user, or group is not listed in the Selected box, select it in the Available box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447121559/btn_add.gif) to add it to the Selected box first, then grant it the privileges accordingly.

   You can make use of the Search box to search for the required roles, users, and groups in the Available or Selected box: type the text of the principal names you want to search for and Server lists the principals that contain the matched text. After typing text in the Search box, you can select the arrow ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420453419415/btn_mvdown1.gif) in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420461456151/btn_dltobj.gif).
3. To remove all privileges from a role, user, or group, first select it in the Selected table, then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420461527319/btn_rmv.gif). Server adds the role, user, or group back to the Available box with no privileges.
4. Select **OK** to apply the changes.

You can also grant privileges to users, groups, and roles while creating or editing the [users](https://devnet.logianalytics.com/hc/en-us/articles/4405684026007-Managing-User-Accounts#Create), [groups](https://devnet.logianalytics.com/hc/en-us/articles/4405684021783-Managing-Groups#Create), and [roles](https://devnet.logianalytics.com/hc/en-us/articles/4405684024983-Managing-Roles#Create).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684024983-Managing-Roles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684020759-Managing-Aliases)
