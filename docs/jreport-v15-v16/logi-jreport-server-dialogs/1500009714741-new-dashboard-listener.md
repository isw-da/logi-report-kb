---
title: "New Dashboard Listener"
id: 1500009714741
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009714741-New-Dashboard-Listener
updated_at: 2021-11-03T06:57:42Z
---

# New Dashboard Listener

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714701-New-Custom-Field)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688782-New-Dynamic-Connection)

# New Dashboard Listener

The New Dashboard Listener dialog is used for uploading and registering an implementation of the [Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/1500009712001-Applying-the-Implementations-of-the-Dashboard-Listener-API).
It appears when you select the New Dashboard Listener link in the Administration > Other > Dashboard Listeners page in the server console.

The dialog is divided into two phases, one for [specifying the implementation file](#File) and the other for [specifying target resources](#Resource).

## Specifying the Implementation File Phase

This is used for adding an implementation file of the Dashboard Listener API.

![New Dashboard Listener dialog - Specify Implementation File](https://devnet.logianalytics.com/hc/article_attachments/4412131467927/nwdshlsn_file.gif)

**Source File**

Uploads an implementation class file of the Dashboard Listener API which could be a .zip or .jar file using the Browse button.

**Next**

Moves forward to the next step of specifying the target resources.

**Cancel**

Cancels the setting and closes the dialog.

**Help**

Displays the help document about this feature.

## Specifying Target Resources Phase

This is used for specifying the target resources that the implementation will take effect on.

![New Dashboard Listener dialog - Specify Target Resources](https://devnet.logianalytics.com/hc/article_attachments/4412131468183/nwdshlsn_rsc.gif)

**Class Name**

Lists class names defined in the specified implementation file. Select a class name from the drop-down list or input the name manually.

**Target**

Specifies the resources that the implementation will take effect on. Multiple selection is supported in the Target box.

If the target value is null, the implementation will not take effect.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif)  
   Opens the [Select Target](https://devnet.logianalytics.com/hc/en-us/articles/1500009689122-Select-Target) dialog for adding a new target.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the selected target values.

**Description**

Specifies the description of the implementation.

**Enabled**

Specifies whether the implementation is enabled. The enabled implementations will take effect.

**Back**

Returns to the step of specifying an implementation file.

**Finish**

Adds the implementation and exits the dialog.

**Cancel**

Cancels the setting and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714701-New-Custom-Field)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688782-New-Dynamic-Connection)
