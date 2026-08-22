---
title: "Publish from Local Directory Dialog Box Properties"
id: 5741427653783
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741427653783-Publish-from-Local-Directory-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:03Z
---

# Publish from Local Directory Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/5741442976407-Preference-Dialog-Box-Properties-)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741421379351-Publish-from-Server-Machine-Dialog-Box-Properties)

# Publish from Local Directory Dialog Box Properties

This topic describes how you can use the Publish from Local Directory dialog box to publish resources to the Logi Report Server resource tree [from a local directory](https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources#LocalDir).

Server displays the dialog box when you select **Publish >** From Local Directory on the task bar of the Resources page on the Server Console.

![Publish from Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/9905676071703/pubfrmdir.gif)

**Publish Resource To**

Server shows the folder in the server resource tree, which you will publish resources to.

**From Zipped File**

Specify where you want to get resources. Select **Browse** to specify the location.

**Publish files and folders in the zipped file to /XXX**

Select to publish files and folders in the zipped file to /XXX directly.

When this option is cleared, the following properties are available, which are the properties of the new folder you want to create in /XXX to locate the resources in the zip file.

* **Resource Node Name**  
   Specify the node name of the folder. Server needs the name as the display name of the folder in the server resource tree.
* **Resource Description**  
   Specify the description of the folder.
* **Resource Real Path**  
   Specify the real path of the folder.
* **Enable Resources from Real Paths**  
   Select to enable getting resources from the folder's real path. Once you enable it, Server maps the real path to the folder in the server resource tree and is able to get the resources and updates from the real path.
* **[Custom Field Name]**  
   Specify the values of the custom fields for the folder.

**Automatically Convert Old Report Schema**

Select if you want Server to convert Logi Report reports of earlier versions into current version reports when publishing the earlier version reports.

**Apply Archive Policy**

Select to apply an archive policy to the resource versions.

* **Archive as New Version**  
   Select to enable multiple versions for a resource.
  + **Maximum Number of Versions**  
     Specify the maximum number of versions that a resource can have. The default value 0 means unlimited version number.
* **Replace Old Version**  
   Select to replace the old version with the new version.

**Set Permissions**

This property is available only when you are going to publish the resources to a public folder and when you have the Grant permission on the folder. Select this property to set user permissions to the resources in the [Set Permissions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741406263447-Set-Permissions-Dialog-Box-Properties).

**Advanced Publish**

Select to publish resources in an advanced way.

* **Checkbox**  
   Specify which resources in the zip file you want to publish.
* **File Name**  
   File name of the resource.
* **Resource Name**  
   Specify the name of the resource. Server needs the name as the display name of the resource in the server resource tree.
* **Description**  
   Specify the description of the resource.
* **[Custom Field Name]**  
   Specify the value of the custom field for the resource.
* **Advanced**  
   Specify the advanced properties for the resource, including the archive policy of the resource and the user permissions on the resource if you are to publish the resource to a public folder.

**OK**

Select to publish the resources to Server.

**Cancel**

Select to close the dialog box without publishing resources.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/5741442976407-Preference-Dialog-Box-Properties-)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741421379351-Publish-from-Server-Machine-Dialog-Box-Properties)
