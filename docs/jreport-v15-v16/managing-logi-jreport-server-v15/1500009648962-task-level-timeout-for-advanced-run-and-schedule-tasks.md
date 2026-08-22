---
title: "Task-level Timeout for Advanced Run and Schedule Tasks"
id: 1500009648962
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks
updated_at: 2021-07-24T20:54:02Z
---

# Task-level Timeout for Advanced Run and Schedule Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648942-Managing-Tasks-in-the-Task-Tables)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648722-Managing-Server-Data)

# Task-Level Timeout for Advanced Run and Schedule Tasks

A task-level timeout mechanism is introduced in order to avoid the never-finished running tasks consuming server resources and thus decreasing the server performance. With the mechanism, you can specify a time duration for a task, and ask Logi JReport Server to cancel the task or to notify you or someone else of the task status via e-mail if the task has not yet finished running when the task duration is up. To do this:

1. Do either of the following to enable the task-level timeout mechanism.
   * In the server.properties file located in `<install_root>\bin`, set the task.duration.enable property to **true**.
   * On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Advanced** from the drop-down menu. On the Configuration - Advanced page, check the **Enable Task Duration** option.
2. Set task duration check frequency. By default, Logi JReport Server checks task duration every 30 seconds. The period value can be reset by either of the following:
   * In the server.properties file, set the task.duration.check\_cycle property.
   * On the Configuration - Advanced page, set the Status Refresh Interval option.

   The period value must be an integer greater than 0. Since task duration check frequency affects server performance, it is recommended that you set the value according to your system environment.
3. Use the Duration tab in the Advanced Run or Schedule dialog to specify task duration.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920486935/advcdrn_drtn.gif)

   1. In the Timeout text box, specify the time limit for when the task can run before notifying of the timeout or canceling the task.
   2. If you want to notify someone of the task status if the task has not yet finished running when the task duration is up, check **Notify by e-mail after the specified time** and specify the mail address in the Mail To text box.
   3. If you want Logi JReport Server to cancel the task when the task duration is up but the task is not finished yet, check **Cancel the task after the specified time**.
4. Submit the task.

Then, when the specified task duration is up but the task has not finished running,

* **For an Advanced Run task**
  + If you have specified to have server cancel the task when the task duration is up, the task will be cancelled automatically, however a record for the task will be still remained in the Background Tasks table of the My Tasks page, shown with a sign of cancellation.
  + In the Duration tab, if you haven't checked the option Cancel the task after the specified time, the task will be switched to run in background mode when the task duration is up, in which case, you can choose to cancel the task manually. To do this, in the Background Tasks table,
    - Select the task row and select **Edit > Delete**  on the task bar of the My Tasks page.
    - Select the task row, right-click in the row and select **Delete** from the shortcut menu.
    - Put the mouse pointer over the task row and select the **Delete** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif) on the floating toolbar.
* **For a Schedule task**
  + If you have specified to have server cancel the task when the task duration is up, the task will be cancelled automatically, and a task completed record will be added in the Completed table of the My Tasks page, with the Is Successful status shown as No.
  + In the Duration tab, if you haven't checked the option Cancel the task after the specified time, the task will still be listed in the Running table of the My Tasks page when the task duration is up. Then, if you want to cancel the task manually, in the Running table,
    - Select the task row and select **Stop** on the task bar of the My Tasks page.
    - Select the task row, right-click in the task row and select **Stop** from the shortcut menu.
    - Put the mouse pointer over the task row and select the **Stop** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926692759/btn_srv_stop.gif) on the floating toolbar.

**Notes:**

* Logi JReport Server may not cancel a task right after the specified task duration is up due to check frequency.
* It is recommended that the task duration is set to about five times of the required time for finishing running the task.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648942-Managing-Tasks-in-the-Task-Tables)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648722-Managing-Server-Data)
