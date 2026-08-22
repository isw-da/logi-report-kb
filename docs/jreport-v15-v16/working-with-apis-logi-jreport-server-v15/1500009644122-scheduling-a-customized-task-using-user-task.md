---
title: "Scheduling a Customized Task Using User Task"
id: 1500009644122
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644122-Scheduling-a-Customized-Task-Using-User-Task
updated_at: 2021-07-24T20:55:27Z
---

# Scheduling a Customized Task Using User Task

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644142-Scheduling-a-Report-Task)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)

# Scheduling a Customized Task Using User Task

In order to provide the means to run tasks defined outside of Logi JReport on Logi JReport Server, and to just use Logi JReport Server's schedule function, Logi JReport provides a task named User Task. With this task, you can implement a customized task with the schedule properties. After creating a class that implements the UserTask interface in the jet.server.api package and adding the class to the class path, you can then submit the task either from a server web page or by calling Server API methods. The task can then be run by the server at the scheduled times just as if it were a report.

**To schedule a customized task using User Task:**

1. Create a task class that implements the UserTask interface and add the path of the class file to the ADDCLASSPATH variable in setenv.bat, which is located in `<install_root>\bin`. You can find the interface in the jet.server.api package available in `<install_root>\help\api`. Logi JReport provides a demo class APIDemoDynamicExportTask.java in `<install_root>\help\samples\APIServer` for your reference.
2. Create a task properties file defining the formats of exporting the task. For example, the content of the properties file is:

   `jrs.rst=result_rtf  
    jrs.pdf=true   
    jrs.text=true   
    jrs.excel=true   
    jrs.ps=true   
    jrs.html=result_html`
3. Submit the task either from a server web page or by calling Server API methods. The task can then be run by the server.
   * **To submit the customized task from a server web page:**
     1. On the Logi JReport Console > Resources page, browse to the desired report, put the mouse pointer over the report row and select the **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422295/btn_srv_schdl.gif) on the floating toolbar. The [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports) dialog is then displayed.
     2. Specify the settings in the General, Publish, Conditions, and Duration tabs as required. Here the Publish tab settings should be switched to those of User Task by selecting the link on the right bottom of the tab. Then, the name of the task class file you have defined that implements the UserTask interface and the task properties that define the export formats must be provided. You can either input the task properties manually or import them from the task properties file that you have created.
     3. Upon finishing, select **Finish** to submit the task.
   * **To submit the customized task by API methods:**
     1. Set the user task class name to the property value of APIConst.TAG\_TASK\_CLASS.
     2. Define the user task properties with the property APIConst.TAG\_USER\_TASK\_PROP with the formats as follows: jrs.user\_task\_prop= jrs.rst=result\_rtf&jrs.pdf=true&jrs.text=true&jrs.excel=true&jrs.ps=true&jrs.html=result\_html. Since the jrs.user\_task\_prop is used to transfer multiple user task properties, the values set to this property must be formatted to be separated with "&" character.
     3. Set a display name for the class with the property APIConst.TAG\_USER\_TASK\_DISPLAY\_NAME.
     4. Except for the above properties, define the other schedule properties as you do with a default task, see APIDemoPublishRpt.java in `<install_root>\help\samples\APIServer` for reference. Then following the API demo you can submit a customized task on the server.

Select **My Tasks** on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

**Note:** You can either schedule to use the Default Task or the User Task at one time. If you specify to schedule a report as a default task, you will not be able to schedule it as a user task, and vice versa.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644142-Scheduling-a-Report-Task)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)
