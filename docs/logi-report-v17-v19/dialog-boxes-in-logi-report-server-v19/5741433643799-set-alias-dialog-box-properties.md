---
title: "Set Alias Dialog Box Properties"
id: 5741433643799
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741433643799-Set-Alias-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:03Z
---

# Set Alias Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741443597975-Select-Target-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741406263447-Set-Permissions-Dialog-Box-Properties)

# Set Alias Dialog Box Properties

This topic describes how you can use the Set Alias dialog box to set an [alias](https://devnet.logianalytics.com/hc/en-us/articles/5741483789079-Managing-Aliases) resource tree for the specified role, group, or user.

Select **Set Role Alias**, **Set Group Alias**, or **Set User Alias** after navigating to the Administration > Security > Alias page on the Server Console. Logi Report Server displays the Set Alias dialog box.

The dialog box includes two phases, one for [selecting a role/group/user](#Select)and the other for [defining the alias tree](#Tree).

## Selecting a Role/Group/User

![Set Alias dialog - Select](https://devnet.logianalytics.com/hc/article_attachments/9905636630295/setalias_select.gif)

**Role Name**/**Group Name**/**User Name**

Server lists the roles, groups, or users for which you can set an alias resource tree. Select one from the list.

**Description**

Information about the roles, groups, or users.

**Next**

Select to [define the alias tree](#Tree).

**Cancel**

Select to close the dialog box without saving any changes.

## Defining the Alias Tree

![Set Alias dialog - Define](https://devnet.logianalytics.com/hc/article_attachments/9905636660631/setalias_tree.gif)

**Alias Tree**

The alias resource tree.

**New**

Select to create a new alias folder in the current folder.

**Remove**

Select to remove the selected alias folder permanently. You cannot remove the root folder.

**Path**

Specify the path of the current folder in the alias resource tree.

**Alias Name**

Specify the name of the current folder.

When you select New to create a new alias folder, the default name for the new alias folder is newAlias.

**Real Resource Name**

Specify the resource in the server resource tree you want to associate with the current alias folder. Select **Browse** to select or update the resource.

When you select New to create a new alias folder, this field is left blank. You will need to specify a resource from the server resource tree with which you want to associate the new alias folder using the Browse button.

**Browse**

Select to specify a resource in the server resource tree that you want to associate with the current alias folder.

* **Resource tree**  
   Server lists the resources in the public folders.
* **Real Resource Name**  
   Specify a resource in a public folder with full path. You can select a resource in the resource tree or type one manually.
* **OK**  
   Select to apply your setting.
* **Cancel**  
   Select to close the dialog box without saving any changes.

**Hide This Alias**

Select if you want the current alias folder and its sub aliases to be invisible to the role, group, or user for whom you set the alias resource tree.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Back**

Select to return to the [previous phase](#Select) and discard any changes you made here.

**Close**

Select to close the dialog box without saving any changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* An alias tree is based on the resource nodes (not virtual resource nodes) of the resource tree.
* By default, the alias resource tree root for each user refers to the resource tree root.
* When you activate an alias tree for a user, Server then controls all resource access by the alias resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741443597975-Select-Target-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741406263447-Set-Permissions-Dialog-Box-Properties)
