---
title: "Managing In-Memory Cubes"
id: 1500009777121
section: "Managing Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes
updated_at: 2021-07-24T00:47:59Z
---

# Managing In-Memory Cubes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777101-Managing-Cached-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777321-Managing-Triggers)

# Managing In-Memory Cubes

In-memory cubes cache aggregations (pre-computed aggregate functions) of business views. This topic describes how you can create, use, and manage in-memory cubes, as an administrator.

You can use the cube data to improve the performance of reports and visualizations, when you analyze and visualize data from any data source, including relational, cloud, and big data sources.

You can generate and update in-memory cubes by scheduling cube tasks. Similar to scheduling report tasks, you can schedule to generate in-memory cubes immediately, at a specific time, or periodically to fetch the data from the DBMS and store it in Logi Report Server. After Server creates an in-memory cube and it is ready for use, all reports, library components, and visual analysis that use the same business view as the in-memory cube will automatically use the cube rather than go to the database for the data. By applying in-memory cubes, your reporting performance will be greatly improved.

This topic contains the following sections:

* [Creating In-Memory Cubes](#Create)
* [Viewing and Managing the Cube Tasks](#View)
* [Recovering In-Memory Cubes](#Recover)
* [Synchronizing In-Memory Cubes With Catalog Republish](#Sync)

## Creating In-Memory Cubes

A business view can have only one in-memory cube. When a business view contains parameters, its in-memory cube can only represent the data of one parameter scenario.

Via Server's scheduling mechanism, you are able to define when to create an in-memory cube for a business view and when to update it at a specific time or periodically. This is especially useful for month and quarter end reports where multiple reports use the same dataset with the same parameters such as begin and end date.

In-memory cubes have no versions: once they are updated, Server keeps only the latest ones for the business views.

**To create an in-memory cube:**

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** > **Cache** > **Cube** from the drop-down menu. Server displays the Cube page.

   ![Cube page](https://devnet.logianalytics.com/hc/article_attachments/4404885416599/mng_cube_pg.gif)

   ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404885352855/criticalicon.gif)If it is the first time you create in-memory cubes, you need to first configure the maximum memory allowed for all in-memory cubes. To do this, select **Configuration** on the task bar of the Cube page (this option is not available to [organization admins](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations)), then in the **Maximum Cube Memory Allowed** text box, specify the allowed maximum cube memory size in megabytes. The total allocated memory for each cube cannot exceed this value. It does not take into consideration the actual memory used by the in-memory cubes or if some of the cubes are swapped to disk. This value should not be larger than 80% of your Java Heap size.
2. Select **New Cube** on the task bar. Server displays the [New Cube](https://devnet.logianalytics.com/hc/en-us/articles/1500009774061-New-Cube-Dialog-Box-Properties) dialog box[.](https://devnet.logianalytics.com/hc/en-us/articles/1500009774061-New-Cube-Dialog-Box-Properties) 

   ![New Cube dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880298775/nwcube_bv.gif)
3. Select ![Select Folder](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) next to the **Select a Folder** text box.
4. Server displays the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009746422-Select-Folder-Dialog-Box-Properties) dialog box. Browse to the folder that contains the required catalog and select **OK**.
5. From the **Select a Catalog** drop-down list, select the required catalog in the specified folder.
6. In the **Select Business View** box, select the business view on which to create the in-memory cube.
   Server uses the business view name as the name of the in-memory cube.
7. Select **OK** to confirm the selection. Server displays a new dialog box for defining the schedule task.
8. In the **General** tab, do the following:

   ![New Cube - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880299287/nwcube_gen.gif)

   1. [Specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values) if the business view uses parameters.
   2. Expand the **Cube Information** section by clicking the down arrow on the right.
   3. Select a priority to the task from the **Priority** drop-down list. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. By default, Server ignores this property unless you modify the file **server.properties** to set **queue.policy** not equal to 0.
   4. Expand the **Advanced** section to configure advanced settings.
   5. Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.
   6. Select the **Add TaskListener to be Invoked** option to call a Java application before/after the task runs so as to obtain information about the task (for more information, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009771141-Applying-TaskListener)).
   7. If you are in a [Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009743402-Logi-Report-Server-Cluster) environment, you can also directly specify an active server in the cluster to perform the schedule task via the **Specify a preferred server to run the task** option.
   8. If you want to enable task recovery, select **Enable Auto Recover Task**. Then specify the maximum number of times to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results.
9. In the **Schedule** tab, specify the updating policy of the in-memory cube.
   1. In the **Time** tab, specify the time for when Server performs the task.

      ![New Cube - Time subtab](https://devnet.logianalytics.com/hc/article_attachments/4404880299543/nwcube_schdl_time.gif)

      From the **Time Zone** drop-down list, select the time zone.

      From the **Time Type** drop-down list, select when to run the task:

      * To run the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**. Then define the date and the time.
      * If you want to run the task repeatedly, select **Run this task periodically**. Then specify the duration, date, and time accordingly. By default, Server generates the in-memory cube according to the specified time condition. If you prefer to run the task only upon the first report running request after each scheduled time, select **Do not generate cached result until a report requests**. To add an exception date on which you do not want to run the task, select **Show Exception**, then select the **Add** button and in the **Select Condition** dialog box select the date. You can add several exception dates as you want. To remove an exception date, select it in the exception date box and select **Remove**.

        ![Exception Date Box](https://devnet.logianalytics.com/hc/article_attachments/4404880230167/sch_cndtn_time_excpt.gif)

      When you select to run the task at a specified time or repeatedly, you can select **Run missed task upon server restart** to run the missed tasks when you restart the server.
   2. If you want to bind a [trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009777321-Managing-Triggers) to the task, switch to the **Trigger** tab.

      ![New Cube - Trigger subtab](https://devnet.logianalytics.com/hc/article_attachments/4404880300055/nwcube_schdl_trgr.gif)

      From the **Select a trigger to bind** drop-down list, select the required trigger or select the **New Trigger**  button to create a new trigger in the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009774281-New-Trigger-Dialog-Box-Properties) dialog box (the button is not available to [organization admins](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations)), then specify the trigger logic with time condition.

      * **Trigger Only**  
         Select if you want to perform the task only when the trigger is fired.
      * **Trigger and Time Condition**   
        Select if you want to perform the task when both time is up and the trigger is fired.

        ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When you selected this logic:

        + No matter which condition is ready, Server performs the task only when its counterpart is ready.
        + If you specify to perform the task at a specific time, you must select the option **Run missed task upon server restart**, otherwise Server regards the task as expired and deletes it when the time condition is ready before the trigger condition.
      * **Time Condition after Trigger**   
         Select if you want to perform the task when time is up after the trigger is fired. If the time condition is ready before the trigger condition, the task will be regarded as expired and will be deleted.
      * **Time Condition or Trigger**  
        Select if you want to perform the task when either time is up or the trigger is fired.
10. In the **Settings** tab,
    configure the following settings:

    ![New Cube - Settings tab](https://devnet.logianalytics.com/hc/article_attachments/4404880300439/nwcube_set.gif)

    1. In the **Maximum Memory Allowed** text box, provide a value for the cube. Otherwise, you cannot continue with the other tabs or to finish the dialog box.
    2. If you would like to cache the cube on disk once the available memory is exhausted, select **Move the cube to disk if insufficient memory is allocated**. If you do not select this option and the memory is not enough for the cube, Server will disable the cube and leave an error message in the log.
    3. If you would like to cache the detail data in the business view on disk, select **Cache Detail on Disk**. Otherwise Server only caches the aggregation data.
11. In the **Notification** tab, specify to notify someone via e-mail of when the task finishes or when it fails. Then in the mail box, type the information of the receivers and the mail content. To send out mail notification, you should have predefined an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009743742-Configuring-the-E-mail-Server) first.

    ![New Cube - Notification tab](https://devnet.logianalytics.com/hc/article_attachments/4404880300951/nwcube_notif.gif)
12. Select **Finish** to submit the task. Server will then perform the task at the requested times to create in-memory cube for the specified business view.

After Server creates an in-memory cube and it is ready for use, all reports, library components, and visual analysis based on the same business view as the cube will automatically use the cube for retrieving data.

An in-memory cube freezes parameters in its related business view. If a report uses an in-memory cube and its business view contains parameters, when running the report, only parameters used in the report are available for specifying values and you cannot edit the business view parameters. In Logi Report, a parameter may depend on another parameter; if the latter is frozen, the former will be frozen as well.

## Viewing and Managing the Cube Tasks

You can view information of the tasks scheduled for creating in-memory cubes and manage the tasks in the [Schedule](#Schedule), [Active](#Active), and [Log](#Log) tables in the Cube page.

**Schedule table**

Server displays all scheduled cube tasks in the Schedule table. You can edit any of the tasks in the table as follows:

* To further edit the scheduling information of a task, select the row in which the task is, then select **Edit > Properties** on the task bar, or the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404885407255/btn_srv_prpty.gif) on the floating toolbar, or right-click on the row and select **Properties** on the shortcut menu. Server displays a dialog box for you to edit the scheduling information. If you change the parameter values or schedule policy, they will only take effect after the next cube update; before that, all reports using the cube will still get the old data.
* To disable a task, select the row where the cube task is, then select **Edit > Disable** on the task bar, or the **Disable** button ![Disable button](https://devnet.logianalytics.com/hc/article_attachments/4404880286871/btn_srv_disable.gif) on the floating toolbar, or right-click on the row and select **Disable** on the shortcut menu.
* To enable a task, select the row where the cube task is, then select **Edit > Enable** on the task bar, or the **Enable** button ![Enable button](https://devnet.logianalytics.com/hc/article_attachments/4404880286487/btn_srv_enable.gif) on the floating toolbar, or right-click on the row and select **Enable** on the shortcut menu.
* To remove a task that is no longer required, select the row where the cube task is, then select **Edit > Delete** on the task bar, or the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885308823/btn_dltobj.gif) on the floating toolbar, or right-click on the row and select **Delete** on the shortcut menu.

The Schedule table contains the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the cube task. |
| Catalog | The catalog that the cube belongs to. |
| Data Source | The data source that the cube belongs to. |
| Status | The task status:  * Pending -   The cube has no data and is waiting to run based on schedule policy.   The cube is not ready for use. * Building -   It is the first time that Server is creating the cube and filling data to the cube. The cube is not ready for use. * Updating -   Server is updating cube data based on the schedule policy. The cube is not ready for use. * Completed -   The task is finished, and the cube is ready for use. * Disabled - Server will not   generate or update the cube following the schedule policy. The cube data cannot be used or released. |
| Create Time | The time when the scheduled task was created. |
| Next Run Time | The next time when the scheduled task will generate or update the cube. |
| Last Run Time | The last time when the scheduled task generated or updated the cube. |
| Times Run | The number of times the scheduled task has generated or updated the cube. If the number is bigger than 0, select it and you will be able to view the details of each running of the cube, including all updating events since the cube was generated. The detail table contains the following columns:   | Column | Description | | --- | --- | | Activity | The type of the event:  * Build -   The cube was created. * Update -   The cube was updated. | | Start Time | The time when the event started. | | End Time | The time when the event ended. | | Status | Show whether the event is successful or failed. | |

**Active table**

Server displays the cube tasks that have generated in-memory cubes which have data and are ready for use, in the Active table. You can edit the tasks here [in the same way as you do in the Schedule table](#Schedule).

The Active table contains the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the cube task. |
| Catalog | The catalog that the cube belongs to. |
| Data Source | The data source that the cube belongs to. |
| Updated Time | The last time when the cube was updated. |
| Allocated | The maximum memory allowed for the cube. |
| Actual | The memory size currently used by the cube. |
| Located At | The location of the cube:  * On Disk - The cube is swapped to the disk. * In Memory - The cube is in the memory. |
| Parameter | You see a parameter icon. After you select the icon, Server displays a dialog box to show all the parameters used in the cube. |
| Usage | The number of reports and library components that have accessed the cube. If the number is bigger than 0, select it and you will get a detail table showing the information of all the web reports and library components that used data from the cube. The detail table contains the following columns:   | Column | Description | | --- | --- | | Name | The name of the web report or the library component that used the cube. | | Type | Indicate whether it is a web report or a library component. | | Dashboard | The name of the dashboard that is using the library component. For library components only. | | User | The user who ran the web report or the library component. | | Description | The description about the web report or the library component. | |

**Log table**

Server records all the events happened on all the cube tasks, in the Log table. You can delete any of the log records from the table if you want. To do this, select a record row and then select **Edit > Delete** on the task bar, or select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885308823/btn_dltobj.gif) on the floating toolbar, or right-click on the record row and select **Delete** on the shortcut menu.

The Log table contains the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the cube task. |
| Catalog | The catalog that the cube belongs to. |
| Data Source | The data source that the cube belongs to. |
| Activities | The type of the event:  * Create - The cube was created. * Edit - The cube was edited. * Initiate - The cube data was initiated and made usable. * Update - The cube data was updated. * Disable - The cube was disabled. * Enable - The cube was enabled. * Delete - The cube was deleted. |
| Start Time | The time when the event started. |
| End Time | The time when the event ended. |
| Status | The event status: Successful or Failed. |
| Message | Messages for failed events. |

**Tips:**

* You can customize the columns shown in the tables as follows: switch to the table, select **Preferences** on the task bar of the Cube page, select the corresponding items in the **Preferences** dialog box, then select **OK** to apply the settings.
* You can sort the records in each table in the ascending or descending order by any column title. To do this, select on the underlined column title on which you want to sort the records. Server displays a sort icon right after the title, showing the sort direction.

## Recovering In-Memory Cubes

If an in-memory cube is updating when Server shuts down, the cube will be disabled after the server restarts. You need to enable the cube task in order for the cube to continue to update at the next scheduled time.

## Synchronizing In-Memory Cubes With Catalog Republish

After you republish a catalog, how the existing in-memory cubes based on the old business views in the catalog will be updated depends on the following conditions:

When no business view changed, the existing in-memory cubes are automatically applicable to the new catalog.

When a business view changed, the in-memory cube based on the old business view behaves as follows:

* Before the next schedule time, the cube cannot retrieve data to reports.
* When it is the next schedule time, Server fetches data from the new business view to generate an updated cube:
  + If you added new parameters in the new business view, Server uses the default values until you specify new values to them.
  + If you deleted old parameters from the new business view, Server removes the parameter values previously specified in the cube.
  + If you changed the parameters and the previously specified values do not match the type, Server provides error messages in the server error log and disables the cube for service.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777101-Managing-Cached-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777321-Managing-Triggers)
