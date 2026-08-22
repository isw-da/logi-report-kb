---
title: "Download from Logi Report Server Dialog Box"
id: 5735522490007
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735522490007-Download-from-Logi-Report-Server-Dialog-Box
updated_at: 2022-11-02T04:14:52Z
---

# Download from Logi Report Server Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513670423-Download-Customized-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565591447-Edit-Additional-Value-Dialog-Box)

# Download from Logi Report Server Dialog Box

You can use the Download from Logi Report Server dialog box to [download resources](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources#DownReport) from a started Server to the specified directory on your local machine. This topic describes the options in the dialog box.

Designer displays the Download from Logi Report Server dialog box when you do one of the following:

* Navigate to File > Download > Download Report from Server.
* Navigate to File > Download > Download Component from Server.
* Navigate to File > Download > Download Report from Server/Download Component from Server, specify the connection and user information in the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box) and select Connect.

![Download from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898474974999/dwldjrsrv.gif)

Designer displays these options:

**Download Resource From**

Specify the folder on Server from which to download the resources. Select **Browse** to select the path in the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544338583-Select-Folder-Dialog-Box).

**Resource tree box**

This box lists the resources, including catalog files and report files, in the specified folder of Server. If you specify to download resources from the Public Reports folder, Designer only lists the resources on which you have the Visible permission in this box. Select the checkboxes ahead of the resources you want to download.

* **Name**  
  This column shows the resource names.
* **Size**  
  This column shows the file size.
* **Type**  
  This column shows the file type.
* **Version Date**  
  This column shows the latest version date of the resources.
* **Description**  
  This column shows other necessary descriptions of the resources if any.
* **Has Read Permission**  
  This column shows whether you have the Read permission on the resources. You can only download resources on which you have the Read permission.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Except for the Name column, you can specify whether to show the other columns in this box by right-clicking on any column header and then selecting/clearing the corresponding items on the shortcut menu.
* You can sort the resources by name, size, type, and so on by selecting on the corresponding column header.

**Download Resource To**

Specify the directory to which to download the resources. By default, Designer displays the path of the currently open catalog here. You can select **Browse** to find another directory.

**Download as XML Format**

Select to save the downloaded resources (excluding library components) in XML.

**OK**

Select to exit the dialog box and start downloading the resources from Server.

**Cancel**

Select to quit downloading resources from Server and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513670423-Download-Customized-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735565591447-Edit-Additional-Value-Dialog-Box)
