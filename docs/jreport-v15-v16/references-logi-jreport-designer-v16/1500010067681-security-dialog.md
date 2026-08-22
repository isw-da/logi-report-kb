---
title: "Security Dialog"
id: 1500010067681
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067681-Security-Dialog
updated_at: 2021-07-24T10:38:27Z
---

# Security Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032822-Search-Reports-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067701-Security-Configuration-Setting-Dialog)

# Security Dialog

The Security dialog helps you to specify the security settings for a [data source security entry](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security#Data). It appears when you right-click Security Entry in the Data Source > Security node in the Catalog Manager, select New Security Entry from the shortcut menu, input a name for the new security policy and then select OK.

![Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901183511/scrty.gif)

The following are details about options in the dialog:

**Users/Groups/Roles**

Lists all the users, roles, groups for the security policy.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a user/group/role. After you select the button, a drop-down menu will be shown:
  + **Add User**  
     Creates a new user in the [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500010064761-Add-User-Dialog) dialog.
  + **Add Group**  
     Creates a new group in the [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010064681-Add-Group-Dialog) dialog.
  + **Add Role**  
     Creates a new role in the [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500010029722-Add-Role-Dialog) dialog.
  + **Import from Logi JReport Server**  
     Opens the [Import from Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010066841-Import-from-JReport-Server-Dialog) dialog to import users, roles, and groups from Logi JReport Server.
  + **Import from File**  
     Imports users, roles, and groups from an xml file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404909158167/btn_expt2fl.gif)  
   Exports the users, roles, and groups to an xml file.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Deletes the selected user/group/role.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif)  
   Edits the selected user/role/group in the displayed dialog.
* **Search box**   
   It allows you to search for the user/role/group in the list below. Type in the text and the principals containing the matched text will be shown.

**Valid RLS**

Specifies whether to use RLS policy for this security entry. If unchecked, the RLS policy will not be applied and all the records will be available to the users.

**Valid CLS**

Specifies whether to use CLS policy for this security entry. If unchecked, the CLS policy will not be applied and all the records will be available to the users.

**Disable Policy Settings**

* When it is unchecked, you are able to specify a security policy for the principal. However, if the record level security and column level security are left blank, the principal will not be able to view any data records, unless it inherits some permissions from another group or role.
* When it is checked, you are not allowed to specify record level security or column level security. The principal will have full access to all the data records in the reports which adopt this security policy entry.

**Record Level Security tab**

Specifies the condition statements.

* **Expression**  
   Specifies the field on which the condition is based. You can type in the field directly or select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the text box to select the desired field.
* **Operator**  
   Specifies the operator to compose the condition expression.  
  + **=**  
     Equal to
  + **>**  
     Greater than
  + **<**  
     Less than
  + **>=**  
     Greater than or equal to
  + **<=**  
     Less than or equal to
  + **<>**  
     Not equal to
  + **in**  
     Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in", multiple values separated by comma (,) are allowed.
* **Value**  
   Specifies the value of how to build the condition. You can type in the value manually or select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the value text box to specify the value.
* **More**  
   Lists some additional commands.
  + **AND**  
     Specifies the relationship between two expression statements as logical AND. If this line is the last line in the expression list, when you select AND or OR, and a new line will be appended to the end of the list as well.
  + **OR**  
     Specifies the relationship between two expression statements as logical OR. If this line is the last line in the expression list, when you select AND or OR, and a new line will be appended to the end of the list as well.
  + **Insert Row**  
     Inserts a new line after the current line.
  + **Delete Row**  
     Deletes the current line.
  + **New Group**  
     Adds a new expression group to the list. The relationships between two groups can be:  
    - **AND**- Logical AND relationship between two groups. Records satisfying both condition groups will be retrieved.
    - **OR**- Logical OR relationship between two groups. Records satisfying either one of the condition groups will be retrieved.
    - **AND NOT** - Records which satisfy the first condition group but not the second will be retrieved.
    - **OR NOT** - Records which satisfy the first condition group, or which do not satisfy the second condition group will be retrieved.

**Column Level Security tab**

Lists all the available resources in the catalog. Select the required resources to allow or deny them to be revealed to the principal.

* **Select Column**  
   Specifies the columns that are to be shown to (or hidden from) the principal.
* **Allow all**  
   Allows all the columns in the field list to be revealed to the principal no matter whether the parent groups/roles allow them.
* **Deny all**  
   Hides all the columns in the field list from the principal no matter whether the parent groups/roles allow them.
* **Allow**  
   Allows the selected columns in the field list to be revealed to the principal no matter whether the parent groups/roles allow them. Whether the principal can see the unselected columns depends on whether the parent groups/roles allow them.
* **Deny**  
   Hides the selected columns in the field list from the principal no matter whether the parent groups/roles allow them. Whether the principal can see the unselected columns depends on whether the parent groups/roles allow them.

**OK**

Accepts changes and closes the dialog.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032822-Search-Reports-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067701-Security-Configuration-Setting-Dialog)
