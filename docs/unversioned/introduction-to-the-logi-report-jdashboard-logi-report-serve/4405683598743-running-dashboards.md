---
title: "Running Dashboards"
id: 4405683598743
section: "Introduction to the Logi Report JDashboard Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683598743-Running-Dashboards
updated_at: 2022-01-27T07:58:33Z
---

# Running Dashboards

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683603479-JDashboard-Window-Elements)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683594647-Creating-and-Saving-Dashboards)

# Running Dashboards

After [saving the dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4405683594647-Creating-and-Saving-Dashboards#Save) you create to the server resource tree, you can run them directly and further edit them in JDashboard. This topic describes how you can run a dashboard on the Server Console by selecting the dashboard name and using the Run and Edit options.

Logi Report provides several sample dashboards in the Public Reports > SampleReports folder in the server resource tree. However, to run dashboards in the public folders, you should have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions) on them.

You can run a dashboard in any of the following ways. Make sure to use the appropriate way because you cannot change the [working mode](https://devnet.logianalytics.com/hc/en-us/articles/4405683592471-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v18#Mode) of JDashboard after you open it and you have to re-run the dashboard using the right way if you need to access the other mode.

* **Selecting the dashboard name**  
   To use this way to run a dashboard in the Public Report folder, you need to have the **Execute** permission on the dashboard so that the dashboard name is shown with hyperlink when you move the cursor on the dashboard row. You can then select the dashboard name to run the dashboard in JDashboard in the mode specified by the [Default Mode for JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#JDashboardMode) option in the server profile. However, if the default mode is Edit Mode but you do not have the **Edit** permission on the dashboard, you will fail to run the dashboard and instead get an error message.
* **Using the Run option to access view mode of JDashboard**  
   To use this way to run a dashboard in the Public Report folder, you need to have the **Execute** permission on the dashboard so that Server displays the **Run** option.
  + Place the mouse pointer on the dashboard row and select the **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4420461539479/btn_srv_run.gif) on the floating toolbar.
  + Select the dashboard row, right-click in the row and select **Run** from the shortcut menu.
  + Select the dashboard row and select **Run** > **Run** on the task bar.

  You can also use the Run option to run multiple dashboards at a time. To do this, select the required dashboards and then select **Run** > **Run** on the task bar, or right-click in any dashboard row and select **Run** from the shortcut menu.
* **Using the Edit option to access edit mode of JDashboard**  
   To use this way to run a dashboard in the Public Report folder, you need to have the
  Execute and Edit permissions on the dashboard so that Server displays the Edit option.
  + Place the mouse pointer on the dashboard row and select the **Edit**  button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420453471767/btn_srv_edit.gif) on the floating toolbar.
  + Select the dashboard row, right-click in the row and select **Edit** from the shortcut menu.
  + Select the dashboard row and then select **Run** > **Edit**  on the task bar.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683603479-JDashboard-Window-Elements)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683594647-Creating-and-Saving-Dashboards)
