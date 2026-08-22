---
title: "Using the Server API"
id: 5741394799255
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741394799255-Using-the-Server-API
updated_at: 2022-10-31T17:15:46Z
---

# Using the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741363396375-Installing-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400342295-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)

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

* If the resource is in the Public Reports folder in the server resource tree, you should start the path with "/". For example, for the /Public Report/SampleReports folder, the path is "/SampleReports".
* If the resource is in the My Reports folder in the server resource tree, you should start the path with "/USERFOLDERPATH/*username/*" (change *username* to the real username with which you sign in to Logi Report Server). For example, suppose your username is Jim and you want to access the /My Reports/Shipments folder, the path in the URL is "/USERFOLDERPATH/Jim/Shipments".

The following list provides you with links on how to perform specific tasks using the Server API. Select the links to view the topics. For more information, see the Logi Report Javadoc.

* [Creating and Getting Instances of Report Engine and Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741400342295-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)
* [Using JSP with a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/5741386497687-Using-JSP-with-a-Dedicated-Machine)
* [Using RMI in Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741415368343-Using-RMI-in-Logi-Report-Server)
* [Publishing Resources from One Server to Another](https://devnet.logianalytics.com/hc/en-us/articles/5741400553623-Publishing-Resources-from-One-Server-to-Another)
* [Working with Resource Versions](https://devnet.logianalytics.com/hc/en-us/articles/5741386771735-Working-with-Resource-Versions)
* [Changing the Runtime Database Connection](https://devnet.logianalytics.com/hc/en-us/articles/5741400603543-Changing-the-Runtime-Database-Connection)
* [Scheduling a Report Task](https://devnet.logianalytics.com/hc/en-us/articles/5741386712599-Scheduling-a-Report-Task)
* [Scheduling a Customized Task Using User Task](https://devnet.logianalytics.com/hc/en-us/articles/5741400624023-Scheduling-a-Customized-Task-Using-User-Task)
* [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/5741395089175-Applying-TaskListener)
* [Writing Customized Load Balancing Algorithm](https://devnet.logianalytics.com/hc/en-us/articles/5741386314391-Writing-Customized-Load-Balancing-Algorithm)
* [Setting Server Reporthome and Properties in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741400319639-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
* [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/5741400384407-Loading-User-Data-Source-Classes-at-Runtime)
* [Passing Customized Variables to User Data Source at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/5741394905879-Passing-Customized-Variables-to-User-Data-Source-at-Runtime)
* [Applying a User Defined CSS to an HTML Output File](https://devnet.logianalytics.com/hc/en-us/articles/5741415075095-Applying-a-User-Defined-CSS-to-an-HTML-Output-File)
* [Specifying Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741415347351-Specifying-Parameter-Values)
* [Specifying Report Running Properties in the Session](https://devnet.logianalytics.com/hc/en-us/articles/5741408571799-Specifying-Report-Running-Properties-in-the-Session)
* [Tracing Server Resource Change Events](https://devnet.logianalytics.com/hc/en-us/articles/5741386288919-Tracing-Server-Resource-Change-Events)
* [Auditing on Exporting, Printing, and Saving of Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741415006743-Auditing-on-Exporting-Printing-and-Saving-of-Reports)
* [Configuring the Security Cache System](https://devnet.logianalytics.com/hc/en-us/articles/5741400164119-Configuring-the-Security-Cache-System)
* [Customizing the Web Report Studio Toolbar](https://devnet.logianalytics.com/hc/en-us/articles/5741395390999-Customizing-the-Web-Report-Studio-Toolbar)
* [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/5741363965079-Customized-Implementation-of-the-Security-API)
* [Advanced Running Reports Using the On-Demand API](https://devnet.logianalytics.com/hc/en-us/articles/5741400530711-Advanced-Running-Reports-Using-the-On-Demand-API)
* [Applying the Implementations of the Dashboard Listener API](https://devnet.logianalytics.com/hc/en-us/articles/5741394931863-Applying-the-Implementations-of-the-Dashboard-Listener-API)
* [Using the NLS API](https://devnet.logianalytics.com/hc/en-us/articles/5741408431895-Using-the-NLS-API)
* [Dynamic Connection API](https://devnet.logianalytics.com/hc/en-us/articles/5741408239895-Dynamic-Connection-API)
* [Dynamic Security API](https://devnet.logianalytics.com/hc/en-us/articles/5741415142807-Dynamic-Security-API)
* [Information Bus API](https://devnet.logianalytics.com/hc/en-us/articles/5741386457495-Information-Bus-API)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741363396375-Installing-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400342295-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)
