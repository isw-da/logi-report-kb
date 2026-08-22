---
title: "Folder Properties"
id: 1500009774401
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774401-Folder-Properties
updated_at: 2021-07-24T00:48:42Z
---

# Folder Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774001-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746042-JDashboard-Profile-Properties)

# Folder Properties

This topic describes how you can use the Folder Properties dialog box to [set the properties of a selected folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009748702-Changing-Resource-Properties).

This topic contains the following sections:

* [General Tab Properties](#General)
* [Permission Tab Properties](#Permission)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

**Reset**

Select **Reset** to restore the dialog box to its default status.

**Help**

Select **Help** to view information about the Folder Properties dialog box.

## General Tab Properties

Specifies the general properties of the folder.

![Folder Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880419991/prptyfldr_gen.gif)

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

Specifies whether to enable getting resources from the folder's real path. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path. For more information, see [Getting and Using Resources from a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009777261-Getting-and-Using-Resources-From-a-Real-Path).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)You can select this option only when an admin user has selected the **Enable Resources from Real Paths** option in the Administration > Configuration > Advanced page in the Server Console.

**[Custom Field Name]**

Specifies value of the custom field for the folder. A [custom field](https://devnet.logianalytics.com/hc/en-us/articles/1500009748662-Working-with-Custom-Fields) can be regarded as a resource property and is available when it is enabled.

**Enable Linked Catalog**

Enables to link the folder with a catalog.

If you have specified a linked catalog for the folder, then reports/library components and subfolders resided in the folder can inherit the linked catalog from the folder once their Enable Linked Catalog property is enabled.

If this option is unselected, the reports/library components and subfolders resided in the folder cannot inherit linked catalog.

* **Use Specified**  
   Links the folder with a catalog in the server resource tree.
  + **Select Another Catalog**  
     Specifies another catalog in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009746402-Select-Another-Catalog-Dialog-Box-Properties) dialog box.
* **Use Inherited**  
   Links the folder with the linked catalog inherited from its parent folder or from the server level if the folder is a [built-in resource folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009777141-Managing-Resources#Folder).

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If the parent level does not enable linked catalog, you cannot select this option.

**Apply Archive Policy**

Applies an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009748742-Applying-an-Archive-Policy) to resource versions in the folder.

* **Archive as New Version**  
   Specifies to use multiple versions for the resources in the folder.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the resources. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

## Permission Tab Properties

Specifies permissions of roles/users/groups on the folder. Folder permissions can be inherited by the files and subfolders in the folder. This tab is available when the folder is in a public folder and when you have the Grant permission on the folder.

![Folder Properties dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4404880420375/prptyfldr_prmsn.gif)

**Enable Setting Permissions**

Enables the setting of permissions.

**Available**

Lists the roles/users/groups to which you can assign permissions.

* **Role**  
   If the option is selected, all roles will be displayed in the Available box for you to assign permissions.
* **User**  
   If the option is selected, all users will be displayed in the Available box for you to assign permissions.
* **Group**  
   If the option is selected, all groups will be displayed in the Available box for you to assign permissions.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880219927/btn_add.gif)

Adds the selected role, user, or group to the Selected box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880220567/btn_rmv.gif)

Removes the selected role, user, or group from the Selected box.

**Selected**

Select a role/user/group in the Selected box and then select the [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) you would like the role/user/group to have on the folder.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774001-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746042-JDashboard-Profile-Properties)
