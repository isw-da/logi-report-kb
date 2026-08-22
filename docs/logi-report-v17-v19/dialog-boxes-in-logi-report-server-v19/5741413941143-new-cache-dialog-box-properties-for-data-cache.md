---
title: "New Cache Dialog Box Properties for Data Cache"
id: 5741413941143
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache
updated_at: 2022-10-31T17:16:57Z
---

# New Cache Dialog Box Properties for Data Cache

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741427157143-New-Cache-Dialog-Box-Properties-for-Connection-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405979671-New-Cube-Dialog-Box-Properties)

# New Cache Dialog Box Properties for Data Cache

This topic describes how you can use the New Cache dialog box to create a schedule task to generate [cached report data](https://devnet.logianalytics.com/hc/en-us/articles/5741453292183-Managing-Cached-Report-Data#Schedule) for the specified data resources.

Server displays the dialog box when an administrator selects **New Cache** in the Administration > Configuration > Cache > Data Cache page on the Server Console.

The dialog box includes two phases, one for [selecting data resources](#Query) and the other for [defining the schedule task](#Schedule).

## Selecting Data Resources Phase

At this phase, you need to specify the data resources for which you want to create cached data.

![New Cache dialog box - Select Data Resource](https://devnet.logianalytics.com/hc/article_attachments/9905676801175/nwcache_query.gif)

**Select a Folder**

Specify the folder in the server resource tree that contains the required catalog. You can select the ellipsis button ![Select Folder](https://devnet.logianalytics.com/hc/article_attachments/9905758084119/btn_chsr3.gif) to open the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443524503-Select-Folder-Dialog-Box-Properties) for selecting the folder.

**Select a Catalog**

Select a catalog in the folder.

**Select Queries**

Server lists the selected data resources.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**  
   Select to open the [Select Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421761431-Select-Queries-Dialog-Box-Properties) to select the data resources that you want to create data caches for.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**  
   Select to remove the selected data resources.

**OK**

Select to go to the next phase to define the schedule information.

**Cancel**

Select to close the dialog box without creating a data cache.

**Help**

Select to view information about the dialog box.

## Defining the Schedule Task Phase

At this phase, you need to define the data resource information and the updating policy of the data cache on these tabs:

* [General](#General)
* [Conditions](#Conditions)
* [Notification](#Notification)

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

![New Cache dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905676820631/nwcache_gen.gif)

**Select Query**

Server lists all the query resources you selected in the [Selecting Data Resources Phase](#Query). Select a query resource from the list, and then specify the general properties of its scheduled CRD task.

**Enter Parameters**

Specify the values of the parameters you want to apply to the selected query resource. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values).

If the query resource does not have parameters, Server displays "No Parameter Needed" here.

**Cached Report Data Info**

Specify the data cache information.

* **Name**  
   Name of the selected query resource. Server also uses it as the name of the new data cache.
* **Data Source**  
   Data source in which the query resource is.
* **Catalog**  
   Path of the catalog in which the query resource is. Server uses the latest catalog version by default.
* **Type**  
   Type of the query resource.
* **Priority**  
   Specify the priority level of the scheduled task. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. By default, Server ignores this property unless you modify [server.properties](https://devnet.logianalytics.com/hc/en-us/articles/5741387498391-Configuring-Server-Using-Properties-in-server-properties) in `<install_root>\bin` to set queue.policy not equal to 0.

**Advanced**

Configure some advanced settings.

* **Connect to [Data Source Name]**  
  Specify the DB user and password for connecting to the data source.
  + **Use the DB user and password defined in catalog**  
     Select if you want to use the DB user and password defined in the catalog.
  + **Use the DB User**  
     Select this property, and you can then specify another DB user and password instead of the one defined in the catalog.
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

### Conditions

Use the Conditions tab to specify the updating policy of the task. The tab contains two more tabs:

* [Time](#Time)
* [Trigger](#Trigger)

#### Time

Use the Time tab to specify the time when you want to perform the task.

![New Cache dialog box - Conditions - Time subtab](https://devnet.logianalytics.com/hc/article_attachments/9905715304855/nwcache_cndtn_time.gif)

**Time Zone**

Select the time zone.

**Time Type**

Specify when you want to perform the task.

* **Run this task immediately**  
   Select if you want to perform the task as soon as you submit it.
* **Run this task at**  
   Select if you want to perform the task at a specific time.
  + **Date**  
     Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif) to select a date from the calendar.
  + **Time**  
     Specify the time of the day.
  + **Run missed task upon server restart**  
     Select if you want to perform missed tasks when you restart the server.
* **Run this task periodically**  
   Select if you want to perform the task on a repeated basis.
  + **Do not generate cached result until a report requests**  
     By default, Server generates the cached report data according to the specified time condition. Select this property if you want the task to perform only upon the first report running request based on the query after each scheduled time.
  + **Duration**  
     Specify the period during which you want to perform the task on a repeated basis.
    - **Run after**  
       Select and then specify the start date and time of the period.
    - **Run until**  
       Select and then specify the end date and time of the period.
  + **Date**  
     Specify the dates when you want to perform the task.  
    - **Daily**  
       Select if you want to perform the task per a specific number of days or every weekday (from Monday to Friday).
    - **Weekly**  
       Select if you want to perform the task on the specific days of the week per a specific number of weeks.
    - **Monthly**  
       Select if you want to perform the task on a specific day of the month or week, per a specific number of months.
    - **Show/Hide Exception**   
      Select to show or hide the exception date box, which lists the dates when you do not want to perform the task.
      * **Add**  
         Select to add an exception date via the Select Condition dialog box.
      * **Remove**  
         Select to remove the selected exception dates.

      ![Exception Date Box](https://devnet.logianalytics.com/hc/article_attachments/9905637403415/sch_cndtn_time_excpt.gif)
  + **Time**  
     Specify the exact time of the day when you want to perform the task.
    - **At**  
       Select if you want to perform the task at a specific time of the day.
    - **Hourly**  
       Select if you want to perform the task at a specific minute per a specific number of hours.
    - **Minutely**  
       Select if you want to perform the task per a specific number of minutes.
  + **Run missed task upon server restart**  
     Select if you want to run missed tasks when you restart the server.

**Expires**

Specify when you want the cached data to expire.

* **Never**  
   Select if you don't want the cached data to expire.
* **At**  
   Select if you want the cached data to expire at a specific date and time.
* **After**  
   Select if you want the cached data to expire after a period.

#### Trigger

Use the Trigger tab to set settings for specifying a trigger for the task.

![New Cache dialog box - Conditions - Trigger subtab](https://devnet.logianalytics.com/hc/article_attachments/9905715332887/nwcache_cndtn_trgr.gif)

**Select a trigger to bind**

Select a trigger from the list for the task.

**New Trigger**

Select to open the [New Trigger dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741406198679-New-Trigger-Dialog-Box-Properties) to create a new trigger.

**Logic with time condition**

Specify the logic between the time condition and trigger condition.

* **Trigger Only**  
   Select if you want to perform the task only when an administrator fires the trigger.
* **Trigger and Time Condition**   
   Select if you want to perform the task when both time is up and an administrator fires the trigger.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) When you select this logic:

  + No matter which condition is ready, Server performs the task only when its counterpart is ready.
  + If you specify to perform the task at a specific time, you must select **Run missed task upon server restart**, otherwise Server regards the task as expired and deletes it when the time condition is ready before the trigger condition.
* **Time Condition after Trigger**   
   Select if you want to perform the task when time is up after an administrator fires the trigger. If the time condition is ready before the trigger condition, Server regards the task as expired and deletes it.
* **Time Condition or Trigger**  
   Select if you want to perform the task when either time is up or an administrator fires the trigger.

### Notification

Use the Notification tab to notify someone by email when the task finishes running, regardless of whether it is successful or not.

![New Cache dialog - Notification tab](https://devnet.logianalytics.com/hc/article_attachments/9905715355799/nwcache_notif.gif)

**When task is successful**

Select if you want to send an email when the task performs successfully.

**When task fails**

Select if you want to send an email when the task fails.

**To**

Specify the address you want to send the email to.

**Cc**

Specify the address you want to copy the email to.

**Bcc**

Specify the address you want to secretly copy the email to.

**Subject**

Specify the subject of the email.

**Comments**

Specify the contents of the mail or comments to the contents.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741427157143-New-Cache-Dialog-Box-Properties-for-Connection-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405979671-New-Cube-Dialog-Box-Properties)
