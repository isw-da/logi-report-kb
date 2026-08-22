---
title: "Set Alias Dialog Box Properties"
id: 45203934114061
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203934114061-Set-Alias-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:17Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Set Alias Dialog Box Properties

This topic describes how you can use the Set Alias dialog box to set an alias resource tree for the specified role, group, or user. 

Select Set Role Alias, Set Group Alias, or Set User Alias after navigating to the Administration > Security > Alias page on the Server Console. Logi Report Server displays the Set Alias dialog box.

The dialog box includes two phases, one for selecting a role/group/user and the other for defining the alias tree.

## 
Selecting a Role/Group/User

Role Name/Group Name/User Name

Server lists the roles, groups, or users for which you can set an alias resource tree. Select one from the list. 

Description

Information about the roles, groups, or users.

Next

Select to define the alias tree.

Cancel

Select to close the dialog box without saving any changes.

## 
Defining the Alias Tree

Alias Tree

The alias resource tree.

New

Select to create a new alias folder in the current folder.

Remove

Select to remove the selected alias folder permanently. You cannot remove the root folder.

Path

Specify the path of the current folder in the alias resource tree.

Alias Name

Specify the name of the current folder.

When you select New to create a new alias folder, the default name for the new alias folder is newAlias.

Real Resource Name

Specify the resource in the server resource tree you want to associate with the current alias folder. Select Browse to select or update the resource. 

When you select New to create a new alias folder, this field is left blank. You will need to specify a resource from the server resource tree with which you want to associate the new alias folder using the Browse button.

Browse

Select to specify a resource in the server resource tree that you want to associate with the current alias folder.

- 
Resource tree
  Server lists the resources in the public folders. 

- 
Real Resource Name
  Specify a resource in a public folder with full path. You can select a resource in the resource tree or type one manually. 

- 
OK
  Select to apply your setting. 

- 
Cancel
 Select to close the dialog box without saving any changes. 

Hide This Alias

Select if you want the current alias folder and its sub aliases to be invisible to the role, group, or user for whom you set the alias resource tree.

OK

Select to apply any changes you made here and exit the dialog box.

Back

Select to return to the previous phase and discard any changes you made here.

Close

Select to close the dialog box without saving any changes.

- An alias tree is based on the resource nodes (not virtual resource nodes) of the resource tree.

- By default, the alias resource tree root for each user refers to the resource tree root. 

- When you activate an alias tree for a user, Server then controls all resource access by the alias resource tree.
