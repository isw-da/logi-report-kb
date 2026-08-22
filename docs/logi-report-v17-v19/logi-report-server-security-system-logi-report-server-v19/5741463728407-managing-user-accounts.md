---
title: "Managing User Accounts"
id: 5741463728407
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts
updated_at: 2022-10-31T17:18:26Z
---

# Managing User Accounts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483884951-Managing-Realms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741475829015-Managing-Groups)

# Managing User Accounts

Managing user accounts includes many functions and they are available to administrators only. This topic describes how you can create user accounts, edit the roles and groups for users, customize the scheduling recipients for users, audit users, and perform other user account functions.

To manage users, first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/5741483884951-Managing-Realms#Select) in which the users are, then on the system toolbar of the Server Console, navigate to **Administration** > **Security** > **User** to display the User page.

![Security - User page](https://devnet.logianalytics.com/hc/article_attachments/9905657202455/scrty_rsc_srv_dtmdl_user.gif)

This topic contains the following sections:

* [Creating a New User Account](#Create)
* [Editing a User Account](#Edit)
* [Searching for Users](#Search)
* [Editing the Roles a User Holds](#EditRole)
* [Editing the Groups a User Belongs To](#EditGroup)
* [Editing the Scheduling Recipients for a User](#Recipient)
* [Auditing a Specific User](#Audit)
* [Changing the Password of a User](#Password)
* [Setting User Preferences](#Preference)
* ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")[Managing Users' Shared Reports](#SharedReport)
* [Deleting a User Account](#Delete)
* [Accessing a User's Personal Folders](#PersonalFolder)

**Tip:** To add or delete a user, you can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/5741485252503-Working-with-Server-via-URL#User) directly.

## Creating a New User Account

1. Select **New User** on the task bar. Server displays the [New User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741433353879-New-User-Dialog-Box-Properties).

   ![New User dialog](https://devnet.logianalytics.com/hc/article_attachments/9905635846551/nwuser.gif)
2. Provide the name, full name, description, email address, and password for the new user.
3. Select **Account Disabled** if you want to disable the user for the time being.
4. The password never expires by default. Select **Expires in N days** and specify in how many days you want the password to get expired.
5. The password can be blank, and its length is unlimited by default. Select **Minimum Length** and type a number for the allowed length. The number should be between 0 and 20.
6. By default, Logi Report will prompt the user to change the password after it gets expired or reset by the administrator. Clear **Ask user to change the password after expired** and **Ask user to change the password after reset by administrator** If you do not want such prompt for the user.
7. Select **Publish** and **Advanced Properties** to give the user the [privileges](https://devnet.logianalytics.com/hc/en-us/articles/5741455284119-Managing-Privileges) of publishing resources to Logi Report Server and of viewing advanced resource properties information.
8. Select **OK** to create the user. Server adds the new user in the user table.

## Editing a User Account

1. In the user table, select the name of the user. Server displays the [Edit User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741413799703-Edit-User-Dialog-Box-Properties).

   ![Edit User dialog](https://devnet.logianalytics.com/hc/article_attachments/9905635878679/edtuser.gif)
2. Edit the [user information](#NewStep).
3. Select **OK** to accept the changes.

## Searching for Users

In the Search box, type the text of the usernames you want to search for and Server lists the users that contain the matched text. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905618988823/btn_mvdown1.gif) in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905616261527/btn_dltobj.gif).

## Editing the Roles a User Holds

You can assign more than one role to a user. A user that holds multiple roles has all the privileges that these roles have.

To edit the roles that a user holds, in the user table, select **roles** of the user. Server displays the role list of the user.

![Edit Roles](https://devnet.logianalytics.com/hc/article_attachments/9905657266711/scrty_rsc_srv_dtmdl_user_role.gif)

The following table describes the options in the role list:

| Option | Description |
| --- | --- |
| Search box | Search for the required roles. |
| Name | Name of the roles. |
| Built-in | Show whether the role is a built-in role. |
| Remove | Select to remove the selected roles from the user. |
| Add Roles | Select to display the roles that you can add to the user. |
| Add | Select to add the selected roles to the user. |

You can edit the roles that the user holds:

* To add a role to the user, select **Add Roles**, select the new role, and then select **Add**.
* To remove a role from the user, select the role and then select **Remove**. Once you remove a role from a user, the user will no longer have the privileges that the role owns.

## Editing the Groups a User Belongs To

You can assign more than one group to a user. A user that belongs to multiple groups has all the privileges that these groups have.

To edit the groups that a user belongs to, in the user table, select **groups** of the user. Server displays the group list of the user, which is similar to the role list of a user as above.

![Edit Groups](https://devnet.logianalytics.com/hc/article_attachments/9905635922199/scrty_rsc_srv_dtmdl_user_group.gif)

You can edit the groups that the user belongs to:

* To add the user to a group, select **Add Groups**, select the new group, and then select **Add**.
* To remove the user from a group, select the group and then select **Remove**. Once you remove a user from a group, the user will no longer have the privileges that the group owns.

## Editing the Scheduling Recipients for a User

Logi Report adopts permission control on the scheduling recipients each user can access, meaning when a user [schedules a report task](https://devnet.logianalytics.com/hc/en-us/articles/5741483471255-Scheduling-Tasks-to-Run-Reports) to publish reports to email, the user can send the reports to the email addresses of the users, groups, and roles in the Logi Report Server security system, depending on the user's permission. The following are the basic rules on which users, groups, and roles are available as the scheduling recipients of a user by default:

* An administrator (the user with the "administrators" role) who does not belong to any organization can see all the users, groups, and roles in the Logi Report Server security system. The permission is unchangeable.
* A normal user (the user without the "administrators" role) can see themselves only.
* An administrator in an organization can see all the users, groups, and roles in the organization. The permission is unchangeable.
* A normal user in an organization cannot see users, groups, and roles outside of the organization.
* A user, group, or role inherits the permissions from its parent users, groups, and roles.

An administrator can customize the scheduling recipients that are available to a normal user:

1. In the user table, select **recipients** of the user. Server displays the recipient list for the user.

   ![Edit Recipients](https://devnet.logianalytics.com/hc/article_attachments/9905657325335/scrty_rsc_srv_dtmdl_user_rcpt.gif)

   The following table describes the options in the recipient list:

   | Option | Description |
   | --- | --- |
   | Search box | Search for the required recipients. |
   | Name | Name of the recipients. |
   | Type | Type of the recipients: User, Group, or Role. |
   | Authentication | Recipients' authentication type: Local or LDAP. |
   | Remove | Select to remove the selected recipients from the user. |
   | Add Recipients | Select to display the recipients that you can add to the user. |
   | Add | Select to add the selected recipients to the user. |
2. Select **Add Recipients**. Server displays the recipients that you can choose.
3. Select the recipients that you would like to be accessible to the user.
4. Select **Add**. Server displays a confirmation message.
5. After you confirm, server moves the recipients you just selected to the recipient list.
6. To remove a recipient from the user, select it in the recipient list and then select **Remove**.

Then when the user schedules to publish reports to email, the user will be able to select the recipients from the [Select Role, Group and User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741448846231-Select-Role-Group-and-User-Dialog-Box-Properties) to use their addresses to send the email.

## Auditing a Specific User

You can have Server to audit a user and record the resulting information into the log files. To audit a user:

1. In the user table, select **Auditing** of the user in the Control column. Server displays the [Auditing dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741432839831-Auditing-Dialog-Box-Properties).

   ![Auditing dialog](https://devnet.logianalytics.com/hc/article_attachments/9905657359767/audit.gif)
2. Specify the events which you want to audit for this user.
3. Select **OK** to confirm the settings.

## Changing the Password of a User

1. In the user table, select **Change Password** of the user. Server displays the [Change Password dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741405657879-Change-Password-Dialog-Box-Properties).

   ![Change Password dialog](https://devnet.logianalytics.com/hc/article_attachments/9905636029847/chgpswd.gif)
2. In the **System Administrator Password** text box, type the password of the currently signed-in user.
3. Specify the new password for the user and confirm it by typing it a second time.
4. Select **OK** to accept the changes.

## Setting User Preferences

1. In the user table, select **Preference** of the user. Server displays the [Preference dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741442976407-Preference-Dialog-Box-Properties-).

   ![Preference dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905636053143/prfrnc.gif)
2. Specify the [server preferences](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile) for the user as well as the [Default](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties#Default) and [Advanced](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties#PropertiesAdvanced) properties you want the user to use in Page Report Studio.
3. Select **OK** to accept the changes.

## This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Managing Users' Shared Reports

When users have [shared their reports](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports), you can view and remove the shared reports if you want.

![](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) System admin cannot see shared reports of organization users, and organization admin can only see shared reports of users in the organization.

Select **N Reports** (N is not zero) for a user in the **Shared** column in the user table. Server displays the user's My Shared page. Here, you see the original reports that the user has shared, where and when the reports were shared, the type of the reports, the descriptions, and the time when the shared reports were modified.

![A User's My Shared Page](https://devnet.logianalytics.com/hc/article_attachments/9905636081815/scrty_rsc_srv_dtmdl_user_share.gif)

To view more information about a report sharing, hover over the report row, and then select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/9905657474071/btn_srv_prpty.gif) on the floating toolbar. Or, you can select the report row, right-click in the report row, and then select **Properties** on the shortcut menu. Server displays the [Sharing Properties dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741427772567-Sharing-Properties). You can only view the properties in the dialog box but cannot change them.

![Share Properties dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905657507991/scrty_rsc_srv_dtmdl_user_shareprop.gif)

To remove a shared report, hover over the report row, and then select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905616261527/btn_dltobj.gif) on the floating toolbar. Or, you can select the report row, right-click in the report row, and then select **Delete** on the shortcut menu. Server asks whether you want to delete the node. Select **OK**. Server will remove the shared report.

## Deleting a User Account

If you find a user account is no longer required, you can delete it by selecting the corresponding **Delete** in the **Control** column of the user table. However, you cannot delete the built-in user accounts such as admin and guest, and users that hold roles other than the everyone role, or that belong to any group. You cannot delete yourself from the user table, either.

## Accessing a User's Personal Folders

You can access and fully control other users' personal folders including My Reports and My Components, for example, you can edit the properties of the folders and remove the redundant folders when necessary.

1. Open the **server.properties** file in `<install_root>\bin` to add the **server.security.expose\_my\_folders=true** property manually.
2. Restart Server.
3. Navigate to the user table. The My Folders link is now available for each other user except yourself in the Control column of the table.
4. Select the link for a user. Server displays the My Reports and My Components folders of the user. You can now perform on the folders with full permissions as the user does.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483884951-Managing-Realms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741475829015-Managing-Groups)
