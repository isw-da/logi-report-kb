---
title: "Installing the Server API"
id: 1500009718362
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718362-Installing-the-Server-API
updated_at: 2021-07-25T07:20:25Z
---

# Installing the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744181-Java-API-for-an-Application)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744221-Using-the-Server-API)

# Installing the Server API

This topic describes the library files of the Logi Report Server API, and how to set the classpath environment variable to the local and remote libraries.

The Server API is installed at the same time when you install Logi Report Server. After the installation, you will have the following library files.

* In `<install_root>\lib`:
  + commons-logging-1.2.jar
  + hsqldb-2.5.0.jar
  + jakarta.servlet-api-4.0.3.jar
  + JREngine.jar (local calls)
  + JRESServlets.jar (local calls)
  + JRSRMI.jar (remote RMI calls)
  + log4j-core-2.12.1.jar
  + log4j-api-2.12.1.jar
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

`<install_root>\lib\JRESServlets.jar; <install_root>\lib\JREngine.jar; <install_root>\lib\jakarta.servlet-api-4.0.3.jar; <install_root>\lib\hsqldb-2.5.0.jar; <install_root>\lib\log4j-core-2.12.1.jar; <install_root>\lib\log4j-api-2.12.1.jar; <install_root>\lib\sac-1.3.jar; <install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-2.3.2.jar; <install_root>\derby\lib\derby.jar; <install_root>\derby\lib\derbyclient.jar; <install_root>\derby\lib\derbynet.jar; <install_root>\derby\lib\derbytools.jar;`

If you are calling the Server API using RMI from a different JVM or different server than where Logi Report Server is running, you need to set the classpath environment variable to the remote libraries. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRSRMI.jar; <install_root>\lib\jakarta.servlet-api-4.0.3.jar; <install_root>\lib\hsqldb-2.5.0.jar; <install_root>\lib\log4j-core-2.12.1.jar; <install_root>\lib\log4j-api-2.12.1.jar； <install_root>\lib\sac-1.3.jar; <install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-2.3.2.jar;`

**Notes:**

* If you are not using Derby as your server DBMS, you need to replace the Derby libraries with the JDBC driver for your DBMS system.
* If you want to export reports to the following formats, you should add the corresponding class package or jar with a valid path to the class path:
  + To e-mail or use the E-mail Notification function: jakarta.mail-1.6.4.jar.
  + To FTP: commons-net-3.6.jar.
  + To Excel: poi-4.1.1.jar.
  + To Page Report Result: JRWebDesign.jar.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744181-Java-API-for-an-Application)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744221-Using-the-Server-API)
