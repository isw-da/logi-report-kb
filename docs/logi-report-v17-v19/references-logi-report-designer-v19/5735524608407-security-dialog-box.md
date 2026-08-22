---
title: "Security Dialog Box"
id: 5735524608407
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735524608407-Security-Dialog-Box
updated_at: 2022-11-02T04:40:16Z
---

# Security Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567555223-Search-Reports-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515319191-Security-Configuration-Setting-Dialog-Box)

# Security Dialog Box

You can use the Security dialog box to specify the security settings for a [data source security entry](https://devnet.logianalytics.com/hc/en-us/articles/5735527007767-Working-with-RLS-and-CLS-at-Data-Source-Scope#Create). This topic describes the options in the dialog box.

Designer displays the Security dialog box when you right-click Security Entry in the Data Source > Security node in the Catalog Manager, select New Security Entry from the shortcut menu, type a name for the new security policy, and then select OK.

![Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898460986903/scrty.gif)

Designer displays these options:

**Users/Groups/Roles panel**

You can define security policies for different users, roles, and groups in this panel.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
  Select to add users/groups/roles. After you select this button, Designer displays a drop-down menu, which contains the following commands:
  + **Add User**  
    Select to open the [Add User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735528371479-Add-User-Dialog-Box) to add a new user.
  + **Add Group**  
    Select to open the [Add Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735564962583-Add-Group-Dialog-Box) to add a new group.
  + **Add Role**  
    Select to open the [Add Role dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735564993175-Add-Role-Dialog-Box) to add a new role.
  + **Import from Logi Report Server**  
    Select to open the [Import from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735551708695-Import-from-Logi-Report-Server-Dialog-Box) to import users, roles, and groups from Server.
  + **Import from File**  
    Select to import users, roles, and groups from an XML file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9898478126743/btn_expt2fl.gif)**Export button**  
  Select to export the users, roles, and groups to an XML file.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the specified user/group/role.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
  Select to edit the specified user/role/group in the [Edit User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500519447-Edit-User-Dialog-Box), [Edit Role dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565718423-Edit-Role-Dialog-Box), or [Edit Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522562071-Edit-Group-Dialog-Box).
* **Search box**  
  Type the keyword in the box and Designer lists the users/roles/groups containing the matched text.
* **Principal box**  
  This box lists all the users, roles, and groups that you add for the security policy. Select a principal to define the security policy for it.

**Valid RLS**

Select to apply record level security (RLS) in this security entry. When you do not select this option, the security entry does not contain RLS and all the records are available to all the principals.

**Valid CLS**

Select to apply column level security (CLS) in this security entry. When you do not select this option, the security entry does not contain CLS and all the columns are available to all the principals.

**Disable Policy Settings**

* When you do not select this option, you can specify a security policy for the selected principal. However, if you leave the record level security and column level security settings blank, the principal is not able to view any record, unless it inherits some permissions from another group or role.
* When you select this option, you cannot specify record level security or column level security for the selected principal. The principal therefore has full access to all the records in the reports which apply this security entry.

**Record Level Security tab**

You can specify the record level security conditions of the security entry in this tab.

* **Expression**  
  Specify the field on which to define the condition. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the field.
* **Operator**  
  Specify the operator to compose the condition.
  + **=**  
    Equal to
  + **>=**  
    Greater than or equal to
  + **>**  
    Greater than
  + **<**  
    Less than
  + **<=**  
    Less than or equal to
  + **!=**/**<>**  
    Not equal to
  + **in**  
    The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "in" operator, you can use multiple values separated by comma (,).
* **Value**  
  Specify the value of how to build the condition. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the value.
* **More**  
  Select to display the additional commands.
  + **AND**  
    Select to apply the logical operator "AND" between two adjacent expressions. If this line is the last line in the expression list, when you select this option, Designer appends a new line to the end of the list as well.
  + **OR**  
    Select to apply the logical operator "OR" between two adjacent expressions. If this line is the last line in the expression list, when you select this option, Designer appends a new line to the end of the list as well.
  + **Insert Row**  
    Select to insert a new line after the current line.
  + **Delete Row**  
    Select to delete the current line.
  + **New Group**  
    Select to add a new expression group to the list. You can specify the relationship between two groups as one of the following:  
    - **AND**  
      Select to apply the logical operator "AND" between two adjacent groups to retrieve records that satisfy both condition groups.
    - **OR**  
      Select to apply the logical operator "OR" between two adjacent groups to retrieve records that satisfy either one of the condition groups.
    - **AND NOT**  
      Select it to retrieve records which satisfy the first condition group but not the second.
    - **OR NOT**  
      Select it to retrieve records which satisfy the first condition group, or which do not satisfy the second condition group.

**Column Level Security tab**

You can specify the column level security settings of the security entry in this tab.

* **Select Column**  
  Select to specify the columns that you want to show or hide from the principal.
* **Allow all**  
  Select to reveal all the columns in the field box to the principal, no matter whether its parent groups/roles allow them.
* **Deny all**  
  Select to hide all the columns in the field box from the principal, no matter whether its parent groups/roles allow them.
* **Allow**  
  Select to reveal the specified columns in the field box to the principal, no matter whether its parent groups/roles allow them.
* **Deny**  
  Select to hide the specified columns in the field box from the principal, no matter whether its parent groups/roles allow them.
* **Field box**  
  This box lists all the data fields in the current catalog data source. Select or clear the fields that you want to show or hide from the principal.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567555223-Search-Reports-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735515319191-Security-Configuration-Setting-Dialog-Box)
