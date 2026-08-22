---
title: "Upgrading Logi JReport Server"
id: 1500009717301
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717301-Upgrading-Logi-JReport-Server
updated_at: 2021-11-03T06:57:01Z
---

# Upgrading Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691002-Logi-Report-Server-Reporthome-Directory-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717241-Migrating-Server-and-Server-Data)

# Upgrading Logi JReport Server

The topic introduces how to upgrade Logi JReport Server in both standalone and integration environment. Upgrading a standalone Logi JReport Server and an integrated Logi JReport Server involves different processes while sharing some common steps. Both updated Logi JReport Servers require converting the report resources in the old version in order to comply with the new server version.

Before upgrading, [back up your system database](https://devnet.logianalytics.com/hc/en-us/articles/1500009691342-Managing-Server-Data#BackRestore) and shut down your Logi JReport Server. If you want to use the old result files in `<install_root>\history`, install the new Logi JReport Server to the same directory with a new license key, overriding the existing program files.

Below is a list of the sections covered in this topic:

* [Upgrading in a Standalone Environment](#Standalone)
* [Upgrading in an Integration Environment](#Integ)

## Upgrading in a Standalone Environment

Logi JReport Server provides two migration tools in `<install_root>\bin` folder, which can help you to convert all the resources on the previous version of Logi JReport Server before version 6.0. Resources the migration tools cover include the security information (realm, user, group, protection, and ACL), report resources (catalog and reports), scheduled tables, completed tables, version and version tables, and other relevant information (such as fonts, NLS, and style groups). If you are upgrading from a release later than version 6.0 these tools are not needed.

**Note:** When installing Logi JReport Server 16 into the same directory as the old version, the report level resources in the old version will be maintained and not be replaced by the report resources of V16. For example, if you installed Logi JReport Server 16 to `C:\JReport\Server13GA`, the backed up files of V13 GA will be maintained in `C:\JReport\ServerV13GA\bak\previous_version`, the removed patches and jar files will be maintained in `C:\JReport\ServerV13GA\bak\xxx\lib`, and the whole folder bin will be maintained in `C:\JReport\ServerV13GA\bak\xxx\bin`.

The following shows upgrading Logi JReport Server from a specific old version to V16.

**Upgrading from V13 GA and later to V16**

To upgrade a version V13 GA and later to V16, take the steps below. Here is a case showing you how to upgrade V13 GA to V16, provided that the old Logi JReport Server is located in `C:\JReport\Server13GA.`

1. Install Logi JReport Server 16 to `C:\JReport\Server13GA`. In the Choose Installation Set screen, choose **Typical Installation** for Standalone Server and select **Next**.
2. In the prompted Installation Warning message window, choose **Upgrading**.
3. The installation turns to the List screen which shows the details of the upgrading, including the removed patches, the modified config files and the backup files.
4. Select **Install** in the Installation Summary screen. After the installation is complete, start Logi JReport Server to check the upgraded version.

**Upgrading from V6.0 and later to V16**

To upgrade a version V6.0 and later to V16, take the steps below. Here is a case showing you how to upgrade V11.1 to V16, provided that the old Logi JReport Server is located in `C:\JReport\Server11.1.`

1. Check the value of properties in dbconfig.xml which locates in `C:\JReport\Server11.1\bin` or back up the file first.
2. Install Logi JReport Server 16 to `C:\JReport\Server11.1`. In the Choose Installation Set screen, choose **Typical Installation for Standalone Server** and select **Next**.
3. In the prompted Installation Warning message window, choose **Yes**.
4. In the System Database screen, input the property values according to the backed up dbconfig.xml file. Or check the **Trial Database** radio button, and replace dbconfig.xml file with the one you backed up.
5. In the List screen you can see the details of the upgrading, including the removed patches, the modified config files and the backup files.
6. Select **Install** in the Installation Summary screen. After the installation is complete, start Logi JReport Server to check the upgraded version.

**Upgrading a version between V5.2 Build 590 and V6 (excluded) to V16**

You can make the upgrade using the migration tool MigrationV52.bat (MigrationV52.sh for Unix) that is available in the `<install_root>\bin` folder. This tool is used to convert all the resources of the versions between V5.2 Build 590 and V6 (excluded) to the resources of Logi JReport Server 16. If you install the new version to the same folder as the old one, the parameter can be omitted.

* **Usage**  
   MigrationV52 [orgReportHome]
* **Options**
  + orgReporthome  
     The reporthome of the original Logi JReport Server. If this parameter is not provided, the reporthome of Logi JReport Server 16 will be used as its value.
* **Case 1: Installing Logi JReport Server 16 to a new folder (recommended)**
  1. Provided that the old Logi JReport Server is located in `C:\JREntServer595`. Install Logi JReport Server 16 to a new folder `C:\JReport\ServerV16`. DO NOT start the newly installed Logi JReport Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run `MigrationV52 C:\JREntServer595`.
* **Case 2: Installing Logi JReport Server 16 to the folder where the old version resides**
  1. Provided that the old Logi JReport Server is located in `C:\JREntServer595`. Install Logi JReport Server 16 to the same location. DO NOT start the newly installed Logi JReport Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run MigrationV52.bat.

**Upgrading a version earlier than V5.2 Build 590 to V16**

You can do the upgrade using the migration tool MigrationBV52.bat (MigrationBV52.sh for Unix) that is available in the `<install_root>\bin` folder. This tool is used to convert all the resources of versions lower than V5.2 Build 590 to the resources of Logi JReport Server 16. If you install the new version to the same folder as the old one, the parameter can be omitted.

* **Usage**  
   MigrationBV52 [orgReportHome]
* **Options**
  + orgReporthome   
     The reporthome of the original Logi JReport Server. If the parameter is not provided, the reporthome of Logi JReport Server 16 will be used as its value.
* **Case 1: Installing Logi JReport Server 16 to a new folder (recommended)**
  1. Provided that the old Logi JReport Server is located in `C:\JREntServer580`. Install Logi JReport Server 16 to a new folder `C:\JReport\ServerV16`. DO NOT start the newly installed Logi JReport Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run `MigrationBV52 C:\JREntServer580`.
* **Case 2: Installing Logi JReport Server 16 to the folder where the old version resides**
  1. Provided that the old Logi JReport Server is located in `C:\JREntServer580`. Install Logi JReport Server 16 to the same location. DO NOT start the newly installed Logi JReport Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run MigrationBV52.bat.

## Upgrading in an Integration Environment

1. Upgrade your standalone Logi JReport Server. In this step you need not convert the old version reports.
2. Backup the dbconfig.xml file in `%REPORTHOME%\bin` and in `<UpgradedServer_install_root>\bin`. Copy the dbconfig.xml file in `%REPORTHOME%\bin` to replace the one in `<UpgradedServer_install_root>\bin`.
3. [Create a self-contained WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) jreport.war based on the upgraded Logi JReport Server. Make sure that the reporthome of the new jreport.war is the same as that of the previous jreport.war. Use -Dreporthome to specify the reporthome, for example:

   `makewar.bat buildWar -Dreporthome=C:\JReport`

   By default the reporthome location is <user.home>/.jreport/default. If you changed it when creating the previous war, you can find it in jreport.war/WEB-INF/web.xml by jreport.rpthome:

   ![Reporthome Location](https://devnet.logianalytics.com/hc/article_attachments/4412139537175/install_upgrd.gif)
4. Use application server Administrative Console to undeploy the previous jreport.war and redeploy the new jreport.war.
5. Clear the temporary files or cached files on the Java application server. Take Tomcat as an example, remove the temp and work directories in `D:\Tomcat`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691002-Logi-Report-Server-Reporthome-Directory-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717241-Migrating-Server-and-Server-Data)
