---
title: "New Cube Dialog Box Properties"
id: 5741405979671
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741405979671-New-Cube-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:58Z
---

# New Cube Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405948567-New-Custom-Field-Dialog-Box-Properties)

# New Cube Dialog Box Properties

This topic describes how you can use the New Cube dialog box to create a schedule task for generating an [in-memory cube](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes) for the specified business view.

Server displays the dialog box when an administrator selects **New Cube** in the Administration > Configuration > Cache > Cube page on the Server Console.

The dialog box includes two phases, one for [selecting the business view](#BV) and the other for [defining the schedule task](#Schedule).

## Selecting Business View Phase

At this phase, you need to specify the business view for which you want to create in-memory cube.

![New Cube dialog box- Select Business View](https://devnet.logianalytics.com/hc/article_attachments/9905715021463/nwcube_bv.gif)

**Select a Folder**

Specify the folder in the server resource tree that contains the required catalog. You can select the ellipsis button ![Select Folder](https://devnet.logianalytics.com/hc/article_attachments/9905758084119/btn_chsr3.gif) to open the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443524503-Select-Folder-Dialog-Box-Properties) for selecting the folder.

**Select a Catalog**

Select a catalog in the folder.

**Select Business View**

Select a business view in the catalog for which you want to create in-memory cube.

**OK**

Select to go to the next phase to define the schedule task.

**Cancel**

Select to close the dialog box without creating in-memory cube.

**Help**

Select to view information about the dialog box.

## Defining the Schedule Task Phase

At this phase, you need to define the business view information and the updating policy of the in-memory cube on these tabs:

* [General](#General)
* [Schedule](#Schedule)
* [Settings](#Settings)
* [Notification](#Notification)

**Back**

Select to go back to the previous tab.

**Next**

Select to go to the next tab.

**Finish**

Select to create the in-memory cube.

**Cancel**

Select to close the dialog box without creating in-memory cube.

**Help**

Select to view information about the dialog box.

### General

Before scheduling a cube task, you need to configure the settings in this tab first.

![New Cube dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905676634263/nwcube_gen.gif)

**Enter Parameters**

Specify values of the parameters you want to apply to the business view. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values).

If the business view does not have parameters, Server displays "No Parameter Needed" here.

**Cube Information**

Specify the in-memory cube information.

* **Cube Location**  
   Location of the cube. It is "Unknown" if it is the first time you schedule a task for the business view.
* **Name**  
   Name of the business view. Server also uses it as the name of the new cube.
* **Data Source**  
   Data source in which the business view is.
* **Catalog**  
   Path of the catalog in which the business view is.
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

### Schedule

Use the Schedule tab to specify the updating policy of the task. The tab contains two more tabs:

* [Time](#Time)
* [Trigger](#Trigger)

#### Time

Use the Time tab to specify the time for when you want to perform the task.

![New Cube dialog box - Schedule - Time subtab](https://devnet.logianalytics.com/hc/article_attachments/9905676674071/nwcube_schdl_time.gif)

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
  + **Run missed task upon Server restart**  
     Select if you want to perform missed tasks when you restart the server.
* **Run this task periodically**  
   Select if you want to perform the task on a repeated basis.
  + **Do not generate cached result until a report requests**  
     By default, Server generates the in-memory cube according to the specified time condition. Select this property if you want the task to perform only upon the first report running request based on the business view after each scheduled time.
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

#### Trigger

Use the Trigger tab to set settings for specifying a trigger for the task.

![New Cube dialog box - Schedule - Trigger subtab](https://devnet.logianalytics.com/hc/article_attachments/9905715107863/nwcube_schdl_trgr.gif)

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

### Settings

Use the Settings tab to configure the location and size of the cube.

![New Cube dialog box - Settings tab](https://devnet.logianalytics.com/hc/article_attachments/9905715141527/nwcube_set.gif)

**Maximum Memory Allowed**

Specify the maximum memory for the cube to use. The value should be no more than the available memory. You must provide the value, otherwise you cannot continue with the other tabs or finish the dialog box.

Each cube has this setting. The total of all cubes' maximum memory allowed should be no more than the [maximum cube memory allowed](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes#Memory).

**Move the cube to disk if insufficient memory is allocated**

Select if you want to cache the cube on the drive when the specified memory size is not enough to hold it. Then, when Server is initiating or updating an in-memory cube, if the memory requirement is bigger than the cube's maximum memory allowed, or if all in-memory cubes' memory usage is bigger than the maximum cube memory allowed, Server swaps the cube to the drive, otherwise if this property is cleared, Server sets the cube status to be disabled.

**Cache Detail on Disk**

Select if you want to cache the aggregation data in the business view into memory and cache the detail data on the drive.

By default, Server only caches the aggregation data in the business view into memory.

**Available Memory**

Memory that you can use to run the cube. The value equals the [maximum cube memory allowed](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes#Memory) for all cubes minus the total memory usage.

**Total Memory Usage**

Total maximum memory allowed for all in-memory cubes which are not in the Disabled status.

**Memory usage table**

Server lists the memory usage of all the other cubes excluding the current.

* **Name**  
   Name of a cube.
* **Maximum Memory Usage**  
   Maximum memory allowed for a cube.

### Notification

Use the Notification tab to notify someone by email when the task finishes running, regardless of whether it is successful or not.

![New Cube dialog box - Notification tab](https://devnet.logianalytics.com/hc/article_attachments/9905676739735/nwcube_notif.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741413941143-New-Cache-Dialog-Box-Properties-for-Data-Cache)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741405948567-New-Custom-Field-Dialog-Box-Properties)
