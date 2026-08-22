---
title: "New Dashboard Listener"
id: 1500009646582
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009646582-New-Dashboard-Listener
updated_at: 2021-07-24T20:54:48Z
---

# New Dashboard Listener

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646562-New-Custom-Field)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646602-New-Dynamic-Connection)

# New Dashboard Listener

The New Dashboard Listener dialog appears when you select the New Dashboard Listener link on the Logi JReport Administration > Configuration > Dashboard Listeners page. This dialog is used for uploading and registering an implementation of the [Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/1500009644002-Applying-the-Implementations-of-the-Dashboard-Listener-API).

The dialog is divided into two phases, one for [specifying the implementation file](#File) and the other for [specifying target resources](#Resource).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying the Implementation File Phase

This is used for adding an implementation file of the Dashboard Listener API. [See the dialog at this phase](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920570007/nwdshlsn_file.gif)

**Source File**

Uploads an implementation class file of the Dashboard Listener API which could be a .zip or .jar file using the Browse button.

**Next**

Moves forward to the next step of specifying the target resources.

**Cancel**

Cancels the setting and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Target Resources Phase

This is used for specifying the target resources that the implementation will take effect on. [See the dialog at this phase](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920570263/nwdshlsn_rsc.gif)

**Class Name**

Lists class names defined in the specified implementation file. Select a class name from the drop-down list or input the name manually.

**Target**

Specifies the resources that the implementation will take effect on. Multiple selection is supported in the Target box.

If the target value is null, the implementation will not take effect.

* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif)  
   Opens the [Select Target](https://devnet.logianalytics.com/hc/en-us/articles/1500009671261-Select-Target) dialog for adding a new target.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646562-New-Custom-Field)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646602-New-Dynamic-Connection)
