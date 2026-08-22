---
title: "Logi JReport Server Guide v15 Server Reporthome Directory Overview"
id: 1500009648242
section: "Installing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648242-Logi-JReport-Server-Guide-v15-Server-Reporthome-Directory-Overview
updated_at: 2021-07-24T20:54:14Z
---

# Logi JReport Server Guide v15 Server Reporthome Directory Overview

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672981-Solving-Installation-Problems)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673001-Uninstalling-Logi-JReport-Server-Guide-v15-Server)

# Logi JReport Server Reporthome Directory Overview

This topic provides a general view of the directories in the Logi JReport Server installation root, including what they contain, what they are used for, and how to set their location if possible.

The following is a list of the server reporthome directories:

| Directory | Contents | Directory Location Configurability |
| --- | --- | --- |
| \_uninst | Files used for uninstalling Logi JReport Server. | Fixed. |
| bin | Command, configuration, and properties files. | Fixed. |
| db | Demo reports' database. | Fixed. |
| derby | The Derby program and database resources. | Fixed. |
| dynamicclasses | UDS jar/zip files. | See [Loading User Data Source Classes at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/1500009668681-Loading-User-Data-Source-Classes-at-Runtime) for details. |
| font | TTF font location for resources used on Logi JReport Server. | See [Customizing TTF Font Location for Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources) for details. |
| gisinfo | Report related Geographic Information files. | Fixed. |
| help | Help documents, Javadoc and sample code introducing the function, features and usage of Logi JReport. | Fixed. |
| history | Version files and parameter files. | See [Storage of versions on disk](https://devnet.logianalytics.com/hc/en-us/articles/1500009673801-Advanced-Version-Topics#Storage) for details. |
| Logi JReports | Demo reports. When scheduling a task to disk, the directory refers to the destination root of the server resource tree. | Fixed. |
| lib | Library files required by Logi JReport runtime. | Fixed. |
| logs | Log files. | See [Configuring Logs](https://devnet.logianalytics.com/hc/en-us/articles/1500009644542-Configuring-Logs) for more information. |
| ntservice | Files for C program and for writing a Windows NT-service to run Logi JReport Server. | Fixed. |
| prestart | Reads customized configuration for launching Logi JReport Console and Administration pages from the Start menu. | Fixed. |
| profiling | Profiling related files. | Fixed. |
| properties | Default location for Logi JReport Server realm database. | The directory location can be specified using the URL option in the Configuration tab on the Logi JReport Administration > Data > Realm DB page. |
| public\_html | Standalone web app folder. | Fixed. |
| realm | Realm files. | Fixed. No sub folders should be created in the realm directory because it may create a realm when the server is started. |
| resources | Language packages for specifying Logi JReport Server UI language. | Fixed. |
| scratchdir | Output files of compiled JSPs. | The directory location can be specified by the servlet.jspservlet.initArgs property in the servlet.properties file in `<install_root>\bin`. |
| script\_files | Script files for creating and deleting system database tables. | Fixed. |
| style | CSS style files and style group files. | The directory location can be specified by stylePath in the report.ini file in `<install_root>\bin`. |
| temp | Server temp result files and engine temp files | Fixed for the server temp result files. For the engine temp files, the directory location can be specified by tempPath in the report.ini file in `<install_root>\bin`. |
| templates | Templates for web reports. | Fixed. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672981-Solving-Installation-Problems)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673001-Uninstalling-Logi-JReport-Server-Guide-v15-Server)
