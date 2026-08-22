---
title: "Publish to Local Server"
id: 1500009714881
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009714881-Publish-to-Local-Server
updated_at: 2021-11-03T06:57:40Z
---

# Publish to Local Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714921-Preference)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688922-Publish-to-Remove-Server-)

# Publish Local Resources

The Publish Local Resources dialog guides you through the process of [publishing resources to Logi JReport Server locally](https://devnet.logianalytics.com/hc/en-us/articles/1500009717841-Publishing-Resources#Locally).
It appears when you select Publish > To Local Server on the task bar of the Resources page in the server console.

![Publish to Local Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131437463/pblclsrv.gif)

**Publish Local Resource to**

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
   The report can be run, advanced run and scheduled on Logi JReport Server.
* **Inactive**  
   The report cannot be run, advanced run or scheduled on Logi JReport Server.
* **Incomplete**  
   The report is not completely designed and cannot be run, advanced run or scheduled Logi JReport Server.

**Resource Real Path**

Specifies the real path of the folder. This option is available for folder type only.

**Enable Resources from Real Paths**

Specifies whether or not to enable getting resources from the folder's real path. This option is available for folder type only. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path.

**[Custom Field Name]**

Specifies values of the custom fields for the resource.

**Automatically Convert Old Report Schema**

Specifies whether or not Logi JReport Server converts Logi JReport reports of earlier versions into current version Logi JReport reports when publishing the earlier version reports.

**Apply Archive Policy**

Applies an archive policy to the resource versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the resource.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the resource. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when the new version is generated.

**Set Permissions**

Available only when the resource is to be published to a public folder and when you have the Grant permission on the folder. Select the link to set user permissions to the resource in the [Set Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009714901-Set-Permissions) dialog.

**Font Directory**

Specifies the font directory of the resource. Select the Browse button to specify the directory. Note that only the font used by the specified resource can be published.

**Style Directory**

Specifies the style directory of the resource. Select the Browse button to specify the directory.

**Geographic Information Directory**

Specifies the geographic information of the resource with reports or library components contained that have geographic information. Select the Browse button to specify the directory.

**Advanced Publish**

Specifies to publish resource in an advanced way.

* **Checkbox**  
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714921-Preference)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688922-Publish-to-Remove-Server-)
