---
title: "Installing the Design API"
id: 45190404977933
section: "Working with APIs - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190404977933-Installing-the-Design-API
updated_at: 2026-04-30T15:11:53Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing the Design API

Both Designer and Server include the full Design API packages.  Designer includes a single threaded Design API, while Server includes a multithreaded Design API. You can also download and install the independent Design API and Server Design API packages on your local machine, then you can program with them without having to install any other Report products. This topic describes how you can install the Design API using different methods.

This topic contains the following sections:

- Installing the Design API by Designer

- Installing the Design API by Server

- Installing Independent Design API

- Installing Independent Server Design API

## 
Installing the Design API by  Designer

When you install Designer, you install the Design API at the same time. After installation, you have the following components in <designer_install_root>\lib:

- JREngine.jar

- report.jar

- sac-1.3.jar

-  log4j-api-2.17.2.jar, log4j-core-2.17.2.jar, log4j-slf4j-impl-2.17.2.jar, and slf4j-api-1.7.36.jar (for the Report logging system)

 In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

You can get the classes for the Design API classes in the JREngine.jar and report.jar archive files. You need to take the following steps before you can compile and run the program.

- Set the CLASSPATH environment variable. Append the following string to your class path that starts the Design API (make sure the path of  JREngine.jar is before that of report.jar):
    <designer_install_root>\lib\JREngine.jar;<designer_install_root>\lib\report.jar;<designer_install_root>\lib\sac-1.3.jar;<designer_install_root>\lib\log4j-api-2.17.2.jar;<designer_install_root>\lib\log4j-core-2.17.2.jar;<designer_install_root>\lib\log4j-slf4j-impl-2.17.2.jar;<designer_install_root>\lib\slf4j-api-1.7.36.jar

- Add JAR files for the JDBC drivers of your database.

- Set the -Dreporthome option to be the same as the root path of Designer.

- Register the Design API licensed user and license key in your source code.

 

## 
Installing the Design API by Server

When you install Server, you install the Server Design API  at the same time. After installation, you have the following components in <server_install_root>\lib:

- JREngine.jar

- JREServlets.jar

- sac-1.3.jar

-  log4j-api-2.17.2.jar, log4j-core-2.17.2.jar, log4j-slf4j-impl-2.17.2.jar, and slf4j-api-1.7.36.jar (for the Report logging system)

You can get the classes for the Server Design API classes  in the JRESServlets.jar and JREngine.jar  archive files. You need to take the following steps before you can compile and run the program.

- Set the CLASSPATH environment variable. Append the following string to your class path that starts the Server Design API:
    <server_install_root>\lib\JRESServlets.jar;<server_install_root>\lib\JREngine.jar;<server_install_root>\lib\sac-1.3.jar;<server_install_root>\lib\log4j-api-2.17.2.jar;<server_install_root>\lib\log4j-core-2.17.2.jar;<server_install_root>\lib\log4j-slf4j-impl-2.17.2.jar;<server_install_root>\lib\slf4j-api-1.7.36.jar

- Add JAR files for the JDBC drivers of your database.

- Set the -Dreporthome option to be the same as the root path of Server.

- Register the Server Design API licensed user and license key in your source code.

 

## 
Installing Independent Design API

To install independent Design API, get the installation file, then run the file and follow the prompts to install. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

After you install the Design API by running the installation file, you need to take the following steps before you can compile and run the program.

- Set the CLASSPATH environment variable. Append the following string to your class path that starts the Design API:
    <designAPI_install_root>\lib\designAPI.jar;<designAPI_install_root>\lib\log4j-api-2.17.2.jar;<designAPI_install_root>\lib\log4j-core-2.17.2.jar;<designAPI_install_root>\lib\log4j-slf4j-impl-2.17.2.jar;<designAPI_install_root>\lib\slf4j-api-1.7.36.jar;<designAPI_install_root>\lib\sac-1.3.jar;<designAPI_install_root>\lib\hsqldb-2.6.1.jar

- Set the -Dreporthome option to be the same as the root path of the Design API.

 

## 
Installing Independent Server Design API

To install independent Server Design API, get the installation file, then run the file and follow the prompts to install. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

 We do not recommend using these libraries, instead we recommend you use the Design API libraries included in Server.

After you have install the Server Design API by running the installation file, you need to take the following steps before you can compile and run the program.

- Set the CLASSPATH environment variable. Append the following string to your class path that starts the Server Design API:
    <svrdesignAPI_install_root>\lib\serverDesignAPI.jar;<svrdesignAPI_install_root>\lib\log4j-api-2.17.2.jar;<svrdesignAPI_install_root>\lib\log4j-core-2.17.2.jar;<svrdesignAPI_install_root>\lib\log4j-slf4j-impl-2.17.2.jar;<svrdesignAPI_install_root>\lib\slf4j-api-1.7.36.jar;<svrdesignAPI_install_root>\lib\sac-1.3.jar;<svrdesignAPI_install_root>\lib\hsqldb-2.6.1.jar

- Set the -Dreporthome option to be the same as the root path of the Server Design API.
