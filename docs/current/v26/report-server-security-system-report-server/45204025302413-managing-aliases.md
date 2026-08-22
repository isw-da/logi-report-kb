---
title: "Managing Aliases"
id: 45204025302413
section: "Report Server Security System Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204025302413-Managing-Aliases
updated_at: 2026-04-30T14:10:50Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Managing Aliases

Report Server organizes its files and directories into a resource tree. Aliases provide certain "views" of the server resource tree and enable different users to see different resource trees. This topic describes how you can create and edit alias resource trees for roles, groups, and users, as an administrator.

An alias is a combination of users and the resource nodes. For example, you can set an alias resource tree for Mary in Sales, which enables her to only see the Sales resource node, allowing her direct access to the report files she is interested in. 

 To manage aliases,  first select the realm where the roles, groups, or users for which you create the aliases, then on the system toolbar of the Server Console, navigate to Administration > Security > Alias to display the Alias page.

This topic contains the following sections:

- Setting an Alias Tree for a Role, Group, or User

- Viewing and Editing the Alias Tree of a Role, Group, or User

## 
Setting an Alias Tree for a Role, Group, or User

- Select the corresponding set alias link.

- In the Set Alias dialog box for selecting role/group/user, select the required role/group/user for which you want to define the alias tree.
	    

- Select Next. Server displays the Set Alias dialog box for defining the alias tree.
        

- Select New to create a new alias node in the root node.

- In the Alias Name field, replace the default name newAlias with a name for the alias node.

- Select Browse to specify a destination resource from the server resource tree that is to be associated with the new alias node. If you do not want the alias node to be shown in the alias resource tree, select Hide This Alias.

- Select OK and the new alias node is then added to the alias tree.

- In the Alias Box, select the node under which you want to create a new alias node and repeat 
 steps 3 to 6 to create a new alias node.

- Create more alias nodes for the role/group/user.
	    To remove any unwanted alias node, select it from the alias tree and then select Remove.

- When you finish the alias tree, select Close to exit the dialog box. 
        You can now see that the just set role/group/user is listed in the corresponding alias table, which contains the following columns.
				

| Option | Description |
| --- | --- |
| Name | Lists the name of roles/groups/users that have been set an alias resource tree. |
| Description | Shows information about a role/group/user that has been assigned an alias. |

## 
Viewing and Editing the Alias Tree of a Role, Group, or User

- In the alias table, select the underlined name of the role/group/user. Server opens the Set Alias dialog box.

-  You can view the alias tree of the role/group/user and further edit the alias tree. The steps for editing the alias tree are the same as those when creating it. 

- Select Close to exit the dialog box. 

- An alias tree is based on the resource nodes (not virtual resource nodes) of the resource tree.

- By default, the alias tree root for each user refers to the resource tree root.

- When you activate an alias tree for a user, the alias resource tree controls all resource access.
