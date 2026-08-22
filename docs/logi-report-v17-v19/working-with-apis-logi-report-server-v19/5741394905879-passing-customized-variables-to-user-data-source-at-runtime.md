---
title: "Passing Customized Variables to User Data Source at Runtime"
id: 5741394905879
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741394905879-Passing-Customized-Variables-to-User-Data-Source-at-Runtime
updated_at: 2022-10-31T17:15:49Z
---

# Passing Customized Variables to User Data Source at Runtime

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400384407-Loading-User-Data-Source-Classes-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415075095-Applying-a-User-Defined-CSS-to-an-HTML-Output-File)

# Passing Customized Variables to User Data Source at Runtime

You can pass customized variables to a user data source (UDS) at runtime, by implementing the **jet.datasource.JRUserServerInfoDataSource** interface and adding customized variables in the session or URL. This topic describes how to pass customized variables to UDS.

1. Implement the **jet.datasource.JRUserServerInfoDataSource** interface so that your UDS can receive customized variables.

   ![JRUserServerInfoDataSource interface](https://devnet.logianalytics.com/hc/article_attachments/9905819794455/wkapi_srv_use_cstmvrbluds.gif)
2. Read customized variables in UDS. Server collects customized variables from the session or URL and stores them in a **java.util.Properties** in the **jet.server.api.ServerInfo** interface. You can then get the **java.util.Properties** to obtain the customized variables, through **ServerInfo.getTaskProperties()**.

   ```
   Properties props = getServerInfo().getTaskProperties();  
   String var1 = props.getProperty("UDP$Var1");  
   String var2 = props.getProperty("UDP$Var2");
   ```
3. You can use the following three ways to set customized variables to UDS, with the priority from highest to lowest:
   * Set customized variables using the Logi Report session variable feature. Use a **java.util.Properties** to collect all customized variables and set the **java.util.Properties** by **HttpSession.setAttribute** to the HttpSession with the key **JReport\_running\_parameter**. See the following example:

     ```
     Properties ssnVars = new Properties();  
     ssnVars.setProperty("Var1", "a");  
     ssnVars.setProperty("Var2", "b");  
       
     HttpSession httpsession = request.getSession();  
     httpsession.setAttribute("JReport_running_parameter", ssnVars);
     ```
   * Set customized variables in the HttpSession, by setting attributes that start with **UDP$**.

     ```
     HttpSession httpsession = request.getSession();  
     httpsession.setAttribute("UDP$Var1", "a");  
     httpsession.setAttribute("UDP$Var2", "b");
     ```
   * Set customized variables in the URL of running a report, by setting parameters that start with **UDP$**.

     ```
     http://localhost:8888/jinfonet/runReport.jsp?jrs.report=%2freport1.wls&jrs.catalog=%2fSampleReports.cat&jrs.result_type=8&UDP$Var1=a&UDP$Var2=b
     ```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400384407-Loading-User-Data-Source-Classes-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415075095-Applying-a-User-Defined-CSS-to-an-HTML-Output-File)
