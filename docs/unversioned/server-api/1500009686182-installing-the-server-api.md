---
title: "Installing the Server API"
id: 1500009686182
section: "Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686182-Installing-the-Server-API
updated_at: 2021-11-03T06:58:36Z
---

# Installing the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711901-Java-API-for-an-Application)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686222-Using-the-Server-API)

# Installing the Server API

When you install Logi JReport Server, Logi JReport Server API is also installed at the same time. After you install Logi JReport Server, you will have the files listed here.

* In  `<install_root>\lib`:
  + JRESServlets.jar (local calls)
  + JREngine.jar (local calls)
  + JRSRMI.jar (remote RMI calls)
  + jakarta.servlet-api-4.0.2.jar
  + hsqldb-2.4.0.jar
  + log4j-core-2.9.1.jar
  + log4j-api-2.9.1.jar
  + sac-1.3.jar
  + commons-logging-1.2.jar
  + quartz-2.3.0.jar
* In `<install_root>\derby\lib`:
  + derby.jar
  + derbyclient.jar
  + derbynet.jar
  + derbytools.jar

The Server API classes are stored in the archive file JRESServlets.jar.

When you install Logi JReport Designer, the libraries for Logi JReport Server can also be found in `<designer_install_root>\server\lib` since Logi JReport Designer includes a full Logi JReport Server for previewing reports.

If you are calling the Server API directly in the same JVM as Logi JReport Server, you need to set the classpath environment variable to the local versions of the classes. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRESServlets.jar; <install_root>\lib\JREngine.jar; <install_root>\lib\jakarta.servlet-api-4.0.2.jar; <install_root>\lib\hsqldb-2.4.0.jar; <install_root>\lib\log4j-core-2.9.1.jar; <install_root>\lib\log4j-api-2.9.1.jar; <install_root>\lib\sac-1.3.jar; <install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-2.3.0.jar; <install_root>\derby\lib\derby.jar; <install_root>\derby\lib\derbyclient.jar; <install_root>\derby\lib\derbynet.jar; <install_root>\derby\lib\derbytools.jar;`

If you are calling the Server API using RMI from a different JVM or different server than where Logi JReport Server is running, you need to set the classpath environment variable to the remote libraries. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRSRMI.jar; <install_root>\lib\jakarta.servlet-api-4.0.2.jar; <install_root>\lib\hsqldb-2.4.0.jar; <install_root>\lib\log4j-core-2.9.1.jar; <install_root>\lib\log4j-api-2.9.1.jar； <install_root>\lib\sac-1.3.jar; <install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-2.3.0.jar;`

**Notes:**

* If you are not using Derby as your server DBMS, you need to replace the Derby libraries with the JDBC driver for your DBMS system.
* If you want to export reports to the following formats, you should add the corresponding class package or jar with a valid path to the class path:
  + To e-mail or use the E-mail Notification function: jakarta.mail.jar.
  + To FTP: commons-net-3.6.jar.
  + To Excel: poi-3.15.jar.
  + To Page Report Result: JRWebDesign.jar.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711901-Java-API-for-an-Application)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686222-Using-the-Server-API)
