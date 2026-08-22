---
title: "Multiple Type Properties"
id: 1500009671041
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009671041-Multiple-Type-Properties
updated_at: 2021-07-24T20:54:44Z
---

# Multiple Type Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671021-Library-Component-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646542-New-Cache)

# Multiple Type Properties

The Multiple Type Properties dialog helps you to [set the properties for multiple resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties) and contains the following two tabs:

* [General](#General)
* [Permission](#Permission)

**Resources Selected**

Shows/Hides the resources you have selected to edit the properties.

**OK**

Retains the settings and submits the task to server.

**Cancel**

Cancels any settings and closes the dialog.

**Reset**

Discards your modifications and restores the dialog to its default status.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## General

Specifies the general properties of the resources. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920563479/prptymltpl_gen.gif)

**Resource Path**

Shows Different Path by default.

**Resource Node Name**

Shows Multiple Resource Names by default.

**Resource Type**

Shows Multiple Type by default.

**Resource Description**

Specifies the resource description. Applies to all the selected resources.

**Status**

Specifies the report status. Applies to report resources only.

* **Active**  
   The reports can be run, advanced run and scheduled.
* **Inactive**  
   The reports cannot be run, advanced run or scheduled.
* **Incomplete**  
   The reports are not completely designed and cannot be run, advanced run or scheduled.

**Enable Linked Catalog**

Enables to link the selected resources with a catalog. Not available when the selected resources are on the root of the server resource tree.

This option works on report, library component and folder resources. For the folder resources, when they are linked with a catalog, reports/library components and sub folders resided in the folders can then inherit the linked catalog from the folders once their Enable Linked Catalog property is enabled.

When a resource is linked with a catalog, even if the resource and the catalog are not in the same directory, it can still be run with the catalog.

* **Use Specified**  
   Links the resources with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009646822-Select-Another-Catalog) dialog.
* **Use Inherited**   
   Links the resources with the linked catalog inherited from their parent folder. Note that if the parent folder of the selected resources does not enable linked catalog, you are not allowed to check this option.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy) to versions of the selected resources.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the resources.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version tables of the resources. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Permission

Specifies [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) of roles/users/groups on the selected resources. This tab is available when the resources are in the Public Reports or Public Components folder. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926736791/prptymltpl_prmsn.gif)

**Enable Setting Permissions**

Enables the setting of permissions.

**Available**

Lists the roles/users/groups to which you can assign permissions.

* **Role**  
   If checked, all roles will be displayed in the Available box for you to assign permissions.
* **User**  
   If checked, all users will be displayed in the Available box for you to assign permissions.
* **Group**  
   If checked, all groups will be displayed in the Available box for you to assign permissions.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected role, user or group to the Selected box.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)

Removes the selected role, user or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box and then select the permissions you would like the role/user/group to have on the resources.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671021-Library-Component-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646542-New-Cache)
