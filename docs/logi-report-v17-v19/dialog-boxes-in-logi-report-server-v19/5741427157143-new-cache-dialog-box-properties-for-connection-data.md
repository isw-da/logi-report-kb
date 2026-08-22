---
title: "New Cache Dialog Box Properties for Connection Data"
id: 5741427157143
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741427157143-New-Cache-Dialog-Box-Properties-for-Connection-Data
updated_at: 2022-10-31T17:18:50Z
---

# New Cache Dialog Box Properties for Connection Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741427584151-Multiple-Type-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache)

# New Cache Dialog Box Properties for Connection Data

This topic describes how you can use the New Cache dialog box to create a schedule task to generate [data cache](https://devnet.logianalytics.com/hc/en-us/articles/5741453292183-Managing-Cached-Report-Data#Schedule) for a connection.

Server displays the dialog box when an administrator selects **New Cache** in the Administration > Configuration > Cache > Connection Data page on the Server Console.

The dialog box includes two phases, one for [selecting a connection](#Connection) and the other for [defining the schedule task](#Schedule).

## Selecting a Connection Phase

At this phase, you need to specify a connection for which you want to create data cache.

![New Cache dialog box - Select Data Resource](https://devnet.logianalytics.com/hc/article_attachments/9905736256919/nwcache_cnct.gif)

**Select a Folder**

Specify the folder in the server resource tree that contains the required catalog. You can select the ellipsis button ![Select Folder](https://devnet.logianalytics.com/hc/article_attachments/9905758084119/btn_chsr3.gif) to open the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443524503-Select-Folder-Dialog-Box-Properties) for selecting the folder.

**Select a Catalog**

Select a catalog in the folder.

**Select Connection**

Select a connection for which you want to create data cache.

Server lists the selected data resources.

**OK**

Select to go to the next phase to define the schedule information.

**Cancel**

Select to close the dialog box without creating a data cache.

**Help**

Select to view information about the dialog box.

## Defining the Schedule Task Phase

At this phase, you need to define the connection information and the updating policy of the data cache on these tabs:

* [General](#General)
* [Conditions](https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache#Conditions)
* [Notification](https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache#Notification)

**Back**

Select to go back to the previous tab.

**Next**

Select to go to the next tab.

**Finish**

Select to create the data cache.

**Cancel**

Select to return to the selecting data resources phase without saving any changes.

**Help**

Select to view information about the dialog box.

### General

Before scheduling the task, you need to configure the settings in this tab first.

![New Cache dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905758221207/nwcache_cnct_gen.gif)

**Enter Parameters**

Specify the values of the parameters you want to apply to the selected connection. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values).

If the connection does not have parameters, Server displays "No Parameter Needed" here.

**Cached Connection Data Info**

Specify the data cache information.

* **Name**  
   Name of the selected connection. Server also uses it as the name of the new data cache.
* **Data Source**  
   Data source in which the connection is.
* **Catalog**  
   Path of the catalog in which the connection is. Server uses the latest catalog version by default.
* **Priority**  
   Specify the priority level of the scheduled task. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. By default, Server ignores this property unless you modify [server.properties](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties) in `<install_root>\bin` to set queue.policy not equal to 0.

**Advanced**

Configure some advanced settings.

* **Add TaskListener to be Invoked**  
   Select to call a Java application before/after the task runs to obtain information about the task.
* **Enable Auto Recover Task**  
   Select if you want Server to automatically recover the task.
  + **Maximum Retry Times**  
     Specify the maximum number of times for retrying running the task to recover it.
  + **Retry Interval**  
     Specify the interval between retries.
  + **Recreate All Results**  
     Select if you want to recreate all results. By default, Server only recreates failed results.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741427584151-Multiple-Type-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache)
