---
title: "Set Alias Dialog Box Properties"
id: 1500009774601
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774601-Set-Alias-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:41Z
---

# Set Alias Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746462-Select-Target-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774321-Set-Permissions-Dialog-Box-Properties)

# Set Alias Dialog Box Properties

This topic describes how you can use the Set Alias dialog box to set an [alias](https://devnet.logianalytics.com/hc/en-us/articles/1500009778601-Managing-Aliases) resource tree for the specified role, group, or user.

Server displays the dialog box when an admin user selects the Set Role Alias, Set Group Alias, or Set User Alias link in the Administration > Security > Alias page in the Server Console.

The dialog box is divided into two phases, one for [selecting the role/group/user](#Select)and the other for [defining the alias tree](#Tree).

## Selecting the Role/Group/User Phase

![Set Alias dialog - Select](https://devnet.logianalytics.com/hc/article_attachments/4404880222615/setalias_select.gif)

**Role Name**/**Group Name**/**User Name**

Lists the roles, groups, or users for which you can set an alias resource tree. Select one from the list.

**Description**

Shows information about the roles, groups, or users.

**Next**

Goes to the [next phase](#Tree).

**Cancel**

Cancels the setting and exits the dialog box.

## Defining the Alias Tree Phase

![Set Alias dialog - Define](https://devnet.logianalytics.com/hc/article_attachments/4404880223127/setalias_tree.gif)

**Alias Tree**

Displays the alias resource tree.

**New**

Creates a new alias node in the current node. A node functions as a folder.

**Remove**

Deletes the selected alias node permanently. The root node cannot be deleted.

**Path**

Displays the path of the current node in the alias resource tree.

**Alias Name**

Displays the name of the current node. You can edit the alias name.

When you select the New button to create a new alias node in the current node, the default name for the new alias node is newAlias.

**Real Resource Name**

Displays the resource in the server resource tree that is associated with the current alias node. You can change the resource using the Browse button.

When you select the New button to create a new alias node in the current node, this field is left blank. You will need to specify a resource from the server resource tree with which to associate the new alias node using the Browse button.

**Browse**

Specifies a destination resource in the server resource tree that is to be associated with the current alias node.

* **Resource tree**  
   Lists the resources in the public folders.
* **Real Resource Name**  
   Specifies a resource in a public folder with full path. You can select a resource in the resource tree or type one manually.
* **OK**  
   Applies the setting.
* **Cancel**  
   Exits the dialog box.

**Hide This Alias**

If this option is selected, the current alias node and its sub aliases will be invisible to the role, group, or user for whom the alias resource tree is set.

**OK**

Applies the settings.

**Back**

Returns to the [previous phase](#Select) if no alias has been set.

**Close**

Exits this dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* An alias tree is based on the resource nodes (not virtual resource nodes) of the resource tree.
* By default, the alias resource tree root for each user refers to the resource tree root.
* When an alias tree is activated for a user, all resource access is then controlled by the alias resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746462-Select-Target-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774321-Set-Permissions-Dialog-Box-Properties)
