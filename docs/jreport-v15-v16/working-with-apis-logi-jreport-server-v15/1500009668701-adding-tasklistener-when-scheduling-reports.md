---
title: "Adding TaskListener When Scheduling Reports"
id: 1500009668701
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports
updated_at: 2021-07-24T20:55:28Z
---

# Adding TaskListener When Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644122-Scheduling-a-Customized-Task-Using-User-Task)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643922-Writing-Customized-Load-Balancing-Algorithm)

# Adding TaskListener When Scheduling Reports

When [scheduling a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports), Logi JReport Server enables you to call your Java application before or after the process.

In Logi JReport Server, a TaskListener interface has been provided in the package jet.server.api for receiving task events before or after running. You can specify one Java class to implement this interface for a task event. When the event of this task occurs, the corresponding methods in the listener will be invoked. The interface contains two methods: beforeRun and afterRun, enabling you to set your Java application call before or after the process of viewing a report or setting up a schedule. Your applications will return true or false. For true, Logi JReport Server will go on running. While for false, Logi JReport Server will stop there.

Below is an example illustrating how to add TaskListener when setting up a schedule on a report.

1. Develop your Java class to implement the interface. Here TestTaskListener.java is used, which is available in  `<install_root>\help\samples\APITaskListener`.
2. Compile TestTaskListener.java to generate the class file.
3. Edit the batch file setenv.bat in `<install_root>\bin`. Assuming that TestTaskListener has been saved in `C:\Logi JReport\Server\tasklistener`, add the path of the class file (`C:\Logi JReport\Server\tasklistener`) to the ADDCLASSPATH variable in setenv.bat.
4. Start Logi JReport Server and set up a schedule on a report, check **Add TaskListerner to be Invoked** in the General tab of the Schedule dialog, then input the class name. In this example, input TastListener, and then submit the task.
5. In this example, the class returns True.

   Print out the task and schedule properties before and after running the task. You will then get task and schedule information in the command window before and after the task is run.

You can also define properties of your own and transmit them through ServerInfo. To do this, use APIConst.TAG\_USERDEFINED\_PROPERTY\_PREFIX as the prefix for the properties.

For example, if you want to transmit the properties host\_name, host\_ip and hosp\_protocol, you will need to insert the properties, before calling the method runTask, into the properties named prop, as follows:

|  |
| --- |
| ``` prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_name", "host");  prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_ip", "127.0.0.1"); prop.put(APIConst. TAG_USERDEFINED_PROPERTY_PREFIX+"host_protocol"+ "TCP/IP"); ``` |

You can get the value of the properties listed above through the server info object, serverInfo, in the method beforeRun or afterRun of the TaskListener class. See the example below:

|  |
| --- |
| ``` host_name=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_ PROPERTY_PREFIX+"host_name"); host_ip=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_ PROPERTY_PREFIX+"host_ip"); host_protocol=serverInfo.getTaskProperties().get(APIConst.TAG_USERDEFINED_ PROPERTY_PREFIX+"host_protocol"); ``` |

**Note:** All properties without the prefix APIConst.TAG\_USERDEFINED\_PROPERTY\_PREFIX will be denied and discarded by Logi JReport Server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644122-Scheduling-a-Customized-Task-Using-User-Task)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643922-Writing-Customized-Load-Balancing-Algorithm)
