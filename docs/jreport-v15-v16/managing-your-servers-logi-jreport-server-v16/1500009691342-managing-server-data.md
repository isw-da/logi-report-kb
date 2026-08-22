---
title: "Managing Server Data"
id: 1500009691342
section: "Managing Your Servers Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691342-Managing-Server-Data
updated_at: 2021-11-03T06:56:55Z
---

# Managing Server Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691382-Managing-Tasks)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717701-Managing-Cached-Report-Data)

# Managing Server Data

During its running process, Logi JReport Server keeps track of server information and stores it to its own database for the purpose of running various managing and monitoring tasks, such as managing the resources on the server, monitoring the task running status, and collecting server running statistics.

The server database includes system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties, global NLS, and so on. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information. You can refer to
[Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database) for details about how to configure the databases.

This topic shows managing server data as follows. You must be an admin user in order to access the Administration page of the server console to perform the tasks.

* [Backing Up and Restoring Server Data](#BackRestore)
* [Archiving and Restoring Server Data](#Archive)
* [Viewing the Summary Information of Archive Files](#View)
* [Clearing Invalid Nodes from the Server Database](#Clear)
* [Checking Server Data Integrity](#Check)

## Backing Up and Restoring Server Data

The server data backup process inspects all of the tables in the database, collecting and then exporting all table data to a ZipEntry. For tables such as the catalog version table, report version table, and report result version table, the data also includes relational real files from the history directory. All server data is compressed to a single Zip file, and all table data and every relational real file is stored as a ZipEntry in this single file.

The Backup and Restore feature supports cross-platform case, for example, you can back up the server data to a zip file on a Windows platform and then restore it on a Linux/Unix system.

**To back up server data:**

You have two alternatives for backing up the server data: through the server console or through command line.

* **Backing up the server data via server console**
  1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **System DB**/**Realm DB**/**Profiling DB** from the drop-down menu to open the corresponding page.
  2. Select the **Backup** tab.

     ![Backup tab](https://devnet.logianalytics.com/hc/article_attachments/4412131438487/mng_data_back.gif)
  3. If you are backing up the realm or profiling database, select a realm from the Select Realm drop-down list at the top right corner.
  4. Type and select the **Browe** button to specify the file path and name of the backup file. The file extension should be included.
  5. If you are backing up the system database, the With External Data checkbox is available. Check it if you want the external data bound with the database which are the physical resources in the server resource tree to be archived at the same time.
  6. Select **Backup** to start the backup process. You will be prompted with the status upon finishing.
* **Backing up the server data by command line**

  A tool is provided to backup the server data. It is [DBMaintain.bat/DBMaintain.sh](https://devnet.logianalytics.com/hc/en-us/articles/1500009691282-Running-as-a-Standalone-Server#DBMaintain) in <`install_root>\bin`. It has two parameters:

  + -Bsystemtables/-Brealmtables/-Bprofiling: Backup the data with the server data in a Logi JReport Server Cluster.
  + -B0realmtables: Only backup the data in the database.

  To back up the server data via the command line, take the following two steps:

  1. In a DOS window, switch to the  `<install_root>\bin` folder.
  2. Use the DBMaintain command and -Bsystemtables/-Brealmtables/-Bprofiling or -B0realmtables parameter. For example:

     `C:\JReport\Server\bin>DBMaintain -Brealmtables:C:\TEMP\cmd_b_realmtables.dat -Bprofiling:C:\TEMP\cmd_b_profiling.dat`

**To restore server data:**

The server data restore process picks up all table data from the backup file and inserts it into the corresponding table in the database. You can only restore server data using the DBMaintain tool with the -Rsystemtables/-Rrealmtables/-Rprofiling or -R0realmtables parameter.

1. In the DOS window, switch to the  `<install_root>\bin` folder.
2. Use the DBMaintain command and -Rsystemtables/-Rrealmtables/-Rprofiling or -R0realmtables parameter, for example:

   `C:\JReport\Server\bin>DBMaintain -Rrealmtables:C:\TEMP\cmd_b_realmtables.dat -Rprofiling:C:\TEMP\cmd_b_profiling.dat`

**Notes:**

* When running DBMaintain.bat/DBMaintain.sh, error may occur if the backup zip file is too large, which is caused by JVM limitation. You can try the -B0realmtables and -R0realmtables options to backup and restore data separately.
* When backing up server data in a cluster environment, it is recommended that you back up the data on every cluster node to make sure no files get lost on any node after they are restored. Also, the system DB and realm DB should be backed up together. Since the external data cannot be backed up once just on one single cluster node, to avoid redundant data backup, you need to manually back up the external files on every cluster node after backing up the system DB and realm DB on any of the cluster nodes.
* When restoring server data in a cluster environment, first make sure all the cluster nodes are shut down, and then restore the data on each cluster node.

## Archiving and Restoring Server Data

Along with the running of the server, the sizes of the result version table (DB: realm) and TaskContext table (DB: profiling) grow larger. Logi JReport Server allows you to archive data to a single backup file then automatically delete it from the database. You can then retrieve the data from the backup file at a later date. However you can only restore server data from an archive file that is archived using the same server version.

Only administrators can archive and restore server data in the realm and profiling databases.

**To archive the server data:**

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **Realm DB**/**Profiling DB** from the drop-down menu.
2. In the Realm DB/Profiling DB page, switch to the **Archive** tab.

   ![Archive tab](https://devnet.logianalytics.com/hc/article_attachments/4412131438743/mng_data_archive.gif)
3. Select a realm from the Select Realm drop-down list at the top right corner.
4. In the Archive Result Version Data panel, the Data Scope text box displays the result version data range and Records Count shows the number of sets of result version data in the database.
5. In the Move to Archive Data Before text box, specify the range of data you want to archive. The range is defined using date, for example, you can archive data before a certain date.
6. Type or select the **Browse** button to specify the file path and name for the archive file.

   If you don't want to backup the archived server data, leave this field blank. The server data will then be removed from the database.
7. Select **Archive**. Server data prior to the specified date will be archived and saved to the archive file using the name specified and the same data will be deleted from the database.

**To restore the archived server data:**

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **Realm DB**/**Profiling DB** from the drop-down menu.
2. In the Realm DB/Profiling DB page, switch to the **Archive** tab.
3. Select a realm from the Select Realm drop-down list.
4. In the Restore Result Version Data panel, type or select the **Browse** button to provide the archive file name and location in the Restore from Archive text box.
5. Select **Restore** to restore the specified data.

## Viewing the Summary Information of Archive Files

After archiving or backing up the realm and profiling databases, you can view the results. The summary information includes Archive, Date, Type, Version, Realm, Database and Scope.

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **Realm DB**/**Profiling DB** from the drop-down menu.
2. In the Realm DB/Profiling DB page, switch to the **Summary** tab.

   ![Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4412112562839/mng_data_view.gif)
3. Select a realm from the Select Realm drop-down list at the top right corner.
4. In the Archive text box, type or select the **Browse** button to specify the data file from which you want to retrieve summary information.
5. Select **Summary**. Logi JReport then begins the summary process and returns summary information about the specified file.

## Clearing Invalid Nodes from the Server Database

When resources, such as folders, catalogs, and reports, have been published using a [real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009717881-Getting-and-Using-Resources-from-a-Real-Path), there is a possibility to produce invalid nodes. Also, after running a report and saving the result to the versioning system or scheduling reports which are saved in the versioning system, either of the following operations will generate invalid nodes:

* Cancel or change the real path setting.
* Publish a resource to replace an existing real path resource.

The invalid nodes are generated in the realm database. They are links to files in the history folder that no longer exist. To clear them:

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **Server DB** > **Realm DB** from the drop-down menu. The Realm DB page is displayed.
2. Select the **Realm DB Check** tab.

   ![Realm DB Check tab](https://devnet.logianalytics.com/hc/article_attachments/4412112563095/mng_data_clear.gif)
3. Select a realm from the Select Realm drop-down list at the top right corner.
4. Select the **Check** button. All invalid resource nodes are then listed.
5. Check the invalid resource nodes you want to delete. To select all the resource nodes, check the checkbox on the top.
6. Select the **Delete** button to delete the selected nodes.

## Checking Server Data Integrity

In abnormal circumstances, server data may not be saved correctly or completely in the database. Logi JReport Server allows you to check the integrity of server data.

The integrity check mainly examines two aspects of the realm database:

* Integrity and consistency among tables. This is to see whether the records among the tables are complete and consistent.
* Integrity and consistency between realm database and the external files. This is to see whether the records in the tables match the related external files.

If any inconsistent or incomplete server data is found, it will be removed from the realm database since it is unused. The same process will also apply to files.

To check server data integrity, do one of the following:

* Launch Logi JReport Server on the command line with the -cleanup parameter. For example:

  `C:\JReport\Server\bin>JRServer -cleanup`
* Open the batch file JRServer.bat stored in `<install_root>\bin`, add the parameter -Dcheck.realmtables=true as follows, then start Logi JReport Server with the edited batch file.

  `"%JAVAHOME%\bin\java.exe" @"%REPORTHOME%\bin\java.option" -Dcheck.realmtables=true -Dinstall.root="%REPORTHOME%"...`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691382-Managing-Tasks)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717701-Managing-Cached-Report-Data)
