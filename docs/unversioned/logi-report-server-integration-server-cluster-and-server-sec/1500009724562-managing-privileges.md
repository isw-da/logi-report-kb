---
title: "Managing Privileges"
id: 1500009724562
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges
updated_at: 2021-07-25T07:18:38Z
---

# Managing Privileges

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751281-Managing-Roles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724522-Managing-Aliases)

# Managing Privileges

Logi Report Server offers these types of privileges for users, groups, and roles: Publish and Advanced Properties. Users need to have the corresponding privilege before they can perform certain task on the server. Users that are granted the Publish privilege and at the same time have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the destination folders on the server resource tree will be able to [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources) to Logi Report Server; users that have the privilege of Advanced Properties are allowed to view advanced information of version properties such as catalog connections and report related resources. By default, only the role "administrators" and the user account "admin" have the Publish and Advanced Properties privileges. This topic describes granting and removing the privileges for users, groups, and roles. Only administrators can perform the privilege management task.

To manage privileges, first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009751261-Managing-Realms#Select) which contains the users, groups, or roles you want to grant privilege for, then in the server console, point to **Administration** on the system toolbar and select **Security** > **Privilege** from the drop-down menu to display the Privilege page.

![Security - Privilege page](https://devnet.logianalytics.com/hc/article_attachments/4404942477079/scrty_rsc_srv_dtmdl_privlg.gif)

**To managing the privileges for users, groups, and roles:**

1. Select the **Role**, **User**, or **Group** radio button.
2. Select a role, user, or group in the Selected box, then select or clear the required privileges.

   If a role, user, or group is not listed in the Selected box, select it in the Available box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404942476823/btn_add.gif) to add it to the Selected box first, then grant it the privileges accordingly.

   You can make use of the Search box to search for the required roles, users, and groups in the Available or Selected box: type the text of the principal names you want to search for and the principals containing the matched text will be listed. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404942446871/btn_dltobj.gif).
3. To remove all privileges from a role, user, or group, first select it in the Selected table, then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404936763159/btn_rmv.gif). The role, user, or group will be added back to the Available box with no privileges.
4. Select the **OK** button to apply the changes.

Administrators can also grant privileges to users, groups, and roles while creating or editing the [users](https://devnet.logianalytics.com/hc/en-us/articles/1500009724582-Managing-User-Accounts#Create), [groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009724542-Managing-Groups#Create), and [roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009751281-Managing-Roles#Create).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751281-Managing-Roles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724522-Managing-Aliases)
