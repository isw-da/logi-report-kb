---
title: "New Cube Dialog Box Properties"
id: 1500009774061
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774061-New-Cube-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:47Z
---

# New Cube Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746102-New-Cache-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746122-New-Custom-Field-Dialog-Box-Properties)

# New Cube Dialog Box Properties

This topic describes how you can use the New Cube dialog box to create a schedule task for generating an [in-memory cube](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes) for the specified business view.

Server displays the dialog box when an admin user selects the New Cube link in the Administration > Configuration > Cache > Cube page in the Server Console.

The dialog box is divided into two phases, one for [selecting the business view](#BV)  and the other for [defining the schedule task](#Schedule).

## Selecting Business View Phase

At this phase, you need to specify the business view for which to create in-memory cube.

![New Cube dialog - Select Business View](https://devnet.logianalytics.com/hc/article_attachments/4404880298775/nwcube_bv.gif)

**Select a Folder**

Specifies the folder in the server resource tree that contains the required catalog. You can select the button ![Select Folder](https://devnet.logianalytics.com/hc/article_attachments/4404880424599/btn_chsr3.gif) to open the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009746422-Select-Folder-Dialog-Box-Properties) dialog box for selecting the folder.

**Select a Catalog**

Specifies the catalog in the folder.

**Select Business View**

Specifies the business view in the catalog for which to create in-memory cube.

**OK**

Goes to the next phase to define the schedule information.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

## Scheduling

At this phase, you need to define the business view information and the updating policy of the in-memory cube with the following tabs:

* [General](#General)
* [Schedule](#Schedule)
* [Settings](#Settings)
* [Notification](#Notification)

**Back**

Goes back to the previous tab.

**Next**

Goes to the next tab.

**Finish**

Applies the settings.

**Cancel**

Cancels any settings and returns to the selecting business view phase.

**Help**

Displays the help document about this feature.

### General

Before you can schedule a cube task, you first need to configure the settings in this tab.

![New Cube dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880299287/nwcube_gen.gif)

**Enter Parameters**

Specifies values of the parameters applied in the business view. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values).

If the business view does not have parameters, Server displays "No Parameter Needed" here.

**Cube Information**

Specifies the in-memory cube information.

* **Cube Location**  
   Shows the location of the cube. It is "Unknown" if it is the first time you schedule a task for the business view.
* **Name**  
   Shows the name of the business view. It is also used as the name of the new cube.
* **Data Source**  
   Shows the data source name.
* **Catalog**  
   Shows the catalog name.
* **Priority**  
   Specifies a priority level to the scheduled task. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. By default, this property is ignored unless server.properties is modified to set queue.policy not equal to 0.

**Advanced**

Configures some advanced settings.

* **Connect to [Data Source Name]**  
   Specifies the DB user and password with which you want to connect to the data source.
  + **Use the DB user and password defined in catalog**  
     If the option is selected, the DB user and password defined in the catalog will be used.
  + **Use the DB User**  
     If the option is selected, you can then specify another DB user and password instead of the one defined in the catalog.
* **Add TaskListener to be Invoked**  
   Enables you to call a Java application before/after the task runs so as to obtain information about the task.
* **Enable Auto Recover Task**  
   Specifies to enable the task to be auto recovered.
  + **Maximum Retry Times**  
     Specifies the maximum number of times in which to retry running the task in order to recover it.
  + **Retry Interval**  
     Specifies the interval between retries.
  + **Recreate All Results**  
     Specifies whether to recreate all results or just the failed results.

### Schedule

The Conditions tab enables you to specify the updating policy of the task. It contains the following two sub tabs:

* [Time](#Time)
* [Trigger](#Trigger)

#### Time

The Time tab enables you to set settings for specifying the time for when the task is to be performed.

![New Cube dialog - Schedule - Time subtab](https://devnet.logianalytics.com/hc/article_attachments/4404880299543/nwcube_schdl_time.gif)

**Time Zone**

Specifies the time zone.

**Time Type**

Specifies when the task will be performed.

* **Run this task immediately**  
   Specifies to run the task as soon as you submit it.
* **Run this task at**  
   Specifies the time for when the task is to be performed once.
  + **Date**   
     Specifies the date to run the task. You can select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif) to select a date from the calendar.
  + **Time**  
     Specifies the time to run the task.
  + **Run missed task upon Server restart**  
     Specifies to run missed tasks when you restart the server.
* **Run this task periodically**  
   Specifies the time for when the task is to be performed on a repeated basis.
  + **Do not generate cached result until a report requests**  
     This option is unselected by default, which means the task will be performed to generate the in-memory cube according to the specified time condition. If it is selected, the task will be performed only upon the first report running request based on the business view after each scheduled time.
  + **Duration**  
     Specifies the period during which the task is to be performed.
    - **Run after**  
       Specifies the start date and time of the period during which the task is to be performed on a repeated basis.
    - **Run until**  
       Specifies the end date and time of the period during which the task is to be performed on a repeated basis.
  + **Date**  
     Specifies the date on which the task is to be performed.
    - **Daily**  
       Performs the task every one day, two days, etc., or every weekday (from Monday to Friday).
    - **Weekly**  
       Performs the task every one week, two weeks, etc., and on Sunday, Monday, Tuesday, etc.
    - **Monthly**  
       Performs the task on the first day, second day, etc. of every one month, two months, etc., or on the first Sunday, Monday, etc. of every one month, two months, etc.
    - **Show/Hide Exception**   
       Shows/Hides the exception date box that lists the dates on which you do not want to run the task.
      * **Add**  
         Adds an exception date via the Select Condition dialog box.
      * **Remove**  
         Removes the selected exception dates.

      ![Exception Date Box](https://devnet.logianalytics.com/hc/article_attachments/4404880230167/sch_cndtn_time_excpt.gif)
  + **Time**  
     Specifies the exact time at which the task is to be performed.
    - **At**  
       Specifies the time to run the task.
    - **Hourly**  
       Performs the task every one hour, two hours, etc., at a certain minute on a selected day.
    - **Minutely**  
       Performs the task every one minute, two minutes, etc.
  + **Run missed task upon server restart**  
     Specifies to run missed tasks when you restart the server.

#### Trigger

The Trigger tab enables you to set settings for specifying a trigger for the task.

![New Cube dialog - Schedule - Trigger subtab](https://devnet.logianalytics.com/hc/article_attachments/4404880300055/nwcube_schdl_trgr.gif)

**Select a trigger to bind**

Specifies the trigger from the drop-down list for the task.

**New Trigger**

Opens the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009774281-New-Trigger-Dialog-Box-Properties) dialog box for you to create a new trigger.

**Logic with time condition**

Specifies the logic between time condition and trigger condition.

* **Trigger Only**  
   Performs the task only when the trigger is fired.
* **Trigger and Time Condition**   
   Performs the task when both time is up and the trigger is fired.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When you selected this logic:

  + No matter which condition is ready, Server performs the task only when its counterpart is ready.
  + If you specify to perform the task at a specific time, you must select the option **Run missed task upon server restart**, otherwise Server regards the task as expired and deletes it when the time condition is ready before the trigger condition.
* **Time Condition after Trigger**   
   Performs a task when time is up after the trigger is fired. If the time condition is ready before the trigger condition, the task will be regarded as expired and will be deleted.
* **Time Condition or Trigger**  
   Performs the task when either time is up or the trigger is fired.

### Settings

The Settings tab enables you to configure the location and size of the cube.

![New Cube dialog - Settings tab](https://devnet.logianalytics.com/hc/article_attachments/4404880300439/nwcube_set.gif)

**Maximum Memory Allowed**

Specifies the maximum memory for the cube to use. Each cube has this setting. The total of all cubes' maximum memory allowed should be no more than the [maximum cube memory allowed](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes#Memory).

The value must be provided, otherwise you are not allowed to continue with the other tabs or to finish the dialog box. The value should be no more than the available memory.

**Move the cube to disk if insufficient memory is allocated**

When the option is selected, the cube will be cached on disk when the specified memory size is not enough to hold it.

If the option is selected, when initiating or updating an in-memory cube, if the memory requirement is bigger than the cube's maximum memory allowed, or if all in-memory cubes' memory usage will be bigger than the maximum cube memory allowed, the cube will be swapped to disk, otherwise if this option is unselected, the cube status will be set to disabled.

**Cache Detail on Disk**

When the option is selected, the aggregation data in the business view will be cached into memory and the detail data will be cached on disk.

When the option is unselected, only the aggregation data in the business view will be cached into memory.

**Available Memory**

Shows the memory that can be used to run the cube. The value equals the [maximum cube memory allowed](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes#Memory) for all cubes minus the total memory usage.

**Total Memory Usage**

Shows the total maximum memory allowed for all in-memory cubes which are not in the Disabled status.

**Memory usage table**

Lists the memory usage of all the other cubes excluding the current.

* **Name**  
   The name of the cube.
* **Maximum Memory Usage**  
   The maximum memory allowed for the cube.

### Notification

The Notification tab enables you to notify someone by e-mail when the task finishes running, regardless of whether it is successful or unsuccessful.

![New Cube dialog - Notification tab](https://devnet.logianalytics.com/hc/article_attachments/4404880300951/nwcube_notif.gif)

**When task is successful**

Specifies to send an e-mail when the task is successful.

**When task fails**

Specifies to send an e-mail when the task is unsuccessful.

**To**

Specifies the address you want to send the e-mail to.

**Cc**

Specifies the address you want to copy to.

**Bcc**

Specifies the address you want to secretly copy to.

**Subject**

Specifies the subject of the e-mail.

**Comments**

Specifies the contents of the mail or comments to the contents.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746102-New-Cache-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746122-New-Custom-Field-Dialog-Box-Properties)
