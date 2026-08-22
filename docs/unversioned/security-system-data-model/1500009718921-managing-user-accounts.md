---
title: "Managing User Accounts"
id: 1500009718921
section: "Security System Data Model"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718921-Managing-User-Accounts
updated_at: 2021-11-03T06:56:31Z
---

# Managing User Accounts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718901-Managing-Realms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718841-Managing-Groups)

# Managing User Accounts

To manage user accounts, you must be a member of the administrator role in order to access the Administration menu in the Logi JReport Server console.

Before managing users, you need to first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009718901-Managing-Realms#Select) in which the users are, then in the server console, point to **Administration** on the system toolbar and select **Security** > **User** from the drop-down menu to display the User page.

![Security - User page](https://devnet.logianalytics.com/hc/article_attachments/4412131404311/scrty_rsc_srv_dtmdl_user.gif)

The following lists the user management tasks. To add or delete a user, you can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009719381-Working-with-Logi-Report-Server#User) directly.

* **Creating a new user account**
  1. Select **New User** on the task bar. The [New User](https://devnet.logianalytics.com/hc/en-us/articles/1500009688902-New-User) dialog appears.

     ![New User dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131404823/nwuser.gif)
  2. Provide the name, full name, description, e-mail address, and password for the new user as required.
  3. To disable the user, select the **Account Disabled** checkbox.
  4. The password never expires by default. If you want to make it expire after specified days, select **Expires in N days** and specify in how many days the password will get expired.
  5. The password can be blank and its length is unlimited by default. To limit the minimum number of characters allowed in the password, check **Minimum Length** and input a number for the allowed length (the number should be between 0 and 20).
  6. By default, Logi JReport will prompt the user to change the password after it gets expired or reset by the administrator. If you do not want such prompt for the user, uncheck **Ask user to change the password after expired** and **Ask user to change the password after reset by administrator**.
  7. To give the user the [privilege](https://devnet.logianalytics.com/hc/en-us/articles/1500009718861-Managing-Privileges) of publishing resources to Logi JReport Server or of viewing advanced resource properties information, select the corresponding checkbox.
  8. Select **OK** to create the user.

  The new user is now added in the user table, which contains the following columns:

  | Column Name | Description |
  | --- | --- |
  | User Name | Lists the users' names. You can view and edit user properties in the [Edit User](https://devnet.logianalytics.com/hc/en-us/articles/1500009714621-Edit-User) dialog by selecting the underlined user names. |
  | Full Name | Displays the user's full names. Full name is a property of a user. |
  | Edit Roles | Edits the roles of the specified user. Select the underlined role(s) to edit the roles. + **Name**  Lists the name of the roles that the user holds. + **Built-in**  Shows whether the role is a built-in role. + **Remove**  Removes the specified roles from the role list. + **Add Roles**  Lists the roles that can be assigned to the user.   - **Add**  Adds the specified roles to the user. |
  | Edit Groups | Edits the groups of the specific user. Select the underlined group(s) to edit the groups. + **Name**  Lists the name of the groups that the user belongs to. + **Remove**   Removes the user from the specified groups. + **Add Groups**  Lists the groups that the user can be added to.   - **Add**  Adds the user to the specified groups. |
  | Authentication | Specifies users' authentication type: Local or LDAP. |
  | Control | Controls the users. The following commands are available: [Auditing](#Audit), [Change Password](#Password), [Preference](#Preference), [Delete](#Delete). |
* **Modifying a user account**
  1. In the user table, select the name of the user. The [Edit User](https://devnet.logianalytics.com/hc/en-us/articles/1500009714621-Edit-User) dialog appears.

     ![Edit User dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112523799/edtuser.gif)
  2. Edit the [user information](#NewStep) as required.
  3. Select **OK** to accept the changes.
* **Searching for users**  
   In the Search box above the user table, type in the text of the user names you want to search for and the users containing the matched text will be listed. After entering text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4412139498007/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case and Match Whole Word**.** To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112483991/btn_dltobj.gif).
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
   You can have the server to audit a user, and the resulting information will be written into the log files. To audit a user:
  1. In the user table, select the **Auditing** link of the user in the Control column. The [Auditing](https://devnet.logianalytics.com/hc/en-us/articles/1500009714561-Auditing) dialog appears.

     ![Auditing dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112524055/audit.gif)
  2. Specify the events which you want to have audited for this user.
  3. Select **OK** to confirm the settings.
* **Changing the password of a user**
  1. In the user table, select the **Change Password** link of the user. The [Change Password](https://devnet.logianalytics.com/hc/en-us/articles/1500009714581-Change-Password) dialog appears.

     ![Change Password dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131405079/chgpswd.gif)
  2. In the System Administrator Password text box, enter the password of the currently logged in user.
  3. Specify the new password for the user and confirm it by entering it a second time.
  4. Select **OK** to accept the changes.
* **Setting user preferences**
  1. In the user table, select the **Preference** link of the user. The [Preference](https://devnet.logianalytics.com/hc/en-us/articles/1500009714921-Preference) dialog appears.

     ![Preference dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112524311/prfrnc.gif)
  2. Specify the [server preferences](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile) and [Page Report Studio preferences](https://devnet.logianalytics.com/hc/en-us/articles/1500009691802-Customizing-Page-Report-Studio-Profile) for the user accordingly.
  3. Select **OK** to accept the changes.
* **Deleting a user account**  
   If you find a user account is no longer required, you can delete it by selecting the corresponding Delete link in the Control column of the user table. However, the built-in user accounts such as admin and guest, and users that hold roles other than the everyone role, or that belong to any group, cannot be deleted. A user cannot delete himself from the user table either.
* **Accessing a user's personal folders**  
   You can access and fully control other users' personal folders including My Reports and My Components, for example, you can edit the properties of the folders, remove the redundant folders when necessary.
  1. Open the file server.properties in the `<install_root>\bin` directory to add the property **server.security.expose\_my\_folders=true** manually.
  2. Restart Logi JReport Server and go to the user table. The My Folders link is now available for each other user except yourself in the Control column of the table.
  3. Select the link for a user and the My Reports and My Components folders of the user are displayed. You can now perform on the folders with full permissions as the user does.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718901-Managing-Realms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718841-Managing-Groups)
