---
title: "Folder Properties"
id: 1500009689002
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009689002-Folder-Properties
updated_at: 2021-11-03T06:57:38Z
---

# Folder Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714661-Enter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688722-JDashboard-Profile)

# Folder Properties

The Folder Properties dialog helps you to [set the properties of a selected folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009717861-Changing-Resource-Properties). It contains the following two tabs: [General](#General) and [Permission](#Permission).

**OK**

Retains the settings and submits the task to server.

**Cancel**

Cancels any settings and closes the dialog.

**Reset**

Discards your modifications and restores the dialog to its default status.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the folder.

![Folder Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131465111/prptyfldr_gen.gif)

**Resource Path**

Shows the resource path.

**Resource Node Name**

Specifies the name for the folder.

**Resource Type**

Shows the type of the resource.

**Resource Description**

Specifies description of the folder.

**Resource Real Path**

Specifies the real path of the folder.

**Last Modified**

Shows the last time the folder was modified. This option is available to administrators.

**Enable Resources from Real Paths**

Specifies whether or not to enable getting resources from the folder's real path. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path. For more information, refer to [Getting and Using Resources from a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009717881-Getting-and-Using-Resources-from-a-Real-Path).

**Note:** This option can only be checked when the Enable Resources from Real Paths option in the Administration > Configuration > Advanced page of the server console has also been checked.

**[Custom Field Name]**

Specifies value of the custom field for the folder. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Enable Linked Catalog**

Enables to link the folder with a catalog.

If you have specified a linked catalog for the folder, then reports/library components and sub folders resided in the folder can inherit the linked catalog from the folder once their Enable Linked Catalog property is enabled.

If this option is unchecked, the reports/library components and sub folders resided in the folder cannot inherit linked catalog.

* **Use Specified**  
   Links the folder with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009715141-Select-Another-Catalog) dialog.
* **Use Inherited**  
   Links the folder with the linked catalog inherited from its parent folder or from the server level if the folder is a [built-in resource folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009717721-Managing-Resources#Folder). Note that if the parent level does not enable linked catalog, you are not allowed to check this option.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009717941-Applying-an-Archive-Policy) to resource versions in the folder.

* **Archive as New Version**  
   Specifies to use multiple versions for the resources in the folder.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the resources. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

## Permission

Specifies permissions of roles/users/groups on the folder. Folder permissions can be inherited by the files and sub folders in the folder. This tab is available when the folder is in a public folder and when you have the Grant permission on the folder.

![Folder Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4412131466263/prptyfldr_prmsn.gif)

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

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) you would like the role/user/group to have on the folder.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714661-Enter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688722-JDashboard-Profile)
