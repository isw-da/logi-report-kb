---
title: "Publish from Local Directory Dialog Box Properties"
id: 1500009746342
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746342-Publish-from-Local-Directory-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:41Z
---

# Publish from Local Directory Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746222-Preference-Dialog-Box-Properties-)   [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774521-Publish-from-Server-Machine-Dialog-Box-Properties)

# Publish from Local Directory Dialog Box Properties

This topic describes how you can use the Publish from Local Directory dialog box to publish resources to the Logi Report Server resource tree [from a local directory](https://devnet.logianalytics.com/hc/en-us/articles/1500009777241-Publishing-Resources#LocalDir). Server displays the dialog box when you select Publish > From Local Directory on the task bar of the Resources page in the Server Console.

![Publish from Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880290839/pubfrmdir.gif)

**Publish Resource To**

Shows where the resources will be published.

**From Zipped File**

Specifies where to get the resources. Select the Browse button to specify the location.

**Publish files and folders in the zipped file to /XXX**

Specifies whether to publish files and folders in the zipped file to /XXX directly.

When this option is not selected, the following options are available, which specify properties of the new folder you want to create in /XXX to locate the resources in the zip file.

* **Resource Node Name**  
   Specifies the node name of the folder. This name is required and is used as the display name of the folder in the server resource tree.
* **Resource Description**  
   Specifies the description of the folder.
* **Resource Real Path**  
   Specifies the real path of the folder.
* **Enable Resources from Real Paths**  
   Specifies whether to enable getting resources from the folder's real path. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path.
* **[Custom Field Name]**  
   Specifies values of the custom fields for the folder.

**Automatically Convert Old Report Schema**

Specifies whether Logi Report Server converts Logi Report reports of earlier versions into current version Logi Report reports when publishing the earlier version reports.

**Apply Archive Policy**

Applies an archive policy to the resource versions.

* **Archive as New Version**  
   Specifies whether to use multiple versions for the resources.
  + **Maximum Number of Versions**  
     Specifies the maximum number of versions that will be listed in the version table of the resource. The default value is 0, which means that the version number is unlimited.
* **Replace Old Version**  
   Specifies to replace the old version when a new version is generated.

**Set Permissions**

Available only when the resources are to be published to a public folder and when you have the Grant permission on the folder. Select the link to set user permissions to the resources in the [Set Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009774321-Set-Permissions-Dialog-Box-Properties) dialog box.

**Advanced Publish**

Specifies to publish resources in an advanced way.

* **Check box**  
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746222-Preference-Dialog-Box-Properties-)   [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774521-Publish-from-Server-Machine-Dialog-Box-Properties)
