---
title: "Retrieve Schedule Task Properties from SystemDB with Server API"
id: 360051752953
section: "Samples"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360051752953-Retrieve-Schedule-Task-Properties-from-SystemDB-with-Server-API
updated_at: 2020-07-28T13:35:31Z
---

# Retrieve Schedule Task Properties from SystemDB with Server API

### Problem

Logi Report Server stores all the scheduled task information in the table named **JR\_QRTZ\_2\_JOB\_DETAILS** in the SystemDB running behind it. Each schedule task includes a lot of properties, and the way it was being stored in the **JR\_QRTZ\_2\_JOB\_DETAILS** table is that all the properties are stored in a BLOB type column named **JOB\_DATA**.  This schema makes it difficult to read the task properties individually.

### Solution

A lot of customers are trying to get the schedule task properties after it was being submitted to Logi Report Server for various purposes. So we made this sample code to show you how can you use Server API to read the information from the **JR\_QRTZ\_2\_JOB\_DETAILS** table directly.

```
try{  
 Class.forName("org.apache.derby.jdbc.ClientDriver");  
 Connection connection = DriverManager.getConnection("jdbc:derby://localhost:8886/realmtable.defaultRealm", "APP", "APP");   
 PreparedStatement pst = connection.prepareStatement("select JOB_NAME,JOB_DATA from JR_QRTZ_2_JOB_DETAILS");  
 ResultSet rs = pst.executeQuery();
```

The code above establishes the JDBC connection to your SystemDB and queries the **JR\_QRTZ\_2\_JOB\_DETAILS** table. Here we use Derby database as the example. If you already switched SystemDB to your own database server, then you will need to put in your own database information here.

```
while(rs.next()){  
 String taskID = rs.getString("JOB_NAME");  
 taskID = taskID.substring(taskID.lastIndexOf("_")+1);  
 Timestamp ts = Timestamp.valueOf(taskID); //task ID is the submitted time of the scheduled task  
   
 Blob b_from = (Blob) rs.getBlob("JOB_DATA");  
 ObjectInputStream in = new ObjectInputStream(b_from.getBinaryStream());  
 Map<?, ?> map = (Map<?, ?>)in.readObject();  
 if(ts.after(Timestamp.valueOf(startTime)) && ts.before(Timestamp.valueOf(endTime))) {  
 pw.println("The parameters of Task ID:<" + map.get(APIConst.TAG_TASK_ID) + "> and Schedule Name:<" + map.get(APIConst.TAG_SCHEDULE_NAME) + ">");  
 map.forEach((k,v)->pw.println(k + "=" + (v.getClass().isArray() ? Arrays.toString((Object[]) v) : v)));  
 pw.println("------------------------------------------------------------------Separate Line------------------------------------------------------------------\n");  
 }
```

Here it starts to read the information from the BLOB type column **JOB\_DATA**and prints out each property in a single line.

To compile and run this sample code, you will need to include the following jar files from Logi Report Server as well as the JDBC driver jar file to connect to your SystemDB:

```
%installroot_LogiReportServer%\lib\JRESServlets.jar  
%installroot_LogiReportServer%\lib\quartz-2.3.2.jar
```

The output of the task properties will look identical to the **taskProperties.txt** file attachment. You can find the explanation of each property by checking the **APIConst** class in Logi Report Server JavaDoc located at <https://www.jinfonet.com/kbase/v17/api/jet/cs/util/APIConst.html> .
