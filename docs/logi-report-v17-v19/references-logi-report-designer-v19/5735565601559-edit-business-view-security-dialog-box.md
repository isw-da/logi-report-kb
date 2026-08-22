---
title: "Edit Business View Security Dialog Box"
id: 5735565601559
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735565601559-Edit-Business-View-Security-Dialog-Box
updated_at: 2022-11-02T04:14:54Z
---

# Edit Business View Security Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513687703-Edit-Aggregation-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513694231-Edit-Color-Dialog-Box)

# Edit Business View Security Dialog Box

You can use the Edit Business View Security dialog box to [define security](https://devnet.logianalytics.com/hc/en-us/articles/5735526952343-Configuring-Business-View-Security-in-a-Catalog) for business views in a catalog. This topic describes the options in the dialog box.

Designer displays the Edit Business View Security dialog box when you do one of the following:

* Navigate to Menu > Tools > Security Configuration in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box).
* In the Catalog Manager, navigate to a data source > Security, right-click Business View Security, and then select Edit Business View Security from the shortcut menu.

![Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898481831831/edtbvscrty.gif)

Designer displays these options:

**Users/Groups/Roles**

This panel lists all the users, roles, and groups (that is, the principals) for the security policy. You can select one or more of them.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
  Select to add a principal. After you select this button, Designer displays a drop-down menu which contains the following commands:
  + **Add User**  
    Select to create a user in the [Add User dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735528371479-Add-User-Dialog-Box).
  + **Add Group**  
    Select to create a group in the [Add Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735564962583-Add-Group-Dialog-Box).
  + **Add Role**  
    Select to create a role in the [Add Role dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735564993175-Add-Role-Dialog-Box).
  + **Import from Logi Report Server**  
    Select to import principals from a started Server. If Designer cannot connect to the Server and sign you in automatically, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the connection and user information first.
  + **Import from File**  
    Select to import principals from an XML file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9898478126743/btn_expt2fl.gif)**Export button**  
  Select to export the principals defined in the security policy to an XML file.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the selected principal. You cannot delete the "everyone" role, and it by default has the Access and Visible permissions on all the data fields.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
  Select to edit the selected principal in the displayed dialog box.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9898481836567/btn_srchusr.gif)**Search box**  
  Type the keyword in the box and Designer lists the principals containing the matched text.
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/9898462307735/btn_down1.gif)**Down button**  
  Select to display the drop-down menu which contains the following options:
  + **Select Role**  
    Select to select all the roles in the list box.
  + **Select Group**  
    Select to select all the groups in the list box.
  + **Select User**  
    Select to select all the users in the list box.

**Resources**

This box lists all the business views in the current catalog data source. You can select one or more of the resources.

* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9898464790935/btn_srchrsc.gif)**Search box**  
  Type the keyword in the box and Designer lists the resources containing the matched text.
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/9898462307735/btn_down1.gif)**Down button**  
  Select to display the drop-down menu which contains the following options:
  + **Select Group**  
    Select to select all the group objects in the resource tree.
  + **Select Aggregation**  
    Select to select all the aggregation objects in the resource tree.
  + **Select Detail**  
    Select to select all the detail objects in the resource tree.
  + **Select Category**  
    Select to select all the categories in the resource tree.

**Security Options**

* **Use Default**  
  Select to use the default security settings of the selected fields. Clear it if you want to specify the data security and resource security for the selected fields.
* **Set as Default**  
  Designer enables this option when you clear Use Default and select only one principal and one field. Select it to save the current data security and resource security settings as the selected field's default security settings.

**Data Security**

* **Access**  
  Specify whether the values of the selected fields are available to the selected principals. Without the Access permission, when the principals run reports which contain objects such as dynamic formulas and filters that reference the selected fields, these objects are not able to get values from the fields and instead get a null value.

  You can set the Access permission to Allow, Deny, or unknown (neither Allow nor Deny).

  If a principal's Access permission on a field finally turns out to be unknown after inheriting permissions from the parent principals, the principal's Access permission on the field is regarded as Deny.

* **Allowed Set**  
  Designer enables this option when you select a group object in the Resources box. Use it to specify which members of the selected group object the selected principals are allowed to access. It can be <All>, some members of the group object, a condition that retrieves certain members, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
    Select to edit the allowed members in the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522699799-Edit-Values-Dialog-Box).
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
    Select to delete the specified members or condition.
* **Denied Set**  
  Designer enables this option when you select a group object in the Resources box. Use it to specify which members of the selected group field the selected principals are not allowed to access. It can be <All>, some members of the group object, a condition, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
    Select to edit the denied members in the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522699799-Edit-Values-Dialog-Box).
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
    Select to delete the specified members or condition.
* **Allow Unspecified Members**  
  Designer displays this option when you select users and a group object. You can use it to specify whether you want the unspecified members available to the users. The unspecified members mean the members of the group object that are not specified in its allowed/denied set for the users or in the inherited allowed/denied set from the parents.

**Resource Security**

* **Visible**  
  Specify whether the selected fields are visible to the selected principals. It can be Allow, Deny, or unknown (neither Allow nor Deny).

  If a principal's Visible permission on a field finally turns out to be unknown after inheriting permissions from the parent principals, the principal's Visible permission on the field is regarded as Deny.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513687703-Edit-Aggregation-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513694231-Edit-Color-Dialog-Box)
