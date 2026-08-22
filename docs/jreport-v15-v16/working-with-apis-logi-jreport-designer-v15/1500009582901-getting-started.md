---
title: "Getting Started"
id: 1500009582901
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582901-Getting-Started
updated_at: 2021-12-31T02:47:42Z
---

# Getting Started

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562362-Installing-the-Design-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582761-Programming-with-the-Design-API)

# Getting Started

To help you start using the Design API, here is an example that shows how to use the Logi JReport Design API package to compile and run a Java class that returns the connection information from a catalog file.

1. Compile the sample code TellMeConnection.java in `<install_root>\help\samples\APICatalog` (make sure that the path of the file JREngine.jar is before that of the file report.jar).

   `javac -classpath <install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar TellMeConnection.java`
2. Set the license key for Design API using the method `dr.setUserInfo("UID","XXXXXXXXXXX")` in TellMeConnection.java.
3. Run the sample code.

   `java -classpath ".;<install_root>\lib\JREngine.jar;<install_root>\lib\report.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\log4j-core-2.7.jar;<install_root>\lib\log4j-api-2.7.jar" -Dreporthome=<install_root> TellMeConnection –path=<catalog path> -catalog=<catalog name>`

   For example,

   `java -classpath "C:\Logi JReport\Designer\lib\JREngine.jar;C:\Logi JReport\Designer\lib\report.jar;C:\Logi JReport\Designer\lib\sac-1.3.jar;C:\Logi JReport\Designer\lib\log4j-core-2.7.jar;C:\Logi JReport\Designer\lib\log4j-api-2.7.jar;C:\Logi JReport\Designer\lib\hsqldb-2.3.4.jar" -Dreporthome=C:\Logi JReport\Designer TellMeConnection -path=C:\Logi JReport\Designer\Demo\Reports\TutorialReports -catalog=JinfonetGourmetJava.cat`

   And the output should be as follows:

   **Name:** Jinfonet demo  
   **Driver:** org.hsqldb.jdbcDriver  
   **URL:**`jdbc:hsqldb:c:\Logi JReport\Designer\Demo\db\JRDemo`  
   **User:** sa  
   **Password**  
   **TimestampFormat:** yyyy-MM-dd HH:mm:ss.SSS  
   **TimeFormat:** HH:mm:ss  
   **DateFormat:** yyyy-MM-dd  
   **ExtraNamePattern:** Default(JDBC)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4411773980183/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562362-Installing-the-Design-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582761-Programming-with-the-Design-API)
