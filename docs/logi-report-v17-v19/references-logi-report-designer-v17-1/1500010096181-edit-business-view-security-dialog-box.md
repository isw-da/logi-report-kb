---
title: "Edit Business View Security Dialog Box"
id: 1500010096181
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096181-Edit-Business-View-Security-Dialog-Box
updated_at: 2021-07-23T19:15:15Z
---

# Edit Business View Security Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096161-Edit-Aggregation-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096201-Edit-Color-Dialog-Box)

# Edit Business View Security Dialog Box

You can use the Edit Business View Security dialog box to [define security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094161-Configuring-Business-View-Security-in-a-Catalog) for business views in a catalog. This topic describes the options in the dialog box.

Designer displays the Edit Business View Security dialog box when you do one of the following:

* Select Menu > Tools > Security Configuration in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058122-Business-View-Editor-Dialog-Box).
* In the Catalog Manager, navigate to a data source > Security, right-click Business View Security, and then select Edit Business View Security from the shortcut menu.

![Edit Business View Security dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856978967/edtbvscrty.gif)

You see the following options in the dialog box:

**Users/Groups/Roles**

The panel lists all the users, roles, and groups (that is, the principals) for the security policy. You can select one or more of them.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to add a principal. After you select the button, Designer displays a drop-down menu which contains the following options:
  + **Add User**  
    Select to create a user in the [Add User](https://devnet.logianalytics.com/hc/en-us/articles/1500010095561-Add-User-Dialog-Box) dialog.
  + **Add Group**  
    Select to create a group in the [Add Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010057942-Add-Group-Dialog-Box) dialog.
  + **Add Role**  
    Select to create a role in the [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/1500010095501-Add-Role-Dialog-Box) dialog.
  + **Import from Logi Report Server**  
    Select to import principals from a started Server. If Designer cannot connect to Server and log you in automatically, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the properties for connecting with Server first.
  + **Import from File**  
    Select to import principals from an XML file.
* ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404856897303/btn_expt2fl.gif)**Export button**  
  Select to export the principals defined in the security policy to an XML file.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the selected principal. You cannot delete the "everyone" role, and it by default has the Access and Visible permissions on all the data fields.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
  Select to edit the selected principal in the displayed dialog box.
* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404848587671/btn_srchusr.gif)**Search box**  
  Type the keyword in the box and Designer lists the principals containing the matched text.
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856922775/btn_down.gif)**Down button**  
  Select to display the drop-down menu which contains the following options:
  + **Select Role**  
    Select to select all the roles in the list box below.
  + **Select Group**  
    Select to select all the groups in the list box below.
  + **Select User**  
    Select to select all the users in the list box below.

**Resources**

The box lists all the business views in the current catalog data source. You can select one or more of the resources.

* ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404856979479/btn_srchrsc.gif)**Search box**  
  Type the keyword in the box and Designer lists the resources containing the matched text.
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856922775/btn_down.gif)**Down button**  
  Select to display the drop-down menu which contains the following options:
  + **Select Group**  
    Select to select all the group objects in the resource tree below.
  + **Select Aggregation**  
    Select to select all the aggregation objects in the resource tree below.
  + **Select Detail**  
    Select to select all the detail objects in the resource tree below.
  + **Select Category**  
    Select to select all the categories in the resource tree below.

**Security Options**

* **Use Default**  
  Select to use the default security settings of the selected fields. Clear the option if you want to specify the data security and resource security for the selected fields.
* **Set as Default**  
  Designer enables this option when you clear Use Default and select only one principal and one field. Select it to save the current data security and resource security settings as the selected field's default security settings.

**Data Security**

* **Access**  
  Specify whether the values of the selected fields are available to the selected principals. Without the Access permission, when the principals run reports which contain objects such as dynamic formulas and filters that reference the selected fields, these objects are not able to get values from the fields and instead get a null value.

  You can set the Access permission to Allow, Deny, or unknown (neither Allow nor Deny).

  If a principal's Access permission on a field finally turns out to be unknown after inheriting permissions from the parent principals, the principal's Access permission on the field is regarded as Deny.

* **Allowed Set**  
  Designer enables this option when you select a group object in the Resources box. Use it to specify which members of the selected group object the selected principals are allowed to access. It can be <All>, some members of the group object, a condition that retrieves certain members, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to edit the allowed members in the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096481-Edit-Values-Dialog-Box).
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified members or condition.
* **Denied Set**  
  Designer enables this option when you select a group object in the Resources box. Use it to specify which members of the selected group field the selected principals are not allowed to access. It can be <All>, some members of the group object, a condition, or null.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to edit the denied members in the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096481-Edit-Values-Dialog-Box).
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified members or condition.
* **Allow Unspecified Members**  
  Designer displays the option when you select users and a group object. Use it to specify whether you want the unspecified members available to the users. The unspecified members mean the members of the group object that are not specified in its allowed/denied set for the users or in the inherited allowed/denied set from the parents.

**Resource Security**

* **Visible**  
  Specify whether the selected fields are visible to the selected principals. It can be Allow, Deny, or unknown (neither Allow nor Deny).

  If a principal's Visible permission on a field finally turns out to be unknown after inheriting permissions from the parent principals, the principal's Visible permission on the field is regarded as Deny.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096161-Edit-Aggregation-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096201-Edit-Color-Dialog-Box)
