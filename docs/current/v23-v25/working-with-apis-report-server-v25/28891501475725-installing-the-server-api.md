---
title: "Installing the Server API"
id: 28891501475725
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891501475725-Installing-the-Server-API
updated_at: 2026-02-26T02:11:01Z
source_host: docs-report.zendesk.com
---
# 
Installing the Server API 

This topic describes the library files of the Report Server API, and how to set the classpath environment variable to the local and remote libraries.

The Server API is installed at the same time when you install Report Server. After the installation, you will have the following library files.

- In <install_root>\lib:
    
- commons-logging-1.2.jar

- hsqldb-2.6.1.jar

- jakarta.servlet-4.0.4.jar

- JREngine.jar (local calls)

- JRESServlets.jar (local calls) 

- JRSRMI.jar (remote RMI calls) 

- log4j-core-2.17.2.jar

- log4j-api-2.17.2.jar

- quartz-2.3.2.jar

- sac-1.3.jar

- In <install_root>\derby\lib:
    
- derby.jar

- derbyclient.jar

- derbynet.jar

- derbytools.jar

Report stores the Server API classes in the archive file JRESServlets.jar.

After you install Report Designer, you can find the libraries for Report Server in <designer_install_root>\server\lib because Report Designer includes a Report Server for previewing reports. 

If you are calling the Server API directly in the same JVM as Report Server, you need to set the classpath environment variable to the local versions of the classes. Append the following jar files to your class path that compile and run applications which call the Server API:

<install_root>\lib\JRESServlets.jar;<install_root>\lib\JREngine.jar;<install_root>\lib\jakarta.servlet-api-4.0.4.jar;<install_root>\lib\hsqldb-2.6.1.jar;<install_root>\lib\log4j-core-2.17.2.jar;<install_root>\lib\log4j-api-2.17.2.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-2.3.2.jar;<install_root>\derby\lib\derby.jar;<install_root>\derby\lib\derbyclient.jar;<install_root>\derby\lib\derbynet.jar;<install_root>\derby\lib\derbytools.jar;

If you are calling the Server API using RMI from a different JVM or different server than where Report Server is running, you need to set the classpath environment variable to the remote libraries. Append the following jar files to your class path that compile and run applications which call the Server API:

<install_root>\lib\JRSRMI.jar;<install_root>\lib\jakarta.servlet-api-4.0.4.jar;<install_root>\lib\hsqldb-2.6.1.jar;<install_root>\lib\log4j-core-2.17.2.jar;<install_root>\lib\log4j-api-2.17.2.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\commons-logging-1.2.jar;<install_root>\lib\quartz-2.3.2.jar;

- If you are not using Derby as your server DBMS, you need to replace the Derby libraries with the JDBC driver for your DBMS system.

- If you want to export reports to the following formats, you should add the corresponding class package or jar with a valid path to the class path:
      
- To email or use the Email Notification function: jakarta.mail-1.6.7.jar.

- To FTP: commons-net-3.8.0.jar.

- To Excel: poi-5.2.2.jar.

- To Page Report Result: JRWebDesign.jar.

- 
In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see Statement on Log4j and Log4Net Vulnerabilities.
