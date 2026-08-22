---
title: "Multiple Type Properties"
id: 28891579808013
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891579808013-Multiple-Type-Properties
updated_at: 2026-02-26T02:12:25Z
source_host: docs-report.zendesk.com
---
# 
Multiple Type Properties

This topic describes how you can use the Multiple Type Properties dialog box to set the properties for multiple resources.

This topic contains the following sections:

- General Tab Properties

- Permission Tab Properties

You see these elements on both tabs:

N Resources Selected

Select to show or hide the resources you have selected.

OK

Select to apply any changes you made here.

Cancel

Select to close the dialog box without saving any changes.

Reset

Select to restore the dialog box to its default status.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Specify the general properties of the resources.

Resource Path

Server shows "Different Path" by default.

Resource Node Name

Server shows "Multiple Resources Names" by default. 

Resource Type

Server shows "Multiple Type" by default. 

Resource Description

Specify the description for all the selected resources.

Status

Specify the status of report resources. 

- 
Active
  You can run, advanced run, and schedule to run the reports.

- 
Inactive
 You cannot run, advanced run, and schedule to run the reports.

- 
Incomplete
 You have not finished designing the reports. You cannot run, advanced run, and schedule to run the reports.

Enable Linked Catalog

Select to link the selected resources with a catalog. This property is not available when the selected resources are in the root of the server resource tree. 

When you link a resource with a catalog, even if the resource and the catalog are not in the same folder, Server can still run the resource with the catalog.

This property works on reports, library components, and folders. When you link a folder with a catalog, reports, library components, and folders in the folder can then inherit the linked catalog from the folder once you enable their Enable Linked Catalog properties.

- 
Use Specified
  Select to link the resources with a catalog in the server resource tree.
    - 
Select Another Catalog
      Select to open the Select Another Catalog dialog box, and then select another catalog.

- 
Use Inherited 
  Select to link the resources with the linked catalog inherited from their parent folder. You cannot select this property if the parent folder of the selected resources does not enable linked catalog.

Apply Archive Policy

Select to apply an archive policy to versions of the selected resources. 

- 
Archive as New Version
  Select to enable multiple versions for the resources.
    - 
Maximum Number of Versions
      Specify the maximum number of versions that a resource can have. The default value 0 means unlimited version number.

- 
Replace Old Version
  Select to replace the old version with the new version.

## 
Permission Tab Properties

Specify  permissions of roles/users/groups on the selected resources. This tab is available when the resources are in a public folder, and if you have the Grant permission on the selected resources.

Enable Setting Permissions

Select if you want to set user permissions on the selected resources.

Available

Server lists the roles/users/groups to which you can assign permissions. You can search for items in the Available box by using the search box.

- 
Role
 Select if you want to display roles in the Available box.

- 
User
 Select if you want to display users in the Available box.

- 
Group
    Select if you want to display groups in the Available box.

 Add button

Select to add the selected role, user, or group to the Selected box.

 Remove button

Select to remove the selected role, user, or group from the Selected box.

Selected

Select a role/user/group in the Selected box, and then select the permissions you would like the role/user/group to have on the resources. 

You can search for items in the Selected box by using the search box.
