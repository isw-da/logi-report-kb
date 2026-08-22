---
title: "Publish to JReport Server Dialog"
id: 1500010032182
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010032182-Publish-to-JReport-Server-Dialog
updated_at: 2021-07-24T10:38:29Z
---

# Publish to JReport Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067461-Publish-Additional-Resources-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067481-Publish-to-Local-Directory-Dialog)

# Publish to JReport Server Dialog

The Publish to JReport Server dialog helps you to [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely) from Logi JReport Designer to a started Logi JReport Server. It appears when you do any of the following:

* Select File > Publish > Publish Report to Server.
* Select File > Publish > Publish Component to Server.
* Select File > Publish > Publish Report to Server/Publish Component to Server, specify the connection and user information in the [Connect to JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog) dialog and select Connect.

![Publish to Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909128855/pubjrsrv.gif)

The following are details about options in the dialog:

**Publish Resource From**

Specifies the directory in which the resources you want to publish are located. By default, the path of the currently opened catalog is shown here. You can select the Browse button to find another directory.

**Select All**

Specifies to publish all the resources in the specified directory.

**Resource tree box**

Lists all the resources in the specified directory in a tree structure. Check the checkboxes ahead of the resources you want to publish.

**Publish Resource To**

Specifies the file path on the server to which the resources will be published. You can select the Browse button to select the path in the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500010032542-Select-Folder-Dialog) dialog.

**More/Less Options**

Shows/hides resource options. Select a to-be-published resource in the resource tree box and set its properties in the following tabs:

* **Properties tab**  
   Specifies properties for the selected resource.
  + **Resource Node Name**  
     Specifies the name of the selected resource. This name is required and is used as the display name of the resource in the server resource tree. The Browse button is used to display all the same type resource names under the Publish Resource To path. Select one of them as the name of the selected resource.
  + **Resource Description**  
     Specifies the description for the selected resource.
  + **Status** (available only when a report is selected)  
     Specifies the status of the selected report. If not specified, the status will be Active by default.
    - **Active**  
       The report can be run, advanced run and scheduled on Logi JReport Server.
    - **Inactive**  
       The report cannot be run, advanced run or scheduled on Logi JReport Server.
    - **Incomplete**  
       The report is not completely designed and cannot be run, advanced run or scheduled on Logi JReport Server.
  + **Resource Real Path** (available only when a folder is selected)  
     Specifies the real path of the folder.
  + **Enable Resources from Real Paths** (available only when a folder is selected)  
     Specifies whether or not to enable getting resources from the folder's real path. Once enabled, the real path resources will be mapped into the resource node of the folder in the server resource tree and the server will always be able to get the resources and updates from the real path. Once you create a real path folder you can no longer publish reports to it from Logi JReport Designer. You need to physically copy the files you want to publish into the specified folder on the server.
  + **Custom Field**  
     Specifies custom field values for the selected resource if there are custom fields enabled on Logi JReport Server.
    - **Name**  
       Displays name of the custom fields.
    - **Value**  
       Specifies value of the custom fields.
  + **Apply Archive Policy**  
     Specifies whether to apply an archive policy to the selected resource.
    - **Archive as New Version**  
       Specifies whether to use multiple versions for the selected resource.
      * **Max Number of Versions**  
         Specifies the maximum number of versions that will be listed in the version table of the selected resource. The default value is 0, which means that the version amount is unlimited.
    - **Replace Old Version**   
       Specifies whether to replace the old version when the new version is generated.
* **Permissions tab** (enabled only when publishing resources to a public folder)  
   Specifies user permissions to the selected resource.
  + **Enable Setting Permissions**  
     Specifies whether to apply user permissions to the selected resource.
  + **Role/User/Group**   
     The tabs list Logi JReport Server roles, users, and groups. You can apply permissions to them by selecting a role/user/group and then checking the checkboxes before the required permissions.
  + **Permissions**  
     Sets permissions to the selected role/user/group by checking the checkboxes before the required permissions.
  + **Add**  
     Adds roles/users/groups and assigns permissions to them.
  + **Remove**  
     Removes the selected role/user/group from the Role/User/Group tab. The removed roles/users/groups are still available for the case when you want to add them back.
* **Connection tab** (only for catalog)  
   Specifies properties of the data source connection. When the data source contains multiple connections only properties of the first connection are listed.
  + **Catalog Data Source**  
     Specifies the data source in the catalog.
  + **Modify**  
     If the listed connection is a JDBC connection, the Modify button is activated. You can select it to modify properties of the JDBC connection in the [Get JDBC Connection Information](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog) dialog.
  + **Name**  
     Lists the name of the connection properties.
  + **Property**  
     Lists the value of the properties.

**OK**

Applies the changes and publishes the resources to Logi JReport Server.

**Cancel**

Closes the dialog, leaving any changes unsaved.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067461-Publish-Additional-Resources-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067481-Publish-to-Local-Directory-Dialog)
