---
title: "Publish to Remove Server "
id: 1500009688922
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009688922-Publish-to-Remove-Server
updated_at: 2021-11-03T06:57:40Z
---

# Publish to Remove Server 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714881-Publish-to-Local-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715001-Report-Properties)

# Publish to Remove Server

The Publish to Remove Server dialog guides you through [publishing resources to Logi JReport Server remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500009717841-Publishing-Resources#Remotely).
It appears when you select Publish > To Remote Server on the task bar of the Resources page in the server console.

![Publish to Remote Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112561815/pbrmtsrv.gif)

**Publish Remote Resource to**

Shows where the resources will be published.

**From Zipped File**

Specifies where to get the resources. Select the Browse button to specify the location.

**Publish files and folders in the zipped file to /XXX**

Specifies whether to publish files and folders in the zipped file to /XXX directly.

When this option is not checked, the following options are available, which specify properties of the new folder you want to create in /XXX to locate the resources in the zip file.

* **Resource Node Name**  
   Specifies the node name of the folder. This name is required and is used as the display name of the folder in the server resource tree.
* **Resource Description**  
   Specifies the description of the folder.
* **Resource Real Path**  
   Specifies the real path of the folder.
* **Enable Resources from Real Paths**  
   Specifies whether or not to enable getting resources from the folder's real path. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path.
* **[Custom Field Name]**  
   Specifies values of the custom fields for the folder.

**Automatically Convert Old Report Schema**

Specifies whether or not Logi JReport Server converts Logi JReport reports of earlier versions into current version Logi JReport reports when publishing the earlier version reports.

**Apply Archive Policy**

Applies an archive policy to the resource versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the resources.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the resource. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

**Set Permissions**

Available only when the resources are to be published to a public folder and when you have the Grant permission on the folder. Select the link to set user permissions to the resources in the [Set Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009714901-Set-Permissions) dialog.

**Advanced Publish**

Specifies to publish resources in an advanced way.

* **Checkbox**  
   Specifies which resources in the zip file you want to publish.
* **File Name**  
   Displays the file name of the resource.
* **Resource Name**  
   Specifies the name of the resource. This name is required and is used as the display name of the resource in the server resource tree.
* **Description**  
   Specifies the description of the resource.
* **[Custom Field Name]**  
   Specifies value of the custom field for the resource.
* **Advanced**  
   Specifies the advanced properties for the resource, which include the archive policy of the resource, and the user permissions on the resource if the resource is to be published to a public folder.

**OK**

Retains the settings and submits the task to server.

**Cancel**

Cancels operations.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714881-Publish-to-Local-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715001-Report-Properties)
