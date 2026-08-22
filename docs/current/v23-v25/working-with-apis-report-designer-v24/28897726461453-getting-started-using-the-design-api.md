---
title: "Getting Started Using the Design API"
id: 28897726461453
section: "Working with APIs - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897726461453-Getting-Started-Using-the-Design-API
updated_at: 2024-09-30T09:13:19Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Getting Started Using the Design API

The topic presents a simple example to help you start using the Design API. The example shows how you can use the  Design API package to compile and run a Java class that returns the connection information from a catalog file.

- Compile the sample code TellMeConnection.java in <install_root>\help\samples\APICatalog (make sure that the path of the file JREngine.jar is before that of the file report.jar).
  javac -classpath <install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar TellMeConnection.java

- Set the license key for Design API using the dr.setUserInfo("UID","XXXXXXXXXXX") method in TellMeConnection.java.

- Run the sample code.
    java -classpath "...;<install_root>\lib\JREngine.jar;<install_root>\lib\report.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\log4j-api-2.17.2.jar;<install_root>\lib\log4j-core-2.17.2.jar;<install_root>\lib\log4j-slf4j-impl-2.17.2.jar;<install_root>\lib\slf4j-api-1.7.36.jar;<install_root>\lib\hsqldb-hsqldb-2.6.1.jar" -Dreporthome=<install_root> TellMeConnection –path=<catalog_path> -catalog=<catalog_name>

For example:

java -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\log4j-api-2.17.2.jar;C:\LogiReport\Designer\lib\log4j-core-2.17.2.jar;C:\LogiReport\Designer\lib\log4j-slf4j-impl-2.17.2.jar;C:\LogiReport\Designer\lib\slf4j-api-1.7.36.jar;C:\LogiReport\Designer\lib\hsqldb-hsqldb-2.6.1.jar" -Dreporthome=C:\LogiReport\Designer TellMeConnection -path=C:\LogiReport\Designer\Demo\Reports\TutorialReports -catalog=JinfonetGourmetJava.cat

And the output should be:

Name: Jinfonet demo
Driver: org.hsqldb.jdbcDriver
URL:jdbc:hsqldb:C:\LogiReport\Designer\Demo\db\DemoDB
User: sa
Password
TimestampFormat: yyyy-MM-dd HH:mm:ss.SSS
TimeFormat: HH:mm:ss
DateFormat: yyyy-MM-dd
ExtraNamePattern: Default(JDBC)

 In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

Previous Topic  Next Topic
