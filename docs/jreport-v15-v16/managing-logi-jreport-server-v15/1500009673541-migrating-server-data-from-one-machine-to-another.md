---
title: "Migrating Server Data from One Machine to Another"
id: 1500009673541
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673541-Migrating-Server-Data-from-One-Machine-to-Another
updated_at: 2021-07-24T20:54:04Z
---

# Migrating Server Data from One Machine to Another

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673521-Clearing-Invalid-Nodes-from-the-Server-Database)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673381-Managing-Cached-Report-Data)

# Migrating Server Data From One Machine to Another

Logi JReport Server resources such as catalogs, reports, users, security, scheduling, etc. can be migrated from one computer to another by simply [Backing up and Restoring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data).

To migrate Logi JReport Server from the development environment on computer A to the production environment on computer B, you need to back up the server database data on computer A, move the backup files to computer B, and then restore the backup data to the server on computer B. You cannot migrate from one platform to another, for examples Windows to Linux or Linux to Windows.

The following example is based on Windows:

1. Back up the server database data including system, realm and profiling databases on computer A. Choose either of the following methods:
   * Use [DBMaintain.bat](https://devnet.logianalytics.com/hc/en-us/articles/1500009673341-Running-as-a-Standalone-Server#DBMaintain) under `<server_install_root>\bin` on computer A. In a DOS window, switch to the `<server_install_root>\bin` folder and run the following commands:

     `DBMaintain -Bsystemtables:C:\temp\systemtables.dat -Brealmtables:C:\temp\realmtables.dat -Bprofiling:C:\temp\profiling.dat`
   * Admin users can back up data on the Logi JReport Administration page.

     Backing up the system database: on the Logi JReport Administration page, select **Data** > **System DB** on the system toolbar. Then go to the Backup tab, specify a file location and select the **Backup** button.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920490519/mng_data_mgrt_sys.gif)

     Backing up the realm database: on the Logi JReport Administration page, select **Data** > **Realm DB**. Then go to the Backup tab, specify a file location, check **With External Data**, then select the **Backup** button. In order to make resources usable you must backup the files with external data. If With External Data is unchecked, your resources will be visible in the server resource tree of the new server but none of the physical files will be in the history folder of the new server so they will fail with file not found errors.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920491287/mng_data_mgrt_rlm.gif)

     Backing up the profiling database: on the Logi JReport Administration page, select **Data** > **Profiling DB**. Then go to the Backup tab, specify a file location and select the **Backup** button. Normally it would not be necessary to backup and restore the profiling database as it only contains records about reports run on the current server, which may not be useful on the new server.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920491927/mng_data_mgrt_prfl.gif)
2. Install Logi JReport Server on computer B and then configure the server database. Note that the server databases on both computer A and B must be different. For example, when computer A uses MySQL database f, then computer B cannot use database f unless they are on different servers.
3. Copy the files created in the step 1 from computer A to the D disk on computer B:

   D:\systemtables.dat   
    D:\realmtables.dat   
    D:\profiling.dat
4. Restore the server database data using [DBMaintain.bat](https://devnet.logianalytics.com/hc/en-us/articles/1500009673341-Running-as-a-Standalone-Server#DBMaintain) in `<server_install_root>\bin` on computer B. In a DOS window switch to the `<server_install_root>\bin` folder, and then run the following commands:

   `DBMaintain -Rrealmtables:D:\realmtables.dat -Rprofiling:D:\profiling.dat -Rsystemtables:D:\systemtables.dat`
5. Start the server on computer B. The migration will be completed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673521-Clearing-Invalid-Nodes-from-the-Server-Database)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673381-Managing-Cached-Report-Data)
