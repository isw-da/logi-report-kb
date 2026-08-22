---
title: "Using the Server API"
id: 45203849318285
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203849318285-Using-the-Server-API
updated_at: 2026-04-30T14:07:44Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Using the Server API 

You can use Report Server API to achieve specific goals. This topic describes the HTTP methods GET and POST and how to specify the full paths of the server resources in the code.

The HTTP methods GET and POST are available for almost all of Report commands. The following is an example of using the POST method in Java program: 

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
When using the Server API to perform tasks on resources in the server resource tree, you need to specify the full path of the resources in the code. The rules are as follows: 

- If the resource is in the Public Reports folder in the server resource tree, you should start the path  with "/". For example, for the /Public Report/SampleReports folder, the path is "/SampleReports".

- If the resource is in the My Reports folder in the server resource tree, you should start the path with "/USERFOLDERPATH/username/" (change username to the real username with which you sign in to Report Server). For example, suppose your username is Jim and you want to access the /My Reports/Shipments folder, the path in the URL is "/USERFOLDERPATH/Jim/Shipments".

The following list provides you with links on how to perform specific tasks using the Server API. Select the links to view the topics. For more information, see the Report Javadoc.

- Creating and Getting Instances of Report Engine and Report Server

- Using JSP with a Dedicated Machine

- Using RMI in Report Server

- Publishing Resources from One Server to Another

- Working with Resource Versions

- Changing the Runtime Database Connection

- Scheduling a Report Task

- Scheduling a Customized Task Using User Task

- Applying TaskListener

- Writing Customized Load Balancing Algorithm

- Setting Server Reporthome and Properties in a Java EE Environment

- Loading User Data Source Classes at Runtime

- Passing Customized Variables to User Data Source at Runtime

- Applying a User Defined CSS to an HTML Output File

- Specifying Parameter Values

- Specifying Report Running Properties in the Session

- Tracing Server Resource Change Events

- Auditing on Exporting, Printing, and Saving of Reports

- Configuring the Security Cache System

- Customizing the Web Report Studio Toolbar

- Customized Implementation of the Security API

- Advanced Running Reports Using the On-Demand API

- Applying the Implementations of the Dashboard Listener API

- Using the NLS API

- Dynamic Connection API

- Dynamic Security API

- Information Bus API
