---
title: "Creating In-memory Cubes"
id: 1500009673441
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes
updated_at: 2021-07-24T20:54:06Z
---

# Creating In-memory Cubes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648682-Managing-In-memory-Cubes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks)

# Creating In-Memory Cubes

A business view can have only one in-memory cube. When a business view contains parameters, its in-memory cube can only represent the data of one parameter scenario.

Using Logi JReport's scheduling mechanism, administrators are able to define when an in-memory cube for a business view will be created and when it will be updated at a specific time or periodically. This is especially useful for month and quarter end reports where multiple reports use the same dataset with the same parameters such as begin and end date.

In-memory cubes have no versions: once they are updated, only the latest one is kept for the business view.

If it is the first time to create in-memory cubes, the administrator needs to first configure the maximum memory allowed for all in-memory cubes.

1. On the Logi JReport Administration page, select **Cube** on the system toolbar.
2. In the Cube page, select **Configuration** on the task bar. This option is not available to [organization admins](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations).
3. In the Maximum Cube Memory Allowed text field, specify the allowed maximum cube memory size in megabytes. The total allocated memory for each cube cannot exceed this value. It does not take into consideration the actual memory used by the in-memory or if some of the cubes are swapped to disk. This value should not be larger than 80% of your Java Heap size.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926695063/mng_cube_crt.gif)
4. Select **OK** to confirm the setting.

**To create an in-memory cube:**

1. On the Logi JReport Administration page, select **Cube** on the system toolbar.
2. In the Cube panel, select **New Cube** on the task bar. The [New Cube](https://devnet.logianalytics.com/hc/en-us/articles/1500009670841-New-Cube) dialog appears[.](https://devnet.logianalytics.com/hc/en-us/articles/1500009670841-New-Cube) 

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920493207/nwcube_bv.gif)
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920370839/btn_chsr2.gif) next to the Select a Folder text field. In the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009671221-Select-Folder) dialog, browse to the folder containing the required catalog and select **OK**.
4. From the Select a Catalog drop-down list, select the required catalog in the specified folder.
5. In the Select Business View box, select the business view on which to create the in-memory cube.
   The business view name will be used as the name of the in-memory cube.
6. Select **OK** to confirm the selection. The tabs for defining the schedule task information are then displayed.
7. In the General tab,

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920493847/nwcube_gen.gif)

   1. [Specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values) if the business view uses parameters.
   2. Expand the **Cube Information**  section, assign a priority to the task from the Priority drop-down list. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
   3. Expand the **Advanced** section to configure some advanced settings.

      Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.

      Check the **Add TaskListener to be Invoked** option to call a Java application when scheduling the task (for details, see [Adding TaskListener When Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)).

      If you are in a [cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster) environment, you can also directly specify an active server in the cluster to perform the schedule task via the Specify a preferred server to run the task option.

      If you want to enable task recovery, check **Enable Auto Recover Task**, then specify the maximum number of times in which to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results.
8. In the Schedule tab, specify the updating policy of the in-memory cube.
   1. In the Time sub tab, specify the time zone and the time for when the task is to be performed.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404920494359/nwcube_schdl_time.gif)

      * To perform the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**, then define the time according to your requirement. Check **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
      * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time accordingly. Check **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
   2. If you want to bind a [trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009648982-Managing-Triggers) to the task, switch to the **Trigger** sub tab.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404920494615/nwcube_schdl_trgr.gif)

      From the Select a trigger to bind drop-down list, select the required trigger or select the **Create New** button to create a new trigger (the button is not available to [organization admins](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations)), then specify the trigger logic with time condition.

      * **Trigger Only**  
         Performs the task only when the trigger is fired.
      * **Trigger and Time Condition**   
         Performs the task when both time is up and the trigger is fired.

        **Note:** When this logic is selected:

        + No matter which condition is ready, the task can only be performed when its counterpart is ready.
        + If you specify the task to be performed at a specific time, you must check the option Run missed task upon server restart, otherwise the task will be regarded as expired and will be deleted when the time condition is ready before the trigger condition.
      * **Time Condition after Trigger**   
         Performs a task when time is up after the trigger is fired. If the time condition is ready before the trigger condition, the task will be regarded as expired and will be deleted.
      * **Time Condition or Trigger**  
         Performs the task when either time is up or the trigger is fired.
9. In the Settings tab,

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920494871/nwcube_set.gif)

   1. In the Maximum Memory Allowed text box, provide a value for the cube. The value must be specified, otherwise you are not allowed to continue with other tabs or to finish the dialog.
   2. If you would like to cache the cube on disk once the available memory is exhausted, select **Move the cube to disk if insufficient memory is allocated**. If this option is not selected and the memory is not enough for the cube, the cube status will be disabled and an error will be shown in the log tab.
   3. If you would like the detail data in the business view to be cached onto disk, select **Cache Detail on Disk**. Otherwise if you need only the aggregation data to be cached, unselect the option.
10. In the Notification tab, specify to notify someone via e-mail of when the task is finished successfully or when it fails, then in the mail box, enter the information of the receivers and the mail content. To send out mail notification, an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009669181-Configuring-the-E-Mail-Server) must have been predefined by the administrator.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404926695703/nwcube_notif.gif)
11. Select **Finish**, and Logi JReport Server will then perform the task at the requested times.

After an in-memory cube is created and [ready for use](https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks#Status), all web reports, library components and visual analyses based on the same business view as the cube will automatically use the cube for retrieving data.

Since an in-memory cube freezes parameters in its related business view, if a report uses an in-memory cube and its business view contains parameters, when running the report, only parameters used in the report are available for specifying values and the business view parameters will be disabled for editing. In Logi JReport, a parameter may depend on another parameter; if the latter is frozen, the former will be frozen as well.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648682-Managing-In-memory-Cubes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks)
