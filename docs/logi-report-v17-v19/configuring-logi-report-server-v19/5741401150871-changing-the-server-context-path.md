---
title: "Changing the Server Context Path"
id: 5741401150871
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741401150871-Changing-the-Server-Context-Path
updated_at: 2022-10-31T17:15:58Z
---

# Changing the Server Context Path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741416097559-Updating-the-Server-License)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741409384343-Tuning-Server-Performance)

# Changing the Server Context Path

In some circumstances, you may want to change the server context path for accessing the Server Console and running Logi Report reports. This topic describes how you can change the server context path in a standalone or an integrated environment.

After you change the context path, you should use the new context path in the URLs when [working on Logi Report Server via URL](https://devnet.logianalytics.com/hc/en-us/articles/5741464810263-Working-on-Logi-Report-Server-via-URL-Logi-Report-Server-v19).

This topic contains the following sections:

* [Changing Standalone Server Context Path](#Standalone)
* [Changing Integrated Server Context Path](#Integ)

## Changing Standalone Server Context Path

Logi Report has the following URL configuration for accessing the Server Console and running Logi Report reports in a standalone environment:

```
http://<hostname>:8888/jrserver  
http://<hostname>:8888/jinfonet/index.jsp  
http://<hostname>:8888/dhtmljsp/...  
http://<hostname>:8888/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat
```

You may want to change the server context path to **/jrp**. Change the URL:

```
http://<hostname>:8888/jrp/jrserver  
http://<hostname>:8888/jrp/jinfonet/index.jsp  
http://<hostname>:8888/jrp/dhtmljsp/...  
http://<hostname>:8888/jrp/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/jrp/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat
```

**To do this:**

1. Copy all files and folders in `<install_root>\public_html` to `<install_root>\public_html\jrp`.
2. Modify the following property values in **server.properties** in the `<install>\bin` directory by adding **/jrp**:

   ```
   web.design_servlet_path=/jrp/webreporting  
   web.dhtml_jsp_path=/jrp/dhtmljsp
         
   web.dhtml_servlet_path=/jrp/dhtml  
   web.help_servlet_path=/jrp/help  
   web.jreport_servlet_path=/jrp/jrserver  
   web.skin.dir=/jrp/skin
   ```
3. Modify the value of **jsp\_path** in redirect.properties in the `<install>\bin` directory by adding **/jrp**:

   ```
   jsp_path=/jrp/jinfonet/
   ```
4. Modify the **mapping.properties** in the `<install>\bin` directory by adding **/jrp**:

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
   /jrp/vt=webos  
   .jsp=jspservlet
   ```
5. Start Server.
6. Access it by either URL:

   ```
   http://<hostname>:8888/jrp/jrserver  
   http://<hostname>:8888/jrp/jinfonet/index.jsp
   ```

   Run a report in Page Report Studio by the URL:

   ```
   http://<hostname>8888/jrp/webos/app/pagestudio/run.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information List.cls
   ```

## Changing Integrated Server Context Path

Suppose that you deployed all server resources to the context root folder **jreport\** after deploying Logi Report Server to an application server. You can use the URL for accessing the Logi Report Server service console and running Logi Report reports in the integrated environment:

```
http://<hostname>:port/jreport/jinfonet/index.jsp  
http://<hostname>:port/jreport/dhtmljsp/...  
http://<hostname>:8888/jreport/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/jreport/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat
```

You may want to change the server context path to **/jreport/myjsp** and the URL will be:

```
http://<hostname>:port/jreport/myjsp/jinfonet/index.jsp  
 http://<hostname>:port/jreport/myjsp/dhtmljsp/...  
http://<hostname>:8888/jreport/myjsp/jinfonet/tryView.jsp?&jrs.report=%2fSampleReports%2fSales Detail Report.wls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8  
http://<hostname>:8888/jreport/myjsp/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fEmployee Information List.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat
```

**To do this:**

1. Move **index.htm** and these folders from **jreport\** to **jreport\myjsp\**:
   admin, dhtmljsp, images, javascript, jinfonet, skin, and style.
2. Create a **jrserver.properties** file in the \WEB-INF directory, add the **skin** and **dhtmljsp** properties and provide the correct paths (excluding the context root):

   ```
   web.skin.dir=/myjsp/skin  
   web.dhtml_jsp_path=/myjsp/dhtmljsp
   ```
3. Access the server by the URL `http://<hostname>:port/jreport/myjsp/jinfonet/index.jsp`.
4. Run a report in Page Report Studio by the URL:

   ```
   http://<hostname>:port/jreport/myjsp/webos/app/pagestudio/run.jsp?jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fEmployee Information List.cls
   ```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741416097559-Updating-the-Server-License)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741409384343-Tuning-Server-Performance)
