---
title: "New Dashboard Listener Dialog Box Properties"
id: 5741442672663
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741442672663-New-Dashboard-Listener-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:57Z
---

# New Dashboard Listener Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741405948567-New-Custom-Field-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741420932375-New-Dynamic-Connection-Dialog-Box-Properties)

# New Dashboard Listener Dialog Box Properties

This topic describes how you can use the New Dashboard Listener dialog box to upload and register an implementation of the [Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/5741394931863-Applying-the-Implementations-of-the-Dashboard-Listener-API).

The dialog box includes two phases, one for [specifying the implementation file](#File) and the other for [specifying target dashboards](#Resource). Server displays the dialog box when an administrator selects **New Dashboard Listener** in the Administration > Other > Dashboard Listeners page on the Server Console.

When an administrator selects an implementation class and then select **Properties**, Server displays the [Specifying Target Dashboards Phase](#Resource).

## Specifying the Implementation File Phase

Add an implementation file of the Dashboard Listener API.

![New Dashboard Listener dialog - Specify Implementation File](https://devnet.logianalytics.com/hc/article_attachments/9905758134807/nwdshlsn_file.gif)

**Source File**

Select **Browse** to upload an implementation class file of the Dashboard Listener API, which could be a .zip or .jar file.

**Next**

Select to move forward to the next step of specifying the target resources.

**Cancel**

Select to close the dialog box without doing anything.

**Help**

Select to view information about the dialog box.

## Specifying Target Dashboards Phase

Specify the dashboards which you want the implementation to take effect on.

![New Dashboard Listener dialog box - Specify Target Resources](https://devnet.logianalytics.com/hc/article_attachments/9905736236055/nwdshlsn_rsc.gif)

**Class Name**

Server lists the class names defined in the specified implementation file. Select a class name from the list or type the name manually.

**Target**

Specify the dashboards you want the implementation to take effect on. If the target box is empty, the implementation will not take effect.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) **Add button**  
   Select to open the [Select Target dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443597975-Select-Target-Dialog-Box-Properties) for adding dashboards or folders that contains dashboards.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**  
   Select to remove the selected items.

**Description**

Specify the description of the implementation.

**Enabled**

Select if you want to enable the implementation. The enabled implementations will take effect.

**Back**

Select to return to the step of specifying an implementation file.

**Finish**

Select to add the implementation and close the dialog box.

**Cancel**

Select to close the dialog box without adding an implementation.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741405948567-New-Custom-Field-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741420932375-New-Dynamic-Connection-Dialog-Box-Properties)
