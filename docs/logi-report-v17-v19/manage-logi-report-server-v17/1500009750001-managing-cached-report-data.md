---
title: "Managing Cached Report Data"
id: 1500009750001
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750001-Managing-Cached-Report-Data
updated_at: 2021-07-25T07:18:59Z
---

# Managing Cached Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes)

# Managing Cached Report Data

Cached report data (CRD) is a cached subset of data fetched from the database and is used as a substitute for the database for retrieving data for reports. This provides several benefits.

* Reports can be run from a specific point in time such as a month end report or quarter end report without going back to the DBMS to get the original data.
* Many users can run reports from data cached from a single data resource without impacting production DBMS users.
* Users running a report will all see the same view of the data, thus the data will not change minute by minute based on current DBMS updates.
* Cached report data can be scheduled for any time frame to simulate real time on-demand reporting for many users while not slowing down the production DBMS.

Cached report data can be created for data resources including queries, stored procedures, imported SQLs, user defined data sources, hierarchical data sources, and parameters whose type is Bind with Single Column or Bind with Cascading Columns.

Administrators can either make cached report data created automatically (auto CRD) or schedule to have a cached data result created for a data resource and updated at a specific time or periodically (scheduled CRD).

* **Auto CRD**  
   Auto CRD are disabled for generation by default. Administrators can enable them and configure the maximum hard disk space for auto CRD and how long an auto CRD can be kept.
* **Scheduled CRD**  
   Via Logi Report's scheduling mechanism, administrators are able to define when a cached data result for a data resource will be created and how it will be updated according to time. If a scheduled CRD is updating when the server shuts down, the CRD will continue with the update when the server restarts. The data before the shutdown will be maintained. Scheduled CRD have no version: once they are updated, only the latest are kept in the data resource.

Select the following links to view the topics:

* [Creating Cached Report Data Automatically](#Auto)
* [Scheduling Cached Report Data Results](#Schedule)
* [Managing Scheduled CRD Tasks](#Manage)

## Creating Cached Report Data Automatically

Cached report data cannot be generated automatically by default. Administrators can enable the generation of auto CRD and configure the maximum hard disk space for auto CRD and how long an auto CRD can be kept.

**To enable creating cached report data automatically:**

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Cache** > **Data Cache** from the drop-down menu. Report Server displays the Data Cache page.

   ![Data Cache Page](https://devnet.logianalytics.com/hc/article_attachments/4404942508439/mng_crd_pg.gif)
2. Select **Cache Configuration** on the task bar. This option is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations).
3. Select **Automatic Cache** to enable creating cached report data automatically.

   ![Cache Configuration dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936803607/mng_crd_auto.gif)
4. In the Maximum Disk Usage text box, specify the maximum hard disk space for the automatically created CRD, which determines how many auto CRD can be held within one server session. The value should be between 4 MB and 1024\*1024 MB.
5. Specify how long an automatically cached data result can be kept
   within one server session.
   * **Never**  
      The auto CRD will not expire.
   * **Custom**  
      Specifies the period an auto CRD exists.
6. In the Maximum Memory Usage text box, specify the maximum memory usage when running reports using CRD. The value should be at least 4 MB and not more than 80% of the JVM current maximum heap size (-Xmx value in JRServer.bat). The number of MBs must be configured in whole numbers.

   All CRD (both auto CRD and scheduled CRD) share the same memory space. If possible, set the maximum memory usage to a number that the memory can tolerate, for example, 1024 MB or bigger. The cache is used to improve performance when multiple users are running reports using the same CRD. Any size CRD can be accessed with even the smallest cache size. The larger the cache size the faster performance will be for concurrent users, but a large cache size may lower performance for users who do not use the CRD.
7. Select **OK** to apply the settings.

When automatic cache is enabled, while running a report, if there is no scheduled CRD created for the data resource that the report is using directly or indirectly (for example, the report is created based on a business view and the business view is built from a data resource), data will be fetched from the data resource, and at the same time the fetched data is cached and becomes an auto CRD.

When there are auto CRD generated for a data resource, the report running request based on the data resource will first search for the auto CRD that contains all the data required by the report. If an auto CRD is located, Logi Report will retrieve data from the CRD to run the report; if no applicable auto CRD can be found, data is fetched from the DBMS and cached to be another auto CRD.

Auto CRD are only available within one server running life cycle, which means that once the server shuts down or restarts, they will be removed and a new cycle of auto CRD generation begins.

## Scheduling Cached Report Data Results

Administrators can schedule to have a cached data result (scheduled CRD) created for a data resource and updated at a specific time or periodically. This is especially useful for month and quarter end reports where multiple reports use the same dataset with the same parameters such as begin and end date.

Scheduled CRD can be generated via Logi Report's scheduling mechanism. In one scheduled CRD task, more than one data resource can be added, then a cached data result will be created for each data resource by applying the same creation and updating policy.

A data resource can have only one scheduled CRD. When a data resource contains parameters, its scheduled CRD can only represent the data of one parameter scenario.

**To create a schedule task to generate cached report data at specified time condition**:

1. In the Data Cache page, select **New Cache** on the task bar. Report Server displays the [New Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009747481-New-Cache) dialog box.

   ![New Cache dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936803863/nwcache_query.gif)
2. Select ![Select Folder](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) next to the Select a Folder text box. In the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009747961-Select-Folder) dialog box, browse to the folder containing the required catalog and select **OK**.
3. From the Select a Catalog drop-down list, select the catalog in the specified folder.
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) beside the Select Queries box. In the [Select Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009748001-Select-Queries) dialog box, select the data resources for which you want to create data cache and select **OK**.

   To remove a data resource from the box, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
5. Select **OK** to confirm the selection. The tabs for defining the schedule task are then displayed.
6. In the General tab,

   ![New Cache - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404942508695/nwcache_gen.gif)

   1. From the Select Query drop-down list, select a data resource to specify the general properties of its scheduled CRD task.
   2. If the data resource uses parameters, you need to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values) in the Enter Parameters section.
   3. Expand the **Cached Report Data Info**  section, assign a priority to the task from the Priority drop-down list. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
   4. Expand the **Advanced** section to configure some advanced settings for the CRD.

      Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.

      Select the **Add TaskListener to be Invoked** option to call a Java application before/after the task runs so as to obtain information about the task (for details, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009718522-Applying-TaskListener)).

      If you are in a [cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009744601-Logi-Report-Server-Cluster) environment, you can also directly specify an active server in the cluster to perform the schedule task via the Specify a preferred server to run the task option.

      If you want to enable task recovery, select **Enable Auto Recover Task**, then specify the maximum number of times in which to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results.
   5. Select another data resource from the Select Query drop-down list and repeat the above steps to define the properties of its scheduled CRD. Do this for all the added data resources.
7. In the Conditions tab,
   specify the updating policy of the data cache. The condition will be applied to generate cached data for all the added data resources.
   1. In the Time sub tab, specify the time for when the task is to be performed.

      ![New Cache - Time subtab](https://devnet.logianalytics.com/hc/article_attachments/4404942510615/nwcache_cndtn_time.gif)

      From the Time Zone drop-down list, select the time zone.

      From the Time Type drop-down list, select how the task will be performed.

      * To perform the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**, then define the time according to your requirement.
      * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time. By default, the task will be performed according to the specified time condition to generate the cached report data. If you prefer to run the task only upon the first report running request based on the query after each scheduled time, select **Do not generate cached result until a report requests**. To add an exception date on which you do not want to run the task, select **Show Exception**, then select the **Add** button and in the Select Condition dialog box select the date as required. You can add several exception dates as you want. To remove an exception date, select it in the exception date box and select **Remove**.

        ![Exception Date Box](https://devnet.logianalytics.com/hc/article_attachments/4404942481431/sch_cndtn_time_excpt.gif)

      From the Expires drop-down list, specify the expiration time for how long to keep the cached data:

      * To make the cached data never expire, select **Never**.
      * To make the cached data expire at a specified time, select **At**, then specify the date and time accordingly.
      * To make the cached data expire after a period of time, select **After**, then specify the time period.

      When you select to run the task at a specified time or repeatedly, you can select **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
   2. If you want to bind a [trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009723162-Managing-Triggers) to the task, switch to the **Trigger** sub tab.

      ![New Cache - Trigger subtab](https://devnet.logianalytics.com/hc/article_attachments/4404936804375/nwcache_cndtn_trgr.gif)

      From the Select a trigger to bind drop-down list, select the required trigger or select the **New Trigger**  button to create a new trigger in the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009720722-New-Trigger) dialog box (the button is not available to [organization admins](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations)), then specify the trigger logic with time condition.

   * **Trigger Only**  
      Performs the task only when the trigger is fired.
   * **Trigger and Time Condition**   
      Performs the task when both time is up and the trigger is fired.

     **Note:** When this logic is selected:

     + No matter which condition is ready, the task can only be performed when its counterpart is ready.
     + If you specify the task to be performed at a specific time, you must select the option Run missed task upon server restart, otherwise the task will be regarded as expired and will be deleted when the time condition is ready before the trigger condition.
   * **Time Condition after Trigger**   
      Performs a task when time is up after the trigger is fired. If the time condition is ready before the trigger condition, the task will be regarded as expired and will be deleted.
   * **Time Condition or Trigger**  
      Performs the task when either time is up or the trigger is fired.
8. In the Notification tab, specify to notify someone via e-mail of when the task is finished successfully or when it fails, then in the mail box, type the information of the receivers and the mail content. To send out mail notification, an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009744921-Configuring-the-E-mail-Server) must have been predefined by the administrator.

   ![New Cache - Notification tab](https://devnet.logianalytics.com/hc/article_attachments/4404942512535/nwcache_notif.gif)
9. Select **Finish** to submit the task. Logi Report Server will then perform the task at the requested times to create cached data for all the specified data resources.

When a scheduled CRD is ready for use, all reports based on the same data resource as the CRD will automatically use the CRD for retrieving data. Since a scheduled CRD freezes parameters in the data resource, if a report uses a scheduled CRD and its data resource contains parameters, when running the report, only parameters used in the report are available for specifying values and the data resource parameters will be disabled for editing. In Logi Report, a parameter may depend on another parameter; if the latter is frozen, the former will be frozen as well.

If the data resource used for creating a scheduled CRD is updated due to [catalog republishing](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources), the scheduled CRD will behave as follows:

* Before the next schedule time, the CRD will be disabled for retrieving data to reports.
* When it is the next schedule time, data is fetched from the new data resource to generate an updated scheduled CRD:
  + If new parameters are added in the new data resource, default values will be used until an administrator specifies values to them.
  + If old parameters are deleted from the new data resource, the parameter values previously specified in the CRD will be removed.
  + If parameters are changed and the previously specified values do not match the type, error messages will be given in the server error log and the CRD is disabled for use.

## Managing Scheduled CRD Tasks

The tasks that have been submitted for generating scheduled CRD are listed in the [Cached Report Data](#Cached), [Scheduled](#Scheduled), [Running](#Running), and [Completed](#Completed) tables in the Data Cache page according to their status.

The following lists the columns each table contains in details.

**Cached Report Data table**

This table displays the scheduled data cache tasks and consists of the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Last Modified | The last time when the scheduled data cache was modified. |

You can further edit the scheduling information of the tasks in the table or remove the tasks.

* To edit a task, select the row in which the task is, then select **Edit > Properties** on the task bar or right-click on the row and select **Properties** from the shortcut menu. If parameters or schedule policy is changed, they will only take effect after the next CRD update time; before that, all reports using the CRD will still get the old data.
* To remove a task, select the row where the task is, then selecting **Edit > Delete** on the task bar; or right-click in the row and select **Delete** from the shortcut menu.

**Scheduled table**

This table displays the data cache tasks that are waiting to be performed. It consists of the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Last Modified | The latest time when the task was modified. |
| Next Run Time | The next scheduled time this task is to be performed. |
| Last Run Time | The last scheduled time this task was performed. |
| Is Successful | Shows whether or not the last running of this task was successfully performed. The value true means that the last running was performed successfully and false means the task failed. If the column is empty, the task has not been run before. |

**Running table**

This table displays the data cache tasks that are currently being performed. It consists of the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Start Time | The time when this task was started. |
| Parameters | The parameters of the query. |

**Completed table**

This table displays the data cache tasks that have already been finished and consists of the following columns.

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Is Successful | Shows whether this task was successfully performed. The value true means that the task was performed successfully and false that the task failed. |
| Completed Time | The time when this task was completed. |
| Parameters | The parameters of the query. |

When a task is listed in the table, the cached report data generated from the schedule task will be ready for use.

You can remove the record of a completed CRD task from the table. To do this, select the row where the record is located and then select **Delete** on the task bar, or right-click on the row and select **Delete** from the shortcut menu.

**Tips:**

* You can customize the columns shown in the tables as follows: switch to the table, select **Preferences** on the task bar of the Data Cache page. In the Preferences dialog box select the check box ahead of the column names which you want to display in the table, then select **OK** to apply the settings.
  For the Running table, you can also use the Parameter Display Size option to specify the display length in characters of the parameters listed in its Parameters column; and for the Completed table, specify the number of days for keeping completed tasks and the display length of the parameters listed in its Parameters column.
* You can make the records in each table sorted ascending or descending by any column title. To do this, select on the underlined column title on which you want the records to be sorted, you will then find a sort icon appear right after the title, showing the sort direction.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes)
