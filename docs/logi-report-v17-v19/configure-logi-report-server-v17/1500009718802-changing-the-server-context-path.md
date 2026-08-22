---
title: "Changing the Server Context Path"
id: 1500009718802
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718802-Changing-the-Server-Context-Path
updated_at: 2021-07-25T07:20:17Z
---

# Changing the Server Context Path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718842-Updating-the-Server-License)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718862-Tuning-Server-Performance)

# Changing the Server Context Path

In some circumstances you may want to change the server context path for accessing Logi Report Server console and running Logi Report reports. This topic introduces how to do this in a standalone or an integrated environment.

After the context path is changed, when [working on Logi Report Server via URLs](https://devnet.logianalytics.com/hc/en-us/articles/1500009724942-Working-on-Logi-Report-Server-via-URLs-Logi-Report-Server-v17), the new context path should be used in the URLs.

Select the following links to view the topics:

* [Changing Standalone Server Context Path](#Standalone)
* [Changing Integrated Server Context Path](#Integ)

## Changing Standalone Server Context Path

Logi Report has the following URL configuration for accessing the Logi Report Server console and running Logi Report reports in a standalone environment:

`http://<hostname>:8888/jrserver  
 http://<hostname>:8888/jinfonet/index.jsp  
http://<hostname>:8888/dhtmljsp/...  
http://<hostname>:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

You may want to change the server context path to /jrp and the URLs will be:

`http://<hostname>:8888/jrp/jrserver  
http://<hostname>:8888/jrp/jinfonet/index.jsp  
http://<hostname>:8888/jrp/dhtmljsp/...  
http://<hostname>:8888/jrp/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/jrp/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

**To do this:**

1. Copy all contents in `<install_root>\public_html` to `<install_root>\public_html\jrp`.
2. Modify the following property values in server.properties in `<install>\bin` directory by adding "/jrp":

   web.design\_servlet\_path=**/jrp**/webreporting  
   web.dhtml\_jsp\_path=**/jrp**/dhtmljsp
     
   web.dhtml\_servlet\_path=**/jrp**/dhtml  
   web.help\_servlet\_path=**/jrp**/help  
   web.jreport\_servlet\_path=**/jrp**/jrserver  
   web.skin.dir=**/jrp**/skin
3. Modify the value of jsp\_path in redirect.properties in `<install>\bin` directory by adding "/jrp":

   jsp\_path=**/jrp**/jinfonet/
4. Modify mapping.properties in `<install>\bin` directory by adding "/jrp":

   ```
   # Map servlets to paths  
   # Properties beginning with a . are extension properties, all other  
   # properties are path properties  
   #  
   # Format:  
   # path or extension = servlet name  
     
   /jrp/jrserver=jrserver  
   /servlet/sendfile=sendfile  
   /jrp/dhtml=dhtml  
   /jrp/help=help  
   .jsp=jspservlet
   ```
5. Start the server and access the server by the URLs:

   `http://<hostname>:8888/jrp/jrserver  
    http://<hostname>:8888/jrp/jinfonet/index.jsp`

   Run a report in Page Report Studio by the URL:

   `http://<hostname>8888/jrp/webos/app/pagestudio/run.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information List.cls`

## Changing Integrated Server Context Path

Suppose that all server resources are deployed to the context root folder jreport\ after deploying Logi Report Server to an application server. You can use the following URLs for accessing the Logi Report Server service console and running Logi Report reports in the integrated environment:

`http://<hostname>:port/jreport/jinfonet/index.jsp  
 http://<hostname>:port/jreport/dhtmljsp/...`  
`http://<hostname>:8888/jreport/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/jreport/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

You may want to change the server context path to /jreport/myjsp and the URLs will be:

`http://<hostname>:port/jreport/myjsp/jinfonet/index.jsp  
 http://<hostname>:port/jreport/myjsp/dhtmljsp/...`  
`http://<hostname>:8888/jreport/myjsp/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/jreport/myjsp/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat`

**To do this:**

1. Move index.htm and the following folders from jreport\ to jreport\myjsp\:
   admin, dhtmljsp, images, javascript, jinfonet, skin and style.
2. Create a jrserver.properties file in the \WEB-INF directory, add the skin and dhtmljsp properties and provide the correct paths (the context root is excluded):

   web.skin.dir=/myjsp/skin  
   web.dhtml\_jsp\_path=/myjsp/dhtmljsp
3. Access the server by the URL: `http://<hostname>:port/jreport/myjsp/jinfonet/index.jsp`

   Run a report in Page Report Studio by the URL:

   `http://<hostname>:port/jreport/myjsp/webos/app/pagestudio/run.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information List.cls`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718842-Updating-the-Server-License)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718862-Tuning-Server-Performance)
