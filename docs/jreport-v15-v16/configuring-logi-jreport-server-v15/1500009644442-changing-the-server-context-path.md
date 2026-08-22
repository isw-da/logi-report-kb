---
title: "Changing the Server Context Path"
id: 1500009644442
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644442-Changing-the-Server-Context-Path
updated_at: 2021-07-24T20:55:21Z
---

# Changing the Server Context Path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669161-Updating-the-Server-License)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669201-Tuning-Server-Performance)

# Changing the Server Context Path

In some circumstances you may want to change the server context path for accessing Logi JReport Server console and running Logi JReport reports. This topic introduces how to do this in a standalone or an integrated environment.

After the context path is changed, when [working on Logi JReport Server via URLs](https://devnet.logianalytics.com/hc/en-us/articles/1500009675421-Working-on-Logi-JReport-Server-Guide-v15-Server-via-URLs), the new context path should be used in the URLs.

Below is a list of the sections covered in this topic:

* [Changing Standalone Server Context Path](#Standalone)
* [Changing Integrated Server Context Path](#Integ)

## Changing Standalone Server Context Path

Logi JReport has the following URL configuration for accessing Logi JReport Server console and running Logi JReport reports in a standalone environment:

`http://<hostname>:8888/jrserver  
 http://<hostname>:8888/jinfonet/index.jsp  
http://<hostname>:8888/dhtmljsp/...  
http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fLink.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

You may want to change the server context path to **`/jrp`** and the URLs will be:

`http://<hostname>:8888/jrp/jrserver  
 http://<hostname>:8888/jrp/jinfonet/index.jsp  
 http://<hostname>:8888/jrp/dhtmljsp/...  
http://localhost:8888/jrp/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fLink.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://localhost:8888/jrp/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

**To do this:**

1. Copy all contents in `<install_root>\public_html` to `<install_root>\public_html\jrp`.
2. Modify the following property values in server.properties in `<install>\bin` directory by adding "/jrp":

   `web.design_servlet_path=/jrp/webreporting  
    web.dhtml_jsp_path=/jrp/dhtmljsp
     
    web.dhtml_servlet_path=/jrp/dhtml  
    web.help_servlet_path=/jrp/help  
    web.Logi JReport_servlet_path=/jrp/jrserver  
    web.skin.dir=/jrp/skin`
3. Modify the value of jsp\_path in redirect.properties in `<install>\bin` directory by adding "/jrp":

   `jsp_path=/jrp/jinfonet/`
4. Modify mapping.properties in `<install>\bin` directory by adding "/jrp":

   |  |
   | --- |
   | ``` # Map servlets to paths # Properties beginning with a . are extension properties, all other # properties are path properties # # Format: # path or extension = servlet name /jrp/jrserver=jrserver /servlet/sendfile=sendfile /jrp/dhtml=dhtml /jrp/help=help .jsp=jspservlet ``` |
5. Start the server and access the server by the URLs:

   `http://localhost:8888/jrp/jrserver  
    http://localhost:8888/jrp/jinfonet/index.jsp`

   Run a report in Page Report Studio by the URL:

   `http://localhost:8888/jrp/webos/app/pagestudio/run.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information.cls`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Changing Integrated Server Context Path

Supposing that all server resources are deployed to the context root folder Logi JReport\ after deploying Logi JReport Server to an application server.

You can use the following URLs for accessing Logi JReport Server service console and running Logi JReport reports in the integrated environment:

`http://<hostname>:port/Logi JReport/jinfonet/index.jsp  
 http://<hostname>:port/Logi JReport/dhtmljsp/...`  
`http://localhost:8888/Logi JReport/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fLink.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://localhost:8888/Logi JReport/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

You may want to change the server context path to `/Logi JReport/myjsp and the URLs will be`:

`http://<hostname>:port/Logi JReport/myjsp/jinfonet/index.jsp  
 http://<hostname>:port/Logi JReport/myjsp/dhtmljsp/...`  
`http://localhost:8888/Logi JReport/myjsp/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fLink.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://localhost:8888/Logi JReport/myjsp/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

**To do this:**

1. Move index.htm and the following folders from `Logi JReport\` to `Logi JReport\myjsp\`:

   admin  
    dhtmljsp  
    images  
    javascript  
    jinfonet  
    skin  
    style
2. Create a file jrserver.properties in the \WEB-INF directory, add the skin and dhtmljsp properties and provide the correct paths (the context root is excluded):

   `web.skin.dir=/myjsp/skin  
    web.dhtml_jsp_path=/myjsp/dhtmljsp`
3. Access the server by the URL: `http://<hostname>:port/Logi JReport/myjsp/jinfonet/index.jsp`

   Run a report in Page Report Studio by the URL:

   `http://<hostname>:port/Logi JReport/myjsp/webos/app/pagestudio/run.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information.cls`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669161-Updating-the-Server-License)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669201-Tuning-Server-Performance)
