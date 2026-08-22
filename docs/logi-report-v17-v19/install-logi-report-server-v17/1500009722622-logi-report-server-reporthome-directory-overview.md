---
title: "Logi Report Server Reporthome Directory Overview"
id: 1500009722622
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722622-Logi-Report-Server-Reporthome-Directory-Overview
updated_at: 2021-07-25T07:19:07Z
---

# Logi Report Server Reporthome Directory Overview

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749621-Installing-Updates-Service-Packs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749641-Upgrading-Logi-Report-Server)

# Logi Report Server Reporthome Directory Overview

This topic provides a general view of the directories in the Logi Report Server installation root, including what they contain, what they are used for, and how to set their location if possible.

The following is a list of the server reporthome directories:

| Directory | Contents | Directory Location Configurability |
| --- | --- | --- |
| \_uninst | Files used for uninstalling Logi Report Server. | Fixed. |
| bin | Command, configuration, and properties files. | Fixed. |
| db | Demo reports' database. | Fixed. |
| derby | The Derby program and database resources. | Fixed. |
| dynamicclasses | UDS jar/zip files. | See [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009744381-Loading-User-Data-Source-Classes-at-Runtime) for details. |
| font | TTF font location for resources used on Logi Report Server. | See [Customizing TTF Font Location for Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009723102-Customizing-TTF-Font-Location-for-Resources) for details. |
| gisinfo | Report related Geographic Information files. | Fixed. |
| help | Help documents, API Javadoc and sample code introducing the function, features and usage of Logi Report. | Fixed. |
| history | Version files and parameter files. | See [Storage of Versions on Disk](https://devnet.logianalytics.com/hc/en-us/articles/1500009723262-Advanced-Version-Topics#Storage) for details. |
| jreports | Demo reports. When scheduling a task to disk, the directory refers to the destination root of the server resource tree. | Fixed. |
| lib | Library files required by Logi Report runtime. | Fixed. |
| logs | Log files. | See [Configuring Logs](https://devnet.logianalytics.com/hc/en-us/articles/1500009744901-Configuring-Logs) for more information. |
| ntservice | Files for C program and for writing a Windows NT-service to run Logi Report Server. | Fixed. |
| prestart | Reads customized configuration for launching the Logi Report Server console from the Start menu. | Fixed. |
| profiling | Profiling related files. | Fixed. |
| properties | Default location for Logi Report Server realm database. | The directory location can be specified using the URL option in the Administration > Configuration > Server DB > Realm DB > Configuration tab in the Logi Report Server console. |
| public\_html | Standalone web app folder. | Fixed. |
| realm | Realm files. | Fixed. No subfolders should be created in the realm directory because it may create a realm when the server is started. |
| resources | Language packages for specifying Logi Report Server UI language. | Fixed. |
| scratchdir | Output files of compiled JSPs. | The directory location can be specified by the servlet.jspservlet.initArgs property in the servlet.properties file in `<install_root>\bin`. |
| script\_files | Script files for creating and deleting system database tables. | Fixed. |
| style | CSS style files and style group files. | The directory location can be specified by stylePath in the report.ini file in `<install_root>\bin`. |
| temp | Server temp result files and engine temp files | Fixed for the server temp result files. For the engine temp files, the directory location can be specified by tempPath in the report.ini file in `<install_root>\bin`. |
| templates | Templates for web reports. | Fixed. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749621-Installing-Updates-Service-Packs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749641-Upgrading-Logi-Report-Server)
