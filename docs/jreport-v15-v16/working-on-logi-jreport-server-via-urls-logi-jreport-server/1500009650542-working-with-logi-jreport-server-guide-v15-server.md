---
title: "Working with Logi JReport Server Guide v15 Server"
id: 1500009650542
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server
updated_at: 2021-07-24T20:53:30Z
---

# Working with Logi JReport Server Guide v15 Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650442-Working-With-Page-Reports)

# Working With Logi JReport Server

You can use URL to work with Logi JReport Server, for example, add and delete users/roles in the server security system, delete a resource node from the server resource tree, get the version table of a resource and so on. [Appendix 1: URL Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties) lists the properties you would need in the URL.

Below is a list of the sections covered in this topic:

* [Viewing Report Results](#ViewResult)
* [Specifying the Application Language](#NLS)
* [Adding and Deleting Users/Roles](#User)
* [Working With Resources](#Resource)
* [Managing Schedule Tasks](#Schedule)
* [Managing Resource Versions](#Version)
* [Loading the Server Preferences Page](#Preference)
* [Changing User Password](#Password)
* [Logging In and Out of Logi JReport Server](#Log)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Viewing Report Results

You can view the report results that are generated when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports#Advanced) or scheduling reports to [publish to the versioning system](https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System) via URL by either of the following two ways.

* **Using jsp**
  + **For the Page Report Result type (RSD)**   
     Page report results can be viewed in Page Report Studio by running runReport.jsp. The URL can call either of the following two groups of properties:
    - jrs.resource\_path and jrs.file
        
       URL Example: `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.resource_path=%2fUSERFOLDERPATH%2fadmin&jrs.file=1980996366.rsd`
    - jrs.rst\_version together with one of the three properties: jrs.version\_id, jrs.report and jrs.result. Logi JReport will search for the three properties one by one starting from the first to the third until it finds one.

      URL Example: `http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.rst_version=1&jrs.report=%2fSampleReports%2fBanded_Link.cls&type=rstfile&jrs.path=%2fSampleReports%2fBanded_Link.cls&jrs.version_id=257`
  + **For other result types**  
     To view the results of other result types such as PDF and HTML, you need to use viewVersion.jsp.  
     URL Example: `http://localhost:8888/jinfonet/viewVersion.jsp?jrs.cmd=jrs.view_ver_rst&jrs.result_type=2&jrs.version_number=1&jrs.ver_suff=.rst&jrs.result=%2fUSERFOLDERPATH%2fadmin%2fBanded_Link&jrs.path=%2fUSERFOLDERPATH%2fadmin%2fBanded_Link`
* **Using servlet**

  URL Format: `http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.view_ver_rst&jrs.hist_file=RESULT_VERSION_FILE_NAME`  
   URL Example: `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Banded_Link.cls?jrs.cmd=jrs.view_ver_rst&jrs.hist_file=1%2fadmin567625353%2f2109098280.pdf`

For details about the properties that would be included in the URL, see [Properties for viewing report results](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties#Result).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying the Application Language

When accessing the Logi JReport Console page or Page Report Studio UI via URL, you can control the language that is applied by setting the property jrs.language. The format of the URL is as follows:

`http://HOST:PORT/CONTEXT/PAGE?PROPERTY=VALUE&jrs.language=LANGUAGE_NAME`

The value of jrs.language should be the same as the language package folder name in the `<server_install_root>\resources\server\languages` directory and be lower-case letters.

The following are two examples:

* URL for accessing the Logi JReport Console page:

  `http://127.0.0.1:8888/jinfonet/index.jsp?jrs.language=zh-cn`
* URL for opening a page report in Page Report Studio:

  `http://127.0.0.1:8888/webos/app/pagestudio/run.jsp?jrs.report=/SampleReports/InvoiceReport.cls&jrs.catalog=/SampleReports/SampleReports.cat&jrs.cat_version=1&jrs.path=/SampleReports/InvoiceReport.cls&jrs.language=zh-cn`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Adding and Deleting Users/Roles

Admin users can run the following JSPs to add or remove users/roles to the security system on Logi JReport Server. However, before they can do this, they should have [logged onto the Logi JReport Server administration console](https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser#Admin)  in order to run the URL successfully.

* **processNewUser.jsp**

  Description: Adds a new user.  
   URL Example: `http://localhost:8889/admin/security/processNewUser.jsp?currentEditRealm=defaultRealm&user=Dean&fullName=Dean%20Black&description=Product%20Manager%20&email=Dean@jinfonet.com&password=123456&confirmPassword=123456&passwordLife=expire&expireTime=25&enableBlank=blank&minLength=6&jrs.privilege_access_advanced_properties=true`
* **processRemoveUser.jsp**

  Description: Deletes a specific user.  
   URL Example**:** `http://localhost:8889/admin/security/processRemoveUser.jsp?currentEditRealm=defaultRealm&userName=testurl`
* **processNewRole.jsp** 

  Description: Adds a new role.  
   URL Example: `http://localhost:8889/admin/security/processNewRole.jsp?currentEditRealm=defaultRealm&roleName=role1&parentRoles=NoneParent&description=TWD&jrs.privilege_publish_report=true`
* **processRemoveRole.jsp** 

  Description: Deletes a specific role.  
   URL Example**:** `http://localhost:8889/admin/security/processRemoveRole.jsp?currentEditRealm=defaultRealm&roleName=role1`

For details about the properties that would be included in the URL, see [Properties for adding and deleting users/roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009668881-Appendix-1-URL-Properties#User).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Working With Resources

* **jrs.get\_cat\_rpts\_new/jrs.get\_subnodes**

  Description: Gets all resource nodes (folder, catalog, report and result) of a folder.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_cat_rpts_new&jrs.path=RESOURCENODE`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_cat_rpts_new&jrs.path=/SampleReports`  
   Response: Resource nodes list.
* **jrs.get\_node\_prop**

  Description: Gets the properties of a resource node.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_node_prop&jrs.path=RESOURCENODE`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_node_prop&jrs.path=/SampleReports/SampleReports.cat`  
   Response: Resource node properties.
* **jrs.delete\_resource**

  Description: Deletes the resource node from the resource tree.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.delete_resource&jrs.path=RESOURCENODE`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.delete_resource&jrs.path=/SampleReports/InvoiceReport.cls`

* **jrs.get\_rpt\_param\_page** 

  Description: Gets the parameter page for specifying parameter values of a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rpt_param_page&jrs.catalog=CATALOG&jrs.report=REPORT`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_rpt_param_page&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/InvoiceReport.cls`
* **jrs.get\_rpt\_desc\_page**

  Description: Gets the Advanced Run page for choosing the result type of a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rpt_desc_page&jrs.catalog=CATALOG&jrs.report=REPORT`  
   URL Example:`http://localhost:8888/jrserver?jrs.cmd=jrs.get_rpt_desc_page&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/InvoiceReport.cls`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Schedule Tasks

* **jrs.submit\_schedule**

  Description: Creates a schedule task for a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.submit_schedule&jrs.catalog=CATALOG_NAME&jrs.report=REPORT_NAME&jrs.task_class=TASK_CLASS_NAME&jrs.launch_type=TIME_TYPE&jrs.param$PARAMETER_NAME=VALUE&jrs.uid=USER_ID&jrs.to_version=BOOLEAN&jrs.to_version_rst=BOOLEAN`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2006-01-01&jrs.param$p_EndDate=2007-12-31&jrs.uid=admin&jrs.to_version=true&jrs.to_version_rst=true&jrs.report=%2fSampleReports%2fCustomerAnalysis.cls`
* j**rs.get\_new\_schd\_page**

  Description: Opens the Schedule page to create a new schedule for a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_new_schd_page&jrs.catalog=CATALOG_NAME&jrs.report=REPORT_NAME`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_new_schd_page&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/CustomerAnalysis.cls`
* **jrs.get\_edit\_schd\_page**

  Description: Opens the Schedule page to edit an existing schedule task.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_edit_schd_page&jrs.task_id=TASK_ID`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_edit_schd_page&jrs.task_id=2003-12-11 11:09:16.455`
* **jrs.get\_schedules**

  Description: Gets the schedules list.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_schedules`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_schedules`
* **jrs.del\_schedule**

  Description: Deletes a schedule.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.del_schedule&jrs.task_id=TASK_ID`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.del_schedule&jrs.task_id=2003-12-11 11:09:16.455`
* **jrs.enable\_schedule** 

  Description: Enables a schedule.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.enable_schedule&jrs.task_id=TASK_ID`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.enable_schedule&jrs.task_id=2003-12-11 11:09:16.455`
* **jrs.disable\_schedule**

  Description: Disables a schedule.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.disable_schedule&jrs.task_id=TASK_ID`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.disable_schedule&jrs.task_id=2003-12-11 11:09:16.455`
* **jrs.get\_completed**

  Description: Gets the completed tasks list.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_completed`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_completed`
* **jrs.get\_active** 

  Description: Gets the active tasks list.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_active`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_active`
* **jrs.get\_ondemands**

  Description: Gets a list of reports running in background.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_ondemands`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_ondemands`  
   Response: Background run report list.
* **jrs.stop\_task**

  Description: Stops an active task.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.stop_task&jrs.task_id=TASK_ID`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.stop_task&jrs.task_id=2003-12-11 11:13:23.02`
* **jrs.del\_completed**

  Description: Deletes a completed task.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.del_completed&jrs.id=RECORD_ID`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.del_completed&jrs.id=1071119897006-154848108`  
   You need to invoke API to get RECORD\_ID. A demo called APIDemoPublishRpt.java in `<install_root>\help\samples\APIServer` shows how to get completed task record including RECORD\_ID.
* **jrs.del\_all\_completed**

  Description: Deletes all completed tasks.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.del_all_completed`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.del_all_completed`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Resource Versions

* **jrs.get\_cat\_vers**

  Description: Gets the version table of a catalog.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_cat_vers&jrs.catalog=CATALOG`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_cat_vers&jrs.catalog=/SampleReports/SampleReports.cat`
* **jrs.get\_rpt\_vers**

  Description: Gets the version table of a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rpt_vers&jrs.report=REPORT`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_rpt_vers&jrs.report=/SampleReports/InvoiceReport.cls`
* **jrs.get\_rst\_vers**

  Description: Gets the result version table of a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rst_vers&jrs.catalog=CATALOG&jrs.report=REPORT_SET`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_rst_vers&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/InvoiceReport.cls`
* **jrs.get\_rst\_doc\_vers**

  Description: Gets the result version table of a result document. The result document can be generated by advanced running or scheduling a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rst_doc_vers&jrs.result=RESULT`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_rst_doc_vers&jrs.result=/SampleReports/InvoiceReport`

* **jrs.get\_ver\_param**

  Description: Gets the parameter file of a report's result version.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.get_ver_param&jrs.version_id=VERSION_ID`  
   URL Example: `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/InvoiceReport.cls?jrs.cmd=jrs.get_ver_param&jrs.version_id=103`
* **jrs.get\_ver\_rst\_page** 

  Description: Gets a result version of the report from the version manager.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_ver_rst_page&jrs.file=FILE_NAME`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_ver_rst_page&jrs.file=1%5cLogi JReport_System_User327406359%5cInvoiceReport.rst`  
   Response: The result file from the version manager.
* **jrs.get\_ver\_rst**

  Description: Gets an HTML page for viewing a result version of a report with the ViewerApplet.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.get_ver_rst&jrs.file=FILE_NAME`  
   URL Example: `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/InvoiceReport.cls?jrs.cmd=jrs.get_ver_rst&jrs.file=1%5cLogi JReport_System_User327406359%5cInvoiceReport.rst`  
   Response: HTML page for viewing the result file with the ViewerApplet.
* **jrs.del\_rpt\_ver**

  Description: Deletes a version of a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.del_rpt_ver&jrs.version_id=VERSION_ID`  
   URL Example:  `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/InvoiceReport.cls?jrs.cmd=jrs.del_rpt_ver&jrs.version_id=103`

* **jrs.del\_rst\_ver**

  Description: Deletes a result version of a report.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.del_rst_ver&jrs.version_id=VERSION_ID`  
   URL Example:  `http://localhost:8888/jrserver/SampleReports/SampleReports.cat/InvoiceReport.cls?jrs.cmd=jrs.del_rst_ver&jrs.version_id=106`

* **jrs.del\_rstdoc\_ver**

  Description: Deletes a version of a result document.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.result=RESULT&jrs.cmd=jrs.del_rstdoc_ver&jrs.version_id=VERSION_ID`  
   URL Example:  `http://localhost:8888/jrserver?jrs.result=/SampleReports/InvoiceReport&jrs.cmd=jrs.del_rstdoc_ver&jrs.version_id=108`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Loading the Server Preferences Page

* **jrs.get\_preference\_page**

  Description: Gets an HTML page in order to change the user preference settings with a web browser.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_preference_page`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_preference_page`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Changing User Password

* **jrs.get\_change\_password\_page**

  Description: Gets an HTML page in order to change the password with a web browser.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.get_change_password_page`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.get_change_password_page`
* **jrs.change\_password** 

  Description: Changes the password for a user.  
   HTTP Method: POST  
   Form Action: `http://HOST:PORT/jrserver?jrs.cmd=jrs.change_password`  
   Content Type: application/x-www-form-urlencoded  
   Content: `jrs.cmd=jrs.change_password&jrs.uid=admin&jrs.password=CURRENT_PASSWORD&jrs.new_password=NEW_PASSWORD&jrs.confirm_new_password=NEW_PASSWORD`   
   Content Example: `jrs.cmd=jrs.change_password&jrs.uid=admin&jrs.password=ad&jrs.new_password=1234&jrs.confirm_new_password=1234`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logging In and Out of Logi JReport Server

* **jrs.logout** 

  Description: Logs out from the server.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.logout`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.logout`
* **jrs.login**

  Description: Logs onto the server from a login dialog with a web browser.  
   HTTP Method: GET/POST  
   URL Format: `http://HOST:PORT/jrserver?jrs.cmd=jrs.login`  
   URL Example: `http://localhost:8888/jrserver?jrs.cmd=jrs.login`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650442-Working-With-Page-Reports)
