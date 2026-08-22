---
title: "Multiple Type Properties"
id: 5741427584151
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741427584151-Multiple-Type-Properties
updated_at: 2022-10-31T17:17:03Z
---

# Multiple Type Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741420798871-Login-Server-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741427157143-New-Cache-Dialog-Box-Properties-for-Connection-Data)

# Multiple Type Properties

This topic describes how you can use the Multiple Type Properties dialog box to [set the properties for multiple resources](https://devnet.logianalytics.com/hc/en-us/articles/5741438178199-Changing-Resource-Properties).

This topic contains the following sections:

* [General Tab Properties](#General)
* [Permission Tab Properties](#Permission)

You see these elements on both tabs:

**N Resources Selected**

Select to show or hide the resources you have selected.

**OK**

Select to apply any changes you made here.

**Cancel**

Select to close the dialog box without saving any changes.

**Reset**

Select to restore the dialog box to its default status.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the resources.

![Multiple Type Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905757858967/prptymltpl_gen.gif)

**Resource Path**

Server shows "Different Path" by default.

**Resource Node Name**

Server shows "Multiple Resources Names" by default.

**Resource Type**

Server shows "Multiple Type" by default.

**Resource Description**

Specify the description for all the selected resources.

**Status**

Specify the status of report resources.

* **Active**  
   You can run, advanced run, and schedule to run the reports.
* **Inactive**  
   You cannot run, advanced run, and schedule to run the reports.
* **Incomplete**  
   You have not finished designing the reports. You cannot run, advanced run, and schedule to run the reports.

**Enable Linked Catalog**

Select to link the selected resources with a catalog. This property is not available when the selected resources are in the root of the server resource tree.

When you link a resource with a catalog, even if the resource and the catalog are not in the same folder, Server can still run the resource with the catalog.

This property works on reports, library components, and folders. When you link a folder with a catalog, reports, library components, and folders in the folder can then inherit the linked catalog from the folder once you enable their Enable Linked Catalog properties.

* **Use Specified**  
   Select to link the resources with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Select to open the [Select Another Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741433783191-Select-Another-Catalog-Dialog-Box-Properties), and then select another catalog.
* **Use Inherited**   
   Select to link the resources with the linked catalog inherited from their parent folder.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)You cannot select this property if the parent folder of the selected resources does not enable linked catalog.

**Apply Archive Policy**

Select to apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy) to versions of the selected resources.

* **Archive as New Version**  
   Select to enable multiple versions for the resources.
  + **Maximum Number of Versions**  
     Specify the maximum number of versions that a resource can have. The default value 0 means unlimited version number.
* **Replace Old Version**  
   Select to replace the old version with the new version.

## Permission Tab Properties

Specify [permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) of roles/users/groups on the selected resources. This tab is available when the resources are in a public folder, and if you have the Grant permission on the selected resources.

![Multiple Type Properties dialog box - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/9905757881367/prptymltpl_prmsn.gif)

**Enable Setting Permissions**

Select if you want to set user permissions on the selected resources.

**Available**

Server lists the roles/users/groups to which you can assign permissions. You can search for items in the Available box by using the search box.

* **Role**  
   Select if you want to display roles in the Available box.
* **User**  
   Select if you want to display users in the Available box.
* **Group**  
   Select if you want to display groups in the Available box.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905636390807/btn_add.gif) **Add button**

Select to add the selected role, user, or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905657793175/btn_rmv.gif) **Remove button**

Select to remove the selected role, user, or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box, and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) you would like the role/user/group to have on the resources.

You can search for items in the Selected box by using the search box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741420798871-Login-Server-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741427157143-New-Cache-Dialog-Box-Properties-for-Connection-Data)
