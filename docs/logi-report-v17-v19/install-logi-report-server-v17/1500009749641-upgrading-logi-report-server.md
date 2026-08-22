---
title: "Upgrading Logi Report Server"
id: 1500009749641
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749641-Upgrading-Logi-Report-Server
updated_at: 2021-07-25T07:19:05Z
---

# Upgrading Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722622-Logi-Report-Server-Reporthome-Directory-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722642-Migrating-Server-and-Server-Data)

# Upgrading Logi Report Server

The topic introduces how to upgrade Logi Report Server in both standalone and integration environment. Upgrading a standalone Logi Report Server and an integrated Logi Report Server involves different processes while sharing some common steps. Both updated Logi Report Servers require converting the report resources in the old version in order to comply with the new server version.

Before upgrading, [back up your system database](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data#BackRestore) and shut down your Logi Report Server. If you want to use the old result files in `<install_root>\history`, install the new Logi Report Server to the same directory with a new license key, overriding the existing program files.

Select the following links to view the topics:

* [Upgrading in a Standalone Environment](#Standalone)
* [Upgrading in an Integration Environment](#Integ)

## Upgrading in a Standalone Environment

Logi Report Server provides two migration tools in `<install_root>\bin` folder, which can help you to convert all the resources on the previous version of Logi Report Server before version 6.0. Resources the migration tools cover include the security information (realm, user, group, protection, and ACL), report resources (catalog and reports), scheduled tables, completed tables, version and version tables, and other relevant information (such as fonts, NLS, and style groups). If you are upgrading from a release later than v6.0, these tools are not needed.

**Note:** When installing Logi Report Server v17 into the same directory as the old version, the report level resources in the old version will be maintained and not be replaced by the report resources of v17. For example, if you installed Logi Report Server v17 to `C:\Serverv13`, the backed up files of v13 will be maintained in `C:\Serverv13\bak\previous_version`, the removed patches and jar files will be maintained in `C:\Serverv13\bak\xxx\lib`, and the whole folder bin will be maintained in `C:\Serverv13\bak\xxx\bin`.

The following shows upgrading Logi Report Server from a specific old version to v17.

**Upgrading from v13 and later to v17**

The following shows upgrading Logi Report Server v13 to v17. It is assumed the old server is located in `C:\Serverv13.`

1. Install Logi Report Server v17 to `C:\Serverv13`. In the Choose Installation Set screen, choose **Typical Installation** for Standalone Server and select **Next**.
2. In the prompted Installation Warning message window, choose **Upgrading**.
3. The installation turns to the List screen which shows the details of the upgrading, including the removed patches, the modified config files and the backup files.
4. Select **Install** in the Installation Summary screen. After the installation is complete, start Logi Report Server to check the upgraded version.

**Upgrading from v6.0 and later to v17**

The following shows upgrading Logi Report Server v11.1 to v17. It is assumed the old server is located in `C:\Serverv11.1.`

1. Check the property values in dbconfig.xml which locates in `C:\Serverv11.1\bin` or back up the file first.
2. Install Logi Report Server v17 to `C:\Serverv11.1`. In the Choose Installation Set screen, choose **Typical Installation for Standalone Server** and select **Next**.
3. In the prompted Installation Warning message window, choose **Yes**.
4. In the System Database screen, input the property values according to the backed up dbconfig.xml file. Or select the **Trial Database** radio button, and replace dbconfig.xml file with the one you backed up.
5. In the List screen you can see the details of the upgrading, including the removed patches, the modified config files and the backup files.
6. Select **Install** in the Installation Summary screen. After the installation is complete, start Logi Report Server to check the upgraded version.

**Upgrading a version between v5.2 Build 590 and v6 (excluded) to v17**

You can make the upgrade using the migration tool MigrationV52.bat (MigrationV52.sh for Unix) that is available in the `<install_root>\bin` folder. This tool is used to convert all the resources of the versions between v5.2 Build 590 and v6 (excluded) to the resources of Logi Report Server v17. If you install the new version to the same folder as the old one, the parameter can be omitted.

* **Usage**  
   MigrationV52 [orgReportHome]
* **Options**
  + orgReporthome  
     The reporthome of the original Logi Report Server. If this parameter is not provided, the reporthome of Logi Report Server v17 will be used as its value.
* **Case 1: Installing Logi Report Server v17 to a new folder (recommended)**
  1. Assuming the old Logi Report Server is located in `C:\Serverv595`, install Logi Report Server v17 to a new folder `C:\Serverv17`. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run `MigrationV52 C:\Serverv595`.
* **Case 2: Installing Logi Report Server v17 to the folder where the old version resides**
  1. Assuming the old Logi Report Server is located in `C:\Serverv595`, install Logi Report Server v17 to the same location. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run MigrationV52.bat.

**Upgrading a version earlier than v5.2 Build 590 to v17**

You can do the upgrade using the migration tool MigrationBV52.bat (MigrationBV52.sh for Unix) that is available in the `<install_root>\bin` folder. This tool is used to convert all the resources of versions lower than v5.2 Build 590 to the resources of Logi Report Server v17. If you install the new version to the same folder as the old one, the parameter can be omitted.

* **Usage**  
   MigrationBV52 [orgReportHome]
* **Options**
  + orgReporthome   
     The reporthome of the original Logi Report Server. If the parameter is not provided, the reporthome of Logi Report Server v17 will be used as its value.
* **Case 1: Installing Logi Report Server v17 to a new folder (recommended)**
  1. Assuming the old Logi Report Server is located in `C:\Serverv580`, install Logi Report Server v17 to a new folder `C:\Serverv17`. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run `MigrationBV52 C:\Serverv580`.
* **Case 2: Installing Logi Report Server v17 to the folder where the old version resides**
  1. Assuming the old Logi Report Server is located in `C:\Serverv580`. Install Logi Report Server v17 to the same location. DO NOT start the newly installed Logi Report Server.
  2. In the DOS window, switch to `<install_root>\bin`, and run MigrationBV52.bat.

## Upgrading in an Integration Environment

1. Upgrade your standalone Logi Report Server. In this step you need not convert the old version reports.
2. Backup the dbconfig.xml file in `%REPORTHOME%\bin` and in `<UpgradedServer_install_root>\bin`. Copy the dbconfig.xml file in `%REPORTHOME%\bin` to replace the one in `<UpgradedServer_install_root>\bin`.
3. [Create a self-contained WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) jreport.war based on the upgraded Logi Report Server. Make sure that the reporthome of the new jreport.war is the same as that of the previous jreport.war. Use -Dreporthome to specify the reporthome, for example:

   `makewar.bat buildWar -Dreporthome=C:\LogiReport`

   By default the reporthome location is <user.home>/.jreport/default. If you changed it when creating the previous war, you can find it in jreport.war/WEB-INF/web.xml by jreport.rpthome:

   ![Reporthome Location](https://devnet.logianalytics.com/hc/article_attachments/4404942519191/install_upgrd.gif)
4. Use application server Administrative Console to undeploy the previous jreport.war and redeploy the new jreport.war.
5. Clear the temporary files or cached files on the Java application server. Take Tomcat as an example, remove the temp and work directories in `D:\Tomcat`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722622-Logi-Report-Server-Reporthome-Directory-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722642-Migrating-Server-and-Server-Data)
