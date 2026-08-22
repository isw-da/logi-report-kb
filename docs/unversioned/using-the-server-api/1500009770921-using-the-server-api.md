---
title: "Using the Server API"
id: 1500009770921
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770921-Using-the-Server-API
updated_at: 2021-07-24T00:49:37Z
---

# Using the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743082-Installing-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771101-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)

# Using the Server API

You can use Logi Report Server API to achieve specific goals. This topic describes the HTTP methods GET and POST and how to specify the full paths of the server resources in the code.

The HTTP methods GET and POST are available for almost all of Logi Report commands. The following is an example of using the POST method in Java program:

```
URL url = new URL("http://jrserver:8888");  
URLConnection uc = url.getConnection();  
if (uc instanceof HttpURLConnection) {  
  HttpURLConnection huc = (HttpURLConnection)uc;  
  //set use POST method.  
  huc.setRequestMethod("POST");  
  huc.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");  
  huc.setDoOutput(true);  
  
  //Write the HTTP query to the output stream.  
  OutputStreamWriter writer = new OutputStreamWriter(huc.getOutputStream());  
  writer.write("jrs.cmd=jrs.get_subnodes");  
  writer.close();  
  huc.getHeaderField(0);  
  
  //Get the response content from the server.  
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

When using the Server API to perform tasks on resources in the server resource tree, you need to specify the full path of the resources in the code. The rules are as follows:

* If the resource is in the Public Reports folder in the server resource tree, the path should be started with "/". For example, for the /Public Report/SampleReports folder, the path is "/SampleReports".
* If the resource is in the My Reports folder in the server resource tree, the path should be started with "/USERFOLDERPATH/*username/*" (change *username* to the real user name with which you log onto Logi Report Server). For example, suppose your server login user name is Jim and you want to access the /My Reports/Shipments folder, the path in the URL is "/USERFOLDERPATH/Jim/Shipments".

The list below provides you with links on how to perform specific tasks using the Server API. Select the links to view the topics. For more information, see the Logi Report Javadoc.

* [Creating and Getting Instances of Report Engine and Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009771101-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)
* [Using JSP with a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009743202-Using-JSP-with-a-Dedicated-Machine)
* [Using RMI in Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009771201-Using-RMI-in-Logi-Report-Server)
* [Publishing Resources from One Server to Another](https://devnet.logianalytics.com/hc/en-us/articles/1500009743242-Publishing-Resources-from-One-Server-to-Another)
* [Working with Resource Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009743342-Working-with-Resource-Versions)
* [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009743262-Changing-the-Runtime-Database-Connection)
* [Scheduling a Report Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009743302-Scheduling-a-Report-Task)
* [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/1500009743282-Scheduling-a-Customized-Task-Using-User-Task)
* [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009771141-Applying-TaskListener)
* [Writing Customized Load Balancing Algorithm](https://devnet.logianalytics.com/hc/en-us/articles/1500009770981-Writing-Customized-Load-Balancing-Algorithm)
* [Setting Server Reporthome and Properties in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009771061-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
* [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009771121-Loading-User-Data-Source-Classes-at-Runtime)
* [Passing Customized Variables to User Data Source at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009743162-Passing-Customized-Variables-to-User-Data-Source-at-Runtime)
* [Applying a User Defined CSS to an HTML Result File](https://devnet.logianalytics.com/hc/en-us/articles/1500009771001-Applying-a-User-Defined-CSS-to-an-HTML-Result-File)
* [Specifying Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009771181-Specifying-Parameter-Values)
* [Specifying Report Running Properties in the Session](https://devnet.logianalytics.com/hc/en-us/articles/1500009771241-Specifying-Report-Running-Properties-in-the-Session)
* [Tracing Server Resource Change Events](https://devnet.logianalytics.com/hc/en-us/articles/1500009770961-Tracing-Server-Resource-Change-Events)
* [Auditing on Exporting, Printing, and Saving of Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009770941-Auditing-on-Exporting-Printing-and-Saving-of-Reports)
* [Configuring the Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/1500009743142-Configuring-the-Security-Cache-System)
* [Customizing the Web Report Studio Toolbar](https://devnet.logianalytics.com/hc/en-us/articles/1500009743322-Customizing-the-Web-Report-Studio-Toolbar)
* [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771221-Customized-Implementation-of-the-Security-API)
* [Advanced Running Reports Using the On-Demand API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771161-Advanced-Running-Reports-Using-the-On-Demand-API)
* [Applying the Implementations of the Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771021-Applying-the-Implementations-of-the-Dashboard-Listener-API)
* [Using the NLS API](https://devnet.logianalytics.com/hc/en-us/articles/1500009743222-Using-the-NLS-API)
* [Dynamic Connection API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771041-Dynamic-Connection-API)
* [Dynamic Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009743182-Dynamic-Security-API)
* [Information Bus API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771081-Information-Bus-API)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743082-Installing-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771101-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)
