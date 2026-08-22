---
title: "Publish from Server Machine"
id: 1500009720902
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009720902-Publish-from-Server-Machine
updated_at: 2021-07-25T07:19:36Z
---

# Publish from Server Machine

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009720882-Publish-to-Remote-Server-)[Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720862-Publish-to-Local-Server)

# Publish from Server Machine

The Publish from Server Machine dialog box is used to publish resources to the Logi Report Server resource tree [from the machine where the server runs](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources#SrvMachine). It appears when you select Publish > From Server Machine on the task bar of the Resources page in the server console.

![Publish from Server Machine dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942502551/pubfrmsrv.gif)

**Publish Resource To**

Shows where the resource will be published to.

**Resource Type**

Specifies the type of the resource.

**From Folder/From File**

Specifies where to get the resource. Select the Browse button to specify the location.

**Resource Node Name**

Specifies the name of the resource. This name is required and is used as the display name of the resource in the server resource tree.

**Resource Description**

Specifies the description of the resource.

**Status**

Specifies the status of the report. If not specified, the status will be Active by default. This option is available for report type only.

* **Active**  
   The report can be run, advanced run and scheduled on Logi Report Server.
* **Inactive**  
   The report cannot be run, advanced run or scheduled on Logi Report Server.
* **Incomplete**  
   The report is not completely designed and cannot be run, advanced run or scheduled Logi Report Server.

**Resource Real Path**

Specifies the real path of the folder. This option is available for folder type only.

**Enable Resources from Real Paths**

Specifies whether or not to enable getting resources from the folder's real path. This option is available for folder type only. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path.

**[Custom Field Name]**

Specifies values of the custom fields for the resource.

**Automatically Convert Old Report Schema**

Specifies whether or not Logi Report Server converts Logi Report reports of earlier versions into current version Logi Report reports when publishing the earlier version reports.

**Apply Archive Policy**

Applies an archive policy to the resource versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the resource.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the resource. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when the new version is generated.

**Set Permissions**

Available only when the resource is to be published to a public folder and when you have the Grant permission on the folder. Select the link to set user permissions to the resource in the [Set Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009747661-Set-Permissions) dialog box.

**Font Directory**

Specifies the font directory of the resource if it uses special font. Select the Browse button to specify the directory.

**Style Directory**

Specifies the style directory of the resource if it applies style group. Select the Browse button to specify the directory.

**Geographic Information Directory**

Specifies the geographic information directory of the resource if it contains geographic information. Select the Browse button to specify the directory.

**Advanced Publish**

Specifies to publish resource in an advanced way.

* **Check box**  
   Specifies the resources you want to publish.
* **File Name**  
   Displays the file name of the resource.
* **Resource Name**  
   Specifies the name of the resource. This name is required and is used as the display name of the resource node in the server resource tree.
* **Description**  
   Specifies the description of the resource.
* **[Custom Field Name]**  
   Specifies value of the custom field for the resource.
* **Advanced**  
   Specifies the advanced properties for the resource, which include the archive policy of the resource, and the user permissions on the resource if the resource is to be published to a public folder.

**OK**

Retains the settings and submits the task to server.

**Cancel**

Cancels the operations.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009720882-Publish-to-Remote-Server-)[Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720862-Publish-to-Local-Server)
