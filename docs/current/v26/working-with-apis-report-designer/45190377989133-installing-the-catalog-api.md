---
title: "Installing the Catalog API"
id: 45190377989133
section: "Working with APIs - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190377989133-Installing-the-Catalog-API
updated_at: 2026-04-30T15:11:52Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing the Catalog API

This topic describes how you can install the Catalog API.

When you install Designer, you install the Catalog API at the same time. After installation, you have the following components in <install_root>\lib:

- report.jar

- JREngine.jar

-  log4j-api-2.17.2.jar, log4j-core-2.17.2.jar, log4j-slf4j-impl-2.17.2.jar, and slf4j-api-1.7.36.jar (for the Report logging system)

- sac-1.3.jar (for installing the Catalog API with the Design API)

- ...

 In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

You can get the Catalog API class in the report.jar archive file. You need to take the following steps before you can compile and run the program.

- Set the CLASSPATH environment variable. Append the following string to your class path that starts the Catalog API (make sure the path of JREngine.jar is before that of  report.jar):
    <install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar;<install_root>\lib\log4j-api-2.17.2.jar;<install_root>\lib\log4j-core-2.17.2.jar;<install_root>\lib\log4j-slf4j-impl-2.17.2.jar;<install_root>\lib\slf4j-api-1.7.36.jar

- In your Java program, you must set the licensed user and Design API license key.
    DesignerUserInfo userInfo=new DesignerUserInfo("UID","Design API Key");

- Set the reporthome parameter to the root path of Designer. You can set this in your environment or with the -Dreporthome option to your JVM.  

Report Server also includes the Catalog API. If you prefer to use the libraries from Server, include <server_install_root>\lib\JRESServlets.jar in your class path instead of report.jar. You then need to use the Server Design API license key rather than the Design API license key.
