---
title: "Specifying Report Running Properties in the Session"
id: 1500009668821
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668821-Specifying-Report-Running-Properties-in-the-Session
updated_at: 2021-07-24T20:55:26Z
---

# Specifying Report Running Properties in the Session

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668741-Specifying-Parameter-Values)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668481-Tracing-Server-Resource-Change-Events)

# Specifying Report Running Properties in the Session

When designing integration and security with your application, compared to putting all information in the URL, setting sensitive information in the session and letting the server fetch them when running reports is a more secure way.

Logi JReport provides the key *Logi JReport\_running\_parameter* for holding property variables in the session. You can set a String or Map object as the session attribute with this key before calling Logi JReport services. For example:

|  |
| --- |
| ``` HttpSession httpSession = ...;   Map<String, String> ssnVariable = new HashMap<String, String>();   ssnVariable.put("jrs.param$psessionurl", "Sample+Data.json");   httpSession.setAttribute("Logi JReport_running_parameter", ssnVariable); ... ``` |

For a String object, it should take the query string format used in the URL for running reports or dashboards and obey application/x-www-form-urlencoded format and be encoded by UTF-8. For example, the application/x-www-form-urlencoded format requires that blankspace should be encoded as "+", in the above sample code, if a String object is used, after Logi JReport Server decodes URL from session variable, "Sample+Data.json" becomes "Sample Data.json". For a Map object, the quoted value will be used directly without any change.

When you run reports or dashboards via URL, Logi JReport gets information first from the URL and then picks up provided information from the session using the key. For information that exists in both the URL and the session, the session setting overrides that of the URL.

For properties both in the URL and the session, the properties in the session will override those in the URL. For properties only in the session, the properties will be appended to the URL to run the report or dashboard.

Below is a list of the sections covered in this topic:

* [For Running Reports via Server JSP](#JSP)
* [For Running Web Reports via JSON](#WebReport)
* [For Running Dashboards via JSON](#Dashboard)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## For Running Reports via Server JSP

**Examples:**

* **Set parameter value in the session:**

  `HttpSession.setAttribute("Logi JReport_running_parameter", "jrs.param$parameter1=xxx&jrs.param$parameter2=xxx...");`
* **Set dynamic connection in the session:**

  `HttpSession.setAttribute("Logi JReport_running_parameter", "jrs.jdbc_driver=com.mysql.jdbc.Driver&jrs.jdbc_url=jdbc:mysql://IP:3306/test&jrs.db_user=xxx&jrs.db_pswd=xxx");`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## For [Running Web Reports via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON)

The following rules are about some special properties when merging them from the session and from the URL:

* **jrd\_report**  
   Session overrides URL. Once this object is specified in the session, only the specified report can be run whenever the URL submits to run any report.
* **jrd\_param$**  
   Session overrides the same-name parameters and appends the other parameters to the URL.
* **jrd\_userinfo**  
   Session overrides the properties in the object.
* **jrd\_datasources**  
   It should contain an object array and use *ds* as the key. The session overrides the objects with the same key and appends the other objects to the array.

**Examples:**

* **Set parameter value in the session (JSON format):**

  `HttpSession.setAttribute("Logi JReport_running_parameter", "jrd_param$={\"parameter1\":\"xxx\", \"parameter2\":\"xxx\"}");`
* **Set dynamic connection in the session (JSON format):**

  `HttpSession.setAttribute("Logi JReport_running_parameter", "jrd_datasources=[{\"ds\":\"Data Source 1\", \"uid\":\"xxx\", \"pwd\":\"xxx\", \"type\":\"0\", \"url\":\"jdbc:mysql://IP:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]");`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## For [Running Dashboards via JSON](https://devnet.logianalytics.com/hc/en-us/articles/1500009650422-Working-With-Dashboards#Open)

The following rules are about some special properties when merging them from the session and from the URL:

* **jrd\_resext**   
   For single properties, session overrides the properties in the URL and adds those not in the URL.
* **reslst**  
   It should contain an object array and use *name* as the key. The objects with the same key plus *dsh\_params* and *dsh\_datasources* settings in the session will be appended to the object in the URL. Other objects from the session will be added to the array in the URL.

  For example:

  `jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2006"}}]}]}`

  Dashboard1.dsh will run with the parameter P\_StartDate="01/01/2006".

  A user can set *Logi JReport\_running\_parameter* in the session as:

  `jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard1.dsh","dsh_params":[{"jrd_params": {"P_StartDate":"01/01/2007","P_EndDate":"12/31/2007"}}]}]}`

  Dashboard1.dsh will then run with P\_StartDate="01/01/2007" (applies the parameter value from session) and P\_EndDate="12/31/2007" (appends the parameter from session to the URL) for all library components.

**Examples:**

* **Set parameter value in the session for a specific library component:**

  `HttpSession.setAttribute("Logi JReport_running_parameter", "jrd_resext={\"active\":0,\"reslst\":[{\"name\":\"/62309_Session/62309.dsh\", \"dsh_params\":[{\"jrd_params\":{\"parameter1\":\"xxx\",\"parameter2\":\"xxx\"}}, {\"lc_names\":[\"s13dfc53ea67\"],\"jrd_params\":{\"parameter1\":\"xxx\",\"parameter2\":\"xxx\"}}, {\"lc_names\":[\"s13dfda08c0a\"],\"jrd_params\":{\"parameter1\":\"xxx\", parameter2:\"xxx\"}}]}]}");`
* **Set dynamic connection in the session for specific library components:**

  `HttpSession.setAttribute("Logi JReport_running_parameter", "jrd_resext={\"active\":0,\"reslst\":[{\"name\":\"/62309_Session/62309_datasource.dsh\", \"dsh_datasources\":[{\"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\", \"url\":\"jdbc:mysql://IP1:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}, {\"lc_names\":[\"/COMPONENT_LIB/62309_Session/62309_datasource.lc\"], \"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\",  \"url\":\"jdbc:mysql://IP2:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}, {\"lc_names\":[\"s13e0cdc04f2\"], \"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\",  \"url\":\"jdbc:mysql://IP3:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}]}]}");`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668741-Specifying-Parameter-Values)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668481-Tracing-Server-Resource-Change-Events)
