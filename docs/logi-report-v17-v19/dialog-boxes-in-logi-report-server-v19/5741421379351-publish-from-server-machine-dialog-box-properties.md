---
title: "Publish from Server Machine Dialog Box Properties"
id: 5741421379351
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741421379351-Publish-from-Server-Machine-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:04Z
---

# Publish from Server Machine Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741427653783-Publish-from-Local-Directory-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741421317271-Publish-to-Server-Dialog-Box-Properties)

# Publish from Server Machine Dialog Box Properties

This topic describes how you can use the Publish from Server Machine dialog box to publish resources to the server resource tree [from the computer where the server runs](https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources#SrvMachine).

Server displays the dialog box when you select **Publish** > **From Server Machine** on the task bar of the Resources page on the Server Console.

![Publish from Server Machine dialog](https://devnet.logianalytics.com/hc/article_attachments/9905714441879/pubfrmsrv.gif)

**Publish Resource To**

Server displays the directory you are going to publish resources to.

**Resource Type**

Select the type of the resources you want to publish.

**From Folder/From File**

Specify the path of a folder or file. System administrators can select **Browse** to specify the folder or file.

**Resource Node Name**

Specify the name of the resource. Server needs the name as the display name of the resource in the server resource tree.

**Resource Description**

Specify the description of the resource.

**Status**

Specify the status of report resources.

* **Active**  
   You can run, advanced run, and schedule to run the reports.
* **Inactive**  
   You cannot run, advanced run, or schedule to run the reports.
* **Incomplete**  
   You haven't finished designing the reports. You cannot run, advanced run, or schedule to run the reports.

**Resource Real Path**

Specify the real path of the folder. This property is available for folder type only.

**Enable Resources from Real Paths**

Select to enable getting resources from the folder's real path. This property is available for folder type only. Once you enable it, Server maps the real path to the folder in the server resource tree and is able to get the resources and updates from the real path.

**[Custom Field Name]**

Specify the values of the custom fields for the resource.

**Automatically Convert Old Report Schema**

Select to convert reports of earlier versions to current version when publishing the earlier version reports.

**Apply Archive Policy**

Select to apply an archive policy to the resource versions.

* **Archive as New Version**  
   Select to enable multiple versions for a resource.
  + **Maximum Number of Versions**  
     Specify the maximum number of versions that a resource can have. The default value 0 means unlimited version number.
* **Replace Old Version**  
   Select to replace the old version with the new version.

**Set Permissions**

Available only when you publish the resources to a public folder and if you have the Grant permission on the folder. Select this property to set user permissions on the resources in the [Set Permissions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741406263447-Set-Permissions-Dialog-Box-Properties).

**Font Directory**

Specify the font directory if the resources use special font. System administrators can select **Browse** to specify the directory.

**Style Directory**

Specify the style directory if the resources apply style group. System administrators can select **Browse** to specify the directory.

**Geographic Information Directory**

Specify the geographic information directory if the resources contain geographic information. System administrators can select **Browse** to specify the directory.

**Advanced Publish**

Select to publish resources in an advanced way.

* **Checkbox**  
   Select the resources you want to publish.
* **File Name**  
   Server displays the file names of the resources.
* **Resource Name**  
   Specify the name of a resource. Server needs the name as the display name of the resource in the server resource tree.
* **Description**  
   Specify the description of a resource.
* **[Custom Field Name]**  
   Specify the value of the custom field for a resource.
* **Advanced**  
   Specify the advanced properties for a resource, including the archive policy of the resource and the user permissions on the resource if you are to publish the resource to a public folder.

**OK**

Select to publish the resources to Server.

**Cancel**

Select to close the dialog box without publishing resources.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741427653783-Publish-from-Local-Directory-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741421317271-Publish-to-Server-Dialog-Box-Properties)
