---
title: "Applying TaskListener"
id: 1500009718522
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718522-Applying-TaskListener
updated_at: 2022-05-04T11:05:57Z
---

# Applying TaskListener

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744481-Scheduling-a-Customized-Task-Using-User-Task)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744261-Writing-Customized-Load-Balancing-Algorithm)

# Applying TaskListener

When [running a report in Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009724222-Running-Reports#Advanced) or scheduling a task such as [report task](https://devnet.logianalytics.com/hc/en-us/articles/1500009751081-Scheduling-Reports), [data cache task](https://devnet.logianalytics.com/hc/en-us/articles/1500009750001-Managing-Cached-Report-Data#Schedule) and [in-memory cube task](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes#Create), Logi Report Server enables you to call your Java application before or after the report or task runs so as to get the information about the task.

The TaskListener interface is provided in the jet.server.api package in the Server API for receiving task events before or after the task running. The interface contains two methods: *beforeRun()* and *afterRun()*, which enable you to set your Java application call before or after the process of viewing a report or scheduling a task. You can specify one Java class to implement this interface for a task event, then when the event of this task occurs, the corresponding method in the listener will be invoked. Your application will return True or False. When True is returned, Logi Report Server will go on running; if False, Logi Report Server will stop there.

The example below shows how to add TaskListener when creating a schedule task on a report.

1. Develop your Java class to implement the TaskListener interface. Here TestTaskListener.java is used, which is available in  `<install_root>\help\samples\APITaskListener`.
2. Compile TestTaskListener.java to generate the class file.
3. Edit the batch file setenv.bat in `<install_root>\bin`. Assuming that TestTaskListener has been saved in `C:\LogiReport\Server\tasklistener`, add the path of the class file (`C:\LogiReport\Server\tasklistener`) to the ADDCLASSPATH variable in setenv.bat.
4. In the Logi Report Server console, create the schedule task on a report. In the General tab of the Schedule dialog box, select **Add TaskListerner to be Invoked** and type the class name. In this example, type **TastListener** and submit the task.
5. In the example, the class returns True. The task and schedule properties will be output to the command window before and after the task runs. You can get the task information in the command window.

You can also define properties of your own and transmit them through the serverInfo object by using APIConst.TAG\_USERDEFINED\_PROPERTY\_PREFIX as the prefix of the properties. Note that all properties without this prefix will be denied and discarded by Logi Report Server.

For example, if you want to transmit the properties host\_name, host\_ip and hosp\_protocol, you can insert them into the properties named prop before calling the method *runTask()* as follows:

```
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_name", "host");  
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_ip", "127.0.0.1");  
prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_protocol"+ "TCP/IP");
```

You can get the value of the properties listed above through the serverInfo object, in the method *beforeRun()* or *afterRun()* of the TaskListener interface. See the example below:

```
host_name=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_  
PROPERTY_PREFIX+"host_name");  
host_ip=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_  
PROPERTY_PREFIX+"host_ip");  
host_protocol=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_  
PROPERTY_PREFIX+"host_protocol");
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744481-Scheduling-a-Customized-Task-Using-User-Task)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744261-Writing-Customized-Load-Balancing-Algorithm)
