---
title: "Applying TaskListener"
id: 5741395089175
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741395089175-Applying-TaskListener
updated_at: 2022-10-31T17:15:50Z
---

# Applying TaskListener

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400624023-Scheduling-a-Customized-Task-Using-User-Task)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386314391-Writing-Customized-Load-Balancing-Algorithm)

# Applying TaskListener

You can call your Java application before or after a report or task runs to get the information about the event, when [running the report in Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports#Advanced) or scheduling the [report task](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports), [data cache task](https://devnet.logianalytics.com/hc/en-us/articles/5741453292183-Managing-Cached-Report-Data#Schedule), or [in-memory cube task](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes#Create). This topic describes the TaskListener interface and how you can add TaskListener when creating a scheduled task on a report.

Logi Report provides the **TaskListener** interface in the **jet.server.api** package in the Server API for receiving the task event before or after a task runs. The interface contains two methods: *beforeRun()* and *afterRun()*, which enable you to set your Java application call before or after the process of viewing a report or scheduling a task. You can specify one Java class to implement this interface for a task event, then when the event of this task occurs, the corresponding method in the listener will be invoked. Your application will return True or False. When it returns True, Logi Report Server will go on running; if False, Logi Report Server will stop there.

The following example shows how to add TaskListener when creating a scheduled task on a report.

1. Develop your Java class to implement the TaskListener interface. Here TestTaskListener.java is used, which is available in  `<install_root>\help\samples\APITaskListener`.
2. Compile TestTaskListener.java to generate the class file.
3. Edit the batch file setenv.bat in `<install_root>\bin`. Assuming that TestTaskListener has been saved in `C:\LogiReport\Server\tasklistener`, add the path of the class file (`C:\LogiReport\Server\tasklistener`) to the ADDCLASSPATH variable in setenv.bat.
4. On the Server Console, create the schedule task on a report. In the General tab of the Schedule dialog box, select **Add TaskListerner to be Invoked** and type the class name. In this example, type **TastListener** and submit the task.
5. In the example, the class returns True. The task and schedule properties will be output to the command window before and after the task runs. You can get the task information in the command window.

You can also define properties of your own and transmit them through the serverInfo object by using **APIConst.TAG\_USERDEFINED\_PROPERTY\_PREFIX** as the prefix of the properties.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)![](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)Logi Report Server denies and discards the properties without the prefix **APIConst.TAG\_USERDEFINED\_PROPERTY\_PREFIX**.

For example, if you want to transmit the properties host\_name, host\_ip, and hosp\_protocol, you can insert them into the properties named **prop** before calling the method *runTask()*:

```
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_name", "host");  
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_ip", "127.0.0.1");  
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_protocol"+ "TCP/IP");
```

You can get the value of the properties through the **serverInfo** object, in the method *beforeRun()* or *afterRun()* of the **TaskListener** interface. See the example:

```
host_name=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_  
PROPERTY_PREFIX+"host_name");  
host_ip=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_  
PROPERTY_PREFIX+"host_ip");  
host_protocol=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_  
PROPERTY_PREFIX+"host_protocol");
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400624023-Scheduling-a-Customized-Task-Using-User-Task)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386314391-Writing-Customized-Load-Balancing-Algorithm)
