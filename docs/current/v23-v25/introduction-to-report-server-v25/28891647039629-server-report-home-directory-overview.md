---
title: " Server Report Home Directory Overview"
id: 28891647039629
section: "Introduction to Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891647039629--Server-Report-Home-Directory-Overview
updated_at: 2026-02-26T02:13:14Z
source_host: docs-report.zendesk.com
---
# 
Report Server Report Home Directory Overview 

This topic describes the directories in the Report Server installation root, including what they contain, what they are used for, and how to set their location. 

The following table lists the server report home directories:

| Directory | Contents | Directory Location Configurability |
| --- | --- | --- |
| _uninst | Files for uninstalling Report Server. | Fixed. |
| bin | Command, configuration, and properties files. | Fixed. |
| db | Demo reports' database. | Fixed. |
| derby | The Derby program and database resources. | Fixed. |
| dynamicclasses | UDS jar/zip files. | For more information, see Loading User Data Source Classes at Runtime. |
| font | TTF font location for resources on Report Server. | For more information, see Customizing TTF Font Location for Resources. |
| gisinfo | Report related Geographic Information files. | Fixed. |
| help | Help documentations, API Javadoc, and sample code introducing the functions, features, and usage of Report. | Fixed. |
| history | Version files and parameter files. | For more information, see Storage of Versions on Disk. |
| jreports | Demo reports. When you schedule a task to disk, this directory is the destination root of the server resource tree. | Fixed. |
| lib | Library files that Report requires at runtime. | Fixed. |
| logs | Log files. | For more information, see Configuring Report Logging System. |
| ntservice | Files for C program and for writing a Windows NT-service to run Report Server. | Fixed. |
| prestart | File that reads customized configuration for launching the Server Console from the Start menu. | Fixed. |
| profiling | Profiling related files. | Fixed. |
| properties | Default location for Report Server realm database. | You can specify the directory location using the URL option in the Administration > Configuration > Server DB > Realm DB > Configuration tab on the Server Console. |
| public_html | Standalone web app folder. | Fixed. |
| realm | Realm files. | Fixed. You should not create subfolders in the realm directory because Server may create a realm when it starts. |
| resources | Language packages for specifying Report Server UI language. | Fixed. |
| scratchdir | Output files of compiled JSPs. | You can specify the directory location by the servlet.jspservlet.initArgs property in the servlet.properties file in \bin. |
| script_files | Script files for creating and deleting system database tables. | Fixed. |
| style | CSS style files and style group files. | You can specify the directory location by stylePath in the report.ini file in \bin. |
| temp | Server temp report files and engine temp files. | Fixed for the server temp report files. For the engine temp files, you can specify the directory location by tempPath in the report.ini file in \bin. |
| templates | Templates for web reports. | Fixed. |
