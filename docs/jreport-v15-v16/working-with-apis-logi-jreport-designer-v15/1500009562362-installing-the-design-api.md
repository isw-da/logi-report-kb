---
title: "Installing the Design API"
id: 1500009562362
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562362-Installing-the-Design-API
updated_at: 2022-10-14T07:45:23Z
---

# Installing the Design API

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582741-Design-API-Packages-License)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582901-Getting-Started)

# Installing the Design API

The full Design API packages are included in Logi JReport Designer and Logi JReport Server. Logi JReport Designer includes a single threaded Design API, while Logi JReport Server includes a multi-threaded Design API. Logi JReport Design API and Logi JReport Server Design API packages can also be downloaded and installed to your local machine. After which, you can then program with them without having to install any other Logi JReport products.

Below is a list of the sections covered in this topic:

> * [Installing the Design API by Logi JReport Designer](#Designer)
> * [Installing the Design API by Logi JReport Server](#Server)
> * [Installing independent Logi JReport Design API](#Independent)
> * [Installing independent Logi JReport Server Design API](#IndependentServer)

## Installing the Design API by Logi JReport Designer

When you install Logi JReport Designer, the Design API is also installed at the same time. After installation, you will have the components listed below in `<designer_install_root>\lib`:

* JREngine.jar
* report.jar
* sac-1.3.jar
* commons-codec-1.2.jar
* log4j-core-2.7.jar and log4j-api-2.7.jar (for the Logi JReport logging system)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4411773980183/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

The Design API classes are stored in the archive files: report.jar and JREngine.jar. You will need to take the following two steps before you can compile and run the program:

1. Set the classpath environment variable. Append the following string to your class path that starts the Design API (make sure that the path of JREngine.jar is before that of report.jar):

   `<designer_install_root>\lib\JREngine.jar;<designer_install_root>\lib\report.jar;<designer_install_root>\lib\log4j-core-2.7.jar;<designer_install_root>\lib\log4j-api-2.7.jar;<designer_install_root>\lib\sac-1.3.jar;<designer_install_root>\commons-codec-1.2.jar;`
2. Add the jar files for your DBMS JDBC drivers.
3. Set the -Dreporthome parameter to be the same as the root path of Logi JReport Designer.
4. You will need to register the Design API licensed user and license key in your source code.

## Installing the Design API by Logi JReport Server

When you install Logi JReport Server, the Server Design API is also installed at the same time. After installation, you will have the components listed below in `<server_install_root>\lib`:

* JREngine.jar
* JREServlets.jar
* sac-1.3.jar
* commons-codec-1.2.jar
* log4j-core-2.7.jar and log4j-api-2.7.jar (for the Logi JReport logging system)

The Server Design API classes are stored in the archive files: JRESServlets.jar and JREngine.jar. You will need to take the following two steps before you can compile and run the program:

1. Set the classpath environment variable. Append the following string to your class path that starts the Design API:

   `<server_install_root>\lib\JRESServlets.jar;<server_install_root>\lib\JREngine.jar;<server_install_root>\lib\log4j-core-2.7.jar;<server_install_root>\lib\log4j-api-2.7.jar;<server_install_root>\lib\sac-1.3.jar;<server_install_root>\commons-codec-1.2.jar;`
2. Add the jar files for our DBMS JDBC drivers.
3. Set the -Dreporthome parameter to be the same as the root path of Logi JReport Server.
4. You will need to register the Server Design API licensed user and license key in your source code.

## Installing independent Logi JReport Design API

Ask the Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)) for the independent Design API installation file. Then, run the file and follow the prompts to install.

After you have installed Logi JReport Design API by running the installation file, you will need to take the following two steps before you compile and run the program:

1. Set the classpath environment variable. Then, append the following string to your class path that starts the Design API:

   `<designAPI_install_root>\lib\designAPI.jar;<designAPI_install_root>\lib\log4j-core-2.7.jar;<designAPI_install_root>\lib\log4j-api-2.7.jar;<designAPI_install_root>\lib\sac-1.3.jar;<designAPI_install_root>\lib\commons-codec-1.2.jar;<designAPI_install_root>\lib\hsqldb-2.3.4.jar`
2. Set the -Dreporthome parameter equal to the root path of the Design API.

## Installing independent Logi JReport Server Design API

Ask the Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)) for the independent Server Design API installation file. Then, run the file and follow the prompts to install. We don't recommend using these libraries, we recommend you use the Design API libraries included in Logi JReport Server.

After you have installed Logi JReport Server Design API by running the installation file, you will need to take the following two steps before you compile and run the program:

1. Set the classpath environment variable. Then, append the following string to your class path that starts the Server Design API:

   `<svrdesignAPI_install_root>\lib\serverDesignAPI.jar;<svrdesignAPI_install_root>\lib\log4j-core-2.7.jar;<svrdesignAPI_install_root>\lib\log4j-api-2.7.jar;<svrdesignAPI_install_root>\lib\sac-1.3.jar;<svrdesignAPI_install_root>\commons-codec-1.2.jar;<svrdesignAPI_install_root>\hsqldb-2.3.4.jar`
2. Set the -Dreporthome parameter to be the same as the root path of the Server Design API.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582741-Design-API-Packages-License)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582901-Getting-Started)
