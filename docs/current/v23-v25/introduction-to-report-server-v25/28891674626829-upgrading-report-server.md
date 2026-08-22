---
title: "Upgrading Report Server"
id: 28891674626829
section: "Introduction to Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891674626829-Upgrading-Report-Server
updated_at: 2026-02-26T02:13:17Z
source_host: docs-report.zendesk.com
---
# 
Upgrading Report Server

This topic describes how you can upgrade Server in both standalone and integration environments. Upgrading a standalone Server and an integrated Server involves different processes while sharing some common steps. Both updated Servers require converting the report resources in the old version in order to comply with the new server version.

Before upgrading, back up your system database and shut down your Server. If you want to use the old report files in <install_root>\history, install the new Server to the same directory with a new license key, replacing the existing program files.

This topic contains the following sections:

- Upgrading Server in a Standalone Environment
                

- Upgrading Server in an Integration Environment
                

## 
Upgrading Server in a Standalone Environment

Server provides two migration tools in the <install_root>\bin folder, to convert the resources on the previous version of Server before version 6.0. Resources that the migration tools cover include the security information (realm, user, group, protection, and ACL), report resources (catalog and reports), scheduled tables, completed tables, versions, and version tables, and other relevant information (such as fonts, NLS, and style groups). If you are upgrading from a release later than v6.0, you do not need these tools. 

 When installing Server v25 into the same directory as the old version, Server maintains the report-level resources in the old version  and does not replace them with the report resources of v25. For example, if you install Server v25 to  C:\Serverv13, Server maintains the backup files of v13   in C:\Serverv13\bak\previous_version, the removed patches and jar files in C:\Serverv13\bak\xxx\lib, and the whole bin folder in C:\Serverv13\bak\xxx\bin.

The following sections show how to upgrade Server from a specific old version to v25.

Upgrading from v13 and later to v25

This section describes  how to upgrade Server v13 to v25. Assume that the old  server is in C:\Serverv13.

-  Install Server v25 to C:\Serverv13. 

- In the Choose Installation Set screen, choose Typical Installation for Standalone Server and select Next. 

- Server displays the  Installation Warning message window. Choose Upgrading. 

- The installation turns to the Lists screen which shows the details of the upgrading, including the removed patches, the modified configuration files, and the backup files. 

- Select Install in the Installation Summary screen. 

- After the installation is complete, start Server to check the upgraded version. 

Upgrading from v6.0 and later to v25

This section describes how to upgrade Server v11.1 to v25. Assume that the old server is in C:\Serverv11.1.

- Check the property values in dbconfig.xml in C:\Serverv11.1\bin or back up the file first.

-  Install Server v25 to C:\Serverv11.1. 

- In the Choose Installation Set screen, choose Typical Installation for Standalone Server and select Next. 

- Server displays the Installation Warning message window. Choose Yes. 

- In the System Database screen, input the property values according to the backup dbconfig.xml file. Or selectTrial Database and replace dbconfig.xml file with the one you backed up. 

- In the Lists screen you can see the details of the upgrading, including the removed patches, the modified configuration files, and the backup files. 

- Select Install in the Installation Summary screen. 

- After the installation is complete, start Server to check the upgraded version.

Upgrading a version between v5.2 Build 590 and v6 (excluded) to v25

You can make the upgrade using the migration tool MigrationV52.bat (MigrationV52.sh for UNIX) in the <install_root>\bin folder. You use this tool to convert the resources of the versions between v5.2 Build 590 and v6 (excluded) to the resources of Server v25. If you install the new version to the same folder as the old one, you can omit the orgReporthome parameter.

- 
Usage
    MigrationV52 [orgReportHome]

- 
Parameter- orgReporthome
          The report home of the original Server. If you do not provide this parameter, Server uses the report home of Server v25 as its value.

- 
Case 1: Installing Server v25 to a new folder (recommended)
- Assuming the old Server is in C:\Serverv595, install Server v25 to a new folder C:\Serverv25. DO NOT start the newly installed Server.

- In the DOS window, switch to <install_root>\bin and run MigrationV52 C:\Serverv595.

- 
Case 2: Installing Server v25 to the folder where the old version resides
- Assuming the old Server is in C:\Serverv595, install Server v25 to the same location. DO NOT start the newly installed Server.

- In the DOS window, switch to <install_root>\bin and run MigrationV52.bat.

Upgrading a version earlier than v5.2 Build 590 to v25

You can do the upgrade using the migration tool MigrationBV52.bat (MigrationBV52.sh for UNIX) in the <install_root>\bin folder. You use this tool to convert the resources of versions lower than v5.2 Build 590 to the resources of Server v25. If you install the new version to the same folder as the old one, you can omit the orgReporthome parameter.

- 
Usage
    MigrationBV52 [orgReportHome]

- 
Parameter- orgReporthome 
          The report home of the original Server. If you do not provide the parameter, Server uses the report home of Server v25 as its value.

- 
Case 1: Installing Server v25 to a new folder (recommended)
- Assuming the old Server is in C:\Serverv580, install Server v25 to a new folder C:\Serverv25. DO NOT start the newly installed Server.

- In the DOS window, switch to <install_root>\bin and run MigrationBV52 C:\Serverv580.

- 
Case 2: Installing Server v25 to the folder where the old version resides
- Assuming the old Server is in C:\Serverv580, install Server v25 to the same location. DO NOT start the newly installed Server.

- In the DOS window, switch to <install_root>\bin and run MigrationBV52.bat.

## 
Upgrading Server in an Integration Environment

- Upgrade your standalone Server. In this step you need not convert the old version reports. 

- Back up the dbconfig.xml file in %REPORTHOME%\bin and in <UpgradedServer_install_root>\bin. 

- Copy the dbconfig.xml file in %REPORTHOME%\bin to replace the one in <UpgradedServer_install_root>\bin.

- 
Create a self-contained WAR/EAR filejreport.war based on the upgraded Server. Make sure that the report home of the new jreport.war is the same as that of the previous jreport.war. Use -Dreporthome to specify the report home, for example: 
    makewar.bat buildWar -Dreporthome=C:\LogiReport

By default, the report home location is <user.home>/.jreport/default. If you changed it when creating the previous war, you can find it in jreport.war/WEB-INF/web.xml by jreport.rpthome:

- Use your application server Administrative Console to undeploy the previous jreport.war and redeploy the new jreport.war.

- Clear the temporary files or cached files on the Java application server. Take Tomcat as an example, remove the temp and work folders in D:\Tomcat.

 If you want to change property values in server.properties in an integration environment after you upgrade Report Server to v18.2 or later, do as follows:

- Make sure you do not start the upgraded Server after the upgrade.

- Create a Report Server WAR, for example, jreport.war.

- Create a file named install.server.properties.

- Add the key and value pairs of the properties you want to change in install.server.properties.

- Add install.server.properties in jreport.war\WEB-INF\lib\jrenv.jar\workspace\bin.

- Deploy Report Server WAR to your application server. 

- Start your application server. Report Server will load the property values from  install.server.properties, replace the values of the same properties in server.properties, and remove the install.server.properties file.
