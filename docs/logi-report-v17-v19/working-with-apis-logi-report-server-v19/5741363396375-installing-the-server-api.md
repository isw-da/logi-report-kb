---
title: "Installing the Server API"
id: 5741363396375
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741363396375-Installing-the-Server-API
updated_at: 2022-10-31T17:15:46Z
---

# Installing the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394666391-Java-API-for-an-Application)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741394799255-Using-the-Server-API)

# Installing the Server API

This topic describes the library files of the Logi Report Server API, and how to set the classpath environment variable to the local and remote libraries.

The Server API is installed at the same time when you install Logi Report Server. After the installation, you will have the following library files.

* In `<install_root>\lib`:
  + commons-logging-1.2.jar
  + hsqldb-2.6.1.jar
  + jakarta.servlet-4.0.4.jar
  + JREngine.jar (local calls)
  + JRESServlets.jar (local calls)
  + JRSRMI.jar (remote RMI calls)
  + log4j-core-2.17.2.jar
  + log4j-api-2.17.2.jar
  + quartz-2.3.2.jar
  + sac-1.3.jar
* In `<install_root>\derby\lib`:
  + derby.jar
  + derbyclient.jar
  + derbynet.jar
  + derbytools.jar

Logi Report stores the Server API classes in the archive file **JRESServlets.jar**.

After you install Logi Report Designer, you can find the libraries for Logi Report Server in `<designer_install_root>\server\lib` because Logi Report Designer includes a Logi Report Server for previewing reports.

If you are calling the Server API directly in the same JVM as Logi Report Server, you need to set the classpath environment variable to the local versions of the classes. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRESServlets.jar;<install_root>\lib\JREngine.jar;<install_root>\lib\jakarta.servlet-api-4.0.4.jar;<install_root>\lib\hsqldb-2.6.1.jar;<install_root>\lib\log4j-core-2.17.2.jar;<install_root>\lib\log4j-api-2.17.2.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-2.3.2.jar;<install_root>\derby\lib\derby.jar;<install_root>\derby\lib\derbyclient.jar;<install_root>\derby\lib\derbynet.jar;<install_root>\derby\lib\derbytools.jar;`

If you are calling the Server API using RMI from a different JVM or different server than where Logi Report Server is running, you need to set the classpath environment variable to the remote libraries. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRSRMI.jar;<install_root>\lib\jakarta.servlet-api-4.0.4.jar;<install_root>\lib\hsqldb-2.6.1.jar;<install_root>\lib\log4j-core-2.17.2.jar;<install_root>\lib\log4j-api-2.17.2.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\commons-logging-1.2.jar;<install_root>\lib\quartz-2.3.2.jar;`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* If you are not using Derby as your server DBMS, you need to replace the Derby libraries with the JDBC driver for your DBMS system.
* If you want to export reports to the following formats, you should add the corresponding class package or jar with a valid path to the class path:
  + To email or use the Email Notification function: jakarta.mail-1.6.7.jar.
  + To FTP: commons-net-3.8.0.jar.
  + To Excel: poi-5.2.2.jar.
  + To Page Report Result: JRWebDesign.jar.
* ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif)In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4net-Vulnerabilities "Read this article to mitigate or remove a Log4j vulnerability from your version of Logi Report.").

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394666391-Java-API-for-an-Application)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741394799255-Using-the-Server-API)
