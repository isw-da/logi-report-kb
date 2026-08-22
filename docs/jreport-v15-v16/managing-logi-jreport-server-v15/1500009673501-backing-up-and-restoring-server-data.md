---
title: "Backing Up and Restoring Server Data"
id: 1500009673501
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data
updated_at: 2021-07-24T20:54:05Z
---

# Backing Up and Restoring Server Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648742-Checking-Server-Data-Integrity)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673481-Archiving-and-Restoring-Server-Data)

# Backing Up and Restoring Server Data

The server data backup process inspects all of the tables in the database, collecting and then exporting all table data to a ZipEntry. For tables such as the catalog version table, report version table, and report result version table, the data also includes relational real files from the history directory. All server data is compressed to a single Zip file, and all table data and every relational real file is stored as a ZipEntry in this single file.

The Backup and Restore feature does not support cross-platform operation. The backup and restore operations must be done on the same operating system. For example, if you backup the server data to a zip file on a Windows platform, you will then not be able to restore it on a Unix system.

Below is a list of the sections covered in this topic:

* [Backing Up Server Data](#Back)
* [Restoring Server Data](#Restore)

## Backing Up Server Data

You have two alternatives for backing up the server data: through the server user interface or through command line.

* **Backing up the server data through server user interface**
  1. On the Logi JReport Administration page, select **Data** on the system toolbar and then select **System DB**/**Realm DB**/**Profiling DB** from the drop-down menu to open the corresponding Data page.
  2. Select the **Backup** tab.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920492311/mng_data_back.gif)
  3. If you are backing up the realm or profiling database, select a realm from the Select Realm drop-down list at the top right corner.
  4. Type and select the **Browe** button to specify the file path and name of the backup file. The file extension should be included.
  5. If you are backing up the system database, the With External Data checkbox is available. Check it if you want the external data bound with the database which are the physical resources in the server resource tree to be archived at the same time.
  6. Select **Backup** to start the backup process. You will be prompted with the status upon finishing.
* **Backing up the server data through command line**

  A tool is provided to backup the server data. It is [DBMaintain.bat/DBMaintain.sh](https://devnet.logianalytics.com/hc/en-us/articles/1500009673341-Running-as-a-Standalone-Server#DBMaintain) in <`install_root>\bin`. It has two parameters:

  + -Bsystemtables/-Brealmtables/-Bprofiling: Backup the data with the server data in a Logi JReport cluster.
  + -B0realmtables: Only backup the data in the database.

  To back up the server data via the command line, take the following two steps:

  1. In a DOS window, switch to the  `<install_root>\bin` folder.
  2. Use the DBMaintain command (DBMaintain.sh on Unix/Linux) and -Bsystemtables/-Brealmtables/-Bprofiling or -B0realmtables parameter. For example:

     `C:\Logi JReport\Server\bin>DBMaintain -Brealmtables:C:\TEMP\cmd_b_realmtables.dat -Bprofiling:C:\TEMP\cmd_b_profiling.dat`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Restoring Server Data

The server data restore process picks up all table data from the backup file and inserts it into the corresponding table in the database. You can only restore server data using the DBMaintain tool with the -Rsystemtables/-Rrealmtables/-Rprofiling or -R0realmtables parameter.

1. In the DOS window, switch to the  `<install_root>\bin` folder.
2. Use the DBMaintain command and -Rsystemtables/-Rrealmtables/-Rprofiling or -R0realmtables parameter, for example:

   `C:\Logi JReport\Server\bin>DBMaintain -Rrealmtables:C:\TEMP\cmd_b_realmtables.dat -Rprofiling:C:\TEMP\cmd_b_profiling.dat`

**Notes:**

* When running DBMaintain.bat/DBMaintain.sh, error may occur if the backup zip file is too large, which is caused by JVM limitation. You can try the -B0realmtables and -R0realmtables options to backup and restore data separately.
* When backing up server data in a cluster environment, it is recommended that you back up the data on every cluster node to make sure no files get lost on any node after they are restored. Also, the system DB and realm DB should be backed up together. Since the external data cannot be backed up once just on one single cluster node, to avoid redundant data backup, you need to manually back up the external files on every cluster node after backing up the system DB and realm DB on any of the cluster nodes.
* When restoring server data in a cluster environment, first make sure all the cluster nodes are shut down, and then restore the data on each cluster node.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648742-Checking-Server-Data-Integrity)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673481-Archiving-and-Restoring-Server-Data)
