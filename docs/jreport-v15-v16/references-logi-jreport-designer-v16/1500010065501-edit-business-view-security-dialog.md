---
title: "Edit Business View Security Dialog"
id: 1500010065501
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065501-Edit-Business-View-Security-Dialog
updated_at: 2021-07-24T10:38:59Z
---

# Edit Business View Security Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065481-Edit-Aggregation-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030382-Edit-Color-Dialog)

# Edit Business View Security Dialog

The Edit Business View Security dialog helps you to [define security](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security#Configure) for business views in a catalog. It appears when you do one of the following:

* Select Menu > Tools > Security Configuration in the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog).
* In the Catalog Manager, navigate to a data source > Security, right-click Business View Security, and then select Edit Business View Security from the shortcut menu.

![Edit Business View Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901270295/edtbvscrty.gif)

The following are details about options in the dialog:

**Users/Groups/Roles**

Lists all the users, roles and groups (also referred to as principals) for the security policy. You can select one or more of them.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a principal. After you select the button, a drop-down menu will be shown:
  + **Add User**  
     Creates a new user in the [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500010064761-Add-User-Dialog) dialog.
  + **Add Group**  
     Creates a new group in the [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010064681-Add-Group-Dialog) dialog.
  + **Add Role**  
     Creates a new role in the [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500010029722-Add-Role-Dialog) dialog.
  + **Import from Logi JReport Server**  
     Imports principals from a started Logi JReport Server. If Logi JReport Designer cannot connect to the server and log you in automatically, you will be prompted with the [Connect to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog) dialog to specify the properties for connecting with the server first.
  + **Import from File**  
     Imports principals from an xml file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404909158167/btn_expt2fl.gif)  
   Exports the principals defined in the security policy to an xml file.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Deletes the selected principal. The everyone role cannot be deleted, and it by default has the Access and Visible permissions on all the data fields.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif)  
   Edits the selected principal in the displayed dialog.
* **![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404901270551/btn_srchusr.gif)**  
   Type in text in the toolbar to search for principals in the list box below. The names containing the matched text will be shown.
* ![Drop-down Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404909226263/btn_drpdwn.gif)  
   The drop-down menu provides the following options:
  + **Select Role**  
     Selects all the roles in the list box below.
  + **Select Group**  
     Selects all the groups in the list box below.
  + **Select User**  
     Selects all the users in the list box below.

**Resources**

Lists all the business views in the current catalog data source. You can select one or more of the resources.

* **![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404901270807/btn_srchrsc.gif)**  
   Searches for resources in the resource tree below. The names containing the matched text will be shown.
* ![Drop-down menu button](https://devnet.logianalytics.com/hc/article_attachments/4404909226263/btn_drpdwn.gif)  
   The drop-down menu provides the following options:
  + **Select Group**  
     Selects all the group objects in the resource tree below.
  + **Select Aggregation**  
     Selects all the aggregation objects in the resource tree below.
  + **Select Detail**  
     Selects all the detail objects in the resource tree below.
  + **Select Category**  
     Selects all the categories in the resource tree below.

**Security Options**

* **Use Default**  
   Specify whether to use the default security settings of the selected fields. Uncheck it to specify the data security and resource security for the selected fields.
* **Set as Default**  
   The option is enabled when Use Default is unchecked and only one principal and one field is selected. It saves the current data security and resource security settings as the selected field's default security settings.

**Data Security**

* **Access**  
   Specifies whether the values of the selected fields are available to the selected principals. Without the Access permission, when the principals run reports which contain objects such as dynamic formulas and filters that reference the selected fields, these objects will not be able to get values from the fields and instead get a null value.

  The Access permission can be set to Allow, Deny, or unknown (neither Allow nor Deny).

  If a principal's Access permission on a field finally turns out to be unknown after inheriting permissions from the parent principals, the principal's Access permission on the field will be regarded as Deny.

* **Allowed Set**  
   The option is enabled when a group field is selected. It specifies the members of the selected group field which the selected principals are allowed to access. It could be <All>, some members of the group field, a condition that retrieves certain members, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif)  
     Edits the allowed members in the [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010030642-Edit-Values-Dialog) dialog.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
     Deletes the specified members or condition.
* **Denied Set**  
   The option is enabled when a group field is selected. It specifies the members of the selected group field which the selected principals are not allowed to access. It could be <All>, some members of the group field, a condition, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif)  
     Edits the denied members in the [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010030642-Edit-Values-Dialog) dialog.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
     Deletes the specified members or condition.
* **Allow Unspecified Members**  
   The option is available when users and a group field is selected. It specifies whether the unspecified members are available to the users. The unspecified members here mean the members of the group field that are not specified in its allowed/denied set for the users or in the inherited allowed/denied set from the parents.

**Resource Security**

* **Visible**  
   Specifies whether the selected fields are visible to the selected principals. Can be set to Allow, Deny, or unknown (neither Allow nor Deny).

  If a principal's Visible permission on a field finally turns out to be unknown after inheriting permissions from the parent principals, the principal's Visible permission on the field will be regarded as Deny.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065481-Edit-Aggregation-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030382-Edit-Color-Dialog)
