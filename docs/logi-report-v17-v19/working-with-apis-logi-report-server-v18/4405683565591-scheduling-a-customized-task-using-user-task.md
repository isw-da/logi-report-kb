---
title: "Scheduling a Customized Task Using User Task"
id: 4405683565591
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683565591-Scheduling-a-Customized-Task-Using-User-Task
updated_at: 2022-01-27T08:00:02Z
---

# Scheduling a Customized Task Using User Task

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683566615-Scheduling-a-Report-Task)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683559319-Applying-TaskListener)

# Scheduling a Customized Task Using User Task

Logi Report Server provides a task named User Task, to run tasks defined outside of Logi Report on Logi Report Server, and to just use Logi Report Server's [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/4405690676119-Scheduling-Reports) function. This topic describes how you can implement a customized task with the schedule properties using User Task.

**To schedule a customized task using User Task:**

1. Create a task class that implements the **UserTask** interface in the jet.server.api package.
2. Add the path of the class file to the ADDCLASSPATH variable in **setenv.bat**, which is in `<install_root>\bin`. You can refer to the demo file **APIDemoDynamicExportTask.java** in `<install_root>\help\samples\APIServer`.
3. Create a task property file, for example **task.properties**, to define the export formats of the task. The contents of the file would be:

   jrs.rst=result\_rtf  
   jrs.pdf=true   
   jrs.text=true   
   jrs.excel=true   
   jrs.ps=true   
   jrs.html=result\_html
4. Submit the task either from the server UI or by calling API methods. Logi Report Server can then run the task at the scheduled times just as if it were a report.
   * **To submit the customized task via UI:**
     1. In the Resources page of the Server Console, browse to the desired report, put the mouse pointer over the report row and select the **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4420447088151/btn_schdl.gif) on the floating toolbar.
     2. In the Schedule dialog box, specify the settings in the General tab as required.
     3. In the Publish tab, select **User Task** on the right bottom to switch the settings to those for User Task. Then, provide the name of the task class file you have defined that implements the UserTask interface and the task properties that define the export formats. You can either type the task properties manually or import them from the task property file that you have created.
     4. Set the settings in the rest tabs respectively.
     5. Select **Finish** to submit the task.
   * **To submit the customized task by API methods:**
     1. Set the user task class name as value of the property APIConst.TAG\_TASK\_CLASS.
     2. Define the user task properties using the property APIConst.TAG\_USER\_TASK\_PROP:

        `jrs.user_task_prop= jrs.rst=result_rtf&jrs.pdf=true&jrs.text=true&jrs.excel=true&jrs.ps=true&jrs.html=result_html`

        Since jrs.user\_task\_prop is used to transfer multiple user task properties, the values set to this property must be separated with the "&" character.
     3. Set a display name for the class with the property APIConst.TAG\_USER\_TASK\_DISPLAY\_NAME.
     4. Besides the preceding properties, define the other schedule properties as you do with a default task. See APIDemoPublishRpt.java in `<install_root>\help\samples\APIServer` for reference. Following the API demo you can submit a customized task on the server.

Select **My Tasks** on the system toolbar to see the status of the task. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) You can schedule to use either the Default Task or the User Task at one time. If you specify to schedule a report as a default task, you will not be able to schedule it as a user task, and vice versa.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683566615-Scheduling-a-Report-Task)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683559319-Applying-TaskListener)
