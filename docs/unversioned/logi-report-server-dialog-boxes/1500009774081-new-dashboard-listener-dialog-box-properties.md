---
title: "New Dashboard Listener Dialog Box Properties"
id: 1500009774081
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774081-New-Dashboard-Listener-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:45Z
---

# New Dashboard Listener Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746122-New-Custom-Field-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746142-New-Dynamic-Connection-Dialog-Box-Properties)

# New Dashboard Listener Dialog Box Properties

This topic describes how you can use the New Dashboard Listener dialog box to upload and register an implementation of the [Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771021-Applying-the-Implementations-of-the-Dashboard-Listener-API).

Server displays the dialog box when an admin user selects the New Dashboard Listener link in the Administration > Other > Dashboard Listeners page in the Server Console.

The dialog box is divided into two phases, one for [specifying the implementation file](#File) and the other for [specifying target resources](#Resource).

## Specifying the Implementation File Phase

This is used for adding an implementation file of the Dashboard Listener API.

![New Dashboard Listener dialog - Specify Implementation File](https://devnet.logianalytics.com/hc/article_attachments/4404885511703/nwdshlsn_file.gif)

**Source File**

Uploads an implementation class file of the Dashboard Listener API which could be a .zip or .jar file using the Browse button.

**Next**

Moves forward to the next step of specifying the target resources.

**Cancel**

Cancels the setting and closes the dialog box.

**Help**

Displays the help document about this feature.

## Specifying Target Resources Phase

This is used for specifying the target resources that the implementation will take effect on.

![New Dashboard Listener dialog - Specify Target Resources](https://devnet.logianalytics.com/hc/article_attachments/4404885512343/nwdshlsn_rsc.gif)

**Class Name**

Lists class names defined in the specified implementation file. Select a class name from the drop-down list or type the name manually.

**Target**

Specifies the resources that the implementation will take effect on. Multiple selection is supported in the Target box.

If the target value is null, the implementation will not take effect.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
   Opens the [Select Target](https://devnet.logianalytics.com/hc/en-us/articles/1500009746462-Select-Target-Dialog-Box-Properties) dialog box for adding a new target.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected target values.

**Description**

Specifies the description of the implementation.

**Enabled**

Specifies whether the implementation is enabled. The enabled implementations will take effect.

**Back**

Returns to the step of specifying an implementation file.

**Finish**

Adds the implementation and exits the dialog box.

**Cancel**

Cancels the setting and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746122-New-Custom-Field-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746142-New-Dynamic-Connection-Dialog-Box-Properties)
