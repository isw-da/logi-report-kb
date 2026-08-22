---
title: "Setting Up the Reporting Environment"
id: 1500009749921
section: "Start Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749921-Setting-Up-the-Reporting-Environment
updated_at: 2021-07-25T07:19:00Z
---

# Setting Up the Reporting Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722922-Starting-Logi-Report-Server-v17)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749961-Running-as-a-Standalone-Server)

# Setting Up the Reporting Environment

Now that you have installed Logi Report Server, you can start it. However, it is better to first check the reporting environment to see whether you have published the reports including the catalog files, added the necessary class paths, and set up the data sources.

**Report publishing & creation**

The separation of the report file and the data is powerful. It facilitates easy re-use of the report's layout. Report files built with Logi Report Designer can then be published to Logi Report Server for running in the thin-client/server mode. Today, computing is a service-based model in which web based applications are rapidly replacing monolithic fat-client hosted and maintained software applications. Logi Report Server is a high performance server for running reports on demand or unattended on a scheduled basis. In this environment, thousands of clients may view, print and generate new reports.

Logi Report Server has its own resource tree with each node mapping to a folder or file in your physical drive. So when publishing report files to the server, it is recommended that you check:

* Whether the report files reside somewhere in the server machine.
* Whether the files are mapped in the resource tree.
* That not only the report files, but also the catalog files (including the .fml file) exist and are in the same directory. In addition, one directory can only contain one catalog. However, it can contain many report files which use that catalog.

**Data sources**

You may have your own catalogs and reports that you developed, and want them to be run and be distributed by Logi Report Server. In order to do this, the data sources used by your catalogs must be correctly set to the runtime environment of Logi Report Server.

Append the class path of your user class files to the first item of the classpath set in your batch file or command line that starts Logi Report Server or in setenv.bat/setenv.sh in the ADDCLASSPATH variable. If you are using Logi Report Server embedded in an application server, add your user class files to the WAR file used to deploy Logi Report Server.

**Additional class paths**

If your reports reference any external classes, you will need to add them to the classpath option in the batch file and command line that starts Logi Report Server. For example, if your reports contain user defined objects (UDO) or user defined formula functions, do not forget to add them to the class path or to the WAR file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722922-Starting-Logi-Report-Server-v17)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749961-Running-as-a-Standalone-Server)
