---
title: "Managing Groups"
id: 1500009674961
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674961-Managing-Groups
updated_at: 2021-07-24T20:53:39Z
---

# Managing Groups

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675021-Managing-Roles)

# Managing Groups

To manage groups, you must be a member of the administrator role in order to access the Logi JReport Administration page.

Before managing groups, you need to first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms#Select) in which the groups are. Then on the Logi JReport Administration page, select **Security** on the system toolbar and select **Group** from the drop-down menu to display the Security - Group page.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920418839/scrty_rsc_srv_dtmdl_group.gif)

The following lists the group management tasks.

* **Creating a new group**
  1. Select the **New Group** link.
  2. In the [New Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009670861-New-Group) dialog, provide the name and description and specify a parent group for the new group.
  3. To give the group the [privilege](https://devnet.logianalytics.com/hc/en-us/articles/1500009650082-Managing-Privileges) of publishing resources to Logi JReport Server or of viewing advanced resource properties information, select the corresponding checkbox.
  4. Select **OK**, the new group is then added into the group table, which consists of the following columns.

     | Column Name | Description |
     | --- | --- |
     | Name | Lists the group names. You can view and edit group properties by selecting the underlined group name. |
     | Members | Edits members of the specified group. Select the underlined member(s) to edit the members. + **Name**  Lists the name of the members that the group holds. + **Type**  Specifies the type of the members that the group holds. + **Authentication**  Specifies the group members' authentication type: Local or LDAP. + **Remove**   Removes the specified members from the group. + **Add Members**  Shows the members that can be added to the group. |
     | Control | Controls the groups. + **Delete**  Deletes the specified group. Groups that have child members or parent members cannot be deleted. |
* **Searching for groups**On the quick search toolbar above the group table, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383255/btn_mvdown1.gif) to specify the search options, then type in the text of the group names you want to search for and the groups containing the matched text will be listed. The quick search toolbar treats the group names as strings and searches by consecutive text.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* **Editing the privileges of a group**In the group table, select the name of the role, then in the displayed dialog, add or remove privileges for the group and select **OK**.
* **Editing members of a group**  
   You can edit members of a group, such as adding a new member, or removing a member from the group. To do this, in the group table browse to the specific group, select the **member(s)** link, then edit the members of the group as follows:
  + To remove a member from the group, check the member and then select the **Remove** button.
  + To add a member to the group, select the **Add Members** link, check the new member, and then select the **Add** button.

  **Notes:**

  + A group can have more than one child member and parent member.
  + A parent member cannot be added to the current group as its child member.
* **Deleting a group**  
   If you find a group is no longer required, you can delete it by selecting the corresponding Delete link in the Control column of the group table. However, groups that are not empty, having child members or parent members, cannot be deleted.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675021-Managing-Roles)
