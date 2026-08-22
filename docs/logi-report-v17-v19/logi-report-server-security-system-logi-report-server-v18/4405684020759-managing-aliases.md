---
title: "Managing Aliases"
id: 4405684020759
section: "Logi Report Server Security System Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684020759-Managing-Aliases
updated_at: 2022-01-27T07:59:48Z
---

# Managing Aliases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684022807-Managing-Privileges)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions)

# Managing Aliases

Logi Report Server organizes its files and directories into a resource tree. Aliases provide certain "views" of the server resource tree and enable different users to see different resource trees. This topic describes how you can create and edit alias resource trees for roles, groups, and users, as an administrator.

An alias is a combination of users and the resource nodes. For example, you can set an alias resource tree for Mary in Sales, which enables her to only see the Sales resource node, allowing her direct access to the report files she is interested in.

To manage aliases, first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/4405690680727-Managing-Realms#Select) where the roles, groups, or users for which you create the aliases, then on the system toolbar of the Server Console, navigate to **Administration** > **Security** > **Alias** to display the Alias page.

![Security - Alias page](https://devnet.logianalytics.com/hc/article_attachments/4420461528215/scrty_rsc_srv_dtmdl_alias.gif)

This topic contains the following sections:

* [Setting an Alias Tree for a Role, Group, or User](#Set)
* [Viewing and Editing the Alias Tree of a Role, Group, or User](#View)

## Setting an Alias Tree for a Role, Group, or User

1. Select the corresponding set alias link.
2. In the [Set Alias](https://devnet.logianalytics.com/hc/en-us/articles/4405683762839-Set-Alias-Dialog-Box-Properties) dialog box for selecting role/group/user, select the required role/group/user for which you want to define the alias tree.

   ![Set Alias dialog - Select Role/Group/User](https://devnet.logianalytics.com/hc/article_attachments/4420461528599/setalias_select.gif)
3. Select **Next**. Server displays the Set Alias dialog box for defining the alias tree.

   ![Set Alias dialog - Define Alias Tree](https://devnet.logianalytics.com/hc/article_attachments/4420461528855/setalias_tree.gif)
4. Select **New** to create a new alias node in the root node.
5. In the **Alias Name** field, replace the default name newAlias with a name for the alias node.
6. Select **Browse** to specify a destination resource from the server resource tree that is to be associated with the new alias node. If you do not want the alias node to be shown in the alias resource tree, select **Hide This Alias**.
7. Select **OK** and the new alias node is then added to the alias tree.
8. In the Alias Box, select the node under which you want to create a new alias node and repeat
   steps 3 to 6 to create a new alias node.
9. Create more alias nodes for the role/group/user.

   To remove any unwanted alias node, select it from the alias tree and then select **Remove**.
10. When you finish the alias tree, select **Close** to exit the dialog box.

    You can now see that the just set role/group/user is listed in the corresponding alias table, which contains the following columns.

    | Option | Description |
    | --- | --- |
    | Name | Lists the name of roles/groups/users that have been set an alias resource tree. |
    | Description | Shows information about a role/group/user that has been assigned an alias. |

## Viewing and Editing the Alias Tree of a Role, Group, or User

1. In the alias table, select the underlined name of the role/group/user. Server opens the Set Alias dialog box.
2. You can view the alias tree of the role/group/user and further edit the alias tree. The steps for editing the alias tree are the same as those when creating it.
3. Select **Close** to exit the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* An alias tree is based on the resource nodes (not virtual resource nodes) of the resource tree.
* By default, the alias tree root for each user refers to the resource tree root.
* When you activate an alias tree for a user, the alias resource tree controls all resource access.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684022807-Managing-Privileges)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions)
