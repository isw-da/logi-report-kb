---
title: " Server Report Home Directory Overview"
id: 5741467275543
section: "Introduction to Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741467275543--Server-Report-Home-Directory-Overview
updated_at: 2022-10-31T17:17:51Z
---

#  Server Report Home Directory Overview

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741437384727-Installing-Server-Service-Packs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741460743831-Upgrading-Logi-Report-Server)

# Logi Report Server Report Home Directory Overview

This topic describes the directories in the Logi Report Server installation root, including what they contain, what they are used for, and how to set their location.

The following table lists the server report home directories:

| Directory | Contents | Directory Location Configurability |
| --- | --- | --- |
| \_uninst | Files for uninstalling Logi Report Server. | Fixed. |
| bin | Command, configuration, and properties files. | Fixed. |
| db | Demo reports' database. | Fixed. |
| derby | The Derby program and database resources. | Fixed. |
| dynamicclasses | UDS jar/zip files. | For more information, see [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/5741400384407-Loading-User-Data-Source-Classes-at-Runtime). |
| font | TTF font location for resources on Logi Report Server. | For more information, see [Customizing TTF Font Location for Resources](https://devnet.logianalytics.com/hc/en-us/articles/5741453460887-Customizing-TTF-Font-Location-for-Resources). |
| gisinfo | Report related Geographic Information files. | Fixed. |
| help | Help documentations, API Javadoc, and sample code introducing the functions, features, and usage of Logi Report. | Fixed. |
| history | Version files and parameter files. | For more information, see [Storage of Versions on Disk](https://devnet.logianalytics.com/hc/en-us/articles/5741462230423--Advanced-Version-Topics-About-Version-Structure-and-Storage#Storage). |
| jreports | Demo reports. When you schedule a task to disk, this directory is the destination root of the server resource tree. | Fixed. |
| lib | Library files that Logi Report requires at runtime. | Fixed. |
| logs | Log files. | For more information, see [Configuring Logi Report Logging System](https://devnet.logianalytics.com/hc/en-us/articles/5741364633239-Configuring-Logi-Report-Logging-System). |
| ntservice | Files for C program and for writing a Windows NT-service to run Logi Report Server. | Fixed. |
| prestart | File that reads customized configuration for launching the Server Console from the Start menu. | Fixed. |
| profiling | Profiling related files. | Fixed. |
| properties | Default location for Logi Report Server realm database. | You can specify the directory location using the URL option in the Administration > Configuration > Server DB > Realm DB > Configuration tab on the Server Console. |
| public\_html | Standalone web app folder. | Fixed. |
| realm | Realm files. | Fixed. You should not create subfolders in the realm directory because Server may create a realm when it starts. |
| resources | Language packages for specifying Logi Report Server UI language. | Fixed. |
| scratchdir | Output files of compiled JSPs. | You can specify the directory location by the **servlet.jspservlet.initArgs** property in the servlet.properties file in `<install_root>\bin`. |
| script\_files | Script files for creating and deleting system database tables. | Fixed. |
| style | CSS style files and style group files. | You can specify the directory location by **stylePath** in the report.ini file in `<install_root>\bin`. |
| temp | Server temp report files and engine temp files. | Fixed for the server temp report files. For the engine temp files, you can specify the directory location by **tempPath** in the report.ini file in `<install_root>\bin`. |
| templates | Templates for web reports. | Fixed. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741437384727-Installing-Server-Service-Packs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741460743831-Upgrading-Logi-Report-Server)
