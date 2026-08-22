---
title: "Installing the Server API"
id: 1500009643642
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009643642-Installing-the-Server-API
updated_at: 2021-07-24T20:55:31Z
---

# Installing the Server API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668201-Java-API-for-an-Application)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643782-Using-the-Server-API)

# Installing the Server API

When you install Logi JReport Server, Logi JReport Server API is also installed at the same time. After installation, you will have the following files:

* In  `<install_root>\lib`:
  + JRESServlets.jar (local calls)
  + JREngine.jar (local calls)
  + JRSRMI.jar (remote RMI calls)
  + javax.servlet-api-3.1.0.jar
  + hsqldb-2.3.4.jar
  + log4j-core-2.7.jar
  + log4j-api-2.7.jar
  + sac-1.3.jar
  + commons-codec-1.2.jar
  + commons-logging-1.2.jar
  + quartz-all-2.2.3.jar
* In `<install_root>\derby\lib`:
  + derby.jar
  + derbyclient.jar
  + derbynet.jar
  + derbytools.jar

The Server API classes are stored in the archive file JRESServlets.jar.

When you install Logi JReport Designer, the libraries for Logi JReport Server can also be found in `<designer_install_root>\server\lib` since Logi JReport Designer includes a full Logi JReport Server for previewing reports.

If you are calling the Server API directly in the same JVM as Logi JReport Server, you need to set the classpath environment variable to the local versions of the classes. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRESServlets.jar; <install_root>\lib\JREngine.jar; <install_root>\lib\javax.servlet-api-3.1.0.jar; <install_root>\lib\hsqldb-2.3.4.jar; <install_root>\lib\log4j-core-2.7.jar; <install_root>\lib\log4j-api-2.7.jar; <install_root>\lib\sac-1.3.jar; <install_root>\lib\commons-codec-1.2.jar; <install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-all-2.2.3.jar; <install_root>\derby\lib\derby.jar; <install_root>\derby\lib\derbyclient.jar; <install_root>\derby\lib\derbynet.jar; <install_root>\derby\lib\derbytools.jar;`

If you are calling the Server API using RMI from a different JVM or different server than where Logi JReport Server is running, you need to set the classpath environment variable to the remote libraries. Append the following jar files to your class path that compile and run applications which call the Server API:

`<install_root>\lib\JRSRMI.jar; <install_root>\lib\javax.servlet-api-3.1.0.jar; <install_root>\lib\hsqldb-2.3.4.jar; <install_root>\lib\log4j-core-2.7.jar; <install_root>\lib\log4j-api-2.7.jar； <install_root>\lib\sac-1.3.jar; <install_root>\lib\commons-codec-1.2.jar; <install_root>\lib\commons-logging-1.2.jar; <install_root>\lib\quartz-all-2.2.3.jar;`

**Notes:**

* If you are not using Derby as your Server DBMS, you need to replace the Derby libraries with the JDBC driver for your DBMS system.
* chart.jar is used in HTML applet and should be placed after jrengine.jar in the class path so as to avoid exceptions.
* If you want to export reports to the following formats, you should add the corresponding class package or jar with a valid path to the class path:
  + To e-mail or use the E-mail Notification function: activation-1.1.1.jar and mail-1.4.7.jar.
  + To FTP: commons-net-3.5.jar.
  + To Excel: poi-3.15.jar.
  + To Page Report Result: JRWebDesign.jar.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668201-Java-API-for-an-Application)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643782-Using-the-Server-API)
