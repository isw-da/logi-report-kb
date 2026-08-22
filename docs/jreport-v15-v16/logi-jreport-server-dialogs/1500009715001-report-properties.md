---
title: "Report Properties"
id: 1500009715001
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009715001-Report-Properties
updated_at: 2021-11-03T06:57:38Z
---

# Report Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009688922-Publish-to-Remove-Server-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715041-Resource-Allocation)

# Report Properties

The Report Properties dialog helps you to [set the properties of a specified report](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties). It contains the following two tabs: [General](#General) and [Permission](#Permission). Some options are disabled or only available when the report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports).

**OK**

Retains the settings and submits the task to server.

**Cancel**

Cancels any settings and closes the dialog.

**Reset**

Discards your modifications and restores the dialog to its default status.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the report.

![Report Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412139566487/prptyrpt_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the report. Disabled for a shared report.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies the description for the report.

**Status**

Specifies the status of the report. If not specified, the status will be Active by default. This option is unavailable to a shared report.

* **Active**  
   The report can be run, advanced run and scheduled.
* **Inactive**  
   The report cannot be run, advanced run or scheduled.
* **Incomplete**  
   The report is not completely designed and cannot be run, advanced run or scheduled.

**National Language Support**

Specifies whether to enable the NLS feature for the report. This option is available to administrators when the report is not a shared report.

**[Custom Field Name]**

Specifies value of the custom field for the report. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Choose Profile**

Specifies the Page Report Studio profile to be applied to run the report which contains [a set of Page Report Studio settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009688622-Page-Report-Studio-Profile). This option is available to administrators when the report is a page report.

**Enable Linked Catalog**

Enables to link the report with a catalog. Once a report is linked with a catalog, even if the report and the catalog are not in the same directory, it can still be run with the catalog. This option is unavailable to a shared report.

When you background run, advanced run or schedule the report, the linked catalog is applied instead of the catalog that is resided in the parent folder and originally used to run the report. For Advanced Run and Schedule, you can change the catalog to another one using the Select Another Catalog option in the General tab of the corresponding dialog.

* **Use Specified**  
   Links the report with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009715141-Select-Another-Catalog) dialog.
* **Use Inherited**   
   Links the report with the linked catalog inherited from its parent folder. Note that if the parent folder does not enable linked catalog, you are not allowed to check this option.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009717941-Applying-an-Archive-Policy) to the report versions. Unavailable to a shared report.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the report.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the report. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

**Allow Edit**

Available when the report is a shared report. It shows whether the report owner allows other users to edit the shared report.

## Permission

Specifies permissions of roles/users/groups on the report. This tab is available when the report is in a public folder and when you have the Grant permission on the report.

![Report Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4412131461143/prptyrpt_prmsn.gif)

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

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112531223/btn_add.gif)

Adds the selected role, user or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112531735/btn_rmv.gif)

Removes the selected role, user or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) you would like the role/user/group to have on the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009688922-Publish-to-Remove-Server-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715041-Resource-Allocation)
