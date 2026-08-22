---
title: "Managing Privileges"
id: 1500009650082
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650082-Managing-Privileges
updated_at: 2021-07-24T20:53:40Z
---

# Managing Privileges

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675021-Managing-Roles)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674941-Managing-Aliases)

# Managing Privileges

Logi JReport Server offers these types of privileges for users, groups, and roles: Publish and Advanced Properties. Users that are granted the Publish privilege will be able to publish resources to Logi JReport Server, while users that have the privilege of Advanced Properties are allowed to view advanced information of version properties such as catalog connections and report related resources. In order to publish resources, users must at the same time have both Publish privilege and [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions). By default, only the "administrators" role and "admin" users have the Publish and Advanced Properties privileges.

To manage privileges, you must be a member of the administrator role in order to access the Logi JReport Administration page.

Before managing privileges, you need to first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms#Select)  which contains the roles/groups/users you want to grant privilege for. Then on the Logi JReport Administration page, select **Security** on the system toolbar and select **Privilege** from the drop-down menu to display the Security - Privilege page.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926660375/scrty_rsc_srv_dtmdl_privlg.gif)

The following lists the privilege management tasks:

* **Searching for roles/groups/users in the Available/Selected table** 
  1. Select the **Search**![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) button above the table to display the quick search toolbar.
  2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383255/btn_mvdown1.gif) on the toolbar to specify the search options.
     + **Highlight All**   
        Specifies whether to highlight all matched text.
     + **Match Case**   
        Specifies whether to search for text that meets the case of the typed text.
     + **Match Whole Word**   
        Specifies whether to search for text that looks the same as the typed text.
  3. The quick search toolbar treats the principal names as strings and searches by consecutive text. Type in the text of the principal names you want to search for and the principals containing the matched text will be listed.
  4. To cancel the search operation, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif) on the quick search toolbar.
* **Granting role/group/user privileges**
  + **For roles/groups/users that already have privileges**  
     Roles/groups/users that already have privileges are listed in the Selected table. To assign privileges to them, select a role/group/user in the table, then check the checkbox beside the type of privilege you want to grant. Select **OK** to apply the changes.
  + **For roles/groups/users that have neither of the privileges**
    1. Select the **Role**/**Group**/**User** radio button below the Available box.
    2. Select the role/group/user in the Available table and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add it to the Selected table.
    3. The newly added role/group/user is selected by default. Check the type of privilege you want to grant.
    4. Select the **OK** button to apply the changes.
* **Removing privileges from a role/group/user**
  + To remove a privilege from a role/group/user, select the role/group/user in the Selected table, uncheck the checkbox beside the privilege, then select **OK** to apply the changes.
  + To remove all privileges from a role/group/user, first select the role/group/user in the Selected table, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif). By doing this, the role/group/user will be deleted from the Selected table.

  You can also remove privileges from a role, group or user when editing the role, group or user.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675021-Managing-Roles)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674941-Managing-Aliases)
