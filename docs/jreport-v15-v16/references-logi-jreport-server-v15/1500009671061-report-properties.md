---
title: "Report Properties"
id: 1500009671061
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009671061-Report-Properties
updated_at: 2021-07-24T20:54:45Z
---

# Report Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646742-Publish-to-Remote-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671141-Resource-Allocation)

# Report Properties

The Report Properties dialog helps you to [set the properties of a specified report](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties) and contains the following two tabs:

* [General](#General)
* [Permission](#Permission)

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

Specifies the general properties of the report. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926736279/prptyrptst_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the report.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies the description for the report.

**Status**

Specifies the status of the report. If not specified, the status will be Active by default.

* **Active**  
   The report can be run, advanced run and scheduled.
* **Inactive**  
   The report cannot be run, advanced run or scheduled.
* **Incomplete**  
   The report is not completely designed and cannot be run, advanced run or scheduled.

**National Language Support**

Specifies whether to enable the NLS feature for the report. This option is available when the Properties dialog is opened from the Logi JReport Administration page.

**[Custom Field Name]**

Specifies value of the custom field for the report. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009648802-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Choose Profile**

Specifies the Page Report Studio profile to be applied to run the report which contains [a set of Page Report Studio settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009646402-Page-Report-Studio-Profile). This option is available when the Properties dialog is opened from the Logi JReport Administration page.

**Enable Linked Catalog**

Enables to link the report with a catalog. Once a report is linked with a catalog, even if the report and the catalog are not in the same directory, it can still be run with the catalog.

When you background run, advanced run or schedule the report, the linked catalog is applied instead of the catalog that is resided in the parent folder and originally used to run the report. For Advanced Run and Schedule, you can change the catalog to another one using the Select Another Catalog option in the General tab of the corresponding dialog.

* **Use Specified**  
   Links the report with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009646822-Select-Another-Catalog) dialog.
* **Use Inherited**   
   Links the report with the linked catalog inherited from its parent folder. Note that if the parent folder does not enable linked catalog, you are not allowed to check this option.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy) to the report versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the report.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the report. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Permission

Specifies permissions of roles/users/groups on the report. This tab is available when the report is in the Public Reports folder. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920562967/prptyrptst_prmsn.gif)

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

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) you would like the role/user/group to have on the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646742-Publish-to-Remote-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671141-Resource-Allocation)
