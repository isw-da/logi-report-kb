---
title: "Scheduling Cached Report Data Results"
id: 1500009673421
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results
updated_at: 2021-07-24T20:54:05Z
---

# Scheduling Cached Report Data Results

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673401-Creating-Cached-Report-Data-Automatically)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648662-Managing-Scheduled-CRD-Tasks)

# Scheduling Cached Report Data Results

Administrators can schedule to have a cached data result (scheduled CRD) created for a data resource and updated at a specific time or periodically. This is especially useful for month and quarter end reports where multiple reports use the same dataset with the same parameters such as begin and end date.

Scheduled CRD can be generated via Logi JReport's scheduling mechanism. In one scheduled CRD task, more than one data resource can be added, then a cached data result will be created for each data resource by applying the same creation and updating policy.

A data resource can have only one scheduled CRD. When a data resource contains parameters, its scheduled CRD can only represent the data of one parameter scenario.

**To create a schedule task to generate cached report data at specified time condition**:

1. On the Logi JReport Administration page, select **Cache** on the system toolbar and select **Data Cache** from the drop-down menu to open the Cache - Data Cache page.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920495383/mng_crd_pg.gif)
2. Select **New Cache** on the task bar. The [New Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009646542-New-Cache) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920495639/nwcache_query.gif)
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920370839/btn_chsr2.gif) next to the Select a Folder text field. In the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009671221-Select-Folder) dialog, browse to the folder containing the required catalog and select **OK**.
4. From the Select a Catalog drop-down list, select the required catalog in the specified folder.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) beside the Select Queries box. In the [Select Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009671241-Select-Queries) dialog, select the data resources for which you want to create data cache. Then select **OK**.

   To remove a data resource from the box, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).
6. Select **OK** to confirm the selection. The tabs for defining the schedule task are then displayed.
7. In the General tab,

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920495895/nwcache_gen.gif)

   1. From the Select Query drop-down list, select a data resource to specify the general properties of its scheduled CRD task.
   2. If the data resource uses parameters, you need to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values) in the Enter Parameters section.
   3. Expand the **Cached Report Data Info**  section, assign a priority to the task from the Priority drop-down list. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
   4. Expand the **Advanced** section to configure some advanced settings for the CRD.

      Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.

      Check the **Add TaskListener to be Invoked** option to call a Java application when scheduling the task (for details, see [Adding TaskListener When Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)).

      If you are in a [cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster) environment, you can also directly specify an active server in the cluster to perform the schedule task via the Specify a preferred server to run the task option.

      If you want to enable task recovery, check **Enable Auto Recover Task**, then specify the maximum number of times in which to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results.
   5. Select another data resource from the Select Query drop-down list and repeat the above steps to define the properties of its scheduled CRD. Do this for all the added data resources.
8. In the Conditions tab,
   specify the updating policy of the data cache. The condition will be applied to generate cached data for all the added data resources.
   1. In the Time sub tab, specify the time zone and the time for when the task is to be performed.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404920496151/nwcache_cndtn_time.gif)

      * To perform the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**, then define the time according to your requirement. Check **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
      * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time accordingly. Check **Run missed task upon server restart** so as to run the missed tasks when you restart the server.

      Next specify when the task will expire:

      * To make the task never expire, select **Never** from the Expires drop-down list.
      * To make the task expire at a specified time, select **At** from the Expires drop-down list, and then specify the date and time.
      * To make the task expire after a period of time, select **After** from the Expires drop-down list and then specify the time period.
   2. If you want to bind a [trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009648982-Managing-Triggers) to the task, switch to the **Trigger** sub tab.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404920496407/nwcache_cndtn_trgr.gif)

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
9. In the Notification tab, specify to notify someone via e-mail of when the task is finished successfully or when it fails, then in the mail box, enter the information of the receivers and the mail content. To send out mail notification, an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009669181-Configuring-the-E-Mail-Server) must have been predefined by the administrator.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926696215/nwcache_notif.gif)
10. Select **Finish** to submit the task. Logi JReport Server will then perform the task at the requested times to create cached data for all the specified data resources.

When a scheduled CRD is ready for use, all reports based on the same data resource as the CRD will automatically use the CRD for retrieving data. Since a scheduled CRD freezes parameters in the data resource, if a report uses a scheduled CRD and its data resource contains parameters, when running the report, only parameters used in the report are available for specifying values and the data resource parameters will be disabled for editing. In Logi JReport, a parameter may depend on another parameter; if the latter is frozen, the former will be frozen as well.

If the data resource used for creating a scheduled CRD is updated due to [catalog republishing](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources), the scheduled CRD will behave as follows:

* Before the next schedule time, the CRD will be disabled for retrieving data to reports.
* When it is the next schedule time, data is fetched from the new data resource to generate an updated scheduled CRD:
  + If new parameters are added in the new data resource, default values will be used until an administrator specifies values to them.
  + If old parameters are deleted from the new data resource, the parameter values previously specified in the CRD will be removed.
  + If parameters are changed and the previously specified values do not match the type, error messages will be given in the server error log and the CRD is disabled for use.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673401-Creating-Cached-Report-Data-Automatically)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648662-Managing-Scheduled-CRD-Tasks)
