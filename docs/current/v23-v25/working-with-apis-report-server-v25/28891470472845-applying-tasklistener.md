---
title: "Applying TaskListener"
id: 28891470472845
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891470472845-Applying-TaskListener
updated_at: 2026-02-26T02:11:07Z
source_host: docs-report.zendesk.com
---
# 
Applying TaskListener 

You can call your Java application before or after a report or task runs to get the information about the event, when running the report in Advanced mode or scheduling the report task, data cache task, or in-memory cube task. This topic describes the TaskListener interface and how you can add TaskListener when creating a scheduled task on a report.

Report provides the TaskListener interface in the jet.server.api package in the Server API for receiving the task event before or after a task runs. The interface contains two methods: beforeRun() and afterRun(), which enable you to set your Java application call before or after the process of viewing a report or scheduling a task. You can specify one Java class to implement this interface for a task event, then when the event of this task occurs, the corresponding method in the listener will be invoked. Your application will return True or False. When it returns True, Report Server will go on running; if False, Report Server will stop there.

The following example shows how to add TaskListener when creating a scheduled task on a report.

- Develop your Java class to implement the TaskListener interface. Here TestTaskListener.java is used, which is available in  <install_root>\help\samples\APITaskListener.

- Compile TestTaskListener.java to generate the class file.

- Edit the batch file setenv.bat in <install_root>\bin. Assuming that TestTaskListener has been saved in C:\LogiReport\Server\tasklistener, add the path of the class file (C:\LogiReport\Server\tasklistener) to the ADDCLASSPATH variable in setenv.bat.

- On the Server Console, create the schedule task on a report. In the General tab of the Schedule dialog box, select Add TaskListerner to be Invoked and type the class name. In this example, type TastListener and submit the task.

- In the example, the class returns True. The task and schedule properties will be output to the command window before and after the task runs. You can get the task information in the command window.

You can also define properties of your own and transmit them through the serverInfo object by using APIConst.TAG_USERDEFINED_PROPERTY_PREFIX as the prefix of the properties. 

Report Server denies and discards the properties without the prefix APIConst.TAG_USERDEFINED_PROPERTY_PREFIX.

For example, if you want to transmit the properties host_name, host_ip, and hosp_protocol, you can insert them into the properties named prop before calling the method runTask():

prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_name", "host");
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_ip", "127.0.0.1");
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_protocol"+ "TCP/IP");
You can get the value of the properties through the serverInfo object, in the method beforeRun() or afterRun()  of the TaskListener interface. See the example:

host_name=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_
PROPERTY_PREFIX+"host_name");
host_ip=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_
PROPERTY_PREFIX+"host_ip");
host_protocol=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_
PROPERTY_PREFIX+"host_protocol");
