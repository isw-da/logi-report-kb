---
title: "Using the Server API"
id: 1500009686222
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686222-Using-the-Server-API
updated_at: 2021-11-03T06:58:36Z
---

# Using the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686182-Installing-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712061-Creating-and-Getting-Instances)

# Using the Server API

This topic shows how to use Logi JReport Server API to achieve specific goals.

The HTTP methods GET and POST are available for almost all of Logi JReport commands. The following is an example of using the POST method in Java program:

```
URL url = new URL("http://jrserver:8888");  
URLConnection uc = url.getConnection();  
if (uc instanceof HttpURLConnection) {  
  HttpURLConnection huc = (HttpURLConnection)uc;  
  //set use POST method.  
  huc.setRequestMethod("POST");  
  huc.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");  
  huc.setDoOutput(true);  
  
  //write the HTTP query to the output stream.  
  OutputStreamWriter writer = new OutputStreamWriter(huc.getOutputStream());  
  writer.write("jrs.cmd=jrs.get_subnodes");  
  writer.close();  
  huc.getHeaderField(0);  
  
  //get the response content from the server.  
  InputStream inStream = uc.getInputStream();  
  if (inStream != null) {  
    BufferedReader reader = new BufferedReader(new InputStreamReader(inStream));  
    String inputLine;  
    while (null != (inputLine = reader.readLine())) {  
      System.out.println(inputLine);  
    }  
  }  
}
```

When using the Server API to perform tasks on resources in the server resource tree, you need to specify the full path of the resources in the code. Below are the rules:

* If the resource is in the Public Reports folder in the server resource tree, the path should be started with "/". For example, for the /Public Report/SampleReports folder, the path is "/SampleReports".
* If the resource is in the My Reports folder in the server resource tree, the path should be started with "/USERFOLDERPATH/*username/*" (change *username* to the real user name with which you log onto Logi JReport Server). For example, suppose your server login user name is Jim and you want to access the /My Reports/Shipments folder, the path in the URL is "/USERFOLDERPATH/Jim/Shipments".

Below shows using the Server API to perform some specific tasks. For detailed usage about the Server API, you can refer to the Logi JReport Javadoc in `<install_root>\help\api`.

* [Creating and Getting Instances](https://devnet.logianalytics.com/hc/en-us/articles/1500009712061-Creating-and-Getting-Instances)
* [Using JSP with a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009686342-Using-JSP-with-a-Dedicated-Machine)
* [Using RMI in Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009712141-Using-RMI-in-Logi-Report-Server)
* [Working with Resource Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009686442-Working-with-Resource-Versions)
* [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009712161-Changing-the-Runtime-Database-Connection)
* [Scheduling a Report Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009686402-Scheduling-a-Report-Task)
* [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009712181-Scheduling-a-Customized-Task-Using-User-Task)
* [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener)
* [Writing Customized Load Balancing Algorithm](https://devnet.logianalytics.com/hc/en-us/articles/1500009686262-Writing-Customized-Load-Balancing-Algorithm)
* [Setting Server Reporthome and Properties in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
* [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009686362-Loading-User-Data-Source-Classes-at-Runtime)
* [Applying a User Defined CSS to an HTML Result File](https://devnet.logianalytics.com/hc/en-us/articles/1500009686282-Applying-a-User-Defined-CSS-to-an-HTML-Result-File)
* [Specifying Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009712121-Specifying-Parameter-Values)
* [Specifying Report Running Properties in the Session](https://devnet.logianalytics.com/hc/en-us/articles/1500009712221-Specifying-Report-Running-Properties-in-the-Session)
* [Tracing Server Resource Change Events](https://devnet.logianalytics.com/hc/en-us/articles/1500009686242-Tracing-Server-Resource-Change-Events)
* [Configuring the Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/1500009711981-Configuring-the-Security-Cache-System)
* [Customizing the Web Report Studio Toolbar](https://devnet.logianalytics.com/hc/en-us/articles/1500009686422-Customizing-the-Web-Report-Studio-Toolbar)
* [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009712201-Customized-Implementation-of-the-Security-API)
* [Advanced Running Reports Using the On-Demand API](https://devnet.logianalytics.com/hc/en-us/articles/1500009712101-Advanced-Running-Reports-Using-the-On-Demand-API)
* [Applying the Implementations of the Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/1500009712001-Applying-the-Implementations-of-the-Dashboard-Listener-API)
* [Using the NLS API](https://devnet.logianalytics.com/hc/en-us/articles/1500009686382-Using-NLS-API)
* [Dynamic Connection API](https://devnet.logianalytics.com/hc/en-us/articles/1500009686302-Dynamic-Connection-API)
* [Dynamic Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009686322-Dynamic-Security-API)
* [Information Bus API](https://devnet.logianalytics.com/hc/en-us/articles/1500009712041-Information-Bus-API)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686182-Installing-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712061-Creating-and-Getting-Instances)
