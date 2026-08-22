---
title: "Edit Business View Security Dialog"
id: 1500009565182
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565182-Edit-Business-View-Security-Dialog
updated_at: 2021-07-24T05:55:27Z
---

# Edit Business View Security Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586361-Edit-Aggregation-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565222-Edit-Color-Dialog)

# Edit Business View Security Dialog

The Edit Business View Security dialog appears when you do one of the following:

* Select Menu > Tools > Security Configuration in the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009564622-Business-View-Editor-Dialog).
* In the Catalog Manager, navigate to a data source > Security, right-click Business View Security, and then select Edit Business View Security from the shortcut menu.

It helps you to [define security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security) for business views. [See the dialog](javascript:%20void(null)).

![Edit Business View Security dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889277847/edtbvscrty.gif)

The following are details about options in the dialog:

**Users/Groups/Roles**

Lists all the users, roles and groups (also referred to as principals) for the security policy. You can select one or more of them.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a principal. After you select the button, a drop-down menu will be shown:
  + **Add User**  
     Creates a new user in the [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500009564502-Add-User-Dialog) dialog.
  + **Add Group**  
     Creates a new group in the [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009585561-Add-Group-Dialog) dialog.
  + **Add Role**  
     Creates a new role in the [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500009585601-Add-Role-Dialog) dialog.
  + **Import from Logi JReport Server**  
     Opens the [Connect to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog) dialog to import principals from Logi JReport Server.
  + **Import from File**  
     Imports principals from an xml file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404889278487/btn_expt2fl.gif)  
   Exports the principals defined in the security policy to an xml file.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Deletes the selected principal. The everyone role cannot be deleted, and it by default has the Access and Visible permissions on all the data fields.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
   Edits the selected principal in the displayed dialog.
* **![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404893927959/btn_srchusr.gif)**  
   Type in text in the toolbar to search for principals in the list box below. The names containing the matched text will be shown.
* ![Drop-down Menu button](https://devnet.logianalytics.com/hc/article_attachments/4404889278103/btn_drpdwn.gif)  
   The drop-down menu provides the following options:
  + **Select Role**  
     Selects all the roles in the list box below.
  + **Select Group**  
     Selects all the groups in the list box below.
  + **Select User**  
     Selects all the users in the list box below.

**Resources**

Lists all the business views in the current catalog data source. You can select one or more of the resources.

* **![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404889369111/btn_srchrsc.gif)**  
   Searches for resources in the resource tree below. The names containing the matched text will be shown.
* ![Drop-down menu button](https://devnet.logianalytics.com/hc/article_attachments/4404889278103/btn_drpdwn.gif)  
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
   The option is enabled when a group field is selected.
  It specifies the members of the selected group field which the selected principals are allowed to access. It could be <All>, some members of the group field, a condition that retrieves certain members, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Edits the allowed members in the [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009565422-Edit-Values-Dialog) dialog.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
     Deletes the specified members or condition.
* **Denied Set**  
   The option is enabled when a group field is selected.
  It specifies the members of the selected group field which the selected principals are not allowed to access. It could be <All>, some members of the group field, a condition, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
     Edits the denied members in the [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009565422-Edit-Values-Dialog) dialog.
  + ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586361-Edit-Aggregation-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565222-Edit-Color-Dialog)
