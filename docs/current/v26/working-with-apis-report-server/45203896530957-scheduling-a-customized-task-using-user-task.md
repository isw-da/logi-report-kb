---
title: "Scheduling a Customized Task Using User Task"
id: 45203896530957
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203896530957-Scheduling-a-Customized-Task-Using-User-Task
updated_at: 2026-04-30T14:07:51Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Scheduling a Customized Task Using User Task 

Report Server provides a task named User Task, to run tasks defined outside of Report on Report Server, and to just use Report Server's Schedule function. This topic describes how you can implement a customized task with the schedule properties using User Task.

To schedule a customized task using User Task:

- Create a task class that implements the UserTask interface in the jet.server.api package. 

- Add the path of the class file to the ADDCLASSPATH variable in setenv.bat, which is in <install_root>\bin. You can refer to the demo file APIDemoDynamicExportTask.java in <install_root>\help\samples\APIServer.

- Create a task property file, for example task.properties, to define the export formats of the task. The contents of the file would be:
                jrs.rst=result_rtf
jrs.pdf=true 
jrs.text=true 
jrs.excel=true 
jrs.ps=true 
jrs.html=result_html

- Submit the task either from the server UI or by calling API methods. Report  Server can then run the task at the scheduled times just as if it were a report.
                
- 
To submit the customized task via UI:
- In the Resources page of the Server Console, browse to the report you want, put the mouse pointer over the report row and select the Schedule button  on the floating toolbar.
				            

- In the Schedule dialog box, specify the settings in the General tab as you want.

- In the Publish tab, select User Task on the right bottom to switch the settings to those for User Task. Then, provide the name of the task class file you have defined that implements the UserTask interface and the task properties that define the export formats. You can either type the task properties manually or import them from the task property file that you have created.

- Set the settings in the rest tabs respectively.
                            

- Select Finish to submit the task.
				            

- 
To submit the customized task by API methods:
- Set the user task class name as value of the property APIConst.TAG_TASK_CLASS.
				            

- Define the user task properties using the property APIConst.TAG_USER_TASK_PROP:
				                jrs.user_task_prop= jrs.rst=result_rtf&jrs.pdf=true&jrs.text=true&jrs.excel=true&jrs.ps=true&jrs.html=result_html

Since jrs.user_task_prop is used to transfer multiple user task properties, the values set to this property must be separated with the "&" character.

- Set a display name for the class with the property APIConst.TAG_USER_TASK_DISPLAY_NAME.

- Besides the preceding properties, define the other schedule properties as you do with a default task. See APIDemoPublishRpt.java in <install_root>\help\samples\APIServer for reference. Following the API demo you can submit a customized task on the server.
				            

Select My Tasks on the system toolbar to see the status of the task. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

 You can schedule to use either the Default Task or the User Task at one time. If you specify to schedule a report as a default task, you will not be able to schedule it as a user task, and vice versa.
