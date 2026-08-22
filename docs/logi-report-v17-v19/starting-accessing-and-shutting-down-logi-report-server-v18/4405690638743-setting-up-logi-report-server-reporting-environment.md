---
title: "Setting Up Logi Report Server Reporting Environment"
id: 4405690638743
section: "Starting, Accessing, and Shutting Down Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690638743-Setting-Up-Logi-Report-Server-Reporting-Environment
updated_at: 2022-01-27T07:59:37Z
---

# Setting Up Logi Report Server Reporting Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683917463-Starting-Accessing-and-Shutting-Down-Logi-Report-Server-v18)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690640535-Running-Logi-Report-Server-as-a-Standalone-Server)

# Setting Up Logi Report Server Reporting Environment

Now that you have installed Logi Report Server, you can start it. However, it is better to first check the reporting environment. This topic describes how you can publish report and catalog files, add the necessary class paths, and set up the data sources.

**Report publishing & creation**

The separation of a report file and its data is powerful. It facilitates easy re-use of the report's layout. You can build report files using Logi Report Designer and then publish them to Logi Report Server for running in the thin-client/server mode. Today, computing is a service-based model in which web-based applications are rapidly replacing monolithic fat-client hosted and maintained software applications. Logi Report Server is a high-performance server for running reports on demand or unattended on a scheduled basis. In this environment, thousands of clients may view, print, and generate new reports.

Logi Report Server has its own resource tree with each node mapping to a folder or file in your physical drive. So, when publishing report files to the server, you should check:

* Whether the report files reside somewhere in the server computer.
* Whether the files are mapped in the resource tree.
* That not only the report files, but also the catalog files (including the .fml file) exist and are in the same directory. In addition, one directory can only contain one catalog. However, it can contain many report files that use the catalog.

**Data sources**

You may have your own catalogs and reports that you developed, and want them to run and distribute in Logi Report Server. In order to do this, you must correctly set the data sources that your catalogs use to the runtime environment of Logi Report Server.

Append the class path of your user class files to the first item of the classpath in your batch file or command line that starts Logi Report Server or in setenv.bat/setenv.sh in the ADDCLASSPATH variable. If you are using Logi Report Server embedded in an application server, add your user class files to the WAR file used to deploy Logi Report Server.

**Additional class paths**

If your reports reference any external classes, you need to add them to the classpath option in the batch file and command line that starts Logi Report Server. For example, if your reports contain user defined objects (UDO) or user defined formula functions, do not forget to add them to the class path or to the WAR file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683917463-Starting-Accessing-and-Shutting-Down-Logi-Report-Server-v18)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690640535-Running-Logi-Report-Server-as-a-Standalone-Server)
