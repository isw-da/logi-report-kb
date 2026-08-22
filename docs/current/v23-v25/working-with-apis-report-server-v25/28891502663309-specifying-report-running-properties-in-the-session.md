---
title: "Specifying Report Running Properties in the Session"
id: 28891502663309
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891502663309-Specifying-Report-Running-Properties-in-the-Session
updated_at: 2026-02-26T02:11:09Z
source_host: docs-report.zendesk.com
---
# 
Specifying Report Running Properties in the Session 

Report provides the key JReport_running_parameter for holding property variables in the session. You can set a String or Map object as the session attribute with this key before calling Report services. This topic describes how you can set properties to the key JReport_running_parameter and how the properties work when you set them both in the URL and in the session.

When designing integration and security with your application, setting sensitive information in the session and letting the server fetch them when running reports is a more secure way, compared to putting all information in the URL.

See the following example: 

HttpSession httpSession = ...;
Map<String, String> ssnVariable = new HashMap<String, String>();
ssnVariable.put("jrs.param$psessionurl", "Sample+Data.json");
httpSession.setAttribute("JReport_running_parameter", ssnVariable);
...
For a String object, it should take the query string format used in the URL for running reports or dashboards and obey application/x-www-form-urlencoded format and be encoded by UTF-8. For example, the application/x-www-form-urlencoded format requires that blankspace should be encoded as "+", in the preceding sample code, if a String object is used, after Report Server decodes URL from session variable, "Sample+Data.json" becomes "Sample Data.json". For a Map object, the quoted value will be used directly without any change.

When you run reports or dashboards via URL, Report gets information first from the URL and then picks up provided information from the session using the key. For information that exists in both the URL and the session, the session setting overrides that of the URL.

For properties both in the URL and the session, the properties in the session will override those in the URL. For properties only in the session, the properties will be appended to the URL to run the report or dashboard.

For running reports via server JSP

- 
Set parameter value in the session:httpSession.setAttribute("JReport_running_parameter", "jrs.param$parameter1=xxx&jrs.param$parameter2=xxx...");

- 
Set dynamic connection in the session:httpSession.setAttribute("JReport_running_parameter", "jrs.jdbc_driver=com.mysql.jdbc.Driver&jrs.jdbc_url=jdbc:mysql://IP:3306/test&jrs.db_user=xxx&jrs.db_pswd=xxx");

For running web reports via JSON

The following rules are about some special properties when merging them from the session and from the URL: 

- 
jrd_report
    Session overrides URL. Once this object is specified in the session, only the specified report can be run whenever the URL submits to run any report. 

- 
jrd_param$
    Session overrides the same-name parameters and appends the other parameters to the URL. 

- 
jrd_userinfo
    Session overrides the properties in the object. 

- 
jrd_datasources
    It should contain an object array and use "ds" as the key. The session overrides the objects with the same key and appends the other objects to the array. 

See some examples: 

- 
Set parameter value in the session (JSON format):httpSession.setAttribute("JReport_running_parameter", "jrd_param$={\"parameter1\":\"xxx\", \"parameter2\":\"xxx\"}");

- 
Set dynamic connection in the session (JSON format):httpSession.setAttribute("JReport_running_parameter", "jrd_datasources=[{\"ds\":\"Data Source 1\", \"uid\":\"xxx\", \"pwd\":\"xxx\", \"type\":\"0\", \"url\":\"jdbc:mysql://IP:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]");

- 
Set time zone in the session (JSON format):httpSession.setAttribute("JReport_running_parameter", "jrd_userinfo={\"prefer\":{\"rpt_timezone\": \"CST\"}}");

For running dashboards via JSON

The following rules are about some special properties when merging them from the session and from the URL:

- 
jrd_resext 
    For single properties, session overrides the properties in the URL and adds those not in the URL. 

- 
reslst
    It should contain an object array and use "name" as the key. The objects with the same key plus dsh_params and dsh_datasources settings in the session will be appended to the object in the URL. Other objects from the session will be added to the array in the URL.
    For example:

jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params":{"P_StartDate":"01/01/2016"}}]}]}

Dashboard 1.dsh will run with the parameter P_StartDate="01/01/2016".

You can set JReport_running_parameter in the session as: 

jrd_resext={"active":0,"reslst":[{"name":"/USERFOLDERPATH/admin/Dashboard 1.dsh","dsh_params":[{"jrd_params": {"P_StartDate":"01/01/2017","P_EndDate":"12/31/2017"}}]}]} 

Dashboard 1.dsh will then run with P_StartDate="01/01/2017" (applies the parameter value from session) and P_EndDate="12/31/2017" (appends the parameter from session to the URL) for all library components.  
  

See some examples: 

- 
Set parameter value in the session for a specific library component:httpSession.setAttribute("JReport_running_parameter", "jrd_resext={\"active\":0,\"reslst\":[{\"name\":\"/62309_Session/62309.dsh\", \"dsh_params\":[{\"jrd_params\":{\"parameter1\":\"xxx\",\"parameter2\":\"xxx\"}}, {\"lc_names\":[\"s13dfc53ea67\"],\"jrd_params\":{\"parameter1\":\"xxx\",\"parameter2\":\"xxx\"}}, {\"lc_names\":[\"s13dfda08c0a\"],\"jrd_params\":{\"parameter1\":\"xxx\", parameter2:\"xxx\"}}]}]}");

- 
Set dynamic connection in the session for specific library components:httpSession.setAttribute("JReport_running_parameter", "jrd_resext={\"active\":0,\"reslst\":[{\"name\":\"/62309_Session/62309_datasource.dsh\", \"dsh_datasources\":[{\"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\", \"url\":\"jdbc:mysql://IP1:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}, {\"lc_names\":[\"/COMPONENT_LIB/62309_Session/62309_datasource.lc\"], \"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\",  \"url\":\"jdbc:mysql://IP2:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}, {\"lc_names\":[\"s13e0cdc04f2\"], \"jrd_datasources\":[{\"ds\":\"Data Source 2\", \"uid\":\"root\", \"pwd\":\"1234\", \"type\":\"0\",  \"url\":\"jdbc:mysql://IP3:3306/test\", \"driver\":\"com.mysql.jdbc.Driver\"}]}]}]}");
