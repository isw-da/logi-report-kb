---
title: "Viewing and Managing the Cube Tasks"
id: 1500009648702
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks
updated_at: 2021-07-24T20:54:06Z
---

# Viewing and Managing the Cube Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673461-Recovering-and-Synchronizing-In-memory-Cubes)

# Viewing and Managing the Cube Tasks

You can view information of the tasks scheduled for creating in-memory cubes and manage the tasks in the [Schedule](#Schedule), [Active](#Active), and [Log](#Log) tables on the Logi JReport Administration > Cube page.

Some columns are not shown by default in the tables. To have them displayed, focus on the required table, select **Preferences** on the toolbar, check the corresponding items in the Preferences dialog, and then select **OK** to apply the settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Schedule Table

All scheduled cube tasks are listed in the Schedule table. You can edit any of the tasks in the table in the following ways:

* To further edit the scheduling information of a task, select the row in which the task is located, then select **Edit > Properties** on the task bar, or the **Properties** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926692119/btn_srv_prpty.gif) on the floating toolbar, or right-click on the row and select Properties on the shortcut menu. In the displayed dialog, edit the scheduling information. If parameters or schedule policy is changed, they will only take effect after the next cube update; before that, all reports using the cube will still get the old data.
* To disable a task that is not disabled, select the row where the cube task is, then select **Edit > Disable**  on the task bar, or the **Disable**button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926693143/btn_srv_disable.gif) on the floating toolbar, or right-click on the row and select **Disable** on the shortcut menu.
* To enable a task that is disabled, select the row where the cube task is, then select **Edit > Enable**  on the task bar, or the **Enable**button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920487831/btn_srv_enable.gif) on the floating toolbar, or right-click on the row and select **Enable** on the shortcut menu.
* To remove a task that is no longer required, select the row where the cube task is, then select **Edit > Delete** on the task bar, or the **Delete**button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif) on the floating toolbar, or right-click on the row and select **Delete** on the shortcut menu.

The following lists the columns in the table:

| Column | Description |
| --- | --- |
| Name | The name of the cube task. |
| Catalog | The catalog that the cube belongs to. |
| Data Source | The data source that the cube belongs to. |
| Status | The task status:  * **Pending**  The cube has no data and is waiting to run based on schedule policy.   The cube is not ready for use. * **Building**  It is the first time creating the cube and filling data to the cube. The cube is not ready for use. * **Updating**  It is updating cube data based on the schedule policy. The cube is not ready for use. * **Completed**  Cube data is available. The task will not be updated any more according to the schedule policy. * **Disabled**  The cube is not allowed to generate or update following the schedule policy. The cube data cannot be used or released. |
| Create Time | The time when the scheduled task was created. |
| Next Run Time | The next time when the scheduled task will generate or update the cube. |
| Last Run Time | The last time when the scheduled task generated or updated the cube. |
| Times Run | The number of times the scheduled task has generated or updated the cube. If the number is bigger than 0, select it and you will be able to view the details of each running of the cube, including all updating events since the cube was generated. The detail table contains the following columns:   | Column | Description | | --- | --- | | Activity | Shows the type of the event.  * **Build**  Indicates that the cube was created. * **Update**  Indicates that the cube was updated. | | Start Time | Shows the time when the event started. | | End Time | Shows the time when the event ended. | | Status | Shows whether the event is successful.  * **Successful**  Indicates that the event is successful. * **Failed**  Indicates that the event failed. | |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Active Table

All the cube tasks that have generated in-memory cubes which have data and are ready for use are listed in the Active table. You can edit the tasks here [in the same way as you do in the Schedule table](#Schedule).

The following lists the columns in the table:

| Column | Description |
| --- | --- |
| Name | The name of the cube task. |
| Catalog | The catalog that the cube belongs to. |
| Data Source | The data source that the cube belongs to. |
| Updated Time | The last time when the cube was updated. |
| Allocated | The maximum memory allowed for the cube. |
| Actual | The memory size currently used by the cube. |
| Located At | Shows the location of the cube:  * **On Disk**   Indicates that the cube is swapped to the disk. * **In Memory**   Indicates that the cube is in the memory. |
| Parameter | Displays a parameter icon. By selecting the icon a dialog will appear to show all the parameters used in the cube. |
| Usage | The number of reports and library components that have accessed the cube. If the number is bigger than 0, select it and you will get a detail table showing the information of all the web reports and library components that used data from the cube. The detail table contains the following columns:   | Column | Description | | --- | --- | | Name | The name of the web report or the library component that used the cube. | | Type | Indicates whether it is a web report or a library component. | | Dashboard | The name of the dashboard that is using the library component. For library components only. | | User | The user who ran the web report or the library component. | | Description | The description about the web report or the library component. | |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Log Tab

All the events happened on all the cube tasks are recorded in the Log table. You can delete any of the log records from the table if you want. To do this, select a record row and then select **Edit > Delete** on the task bar, or the **Delete**button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif) on the floating toolbar, or right-click on the record row and select **Delete** on the shortcut menu.

The following lists the columns in the table:

| Column | Description |
| --- | --- |
| Name | The name of the cube task. |
| Catalog | The catalog that the cube belongs to. |
| Data Source | The data source that the cube belongs to. |
| Activities | The type of the event:  * **Create**  The cube was created. * **Edit**  The cube was edited. * **Initiate**  The cube data was initiated and made usable. * **Update**  The cube data was updated. * **Disable**  The cube was disabled. * **Enable**  The cube was enabled. * **Delete**  The cube was deleted. |
| Start Time | The time when the event started. |
| End Time | The time when the event ended. |
| Status | The event status:  * **Successful**  The event was successful. * **Failed**  The event failed. |
| Message | Messages for failed events. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673461-Recovering-and-Synchronizing-In-memory-Cubes)
