---
title: "Getting Started Using the Design API"
id: 4405661322263
section: "Working with APIs - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661322263-Getting-Started-Using-the-Design-API
updated_at: 2022-01-27T20:38:23Z
---

# Getting Started Using the Design API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664348439-Making-Preparations-Before-Using-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661317399-Designing-Reports-with-the-Design-API)

# Getting Started Using the Design API

The topic presents a simple example to help you start using the Design API. The example shows how you can use the Design API package to compile and run a Java class that returns the connection information from a catalog file.

1. Compile the sample code **TellMeConnection.java** in `<install_root>\help\samples\APICatalog` (make sure that the path of the file **JREngine.jar** is before that of the file **report.jar**).

   `javac -classpath <install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar TellMeConnection.java`
2. Set the license key for Design API using the method *dr.setUserInfo("UID","XXXXXXXXXXX")* in TellMeConnection.java.
3. Run the sample code.

   `java -classpath ".;<install_root>\lib\JREngine.jar;<install_root>\lib\report.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\log4j-core-``2.17.1.jar``;<install_root>\lib\log4j-api-``2.17.1.jar``" -Dreporthome=<install_root> TellMeConnection –path=<catalog path> -catalog=<catalog name>`

   For example:

   `java -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\log4j-core-``2.17.1.jar``;C:\LogiReport\Designer\lib\log4j-api-``2.17.1.jar``;C:\LogiReport\Designer\lib\hsqldb-hsqldb-``![This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.](https://devnet.logianalytics.com/hc/article_attachments/4420542050071/___newv18.3.jpg "New for version 18.3.")2.6.1.jar``-Dreporthome=C:\LogiReport\Designer TellMeConnection -path=C:\LogiReport\Designer\Demo\Reports\TutorialReports -catalog=JinfonetGourmetJava.cat`

   And the output should be:

   **Name:** Jinfonet demo  
   **Driver:** org.hsqldb.jdbcDriver  
   **URL:**`jdbc:hsqldb:C:\LogiReport\Designer\Demo\db\DemoDB`  
   **User:** sa  
   **Password**  
   **TimestampFormat:** yyyy-MM-dd HH:mm:ss.SSS  
   **TimeFormat:** HH:mm:ss  
   **DateFormat:** yyyy-MM-dd  
   **ExtraNamePattern:** Default(JDBC)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664348439-Making-Preparations-Before-Using-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661317399-Designing-Reports-with-the-Design-API)
