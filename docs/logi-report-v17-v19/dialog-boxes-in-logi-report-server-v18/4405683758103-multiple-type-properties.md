---
title: "Multiple Type Properties"
id: 4405683758103
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683758103-Multiple-Type-Properties
updated_at: 2022-01-27T07:59:05Z
---

# Multiple Type Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690549655-Login-Server-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683750039-New-Cache-Dialog-Box-Properties)

# Multiple Type Properties

This topic describes how you can use the Multiple Type Properties dialog box to [set the properties for multiple resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties).

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

![Multiple Type Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420461668247/prptymltpl_gen.gif)

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
     Select to open the [Select Another Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683770519-Select-Another-Catalog-Dialog-Box-Properties), and then select another catalog.
* **Use Inherited**   
   Select to link the resources with the linked catalog inherited from their parent folder.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)You cannot select this property if the parent folder of the selected resources does not enable linked catalog.

**Apply Archive Policy**

Select to apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/4405690645271-Applying-an-Archive-Policy) to versions of the selected resources.

* **Archive as New Version**  
   Select to enable multiple versions for the resources.
  + **Maximum Number of Versions**  
     Specify the maximum number of versions that a resource can have. The default value 0 means unlimited version number.
* **Replace Old Version**  
   Select to replace the old version with the new version.

## Permission Tab Properties

Specify [permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions) of roles/users/groups on the selected resources. This tab is available when the resources are in a public folder, and if you have the Grant permission on the selected resources.

![Multiple Type Properties dialog box - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4420461668503/prptymltpl_prmsn.gif)

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

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447121559/btn_add.gif) **Add button**

Select to add the selected role, user, or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461527319/btn_rmv.gif) **Remove button**

Select to remove the selected role, user, or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box, and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions) you would like the role/user/group to have on the resources.

You can search for items in the Selected box by using the search box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690549655-Login-Server-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683750039-New-Cache-Dialog-Box-Properties)
