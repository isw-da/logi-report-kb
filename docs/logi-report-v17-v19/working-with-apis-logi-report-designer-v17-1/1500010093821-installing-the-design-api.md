---
title: "Installing the Design API"
id: 1500010093821
section: "Working with APIs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093821-Installing-the-Design-API
updated_at: 2022-10-14T07:17:56Z
---

# Installing the Design API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056522-Design-API-Packages-and-License)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056542-Making-Preparations-Before-Using-the-Design-API)

# Installing the Design API

Both Designer and Server include the full Design API packages. Designer includes a single threaded Design API, while Server includes a multi-threaded Design API. You can also download and install the independent Design API and Server Design API packages on your local machine, then you can program with them without having to install any other Logi Report products. This topic describes how you can install the Design API using different methods.

This topic contains the following sections:

* [Installing the Design API by Designer](#Designer)
* [Installing the Design API by Server](#Server)
* [Installing Independent Design API](#IndependentDesign)
* [Installing Independent Server Design API](#IndependentServer)

## Installing the Design API by Designer

When you install Designer, you install the Design API at the same time. After installation, you have the following components in `<designer_install_root>\lib`:

* JREngine.jar
* report.jar
* sac-1.3.jar
* log4j-core-2.13.3.jar and log4j-api-2.13.3.jar (for the Logi Report logging system)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

You can get the classes for the Design API classes in the archive files: report.jar and JREngine.jar. You need to take the following steps before you can compile and run the program:

1. Set the classpath environment variable. Append the following string to your class path that starts the Design API (make sure that the path of **JREngine.jar** is before that of **report.jar**):

   `<designer_install_root>\lib\JREngine.jar;<designer_install_root>\lib\report.jar;<designer_install_root>\lib\log4j-core-2.13.3.jar;<designer_install_root>\lib\log4j-api-2.13.3.jar;<designer_install_root>\lib\sac-1.3.jar;`
2. Add the jar files for your DBMS JDBC drivers.
3. Set the **-Dreporthome** parameter to be the same as the root path of Designer.
4. Register the Design API licensed user and license key in your source code.

## Installing the Design API by Server

When you install Server, you install the Server Design API at the same time. After installation, you have the following components in `<server_install_root>\lib`:

* JREngine.jar
* JREServlets.jar
* sac-1.3.jar
* log4j-core-2.13.3.jar and log4j-api-2.13.3.jar (for the Logi Report logging system)

You can get the classes for the Server Design API classes in the archive files: JRESServlets.jar and JREngine.jar. You need to take the following steps before you can compile and run the program:

1. Set the classpath environment variable. Append the following string to your class path that starts the Server Design API:

   `<server_install_root>\lib\JRESServlets.jar;<server_install_root>\lib\JREngine.jar;<server_install_root>\lib\log4j-core-2.13.3.jar;<server_install_root>\lib\log4j-api-2.13.3.jar;<server_install_root>\lib\sac-1.3.jar;`
2. Add the jar files for our DBMS JDBC drivers.
3. Set the **-Dreporthome** parameter to be the same as the root path of Server.
4. Register the Server Design API licensed user and license key in your source code.

## Installing Independent Design API

Ask the Logi Analytics Support ([support@logianalytics.com](mailto:support@logianalytics.com)) for the independent Design API installation file. Then, run the file and follow the prompts to install.

After you install the Design API by running the installation file, you need to take the following steps before you can compile and run the program:

1. Set the classpath environment variable. Append the following string to your class path that starts the Design API:

   `<designAPI_install_root>\lib\designAPI.jar;<designAPI_install_root>\lib\log4j-core-2.13.3.jar;<designAPI_install_root>\lib\log4j-api-2.13.3.jar;<designAPI_install_root>\lib\sac-1.3.jar;<designAPI_install_root>\lib\hsqldb``-2.5.1.jar`
2. Set the **-Dreporthome** parameter to be the same as the root path of the Design API.

## Installing Independent Server Design API

Ask the Logi Analytics Support ([support@logianalytics.com](mailto:support@logianalytics.com)) for the independent Server Design API installation file. Then, run the file and follow the prompts to install. We don't recommend using these libraries, instead we recommend you use the Design API libraries included in Server.

After you have install the Server Design API by running the installation file, you need to take the following steps before you can compile and run the program:

1. Set the classpath environment variable. Append the following string to your class path that starts the Server Design API:

   `<svrdesignAPI_install_root>\lib\serverDesignAPI.jar;<svrdesignAPI_install_root>\lib\log4j-core-2.13.3.jar;<svrdesignAPI_install_root>\lib\log4j-api-2.13.3.jar;<svrdesignAPI_install_root>\lib\sac-1.3.jar;<svrdesignAPI_install_root>\lib\hsqldb``-2.5.1.jar`
2. Set the **-Dreporthome** parameter to be the same as the root path of the Server Design API.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056522-Design-API-Packages-and-License)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056542-Making-Preparations-Before-Using-the-Design-API)
