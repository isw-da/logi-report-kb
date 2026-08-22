---
title: "Migrating Server and Server Data"
id: 1500009722642
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722642-Migrating-Server-and-Server-Data
updated_at: 2021-07-25T07:19:06Z
---

# Migrating Server and Server Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749641-Upgrading-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749601-Uninstalling-Logi-Report-Server)

# Migrating Server and Server Data

This topic introduces how to migrate a whole server and server data.

Select the following links to view the topics:

* [Migrating Server from One Machine to Another](#Server)
* [Migrating Server Data](#Data)
* [Migrating Server Data Between Docker Containers](#DataDocker)

## Migrating Server from One Machine to Another

By duplicating the environment of a Logi Report Server, you can migrate the server to another Logi Report Server on other computers. The migration procedure is divided into two parts: [migrating server system configurations](#Configuration) and [migrating server data between computers](#Data). This document explains the migration based on Windows. It also applies to other systems.

### Migrating Server System Configurations

When two Logi Report Servers have the same license, same Logi Report and JDK versions, and different system databases, you can migrate the system configurations of the original Logi Report Server on computer A to the target Logi Report Server on computer B. The server system configurations that can be migrated include JVM class path, JVM heap size, other JVM options, patch, JDBC driver, customized classes (UDS, UDF, UDO, etc.), customized JSP, white label, configurations stored in files like server.properties, and so on.

**To synchronize the server system configurations:**

* If the following are the same on both Logi Report Servers: operating system and the installation directories of the server and JDK, copy all the .properties files and .ini files, JRServer.bat, setenv.bat, DBMaintain.bat, and datasource.xml from the bin folder of the original server's installation directory to the same location of the target server.
* Otherwise, copy the following files and folders from the installation directory of the original server to the same folder in the installation directory of the target server.
  + All the .properties files and .ini files, JRServer.bat, setenv.bat, DBMaintain.bat, and datasource.xml in `<install_root>\bin` if they are changed.
  + The history, font, style folders including their subfolders in the installation directory.
  + All the additional classes (like JDBC driver) and customized JSP files.
  + If you applied patches on the original server, you need to apply the same patches on the target server.

### Migrating Server Data Between Computers

Data resources such as catalogs, reports, users, schedule tasks, security, and so on can be migrated from the original Logi Report Server on computer A to the target Logi Report Server on computer B, provided that the two servers use different databases. For example, when Logi Report Server on computer A uses MySQL database f, Logi Report Server on computer B cannot use database f unless the database is on different DB servers.

Take the following steps to migrate the server data between two computers:

1. [Back up the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data#Back) in the system, realm and profiling databases of the Logi Report Server on computer A.
2. Copy the files created in step 1 from computer A to computer B.
3. [Restore the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data#Restore) to the Logi Report Server on computer B.
4. Start the Logi Report Server on computer B. The migration will be completed.

If your server is V16 or above, you can [migrate the server data](#Data) in an easier way.

## Migrating Server Data

Logi Report Server provides a migration tool for easy migration of server data to the same version or higher in the Windows/Linux command console. This is convenient when you want to install Logi Report Server in a new location and continue to work with the data of an old server. The migration tool is MigrationTool.bat/MigrationTool.sh located in the `<install_root>\bin` directory. The class of the tool is jet.server.tools.ServerDataMigration.

The following are the parameters of the migration tool:

| Parameter | Description |
| --- | --- |
| -? | Prints the help information. |
| -backup:<filename> | Backups the server data to a migration file, for example: `MigrationTool –backup:d:\tmp\bk.dat` |
| -restore:<filename> | Restores the server data from a migration file, for example: `MigrationTool –restore:d:\tmp\bk.dat` . |

To migrate server data using the migration tool, launch the tool in the old server to collect the server data and save it to a migration file, then launch the tool in the new server to read the server data from the migration file and save it to the server.

The following server data information can be saved in a migration file:

* Logi Report Server DB tables including system tables and realm tables
* The following files in `<install_root>\bin`:
  + classes.properties
  + ConnectionPoolConfig.properties
  + content-type.properties
  + datasource.xml
  + dbconfig.xml
  + dhtml.properties
  + faxconfig.properties
  + formulaConfig.properties
  + interactiveReportPrecisionMapping.xml
  + jdbcdrivers.properties
  + JdbcDriversConfig.properties
  + jgroups.xml
  + LogConfig.properties
  + mailconfig.properties
  + mapConfiguration.xml
  + mapping.properties
  + plugin.properties
  + quartz.properties
  + redirect.properties
  + server.properties
  + servlet.properties
* The following folders in the server installation root directory:
  + cache
  + font
  + gisinfo
  + plugins
  + properties
  + realm
  + style
  + templates

## Migrating Server Data Between Docker Containers

Using the utility shell script docker-container-migration.sh located in the `<install_root>\bin` directory, you can easily migrate the server data of a Logi Report Server docker container.

The usage of the utility script is:

`./docker-container-migration.sh [options]`

The following are the options of the utility script:

| Option | Description |
| --- | --- |
| -h, --help | Prints the help information. |
| -l, --list | Lists all the containers on the host. |
| -cn, --container-name name | The container name or ID for the previous version of Logi Report Server. Required. |
| -ni, --new-image image | The new version of Logi Report Server docker image. Default to logianalytics/logireport-server. |

To migrate server data between Logi Report Server docker containers, launch the script and provide the Logi Report Server container names of the old version and new version. When finished successfully, the server data of the old version will be available in the new version.

Assume that you have a previous version Logi Report Server container named server15.6 and want to migrate all its data to the new version Logi Report Server container, do as follows:

1. Download the latest image of Logi Report Server from <https://hub.docker.com/r/logianalytics/logireport-server/tags>. You can find all available versions on the page.

   `docker pull logianalytics/logireport-server:latest`
2. List all the containers on your host. Pick up the previous version Logi Report Server container name, here it is server15.6.

   `./docker-container-migration.sh -l`
3. Start the migration process. Note that the previous version Logi Report Server container will be stopped during the process.

   `./docker-container-migration.sh -cn server15.6 -ni logianalytics/logireport-server:latest`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749641-Upgrading-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749601-Uninstalling-Logi-Report-Server)
