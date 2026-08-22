---
title: "Migrating Server and Server Data"
id: 1500009776701
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776701-Migrating-Server-and-Server-Data
updated_at: 2021-07-24T00:48:06Z
---

# Migrating Server and Server Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748302-Upgrading-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748262-Uninstalling-Logi-Report-Server)

# Migrating Server and Server Data

This topic describes how you can migrate a whole server and server data.

This topic contains the following sections:

* [Migrating Server from One Machine to Another](#Server)
* [Migrating Server Data](#Data)
* [Migrating Server Data Between Docker Containers](#DataDocker)

## Migrating Server from One Machine to Another

You can migrate a Logi Report Server to another Server on other computers, by duplicating the environment of the Server. The migration procedure is divided into two parts: [migrating server system configurations](#Configuration) and [migrating server data between computers](#Data). This section describes the migration based on Windows. It also applies to other systems.

### Migrating Server System Configurations

When two Servers have the same license, same Logi Report and JDK versions, and different system databases, you can migrate the system configurations of the original Server on computer A to the target Server on computer B. The server system configurations that you can migrate include JVM class path, JVM heap size, other JVM options, patch, JDBC driver, customized classes (UDS, UDF, UDO, etc.), customized JSP, white label, configurations stored in files like server.properties, and so on.

**To synchronize the server system configurations:**

* If the following factors are the same on both Servers: operating system, the installation directories of the server, and JDK, copy all the .properties files and .ini files, JRServer.bat, setenv.bat, DBMaintain.bat, and datasource.xml from the **bin** folder of the original server's installation directory to the same location of the target server.
* Otherwise, copy the following files and folders from the installation directory of the original server to the same folder in the installation directory of the target server.
  + All the .properties files and .ini files, JRServer.bat, setenv.bat, DBMaintain.bat, and datasource.xml in `<install_root>\bin` if you have changed them.
  + The history, font, style folders including their subfolders in the installation directory.
  + All the additional classes (like JDBC driver) and customized JSP files.
  + If you applied patches on the original server, you need to apply the same patches on the target server.

### Migrating Server Data Between Computers

You can migrate data resources such as catalogs, reports, users, schedule tasks, and security from the original Server on computer A to the target Server on computer B, provided that the two servers use different databases. For example, when Server on computer A uses MySQL database f, Server on computer B cannot use database f unless the database is on different DB servers.

Take the following steps to migrate the server data between two computers:

1. [Back up the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009748642-Managing-Server-Data#Back) in the system, realm, and profiling databases of the Server on computer A.
2. Copy the files that you created in step 1 from computer A to computer B.
3. [Restore the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009748642-Managing-Server-Data#Restore) to the Server on computer B.
4. Start the Server on computer B. The migration will be completed.

If your server is V16 or above, you can [migrate the server data](#Data) in an easier way.

## Migrating Server Data

Server provides a migration tool for easy migration of server data to the same version or higher in the Windows/Linux command console. This is convenient when you want to install Server in a new location and continue to work with the data of an old server. The migration tool is MigrationTool.bat/MigrationTool.sh in the `<install_root>\bin` directory. The class of the tool is jet.server.tools.ServerDataMigration.

See the following parameters of the migration tool:

| Parameter | Description |
| --- | --- |
| -? | Print the help information. |
| -backup:<filename> | Back up the server data to a migration file, for example: `MigrationTool –backup:d:\tmp\bk.dat` |
| -restore:<filename> | Restore the server data from a migration file, for example: `MigrationTool –restore:d:\tmp\bk.dat` . |

To migrate server data using the migration tool, launch the tool in the old server to collect the server data and save it to a migration file, then launch the tool in the new server to read the server data from the migration file and save it to the server.

You can save the following server data information in a migration file:

* Server DB tables including system tables and realm tables
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

You can easily migrate the server data of a Server docker container, using the utility shell script **docker-container-migration.sh** in the `<install_root>\bin` directory.

You can use the utility script as follows:

`./docker-container-migration.sh [options]`

See the following properties of the utility script:

| Option | Description |
| --- | --- |
| -h, --help | Print the help information. |
| -l, --list | List all the containers on the host. |
| -cn, --container-name name | The container name or ID for the previous version of Server. This property is a must. |
| -ni, --new-image image | The new version of Server docker image. Default to logianalytics/logireport-server. |

To migrate server data between two Server docker containers, launch the script and provide the Server container names of both Server versions. When the migration finishes successfully, the server data of the old version will be available in the new version.

Assume that you have a previous version Server container named **server15.6** and want to migrate all its data to the new version Server container, do as follows:

1. Download the latest image of Server from <https://hub.docker.com/r/logianalytics/logireport-server/tags>. You can find all available versions on the page.

   `docker pull logianalytics/logireport-server:latest`
2. List all the containers on your host. Pick up the previous version Server container name. Here it is **server15.6**.

   `./docker-container-migration.sh -l`
3. Start the migration process.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)The previous version Server container stops during the process.

   `./docker-container-migration.sh -cn server15.6 -ni logianalytics/logireport-server:latest`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748302-Upgrading-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748262-Uninstalling-Logi-Report-Server)
