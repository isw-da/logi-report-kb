---
title: "Working with  Server via URL"
id: 28891698016909
section: "Working on Report Server via URL Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891698016909-Working-with-Server-via-URL
updated_at: 2026-02-26T02:14:06Z
source_host: docs-report.zendesk.com
---
# 
Working with Report Server via URL

You can use URL to  add and delete users/roles/groups in the server security system, delete a resource node from the server resource tree, and get the version table of a resource. This topic describes how you can work with Report Server via URL.

For more information, see URL Properties for Running, Scheduling, and Viewing Reports via URL.

This topic contains the following sections:

- Viewing Reports via URL
                

- Specifying the Application Language via URL
                

- Adding and Deleting Users/Roles/Groups via URL
                

- Working with Resources via URL
                

- Managing Scheduled Tasks via URL
                

- Managing Resource Versions via URL
                

- Loading the Server Preferences Page via URL
                

- Changing User Password via URL
                

- Signing in and out of Report Server via URL
                

## 
Viewing Reports via URL

You can view the reports, which Server generated when advanced running or scheduling publish reports to the versioning system, via URL by either of the following two ways.

- 
Using JSP
- 
For the Page Report Result type (RSD) 
You can view page report results in Page Report Studio by running runReport.jsp. The URL can call one of the following three groups of properties:
        
- 
jrs.resource_path and jrs.file for specifying a folder path in the server resource tree and a file name separately
URL Example: http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.resource_path=%2fUSERFOLDERPATH%2fadmin&jrs.file=1980996366.rsd

- 
jrs.file for specifying a file path on the drive
URL Example: http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.file=D:\LogiReport\report1.rst.rsd

- 
jrs.rst_version together with one of the three properties: jrs.version_id, jrs.report, and jrs.result, for specifying a result version in the server resource tree. Report will search for the three properties one by one starting from the first to the third until it finds one.URL Example: http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.rst_version=1&jrs.report=%2fSampleReports%2fPayroll Report.cls&type=rstfile&jrs.path=%2fSampleReports%2fPayroll Report.cls&jrs.version_id=257

- 
For other report types
To view the report files of other types such as PDF and HTML, you need to use viewVersion.jsp.
URL Example: http://localhost:8888/jinfonet/viewVersion.jsp?jrs.cmd=jrs.view_ver_rst&jrs.result_type=2&jrs.version_number=1&jrs.ver_suff=.rst&jrs.result=%2fUSERFOLDERPATH%2fadmin%2fBanded_Link&jrs.path=%2fUSERFOLDERPATH%2fadmin%2fBanded_Link

- 
Using servletURL Format: http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.view_ver_rst&jrs.hist_file=RESULT_VERSION_FILE_NAME
URL Example: http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Payroll Report.cls?jrs.cmd=jrs.view_ver_rst&jrs.hist_file=1%2fadmin567625353%2f2109098280.pdf

For more information, see URL Properties for Viewing Reports.

## 
Specifying the Application Language via URL

When accessing the Server Console or Page Report Studio via URL, you can control the UI language by setting the property jrs.language. The format of the URL is:

http://HOST:PORT/CONTEXT/PAGE?PROPERTY=VALUE&jrs.language=LANGUAGE_NAME

The value of jrs.language should be the same as the language package folder name in the <server_install_root>\resources\server\languages directory and be lower-case letters.

The following are two examples:

- URL for accessing the Server Console:
    http://127.0.0.1:8888/jinfonet/index.jsp?jrs.language=zh-cn

- URL for opening a page report in Page Report Studio:
    http://127.0.0.1:8888/webos/app/pagestudio/run.jsp?jrs.report=/SampleReports/Payroll Report.cls&jrs.catalog=/SampleReports/SampleReports.cat&jrs.cat_version=1&jrs.path=/SampleReports/Payroll Report.cls&jrs.language=zh-cn

## 
Adding and Deleting Users/Roles/Groups via URL

You need to be an administrator to run the following JSPs to add or remove users/roles/groups to the security system on Report Server. However, before doing this, you should have signed in to the Server Console to run the URL successfully.

- 
processNewUser.jspDescription: Add a new user.
URL Example: http://localhost:8888/admin/security/processNewUser.jsp?currentEditRealm=defaultRealm&user=Dean&fullName=Dean%20Black&description=Product%20Manager%20&email=Dean@jinfonet.com&password=123456&confirmPassword=123456&passwordLife=expire&expireTime=25&enableBlank=blank&minLength=6&jrs.privilege_access_advanced_properties=true

- 
processRemoveUser.jspDescription: Delete a specific user.
URL Example: http://localhost:8888/admin/security/processRemoveUser.jsp?currentEditRealm=defaultRealm&userName=Dean

- 
processNewRole.jsp Description: Add a new role.
URL Example: http://localhost:8888/admin/security/processNewRole.jsp?currentEditRealm=defaultRealm&roleName=role1&parentRoles=NoneParent&description=TWD&jrs.privilege_publish_report=true

- 
processRemoveRole.jsp Description: Delete a specific role.
URL Example: http://localhost:8888/admin/security/processRemoveRole.jsp?currentEditRealm=defaultRealm&roleName=role1

- 
processNewGroup.jsp Description: Add a new group.
URL Example: http://localhost:8888/admin/security/processNewGroup.jsp?currentEditRealm=defaultRealm&groupName=group1&parentGroups=NoneParent&description=DevelopmentGroup&jrs.privilege_publish_report=true&jrs.privilege_access_advanced_properties=true

- 
processRemoveGroup.jsp Description: Delete a specific group.
URL Example: http://localhost:8888/admin/security/processRemoveGroup.jsp?currentEditRealm=defaultRealm&groupName=group1

For more information, see URL Properties for Adding and Deleting Users/Roles/Groups.

## 
Working with Resources via URL

- 
jrs.get_cat_rpts_new/jrs.get_subnodesDescription: Get all resource nodes (folder, catalog, report, and result) of a folder.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_cat_rpts_new&jrs.path=RESOURCENODE
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_cat_rpts_new&jrs.path=/SampleReports
Response: Resource nodes list.

- 
jrs.get_node_propDescription: Get the properties of a resource node.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_node_prop&jrs.path=RESOURCENODE
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_node_prop&jrs.path=/SampleReports/SampleReports.cat
Response: Resource node properties.

- 
jrs.delete_resourceDescription: Delete the resource node from the resource tree.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.delete_resource&jrs.path=RESOURCENODE
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.delete_resource&jrs.path=/SampleReports/Payroll Report.cls

- 
jrs.get_rpt_param_page Description: Get the parameter page for specifying parameter values of a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rpt_param_page&jrs.catalog=CATALOG&jrs.report=REPORT
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_rpt_param_page&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Shipment Status Report.wls

- 
jrs.get_rpt_desc_pageDescription: Get the Advanced Run page for choosing the report type.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rpt_desc_page&jrs.catalog=CATALOG&jrs.report=REPORT
URL Example:http://localhost:8888/jrserver?jrs.cmd=jrs.get_rpt_desc_page&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Payroll Report.cls

## 
Managing Scheduled Tasks via URL

- 
jrs.submit_scheduleDescription: Create a schedule task for a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.submit_schedule&jrs.catalog=CATALOG_NAME&jrs.report=REPORT_NAME&jrs.task_class=TASK_CLASS_NAME&jrs.launch_type=TIME_TYPE&jrs.param$PARAMETER_NAME=VALUE&jrs.uid=USER_ID&jrs.to_version=BOOLEAN&jrs.to_version_rst=BOOLEAN
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.submit_schedule&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.task_class=jet.server.schedule.jrtasks.PublishRptTask&jrs.launch_type=0&jrs.param$P_StartDate=2016-01-01&jrs.param$p_EndDate=2017-12-31&jrs.uid=admin&jrs.to_version=true&jrs.to_version_rst=true&jrs.report=%2fSampleReports%2fABC.cls

- jrs.get_new_schd_pageDescription: Open the Schedule page to create a new schedule for a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_new_schd_page&jrs.catalog=CATALOG_NAME&jrs.report=REPORT_NAME
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_new_schd_page&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information List.cls

- 
jrs.get_edit_schd_pageDescription: Open the Schedule page to edit an existing schedule task.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_edit_schd_page&jrs.task_id=TASK_ID
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_edit_schd_page&jrs.task_id=2003-12-11 11:09:16.455

- 
jrs.get_schedulesDescription: Get the schedule tasks list.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_schedules
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_schedules

- 
jrs.del_scheduleDescription: Delete a schedule task.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.del_schedule&jrs.task_id=TASK_ID
 URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.del_schedule&jrs.task_id=2003-12-11 11:09:16.455

- 
jrs.enable_schedule Description: Enable a schedule task.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.enable_schedule&jrs.task_id=TASK_ID
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.enable_schedule&jrs.task_id=2003-12-11 11:09:16.455

- 
jrs.disable_scheduleDescription: Disable a schedule task.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.disable_schedule&jrs.task_id=TASK_ID
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.disable_schedule&jrs.task_id=2003-12-11 11:09:16.455

- 
jrs.get_completedDescription: Get the completed tasks list.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_completed
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_completed

- 
jrs.get_active Description: Get the active tasks list.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_active
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_active

- 
jrs.get_ondemandsDescription: Get a list of reports running in the background.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_ondemands
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_ondemands
Response: The list of reports running in the background.

- 
jrs.stop_taskDescription: Stop an active task.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.stop_task&jrs.task_id=TASK_ID
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.stop_task&jrs.task_id=2003-12-11 11:13:23.02

- 
jrs.del_completedDescription: Delete a completed task.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.del_completed&jrs.id=RECORD_ID
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.del_completed&jrs.id=1071119897006-154848108
You need to invoke API to get RECORD_ID. A demo called APIDemoPublishRpt.java in <install_root>\help\samples\APIServer shows how to get completed task record including RECORD_ID.

- 
jrs.del_all_completedDescription: Delete all completed tasks.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.del_all_completed
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.del_all_completed

## 
Managing Resource Versions via URL

- 
jrs.get_cat_versDescription: Get the version table of a catalog.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_cat_vers&jrs.catalog=CATALOG
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_cat_vers&jrs.catalog=/SampleReports/SampleReports.cat

- 
jrs.get_rpt_versDescription: Get the version table of a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rpt_vers&jrs.report=REPORT
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_rpt_vers&jrs.report=/SampleReports/Payroll Report.cls

- 
jrs.get_rst_versDescription: Get the version table of a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rst_vers&jrs.catalog=CATALOG&jrs.report=REPORT_SET
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_rst_vers&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Payroll Report.cls

- 
jrs.get_rst_doc_versDescription: Get the version table of a result document. The result document comes from advanced running or scheduling a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_rst_doc_vers&jrs.result=RESULT
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_rst_doc_vers&jrs.result=/SampleReports/Payroll Report

- 
jrs.get_ver_paramDescription: Get the parameter file of a report version.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.get_ver_param&jrs.version_id=VERSION_ID
URL Example: http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Shipment Status Report.wls?jrs.cmd=jrs.get_ver_param&jrs.version_id=103

- 
jrs.get_ver_rst_page Description: Get a version of a report from the version manager.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_ver_rst_page&jrs.file=FILE_NAME
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_ver_rst_page&jrs.file=1%5cReport_System_User327406359%5cPayroll Report.rst
Response: The report file from the version manager.

- 
jrs.get_ver_rstDescription: Get an HTML page for viewing a report version with the ViewerApplet.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.get_ver_rst&jrs.file=FILE_NAME
URL Example: http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Payroll Report.cls?jrs.cmd=jrs.get_ver_rst&jrs.file=1%5cReport_System_User327406359%5cPayroll Report.rst
Response: HTML page for viewing the report file with the ViewerApplet.

- 
jrs.del_rpt_verDescription: Delete a version of a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.del_rpt_ver&jrs.version_id=VERSION_ID
URL Example:  http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Payroll Report.cls?jrs.cmd=jrs.del_rpt_ver&jrs.version_id=103

- 
jrs.del_rst_verDescription: Delete a version of a report.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver/REPORT?jrs.cmd=jrs.del_rst_ver&jrs.version_id=VERSION_ID
URL Example:  http://localhost:8888/jrserver/SampleReports/SampleReports.cat/Payroll Report.cls?jrs.cmd=jrs.del_rst_ver&jrs.version_id=106

- 
jrs.del_rstdoc_verDescription: Delete a version of a result document.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.result=RESULT&jrs.cmd=jrs.del_rstdoc_ver&jrs.version_id=VERSION_ID
URL Example:  http://localhost:8888/jrserver?jrs.result=/SampleReports/Payroll Report&jrs.cmd=jrs.del_rstdoc_ver&jrs.version_id=108

## 
Loading the Server Preferences Page via URL

- 
jrs.get_preference_pageDescription: Get an HTML page to change the user preference settings with a web browser.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_preference_page
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_preference_page

## 
Changing User Password via URL

- 
jrs.get_change_password_pageDescription: Get an HTML page to change the password with a web browser.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.get_change_password_page
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.get_change_password_page

- 
jrs.change_password Description: Change the password of a user.
HTTP Method: POST
Form Action: http://HOST:PORT/jrserver?jrs.cmd=jrs.change_password
Content Type: application/x-www-form-urlencoded
Content: jrs.cmd=jrs.change_password&jrs.uid=admin&jrs.password=CURRENT_PASSWORD&jrs.new_password=NEW_PASSWORD&jrs.confirm_new_password=NEW_PASSWORD
Content Example: jrs.cmd=jrs.change_password&jrs.uid=admin&jrs.password=ad&jrs.new_password=1234&jrs.confirm_new_password=1234

## 
Signing in and out of Report Server via URL

- 
jrs.loginDescription: Sign into the server from a signing in dialog box with a web browser.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.login
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.login

- 
jrs.logout Description: Sign out of the server.
HTTP Method: GET/POST
URL Format: http://HOST:PORT/jrserver?jrs.cmd=jrs.logout
URL Example: http://localhost:8888/jrserver?jrs.cmd=jrs.logout
