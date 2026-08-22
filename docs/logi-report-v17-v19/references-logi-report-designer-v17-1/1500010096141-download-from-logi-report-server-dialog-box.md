---
title: "Download from Logi Report Server Dialog Box"
id: 1500010096141
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096141-Download-from-Logi-Report-Server-Dialog-Box
updated_at: 2021-07-23T19:15:15Z
---

# Download from Logi Report Server Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058662-Download-Customized-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058682-Edit-Additional-Value-Dialog-Box)

# Download from Logi Report Server Dialog Box

You can use the Download from Logi Report Server dialog box to [download resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#DownReport) from a started Server to the specified directory on your local machine. This topic describes the options in the dialog box.

Designer displays the Download from Logi Report Server dialog box when you do any of the following:

* Select File > Download > Download Report from Server.
* Select File > Download > Download Component from Server.
* Select File > Download > Download Report from Server/Download Component from Server, specify the connection and user information in the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) and select Connect.

![Download from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856841623/dwldjrsrv.gif)

You see the following options in the dialog box:

**Download Resource From**

Specify the folder on Server from which to download the resources. You can select the Browse button to select the path in the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060442-Select-Folder-Dialog-Box).

**Resource tree box**

The box lists the resources, including catalog files and report files, in the specified folder of Server. If you specify to download resources from the Public Reports folder, Designer only lists the resources on which you have the Visible permission in this box. Select the checkboxes ahead of the resources you want to download.

* **Name**  
  The column shows the resource names.
* **Size**  
  The column shows the file size.
* **Type**  
  The column shows the file type.
* **Version Date**  
  The column shows the latest version date of the resources.
* **Description**  
  The column shows other necessary descriptions of the resources if any.
* **Has Read Permission**  
  The column shows whether you have the Read permission on the resources. You can only download resources on which you have the Read permission from Server.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Except for the Name column, you can specify whether or not to show the other columns in this box by right-clicking on any column header and then selecting/clearing the corresponding items on the shortcut menu.
* You can sort the resources by name, size, type, and so on by selecting on the corresponding column header.

**Download Resource To**

Specify the directory to which to download the resources. By default, Designer displays the path of the currently open catalog here. You can select the Browse button to find another directory.

**Download as XML Format**

Select to save the downloaded resources in XML. Only catalog and page report resources support this format.

**OK**

Select to apply the changes and download the resources from Server to the specified directory.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058662-Download-Customized-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058682-Edit-Additional-Value-Dialog-Box)
