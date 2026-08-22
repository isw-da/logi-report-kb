---
title: "Specifying Report Running Properties in the Session"
id: 1500009718582
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718582-Specifying-Report-Running-Properties-in-the-Session
updated_at: 2021-07-25T07:20:21Z
---

# Specifying Report Running Properties in the Session

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744421-Specifying-Parameter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744241-Tracing-Server-Resource-Change-Events)

# Specifying Report Running Properties in the Session

When designing integration and security with your application, compared to putting all information in the URL, setting sensitive information in the session and letting the server fetch them when running reports is a more secure way.

Logi Report provides the key JReport\_running\_parameter for holding property variables in the session. You can set a String or Map object as the session attribute with this key before calling Logi Report services. For example:

```
HttpSession httpSession = ...;  

Map<String, String> ssnVariable = new HashMap<String, String>();  

ssnVariable.put("jrs.param$psessionurl", "Sample+Data.json");  

httpSession.setAttribute("JReport_running_parameter", ssnVariable);  

...
```

For a String object, it should take the query string format used in the URL for running reports or dashboards and obey application/x-www-form-urlencoded format and be encoded by UTF-8. For example, the application/x-www-form-urlencoded format requires that blankspace should be encoded as "+", in the above sample code, if a String object is used, after Logi Report Server decodes URL from session variable, "Sample+Data.json" becomes "Sample Data.json". For a Map object, the quoted value will be used directly without any change.

When you run reports or dashboards via URL, Logi Report gets information first from the URL and then picks up provided information from the session using the key. For information that exists in both the URL and the session, the session setting overrides that of the URL.

For properties both in the URL and the session, the properties in the session will override those in the URL. For properties only in the session, the properties will be appended to the URL to run the report or dashboard.

**For [running reports via server JSP](https://devnet.logianalytics.com/hc/en-us/articles/1500009751721-Running-Reports)**

* **Set parameter value in the session:**

  `HttpSession.setAttribute("JReport_running_parameter", "jrs.param$parameter1=xxx&jrs.param$parameter2=xxx...");`
* **Set dynamic connection in the session:**

  `HttpSession.setAttribute("JReport_running_parameter", "jrs.jdbc_driver=com.mysql.jdbc.Driver&jrs.jdbc_url=jdbc:mysql://IP:3306/test&jrs.db_user=xxx&jrs.db_pswd=xxx");`

**For [running web reports via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009751721-Running-Reports#JSON)**

The following rules are about some special properties when merging them from the session and from the URL:

* **jrd\_report**  
   Session overrides URL. Once this object is specified in the session, only the specified report can be run whenever the URL submits to run any report.
* **jrd\_param$**  
   Session overrides the same-name parameters and appends the other parameters to the URL.
* **jrd\_userinfo**  
   Session overrides the properties in the object.
* **jrd\_datasources**  
   It should contain an object array and use "ds" as the key. The session overrides the objects with the same key and appends the other objects to the array.

See some examples below:

* **Set parameter value in the session (JSON format):**

  `HttpSession.setAttribute("JReport_running_parameter", "jrd_param$={\"parameter1\":\"xxx\", \"parameter2\":\"xxx\"}");`
* **Set dynamic connection in the session (JSON format):**

  `HttpSession.setAttribute("JReport_running_parameter", "jrd_datasources=[{\"ds\":\"Data Source 1\", \"uid\":\"xxx\", \"pwd\":\"xxx\", \"type\":\"0\", \"url\":\"jdbc:mysql://IP:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]");`

**For [running dashboards via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009724982-Working-with-Dashboards#Open)**

The following rules are about some special properties when merging them from the session and from the URL:

* **jrd\_resext**   
   For single properties, session overrides the properties in the URL and adds those not in the URL.
* **reslst**  
   It should contain an object array and use "name" as the key. The objects with the same key plus dsh\_params and dsh\_datasources settings in the session will be appended to the object in the URL. Other objects from the session will be added to the array in the URL.

  For example:

  `jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2016"}}]}]}`

  Dashboard 1.dsh will run with the parameter P\_StartDate="01/01/2016".

  You can set JReport\_running\_parameter in the session as:

  `jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params": {"P_StartDate":"01/01/2017","P_EndDate":"12/31/2017"}}]}]}`

  Dashboard 1.dsh will then run with P\_StartDate="01/01/2017" (applies the parameter value from session) and P\_EndDate="12/31/2017" (appends the parameter from session to the URL) for all library components.

See some examples:

* **Set parameter value in the session for a specific library component:**

  `HttpSession.setAttribute("JReport_running_parameter", "jrd_resext={\"active\":0,\"reslst\":[{\"name\":\"/62309_Session/62309.dsh\", \"dsh_params\":[{\"jrd_params\":{\"parameter1\":\"xxx\",\"parameter2\":\"xxx\"}}, {\"lc_names\":[\"s13dfc53ea67\"],\"jrd_params\":{\"parameter1\":\"xxx\",\"parameter2\":\"xxx\"}}, {\"lc_names\":[\"s13dfda08c0a\"],\"jrd_params\":{\"parameter1\":\"xxx\", parameter2:\"xxx\"}}]}]}");`
* **Set dynamic connection in the session for specific library components:**

  `HttpSession.setAttribute("JReport_running_parameter", "jrd_resext={\"active\":0,\"reslst\":[{\"name\":\"/62309_Session/62309_datasource.dsh\", \"dsh_datasources\":[{\"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\", \"url\":\"jdbc:mysql://IP1:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}, {\"lc_names\":[\"/COMPONENT_LIB/62309_Session/62309_datasource.lc\"], \"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\",  \"url\":\"jdbc:mysql://IP2:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}, {\"lc_names\":[\"s13e0cdc04f2\"], \"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\",  \"url\":\"jdbc:mysql://IP3:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}]}]}");`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744421-Specifying-Parameter-Values)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744241-Tracing-Server-Resource-Change-Events)
