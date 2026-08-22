---
title: "Upgrading Logi Report Server"
id: 1500009748302
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748302-Upgrading-Logi-Report-Server
updated_at: 2021-07-24T00:48:06Z
---

# Upgrading Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748242--Server-Report-Home-Directory-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776701-Migrating-Server-and-Server-Data)

# Upgrading Logi Report Server

This topic describes how you can upgrade Server in both standalone and integration environment. Upgrading a standalone Server and an integrated Server involves different processes while sharing some common steps. Both updated Servers require converting the report resources in the old version in order to comply with the new server version.

Before upgrading, [back up your system database](https://devnet.logianalytics.com/hc/en-us/articles/1500009748642-Managing-Server-Data#BackRestore) and shut down your Server. If you want to use the old result files in `<install_root>\history`, install the new Server to the same directory with a new license key, overriding the existing program files.

This topic contains the following sections:

* [Upgrading Server in a Standalone Environment](#Standalone)
* [Upgrading Server in an Integration Environment](#Integ)

## Upgrading Server in a Standalone Environment

Server provides two migration tools in `<install_root>\bin` folder, to convert the resources on the previous version of Server before version 6.0. Resources that the migration tools cover include the security information (realm, user, group, protection, and ACL), report resources (catalog and reports), scheduled tables, completed tables, versions and version tables, and other relevant information (such as fonts, NLS, and style groups). If you are upgrading from a release later than v6.0, you do not need these tools.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When installing Server v17.1 into the same directory as the old version, the report level resources in the old version will be maintained and not be replaced by the report resources of v17.1. For example, if you installed Server v17.1 to `C:\Serverv13`, the backup files of v13 will be maintained in `C:\Serverv13\bak\previous_version`, the removed patches and jar files will be maintained in `C:\Serverv13\bak\xxx\lib`, and the whole folder **bin** will be maintained in `C:\Serverv13\bak\xxx\bin`.

The following sections shows how to upgrade Server from a specific old version to v17.1.

**Upgrading from v13 and later to v17.1**

This section shows how to upgrade Server v13 to v17.1. Assume that the old server is located in `C:\Serverv13.`

1. Install Server v17.1 to `C:\Serverv13`. In the Choose Installation Set screen, choose **Typical Installation for Standalone Server** and select **Next**.
2. Server displays the Installation Warning message window. Choose **Upgrading**.
3. The installation turns to the Lists screen which shows the details of the upgrading, including the removed patches, the modified configuration files, and the backup files.
4. Select **Install** in the Installation Summary screen.
5. After the installation is complete, start Server to check the upgraded version.

**Upgrading from v6.0 and later to v17.1**

This section shows how to upgrade Server v11.1 to v17.1. Assume that the old server is located in `C:\Serverv11.1.`

1. Check the property values in **dbconfig.xml** in `C:\Serverv11.1\bin` or back up the file first.
2. Install Server v17.1 to `C:\Serverv11.1`. In the Choose Installation Set screen, choose **Typical Installation for Standalone Server** and select **Next**.
3. Server displays the Installation Warning message window. Choose **Yes**.
4. In the System Database screen, input the property values according to the backed up dbconfig.xml file. Or select the **Trial Database** radio button and replace dbconfig.xml file with the one you backed up.
5. In the Lists screen you can see the details of the upgrading, including the removed patches, the modified configuration files, and the backup files.
6. Select **Install** in the Installation Summary screen.
7. After the installation is complete, start Server to check the upgraded version.

**Upgrading a version between v5.2 Build 590 and v6 (excluded) to v17.1**

You can make the upgrade using the migration tool MigrationV52.bat (MigrationV52.sh for Unix) in the `<install_root>\bin` folder. This tool is used to convert the resources of the versions between v5.2 Build 590 and v6 (excluded) to the resources of Server v17.1. If you install the new version to the same folder as the old one, you can omit the parameter **orgReporthome**.

* **Usage**  
   MigrationV52 [orgReportHome]
* **Parameter**
  + orgReporthome  
     The report home of the original Server. If you do not provide this parameter, Server uses the report home of Server v17.1 as its value.
* **Case 1: Installing Server v17.1 to a new folder (recommended)**
  1. Assuming the old Server is located in `C:\Serverv595`, install Server v17.1 to a new folder `C:\Serverv17.1`. DO NOT start the newly installed Server.
  2. In the DOS window, switch to `<install_root>\bin` and run `MigrationV52 C:\Serverv595`.
* **Case 2: Installing Server v17.1 to the folder where the old version resides**
  1. Assuming the old Server is located in `C:\Serverv595`, install Server v17.1 to the same location. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin` and run MigrationV52.bat.

**Upgrading a version earlier than v5.2 Build 590 to v17.1**

You can do the upgrade using the migration tool MigrationBV52.bat (MigrationBV52.sh for Unix) in the `<install_root>\bin` folder. This tool is used to convert the resources of versions lower than v5.2 Build 590 to the resources of Server v17.1. If you install the new version to the same folder as the old one, you can omit the parameter **orgReporthome**.

* **Usage**  
   MigrationBV52 [orgReportHome]
* **Parameter**
  + orgReporthome   
     The report home of the original Server. If you do not provide the parameter, Server uses the report home of Server v17.1 as its value.
* **Case 1: Installing Server v17.1 to a new folder (recommended)**
  1. Assuming the old Server is located in `C:\Serverv580`, install Server v17.1 to a new folder `C:\Serverv17.1`. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin` and run `MigrationBV52 C:\Serverv580`.
* **Case 2: Installing Server v17.1 to the folder where the old version resides**
  1. Assuming the old Server is located in `C:\Serverv580`, install Server v17.1 to the same location. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin` and run MigrationBV52.bat.

## Upgrading Server in an Integration Environment

1. Upgrade your standalone Server. In this step you need not convert the old version reports.
2. Back up the **dbconfig.xml** file in `%REPORTHOME%\bin` and in `<UpgradedServer_install_root>\bin`. Copy the dbconfig.xml file in `%REPORTHOME%\bin` to replace the one in `<UpgradedServer_install_root>\bin`.
3. [Create a self-contained WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)**jreport.war** based on the upgraded Server. Make sure that the report home of the new jreport.war is the same as that of the previous jreport.war. Use **-Dreporthome** to specify the report home, for example:

   `makewar.bat buildWar -Dreporthome=C:\LogiReport`

   By default, the report home location is <user.home>/.jreport/default. If you changed it when creating the previous war, you can find it in jreport.war/WEB-INF/web.xml by **jreport.rpthome**:

   ![Reporthome Location](https://devnet.logianalytics.com/hc/article_attachments/4404885430807/install_upgrd.gif)
4. Use your application server Administrative Console to undeploy the previous jreport.war and redeploy the new jreport.war.
5. Clear the temporary files or cached files on the Java application server. Take Tomcat as an example, remove the temp and work directories in `D:\Tomcat`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748242--Server-Report-Home-Directory-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776701-Migrating-Server-and-Server-Data)
