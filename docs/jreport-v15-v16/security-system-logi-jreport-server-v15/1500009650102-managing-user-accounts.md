---
title: "Managing User Accounts"
id: 1500009650102
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts
updated_at: 2022-03-18T20:30:02Z
---

# Managing User Accounts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674961-Managing-Groups)

# Managing User Accounts

To manage user accounts, you must be a member of the administrator role in order to access the Logi JReport Administration page.

Before managing users, you need to first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms#Select) in which the users are. Then on the Logi JReport Administration page, select **Security** on the system toolbar and select **User** from the drop-down menu to display the Security - Use page.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920417303/scrty_rsc_srv_dtmdl_user.gif)

The following lists the user management tasks. To add or delete a user, you can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#User) directly.

* **Creating a new user account**
  1. Select the **New User** link.
  2. In the [New User](https://devnet.logianalytics.com/hc/en-us/articles/1500009646682-New-User) dialog, provide the name, full name, description, e-mail address, and password for the new user as required. Then confirm the password by input it again.
  3. To disable the user, select the **Account Disabled** checkbox.
  4. The password never expires by default. You can make it expire after specified days: select the **Expires in N days** option and then input a number.
  5. The password can be blank and its length is unlimited by default. You can limit the minimum number of characters allowed in the password: select the **Minimum Length** option and then input a number.
  6. To give the user the [privilege](https://devnet.logianalytics.com/hc/en-us/articles/1500009650082-Managing-Privileges) of publishing resources to Logi JReport Server or of viewing advanced resource properties information, select the corresponding checkbox.
  7. Select **OK**, the new user is then added to the user table, which consists of the following columns.

     | Column Name | Description |
     | --- | --- |
     | User Name | Lists the users' names. You can view and edit user properties by selecting the underlined user names. |
     | Full Name | Displays the user's full names. Full name is a property of a user. |
     | Edit Roles | Edits the roles of the specified user. Select the underlined role(s) to edit the roles. + **Name**  Lists the name of the roles that the user holds. + **Built-in**  Shows whether the role is a built-in role. + **Remove**  Removes the specified roles from the role list. + **Add Roles**  Lists the roles that can be assigned to the user.   - **Add**  Adds the specified roles to the user. |
     | Edit Groups | Edits the groups of the specific user. Select the underlined group(s) to edit the groups. + **Name**  Lists the name of the groups that the user belongs to. + **Remove**   Removes the user from the specified groups. + **Add Groups**  Lists the groups that the user can be added to.   - **Add**  Adds the user to the specified groups. |
     | Authentication | Specifies users' authentication type: Local or LDAP. |
     | Control | Controls the users. The following commands are available: [Auditing](#Audit), [Change Password](#Password), [Preference](#Preference), [Delete](#Delete). |
* **Modifying a user account**
  1. In the user table, select the name of the user.
  2. In the displayed dialog, edit the [user information](#NewStep) as required.
  3. When done, select **OK**  to accept the changes.
* **Searching for users**On the quick search toolbar above the user table, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383255/btn_mvdown1.gif) to specify the search options, then type in the text of the user names you want to search for and the users containing the matched text will be listed. The quick search toolbar treats the user names as strings and searches by consecutive text.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* **Adding roles to a user**  
   A user can be assigned more than one role. A user that holds multiple roles has all the privileges that these roles have.
  1. In the user table, select the **role(s)** link of the user.
  2. In the displayed page, select the **Add Roles** link.
  3. In the role table, check the roles that you want to add to the user, then select the **Add** button.
  4. Select **Security** > **User** to return to the user table.
* **Adding a user to groups**  
   A user can be assigned to more than one group. A user that belongs to multiple groups has all the privileges that these groups have. To add a user to some groups:
  1. In the user table, select the **group(s)**  link of the user.
  2. In the displayed page, select the **Add Groups**  link.
  3. In the group table, check the groups that you want to add the user to, then select the **Add** button.
  4. Select **Security** > **User** to return to the user table.
* **Removing roles/groups from a user**  
   If you want to remove certain roles a user holds, or some groups a user belongs to from a user, follow the steps below:
  1. In the user table, select the **role(s)**/**group(s)**  link of the user.
  2. In the roles/groups table of the user, check the roles/groups you want to remove, then select the **Remove** button.Once a role or group is removed from a user, the user will no longer have the privileges the role or group has.
* **Auditing a specific user**  
   You can have the server to audit a user, and the resulting information will be written into the log files.
  To audit a user:
  1. In the user table, select the **Auditing** link of the user in the Control column.
  2. In the [Auditing](https://devnet.logianalytics.com/hc/en-us/articles/1500009670721-Auditing) dialog, specify the events which you want to have audited for this user.
  3. When done, select **OK** to accept the changes.
* **Changing the password of a user**
  1. In the user table, select the **Change Password** link of the user.
  2. In the Change Password dialog, specify the password of the current logged in user.
  3. Specify the new password for the user and confirm it by entering it a second time.
  4. When done, select **OK** to accept the changes.
* **Setting user preferences**
  1. In the user table, select the **Preference** link of the user.
  2. In the Preference dialog, specifies the [server preferences](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile) and [Page Report Studio preferences](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile) for the user accordingly.
  3. When done, select **OK** to accept the changes.
* **Deleting a user account**  
   If you find a user account is no longer required, you can delete it by selecting the corresponding Delete link in the Control column of the user table. However, the built-in user accounts, such as admin and guest, and users that hold roles other than the everyone role, or that belong to any group, cannot be deleted. A user cannot delete himself from the user table either.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674961-Managing-Groups)
