---
title: "Logi Report Server Unable to Find JAR File"
id: 360051648593
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360051648593-Logi-Report-Server-Unable-to-Find-JAR-File
updated_at: 2020-07-27T22:37:04Z
---

# Logi Report Server Unable to Find JAR File

**Problem**

When trying to run the report that has been deployed on the Logi Report server, the server is unable to find the jar file.

**Solution**

The solution for the issue is to add the directory containing the jar file into the CLASSPATH environment variable.

***Note**: Solution below is specifically referring to 'com.mysql.jdbc.Driver' jar file. ( Adding mysql JDBC Driver jar file into CLASSPATH)*

Below are the steps to achieve the output :

|  |
| --- |
| **Scenario 1: If the Logi Report Server is in a standalone environment** |
| 1. Shut down your Logi Report Server  2. Take one of these steps below:   * Modify the startup script file of Logi Report Server (e.g. %JReportServer\_installroot%\bin\JRServer.bat | JRServer.sh) to include the mysql JDBC jar in the classpath, for example: CLASSPATH=C:\DBDriver\MySql\mysql-connector-java-5.1.29-bin.jar;%REPORTHOME%\derby\lib\*;%REPORTHOME%\lib\JREngine.jar;...  OR * Copy the mysql JDBC jar file to %installroot%\lib directory directly.   3. Restart Server |

|  |
| --- |
| **Scenario 2: If the Logi Report Server is running as an OS (Windows/Linux/Unix) Service** |
| 1.Shut down your Logi Report Server  2. Take one of these steps below:   * Modify the file NTService.ini under %JReportServer\_installroot%\bin to include the patch the mysql JDBC jar in the classpath of both StartArg and ShutdownArg, for example: StartArg= "-Dinstall.root=D:\JReport\Server15" -classpath "C:\DBDriver\MySql\mysql-connector-java-5.1.29-bin.jar;D:\JReport\Server15\derby\lib\*;D:\JReport\Server15\lib\JREngine.jar;  ShutdownArg= "-Dinstall.root=D:\JReport\Server15" -classpath "C:\DBDriver\MySql\mysql-connector-java-5.1.29-bin.jar;D:\JReport\Server15\derby\lib\*;D:\JReport\Server15\lib\JREngine.jar;  OR * Copy the mysql JDBC jar file to %installroot%\lib directory directly.   3. Start Server |
|  |

|  |
| --- |
| **Scenario 3: If Logi report server is running in an integrated environment** |
| 1. Copy the mySQL jar file into %Your JReport war%/WEB-INF/lib/  2. Redeploy WAR and start service |
