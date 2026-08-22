---
title: "Installing Using the Installation Wizard"
id: 1500009648362
section: "Installing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648362-Installing-Using-the-Installation-Wizard
updated_at: 2021-07-24T20:54:12Z
---

# Installing Using the Installation Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648222-Supported-Report-Databases)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009672961-Installing-Silently)

# Installing Using the Installation Wizard

Installing with the Installation Wizard is intuitive. You only need to follow the screens and enter the required information. The Installation Wizard provides two installation types:

* **Typical Installation for Standalone Server**  
   Installs Logi JReport Server with the default configuration settings.
* **Custom Installation for Standalone Server**  
   Installs Logi JReport Server in a standalone environment. If you choose this installation type, you can configure the server system environment in the Installation Wizard.

During the installation, if you select to install Logi JReport Server in a folder that already contains an existing Logi JReport Server, you can choose to continue the installation in either the upgrading way or overwriting way. If you choose the upgrading way, the installer will replace the packages and create new batch/script files. Meanwhile, a copy of the old batch/script files will be kept for your reference. You should use the batch/script files that come with the installer in order to make sure that all new packages are added to the class path and manually merge any changes you made into the new version. However, your configuration files and server runtime data of the existing copy will be kept, and you can choose to recover the previous version during the uninstallation of the newly installed Logi JReport Server.

This document shows you how to install Logi JReport Server to different systems with the Installation Wizard and configure the server according to your requirements.

Below is a list of the sections covered in this topic:

* [Installing on Windows](#Win)
* [Installing on Unix](#Unix)
* [Installing on z/Linux](#Linux)
* [Configuring System Database](#DB)
* [Configuring System Environment](#System)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Installing on Windows

To install Logi JReport Server on a Windows platform, take the following steps:

1. Download the Logi JReport Server installation file for Windows from the Jinfonet download center: [http://www.jinfonet.com/downloadLogi JReport/](http://www.jinfonet.com/downloadjreport/).
2. Run the installation file and follow the prompts to install.

During installation, pay attention to the following:

* The installer requires that you choose a Java JDK to complete the installation. You can download the appropriate JDK from [http://java.sun.com](http://java.sun.com/javase/downloads/index.jsp) or your computer vendor's website.
* The Installation Wizard will first find a JVM to get started. If no JVM is found, the Logi JReport installer will fail to launch. To solve this issue, you can try either way:
  + Set JAVA\_HOME variable and append `%JAVA_HOME%\bin` to Path variable in system environment.
  + Install Logi JReport Server from a DOS command by specifying the `LAX_VM` option for the Installation Wizard as follows:

    `jrserver-xxx-windows.exe LAX_VM "C:\jdk1.7.0_17\bin\java.exe"` (change *jrserver-xxx-windows.exe* to the real file name of the installation file)

    The JDK path should use absolute path and be quoted by "".
* The installer provides a chance for you to add additional class paths. You can also choose to add them manually into the setenv.bat in  `<install_root>\bin` after installation.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Installing on Unix

Logi JReport Server supports Solaris, Linux, HP-Unix, and AIX. In the following process, an X server is running and Java 1.6 or above is available, otherwise ask your administrator for help. Installing and running Logi JReport Server requires that an X server has been configured.

1. Download the Logi JReport Server installation file for Unix from the Jinfonet download center: [http://www.jinfonet.com/downloadLogi JReport/](http://www.jinfonet.com/downloadjreport/).

   If you need to transfer the installation file from your download machine to your Unix box, you should transfer it using FTP in binary mode.
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window, and change the directory to the location of the file. Following are examples of the commands that can be used:

   `$ cd /opt/Logi JReport/Server` (or your preferred install location)

   To make the installation file executable, type the command:

   `$ chmod +x jrserver-xxx-linux.bin` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

   To run the installation file:

   `$ ./jrserver-xxx-linux.bin` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

   The Installation Wizard will first locate a JVM to get started. If no JVM is found, the installer will fail to launch. To solve this issue, you can try either way:

   * Set JAVA\_HOME variable and append `$JAVA_HOME/bin` to PATH variable in system environment.
   * Specify a JVM for Installation Wizard with the option `LAX_VM` as follows:

     `$ ./jrserver-xxx-linux.bin LAX_VM "/opt/jdk1.7.0_17/bin/java"` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

     The JDK path should use absolute path and be quoted by "".
3. Once the Installation Wizard has successfully loaded, you can follow the standard prompts to install Logi JReport Server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Installing on z/Linux

Logi JReport Server supports Linux on IBM system z. In the following process, an X server is running and a JDK specially used for IBM is available, otherwise ask your administrator for help. Installing and running Logi JReport Server requires that an X server has been configured.

1. Download the Logi JReport Server installation file for z/Linux from the Jinfonet download center: [http://www.jinfonet.com/downloadLogi JReport/](http://www.jinfonet.com/downloadjreport/).

   If you need to transfer the installation file from your download machine to your z/Linux box, you should transfer it using FTP in binary mode.
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window, and change the directory to the location of the file. Following are examples of the commands that can be used:

   `$ cd /opt/Logi JReport/Server` (or your preferred install location)

   To make the installation file executable, type the command:

   `$ chmod +x jrserver-xxx-linux.bin` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

   To run the installation file:

   `$ ./jrserver-xxx-linux.bin` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

   The Installation Wizard will first locate a JVM to get started. If no JVM is found, the installer will fail to launch. To solve this issue, you can try either way:

   * Set JAVA\_HOME variable and append `$JAVA_HOME/bin` to PATH variable in system environment.
   * Specify a JVM for Installation Wizard with the option `LAX_VM` as follows:

     `$ ./jrserver-xxx-linux.bin LAX_VM "/opt/ibm-java2-sdk-6.0/bin/java"` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

     The JDK path should use absolute path and be quoted by "".
3. Once the Installation Wizard has successfully loaded, you can follow the standard prompts to install Logi JReport Server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Configuring System Database

Configuring the system database is a step on the server installation wizard available to a production key or a temporary key.

By default the trial database Derby is used. The port is configurable in case it is being used.

However in a production environment, you need to configure your own production DBMS instead of using the default Derby which is provided for testing and evaluation purposes only and which should not be used in a production system. To do this, select **Production Database** and then set the correct database connection information. If the connection failed after selecting Next, a message will pop up, you can choose to reset the connection. Or if you choose to continue with the failure, after the installation, you will need to configure the database. For details, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database).

These databases have been tested workable as the production database: Apache Derby, HSQLDB, MySQL, Microsoft SQL Server, IBM DB2, Oracle, Sybase, PostgreSQL, and Informix.

**Notes:**

* ODBC is not supported as the server database.
* When setting SQL 2000 as the server database, the driver should use jtds.jar, otherwise the scheduling feature cannot work.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Configuring System Environment

When installing Logi JReport Server using the Installation Wizard, if you choose Custom Installation for Standalone Server, you can configure the server system environment according to your requirements during the installation.

* **[Service](https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service)**
* [**Cluster**](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster#During)
* [**E-mail**](https://devnet.logianalytics.com/hc/en-us/articles/1500009644522-Configuring-Export-Settings#Email)
* **[Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009669021-Configuring-Cache)**
  + **Cache Loaded Catalogs**Specifies whether to keep a catalog in memory, or to remove it from memory after a report is completed.

    Normally, after a report has been generated, the catalog that is used to generate the report will be removed from memory. However, if you specify this option, the catalog will be cached rather than removed.

    **Cache Loaded Page Reports**Specifies whether to keep the page reports in memory or remove them from memory after they have been generated.
* **[Performance](https://devnet.logianalytics.com/hc/en-us/articles/1500009669201-Tuning-Server-Performance#Preload)**  
   Pre-loading the Java classes and fonts which are used by catalogs, reports and Logi JReport Engine at startup time will improve performance when these classes are needed at runtime.
  + **Maximum Number of Concurrent Reports in the Queue**  
     Specifies the [maximum number of concurrent reports in the queue](https://devnet.logianalytics.com/hc/en-us/articles/1500009668861-Appendix-2-Properties-in-server-properties#performance.max.reports), which must be less than or equal to the number that the license permits.

* **[Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500009644402-Configuring-Advanced-Server-Settings)**
* **Demo**
  + **Install Demo Reports**  
     Specifies whether to install demo reports and dashboards which will be available in the Public Reports folder in the server resource tree.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648222-Supported-Report-Databases)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009672961-Installing-Silently)
