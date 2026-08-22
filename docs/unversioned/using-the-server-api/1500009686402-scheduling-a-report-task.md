---
title: "Scheduling a Report Task"
id: 1500009686402
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task
updated_at: 2021-11-03T06:58:31Z
---

# Scheduling a Report Task

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712161-Changing-the-Runtime-Database-Connection)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712181-Scheduling-a-Customized-Task-Using-User-Task)

# Scheduling a Report Task

This topic introduces how to schedule a report task in your program using time condition and trigger. The properties for scheduling reports are available in the jet.cs.util.APIConst class in the Logi JReport Server Javadoc which is located in `<install_root>\help\api`.

Below is a list of the sections covered in this topic:

* [Scheduling a Report Task Using Time Condition](#Time)
* [Scheduling a Report Task Using Trigger](#Trigger)

## Scheduling a Report Task Using Time Condition

The following introduces how to schedule a report task in your program using time condition. You can also refer to the API sample APIDemoPublishRpt.java in `<install_root>\help\samples\APIServer` for additional information.

1. Connect to Logi JReport Server as follows:

   `RptServer server = null;  
   server = HttpUtil.getHttpRptServer();`
2. Set the schedule task properties.

   The following example publishes the report Employee Information List.cls in the Public Reports > SampleReports folder to disk in the PDF format.

   ```
   // Set task properties  

   Properties props = new Properties();  

   props.put(APIConst.TAG_TASK_CLASS, APIConst.TASK_TO_RPT);  

   props.put(APIConst.TAG_LAUNCH_TYPE, String.valueOf(APIConst.IMMEDIATELY));  

   props.put(APIConst.TAG_CATALOG, "/SampleReports/SampleReports.cat");  

   props.put(APIConst.TAG_REPORT, "Employee Information List.cls");  

   props.put(APIConst.TAG_TO_DISK, "true");  
     
   							
   // TO Disk   

   // Set the value of PDF for TO_DISK  

   props.put(APIConst.TAG_TO_PDF, "true");  

   props.put(APIConst.TAG_PDF, "Employee Information List.cls.pdf");  

   props.put(APIConst.TAG_REPORT_LANGUAGE, "en_US");  

   String today = DateFormat.getDateInstance(DateFormat.LONG, new Locale("en", "US")).format(new Date());  

   props.put(APIConst.TAG_PDF_DIR, "/SampleReports");
   ```
3. Submit and trigger the task as follows:

   `String taskID = server.submitScheduledTask("admin", props);`
4. Get the task result:

   `CompletedTaskTable completeTable = server.getCompletedTaskTable();`
5. Shut down the server:

   `server.shutdown();`

## Scheduling a Report Task Using Trigger

The following introduces how to schedule a report task using trigger in your program. You can also refer to the API sample DemoTrigger.java in `<install_root>\help\samples\APIServer` for additional information.

1. Connect to Logi JReport Server as follows:

   ```
   // get instance of RptServer  

   RptServer svr = RemoteReportServerToolkit.getRemoteWrappedRptServer("127.0.0.1", "1129");  

   TriggerManager trigMan = svr.getTriggerManager();  

   String exTriggerName = "exTriggerDemo";  

   if (!trigMan.contains(exTriggerName)) {  

   trigMan.createTrigger(exTriggerName, "an external trigger demo");  

   }
   ```
2. Set the schedule task properties.

   The following example publishes the report Payroll Report.cls in the Public Reports > SampleReports folder to the versioning system in the PDF format.

   ```
   Properties props = new Properties();  

   props.put(APIConst.TAG_TASK_CLASS, APIConst.TASK_TO_RPT);  

   props.put(APIConst.TAG_LAUNCH_TYPE, String.valueOf(APIConst.IMMEDIATELY));  

   props.put(APIConst.TAG_TRIGGERS_LOGIC, "ONLY");  

   props.put(APIConst.TAG_TRIGGERS_ARRAY, "exTriggerDemo");  

   props.put(APIConst.TAG_CATALOG, "/SampleReports/SampleReports.cat");  

   props.put(APIConst.TAG_REPORT, "/SampleReports/Payroll Report.cls");  

   props.put(APIConst.TAG_TO_VERSION, "true");  

   props.put(APIConst.TAG_TO_VERSION_PDF, "true");
   ```
3. Submit the task as follows:

   `taskID = svr.submitScheduledTask("admin", props);`
4. Trigger the task as follows:

   `Properties userData = new Properties();  
   trigMan.fire(exTriggerName, userData);`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712161-Changing-the-Runtime-Database-Connection)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712181-Scheduling-a-Customized-Task-Using-User-Task)
