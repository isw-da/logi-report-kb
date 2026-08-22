---
title: "Scheduling a Customized Task Using User Task"
id: 1500009712181
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712181-Scheduling-a-Customized-Task-Using-User-Task
updated_at: 2021-11-03T06:58:32Z
---

# Scheduling a Customized Task Using User Task

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener)

# Scheduling a Customized Task Using User Task

In order to provide the means to run tasks defined outside of Logi JReport on Logi JReport Server, and to just use Logi JReport Server's [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009692482-Scheduling-Reports) function, Logi JReport Server provides a task named User Task. Using this task, you can implement a customized task with the schedule properties. After creating a class that implements the UserTask interface in the jet.server.api package and adding the class to the class path, you can then submit the task either from the server UI or by calling API methods. The task can then be run by Logi JReport Server at the scheduled times just as if it were a report.

**To schedule a customized task using User Task:**

1. Create a task class that implements the UserTask interface and add the path of the class file to the ADDCLASSPATH variable in setenv.bat, which is located in `<install_root>\bin`. The demo file APIDemoDynamicExportTask.java is provided in `<install_root>\help\samples\APIServer` for your reference.
2. Create a task property file, for example task.properties, to define the export formats of the task. The content of the file would be as follows:

   jrs.rst=result\_rtf  
   jrs.pdf=true   
   jrs.text=true   
   jrs.excel=true   
   jrs.ps=true   
   jrs.html=result\_html
3. Submit the task either from the server UI or by calling API methods. The task can then be run by Logi JReport Server.
   * **To submit the customized task via UI:**
     1. In the Resources page of the Logi JReport Server console, browse to the desired report, put the mouse pointer over the report row and select the **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4412139508887/btn_schdl.gif) on the floating toolbar.
     2. In the Schedule dialog, specify the settings in the General tab as required.
     3. In the Publish tab, select **User Task** on the right bottom to switch the settings to those for User Task. Then, provide the name of the task class file you have defined that implements the UserTask interface and the task properties that define the export formats. You can either input the task properties manually or import them from the task property file that you have created.
     4. Set the settings in the rest tabs respectively.
     5. Select **Finish** to submit the task.
   * **To submit the customized task by API methods:**
     1. Set the user task class name as value of the property APIConst.TAG\_TASK\_CLASS.
     2. Define the user task properties using the property APIConst.TAG\_USER\_TASK\_PROP as follows:

        `jrs.user_task_prop= jrs.rst=result_rtf&jrs.pdf=true&jrs.text=true&jrs.excel=true&jrs.ps=true&jrs.html=result_html`

        Since jrs.user\_task\_prop is used to transfer multiple user task properties, the values set to this property must be separated with the "&" character.
     3. Set a display name for the class with the property APIConst.TAG\_USER\_TASK\_DISPLAY\_NAME.
     4. Besides the above properties, define the other schedule properties as you do with a default task. See APIDemoPublishRpt.java in `<install_root>\help\samples\APIServer` for reference. Following the API demo you can submit a customized task on the server.

Select **My Tasks** on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

**Note:** You can either schedule to use the Default Task or the User Task at one time. If you specify to schedule a report as a default task, you will not be able to schedule it as a user task, and vice versa.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener)
