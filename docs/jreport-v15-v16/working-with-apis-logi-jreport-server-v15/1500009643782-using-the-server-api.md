---
title: "Using the Server API"
id: 1500009643782
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009643782-Using-the-Server-API
updated_at: 2021-07-24T20:55:31Z
---

# Using the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009643642-Installing-the-Server-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644042-Creating-and-Getting-Instances-of-ReportEngine)

# Using the Server API

This topic shows how to use Logi JReport Server API to achieve specific goals.

The HTTP methods GET and POST are available for almost all of Logi JReport commands. The following is an example of using the POST method in Java program:

|  |
| --- |
| ``` URL url = new URL("http://jrserver:8888"); URLConnection uc = url.getConnection(); if (uc instanceof HttpURLConnection) {   HttpURLConnection huc = (HttpURLConnection)uc;    //set use POST method.   huc.setRequestMethod("POST");   huc.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");   huc.setDoOutput(true);     //write the HTTP query to the output stream.   OutputStreamWriter writer = new OutputStreamWriter(huc.getOutputStream());   writer.write("jrs.cmd=jrs.get_subnodes");   writer.close();   huc.getHeaderField(0);     //get the response content from the server.   InputStream inStream = uc.getInputStream();   if (inStream != null) {     BufferedReader reader = new BufferedReader(new InputStreamReader(inStream));     String inputLine;     while (null != (inputLine = reader.readLine())) {       System.out.println(inputLine);     }   } } ``` |

Pick a task from below:

* [Creating and Getting Instances of ReportEngine](https://devnet.logianalytics.com/hc/en-us/articles/1500009644042-Creating-and-Getting-Instances-of-ReportEngine)
* [Creating and Getting Instances of RptServer or HttpRptServer](https://devnet.logianalytics.com/hc/en-us/articles/1500009668801-Creating-and-Getting-Instances-of-RptServer-or-HttpRptServer)
* [Using JSP With a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009644062-Using-JSP-With-a-Dedicated-Machine)
* [Using RMI in Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009668761-Using-RMI-in-Logi-JReport-Server-Guide-v15-Server)
* [Working With Resource Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009668841-Working-With-Resource-Versions)
* [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009644102-Changing-the-Runtime-Database-Connection)
* [Scheduling a Report Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009644142-Scheduling-a-Report-Task)
* [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009644122-Scheduling-a-Customized-Task-Using-User-Task)
* [Adding TaskListener When Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)
* [Writing Customized Load Balancing Algorithm](https://devnet.logianalytics.com/hc/en-us/articles/1500009643922-Writing-Customized-Load-Balancing-Algorithm)
* [Setting Server Reporthome and Properties in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009668641-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
* [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009668681-Loading-User-Data-Source-Classes-at-Runtime)
* [Applying a User-Defined CSS to HTML Result File](https://devnet.logianalytics.com/hc/en-us/articles/1500009643962-Applying-a-User-Defined-CSS-to-HTML-Result-File)
* [Specifying Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009668741-Specifying-Parameter-Values)
* [Specifying Report Running Properties in the Session](https://devnet.logianalytics.com/hc/en-us/articles/1500009668821-Specifying-Report-Running-Properties-in-the-Session)
* [Tracing Server Resource Change Events](https://devnet.logianalytics.com/hc/en-us/articles/1500009668481-Tracing-Server-Resource-Change-Events)
* [Configuring the Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System)
* [Customizing the Web Report Studio Toolbar](https://devnet.logianalytics.com/hc/en-us/articles/1500009644162-Customizing-the-Web-Report-Studio-Toolbar)
* [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668781-Customized-Implementation-of-the-Security-API)
* [Specifying Paths for the Result Files When Using On-Demand API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668721-Specifying-Paths-for-the-Result-Files-When-Using-On-Demand-API)
* [Applying the Implementations of the Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/1500009644002-Applying-the-Implementations-of-the-Dashboard-Listener-API)
* [Using the NLS API](https://devnet.logianalytics.com/hc/en-us/articles/1500009644082-Using-NLS-API)
* [Dynamic Connection API](https://devnet.logianalytics.com/hc/en-us/articles/1500009644022-Dynamic-Connection-API)
* [Dynamic Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668621-Dynamic-Security-API)
* [Information Bus API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668661-Information-Bus-API)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009643642-Installing-the-Server-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644042-Creating-and-Getting-Instances-of-ReportEngine)
