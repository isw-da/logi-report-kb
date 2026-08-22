---
title: "Security Dialog Box"
id: 1500010060282
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060282-Security-Dialog-Box
updated_at: 2021-07-23T19:15:55Z
---

# Security Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098901-Search-Reports-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098561-Security-Configuration-Setting-Dialog-Box)

# Security Dialog Box

The Security dialog box helps you to specify the security settings for a [data source security entry](https://devnet.logianalytics.com/hc/en-us/articles/1500010094221-Working-with-RLS-and-CLS-at-Data-Source-Scope#Create). It appears when you right-click Security Entry in the Data Source > Security node in the Catalog Manager, select New Security Entry from the shortcut menu, type a name for the new security policy and then select OK.

![Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856896919/scrty.gif)

The following are details about options in the dialog box:

**Users/Groups/Roles**

Lists all the users, roles, groups for the security policy.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)  
  Adds a user/group/role. After you select the button, a drop-down menu will be shown:
  + **Add User**  
    Creates a new user in the [Add User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095561-Add-User-Dialog-Box).
  + **Add Group**  
    Creates a new group in the [Add Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010057942-Add-Group-Dialog-Box).
  + **Add Role**  
    Creates a new role in the [Add Role dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095501-Add-Role-Dialog-Box).
  + **Import from Logi Report Server**  
    Opens the [Import from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059582-Import-from-Logi-Report-Server-Dialog-Box) to import users, roles, and groups from Server.
  + **Import from File**  
    Imports users, roles, and groups from an xml file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404856897303/btn_expt2fl.gif)**Export button**  
  Exports the users, roles, and groups to an xml file.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Deletes the selected user/group/role.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
  Edits the selected user/role/group in the displayed dialog box.
* **Search box**   
  Type the keyword in the box and Designer lists the users/roles/groups containing the matched text.

**Valid RLS**

Specifies whether to use RLS policy for this security entry. If the option is unselected, the RLS policy will not be applied and all the records will be available to the users.

**Valid CLS**

Specifies whether to use CLS policy for this security entry. If the option is unselected, the CLS policy will not be applied and all the records will be available to the users.

**Disable Policy Settings**

* When it is unselected, you are able to specify a security policy for the principal. However, if the record level security and column level security are left blank, the principal will not be able to view any data records, unless it inherits some permissions from another group or role.
* When it is selected, you are not allowed to specify record level security or column level security. The principal will have full access to all the data records in the reports which adopt this security policy entry.

**Record Level Security tab**

Specifies the condition statements.

* **Expression**  
  Specifies the field on which the condition is based. You can type the name of the field in the text box or select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the text box to select the desired field.
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
  Specifies the value of how to build the condition. You can type the value in the text box manually or select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the value text box to specify the value.
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

Accepts changes and closes the dialog box.

**Cancel**

Does not retain the changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098901-Search-Reports-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098561-Security-Configuration-Setting-Dialog-Box)
