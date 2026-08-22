---
title: "Download from Logi Report Server Dialog"
id: 1500009630581
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630581-Download-from-Logi-Report-Server-Dialog
updated_at: 2021-07-24T16:04:49Z
---

# Download from Logi Report Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607802-Download-Customized-Control-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630601-Edit-Additional-Value-Dialog)

# Download from Logi Report Server Dialog

The Download from Logi Report Server dialog helps you to [download resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#DownReport) from a started Logi Report Server to the specified directory on your local. It appears when you do any of the following:

* Select File > Download > Download Report from Server.
* Select File > Download > Download Component from Server.
* Select File > Download > Download Report from Server/Download Component from Server, specify the connection and user information in the [Connect to Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog) dialog and select Connect.

![Download from Logi Report Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911630999/dwldjrsrv.gif)

The following are details about options in the dialog:

**Download Resource From**

Specifies the folder on the server from which resources will be downloaded. You can select the Browse button to select the path in the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009610342-Select-Folder-Dialog) dialog.

**Resource tree box**

Lists the resources, including catalog files and report files, in the specified folder of Logi Report Server. If you specify to download resources from the Public Reports folder on the server, only the resources on which you have the Visible permission are listed in this box. Select the checkboxes ahead of the resources you want to download.

* **Name**  
   Displays the resource names.
* **Size**  
   Displays the file size.
* **Type**  
   Displays the file type.
* **Version Date**  
   Displays the latest version date of the resources.
* **Description**  
   Shows other necessary descriptions of the resources if any.
* **Has Read Permission**  
   Shows whether you have the Read permission on the resources. You can only download resources on which you have the Read permission from Logi Report Server.

**Tips:**

* Except for the Name column, you can specify whether or not to show the other columns in this box by right-clicking on any column header and then selecting/clearing the corresponding items on the shortcut menu.
* You can sort the resources by name, size, type, and so on by selecting on the corresponding column header.

**Download Resource To**

Specifies the directory to which the resources will be downloaded. By default, the path of the currently open catalog is shown here. You can select the Browse button to find another directory.

**Download as XML Format**

Specifies whether to save the downloaded resources in the XML format. Only catalog and page report resources support this format.

**OK**

Applies the changes and downloads the resources from Logi Report Server to the specified directory.

**Cancel**

Closes the dialog, leaving any changes unsaved.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607802-Download-Customized-Control-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630601-Edit-Additional-Value-Dialog)
