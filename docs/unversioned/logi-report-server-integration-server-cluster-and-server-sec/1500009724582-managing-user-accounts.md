---
title: "Managing User Accounts"
id: 1500009724582
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724582-Managing-User-Accounts
updated_at: 2021-07-25T07:18:37Z
---

# Managing User Accounts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751261-Managing-Realms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724542-Managing-Groups)

# Managing User Accounts

Managing user accounts includes many functions and they are available to administrators only. This topic describes creating user accounts, editing the roles and groups for users, customizing the scheduling recipients for users, auditing users, and other user account functions.

To manage users, first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009751261-Managing-Realms#Select) in which the users are, then in the server console, point to **Administration** on the system toolbar and select **Security** > **User** from the drop-down menu to display the User page.

![Security - User page](https://devnet.logianalytics.com/hc/article_attachments/4404936761239/scrty_rsc_srv_dtmdl_user.gif)

You can select the following links for the user management tasks:

* [Creating a New User Account](#Create)
* [Editing a User Account](#Edit)
* [Searching for Users](#Search)
* [Editing the Roles a User Holds](#EditRole)
* [Editing the Groups a User Belongs To](#EditGroup)
* [![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")Editing the Scheduling Recipients for a User](#Recipient)
* [Auditing a Specific User](#Audit)
* [Changing the Password of a User](#Password)
* [Setting User Preferences](#Preference)
* [Deleting a User Account](#Delete)
* [Accessing a User's Personal Folders](#PersonalFolder)

**Tip:** To add or delete a user, you can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009725002-Working-with-Logi-Report-Server#User) directly.

## Creating a New User Account

1. Select **New User** on the task bar. Report Server displays the [New User](https://devnet.logianalytics.com/hc/en-us/articles/1500009720742-New-User) dialog box.

   ![New User dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942474263/nwuser.gif)
2. Provide the name, full name, description, e-mail address, and password for the new user as required.
3. Select **Account Disabled** if you want to disable the user for the time being.
4. The password never expires by default. Select **Expires in N days** and specify in how many days you want the password to get expired.
5. The password can be blank and its length is unlimited by default. Select **Minimum Length** and type a number for the allowed length (the number should be between 0 and 20).
6. By default, Logi Report will prompt the user to change the password after it gets expired or reset by the administrator. Clear the **Ask user to change the password after expired** check box and **Ask user to change the password after reset by administrator** If you do not want such prompt for the user.
7. Select **Publish** and **Advanced Properties** to give the user the [privileges](https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges) of publishing resources to Logi Report Server and of viewing advanced resource properties information.
8. Select **OK** to create the user. The new user is now added in the user table.

## Editing a User Account

1. In the user table, select the name of the user. Report Server displays the [Edit User](https://devnet.logianalytics.com/hc/en-us/articles/1500009747401-Edit-User) dialog box.

   ![Edit User dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942474519/edtuser.gif)
2. Edit the [user information](#NewStep) as required.
3. Select **OK** to accept the changes.

## Searching for Users

In the Search box, type the text of the user names you want to search for and the users containing the matched text will be listed. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404942446871/btn_dltobj.gif).

## Editing the Roles a User Holds

A user can be assigned more than one role. A user that holds multiple roles has all the privileges that these roles have.

To edit the roles a user holds, in the user table, select the **roles** link of the user. The role list of the user is then displayed.

![Edit Roles](https://devnet.logianalytics.com/hc/article_attachments/4404936761495/scrty_rsc_srv_dtmdl_user_role.gif)

The following shows the options in the role list:

| Option | Description |
| --- | --- |
| Search box | Searches for the required roles. |
| Name | Shows the name of the roles. |
| Built-in | Shows whether the role is a built-in role. |
| Remove | Click to remove the selected roles from the user. |
| Add Roles | Click to display the roles that can be added to the user. |
| Add | Click to add the selected roles to the user. |

You can edit the roles the user holds as follows:

* To add a role to the user, select the **Add Roles** link, select the new role, and then select the **Add** button.
* To remove a role from the user, select the role and then select the **Remove** button. Once a role is removed from a user, the user will no longer have the privileges the role owns.

## Editing the Groups a User Belongs To

A user can be assigned to more than one group. A user that belongs to multiple groups has all the privileges that these groups have.

To edit the groups a user belongs to, in the user table, select the **groups** link of the user. The group list of the user is then displayed, which is similar to the role list as seen above.

![Edit Groups](https://devnet.logianalytics.com/hc/article_attachments/4404942474775/scrty_rsc_srv_dtmdl_user_group.gif)

You can edit the groups the user belongs to as follows:

* To add the user to a group, select the **Add Groups** link, select the new group, and then select the **Add** button.
* To remove the user from a group, select the group and then select the **Remove** button. Once a user is removed from a group, the user will no longer have the privileges the group owns.

## This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Editing the Scheduling Recipients for a User

Logi Report adopts permission control on the scheduling recipients each user can access, meaning when a user [schedules a report task](https://devnet.logianalytics.com/hc/en-us/articles/1500009724262-Scheduling-Tasks-to-Run-Reports) to publish the report results to e-mail, the user can send the report results to the e-mail addresses of the users, groups, and roles in the Logi Report Server security system, depending on the user's permission. The following are the basic rules on which users, groups, and roles are available as the scheduling recipients of a user by default:

* An admin user (the user with the "administrators" role) who does not belong to any organization can see all the users, groups, and roles in the Logi Report Server security system. The permission is unchangeable.
* A normal user (the user without the "administrators" role) can see himself only.
* An admin user in an organization can see all the users, groups, and roles in the organization. The permission is unchangeable.
* A normal user in an organization cannot see users, groups, and roles outside of the organization.
* A user, group, or role inherits the permissions from its parent users, groups, and roles.

An admin user can customize the scheduling recipients that are available to a normal user as follows:

1. In the user table, select the **recipients** link of the user. Report Server displays the recipient list for the user.

   ![Edit Recipients](https://devnet.logianalytics.com/hc/article_attachments/4404942475031/scrty_rsc_srv_dtmdl_user_rcpt.gif)

   The following shows the options in the recipient list:

   | Option | Description |
   | --- | --- |
   | Search box | Searches for the required recipients. |
   | Name | Shows the name of the recipients. |
   | Type | Shows the type of the recipients: User, Group, or Role. |
   | Authentication | Shows the recipients' authentication type: Local or LDAP. |
   | Remove | Click to remove the selected recipients from the user. |
   | Add Recipients | Click to display the recipients that can be added to the user. |
   | Add | Click to add the selected recipients to the user. |
2. Select **Add Recipients**. Server displays the recipients that you can choose.
3. Select the recipients that you would like to be accessible to the user.
4. Select **Add**. Server displays a confirmation message. After you confirm, server moves the recipients you just selected to the recipient list above.

   To remove a recipient from the user, select it in the above recipient list and then select **Remove**.

Then when the user schedules to publish the report results to e-mail, the user will be able to select the recipients from the [Select Role, Group and User](https://devnet.logianalytics.com/hc/en-us/articles/1500009720982-Select-Role-Group-and-User) dialog box to use their addresses to send the e-mail.

## Auditing a Specific User

You can have the server to audit a user, and the resulting information will be written into the log files. To audit a user:

1. In the user table, select the **Auditing** link of the user in the Control column. Report Server displays the [Auditing](https://devnet.logianalytics.com/hc/en-us/articles/1500009720502-Auditing) dialog box.

   ![Auditing dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936761751/audit.gif)
2. Specify the events which you want to have audited for this user.
3. Select **OK** to confirm the settings.

## Changing the Password of a User

1. In the user table, select the **Change Password** link of the user. Report Server displays the [Change Password](https://devnet.logianalytics.com/hc/en-us/articles/1500009720522-Change-Password) dialog box.

   ![Change Password dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942475287/chgpswd.gif)
2. In the System Administrator Password text box, type the password of the currently logged in user.
3. Specify the new password for the user and confirm it by typing it a second time.
4. Select **OK** to accept the changes.

## Setting User Preferences

1. In the user table, select the **Preference** link of the user. Report Server displays the [Preference](https://devnet.logianalytics.com/hc/en-us/articles/1500009720782-Preference) dialog box.

   ![Preference dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942475543/prfrnc.gif)
2. Specify the [server preferences](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile) and [Page Report Studio preferences](https://devnet.logianalytics.com/hc/en-us/articles/1500009750581-Customizing-Page-Report-Studio-Profile) for the user accordingly.
3. Select **OK** to accept the changes.

## Deleting a User Account

If you find a user account is no longer required, you can delete it by selecting the corresponding Delete link in the Control column of the user table. However, the built-in user accounts such as admin and guest, and users that hold roles other than the everyone role, or that belong to any group, cannot be deleted. A user cannot delete himself from the user table either.

## Accessing a User's Personal Folders

You can access and fully control other users' personal folders including My Reports and My Components, for example, you can edit the properties of the folders, remove the redundant folders when necessary.

1. Open the file server.properties in the `<install_root>\bin` directory to add the property **server.security.expose\_my\_folders=true** manually.
2. Restart Logi Report Server and go to the user table. The My Folders link is now available for each other user except yourself in the Control column of the table.
3. Select the link for a user and the My Reports and My Components folders of the user are displayed. You can now perform on the folders with full permissions as the user does.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751261-Managing-Realms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724542-Managing-Groups)
