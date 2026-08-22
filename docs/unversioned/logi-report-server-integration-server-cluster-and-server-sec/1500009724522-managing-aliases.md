---
title: "Managing Aliases"
id: 1500009724522
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724522-Managing-Aliases
updated_at: 2021-07-25T07:18:38Z
---

# Managing Aliases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions)

# Managing Aliases

Logi Report Server organizes its files and directories into a resource tree. Aliases are used to provide certain "views" of the tree, and allow different users to have different views. For example, you can set an alias resource tree (based on the resource tree) for Mary in Sales, which enables her to only see the Sales resource node, allowing her direct access to the report files she is interested in. An alias is a combination of users and the resource node. This topic describes editing the alias trees for roles, groups, and users. Only administrators can perform the alias management tasks.

To manage aliases, first [select the realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009751261-Managing-Realms#Select) where the roles, groups, or users for which the aliases will be created are, then in the server console, point to **Administration** on the system toolbar and select **Security** > **Alias** from the drop-down menu to display the Alias page.

![Security - Alias page](https://devnet.logianalytics.com/hc/article_attachments/4404942477975/scrty_rsc_srv_dtmdl_alias.gif)

You can select the following links for the alias management tasks:

* [Setting an Alias Tree for a Role, Group, or User](#Set)
* [Viewing and Editing the Alias Tree of a Role, Group, or User](#View)

## Setting an Alias Tree for a Role, Group, or User

1. Select the corresponding set alias link.
2. In the [Set Alias](https://devnet.logianalytics.com/hc/en-us/articles/1500009747841-Set-Alias) dialog box for selecting role/group/user, select the required role/group/user for which you want to define the alias tree.

   ![Set Alias dialog - Select Role/Group/User](https://devnet.logianalytics.com/hc/article_attachments/4404942478231/setalias_select.gif)
3. Select the **Next** button and Report Server displays the Set Alias dialog box for defining the alias tree.

   ![Set Alias dialog - Define Alias Tree](https://devnet.logianalytics.com/hc/article_attachments/4404936763927/setalias_tree.gif)
4. Select the **New** button to create a new alias node in the root node.
5. In the Alias Name field, replace the default name newAlias with a name for the alias node.
6. Select the **Browse** button to specify a destination resource from the server resource tree that is to be associated with the new alias node. If you do not want the alias node to be shown in the alias resource tree, select the **Hide This Alias** option.
7. Select the **OK** button and the new alias node is then added to the alias tree.
8. In the Alias Box, select the node under which you want to create a new alias node and repeat
   steps 3 to 6 to create a new alias node.
9. Create more alias nodes for the role/group/user.

   To remove any unwanted alias node, select it from the alias tree and then select **Remove**.
10. When you finish the alias tree, select the **Close** button to exit the dialog box.

    You can now see that the just set role/group/user is listed in the corresponding alias table, which contains the following columns.

    | Option | Description |
    | --- | --- |
    | Name | Lists the name of roles/groups/users that have been set an alias resource tree. |
    | Description | Shows information about a role/group/user that has been assigned an alias. |

## Viewing and Editing the Alias Tree of a Role, Group, or User

1. In the alias table, select the underlined name of the role/group/user. The Set Alias dialog box is then opened.
2. You can view the alias tree of the role/group/user and further edit the alias tree. The steps for editing the alias tree are the same as those when creating it.
3. Select **Close** the exit the dialog box.

**Notes:**

* An alias tree is based on the resource nodes (not virtual resource nodes) of the resource tree.
* By default, the alias tree root for each user refers to the resource tree root.
* When an alias tree is activated for a user, all resource access is then controlled by the alias resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions)
