---
title: "Archiving and Restoring Server Data"
id: 1500009673481
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673481-Archiving-and-Restoring-Server-Data
updated_at: 2021-07-24T20:54:05Z
---

# Archiving and Restoring Server Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673561-Viewing-the-Summary-Information-of-Archive-Files)

# Archiving and Restoring Server Data

Administrators can archive and restore server data in the realm and profiling databases.

Below is a list of the sections covered in this topic:

* [Archiving Server Data](#Archive)
* [Restoring the Archived Server Data](#Restore)

## Archiving Server Data

Along with the running of the server, the sizes of the result version table (DB: realm) and TaskContext table (DB: profiling) grow larger. Logi JReport Server allows you to archive data to a single backup file then automatically delete it from the database. You can then retrieve the data from the backup file at a later date.

**To archive the server data:**

1. On the Logi JReport Administration page, select **Data** on the system toolbar and then select **Realm DB**/**Profiling DB** from the drop-down menu to open the corresponding Data page.
2. Switch to the **Archive** tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920492823/mng_data_archive.gif)
3. Select a realm from the Select Realm drop-down list at the top right corner.
4. In the Archive Result Version Data panel, the Data Scope text field displays the result version data range and Records Count shows the number of sets of result version data in the database.
5. In the Move to Archive Data Before text field, specify the range of data you want to archive. The range is defined using date, for example, you can archive data before a certain date.
6. Type or select the **Browse** button to specify the file path and name for the archive file.

   If you don't want to backup the archived server data, leave this field blank. The server data will then be removed from the database.
7. Select **Archive**. Server data prior to the specified date will be archived and saved to the archive file using the name specified and the same data will be deleted from the database.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Restoring the Archived Server Data

After data has been saved to an archive file, you then have the option to restore it. However, you can only restore server data from an archive file that is archived using the same server version.

**To restore the archived server data:**

1. On the Logi JReport Administration page, select **Data** on the system toolbar and then select **Realm DB**/**Profiling DB** from the drop-down menu.
2. Select a realm from the Select Realm drop-down list.
3. Switch to the **Archive** tab.
4. In the Restore Result Version Data panel, type or select the **Browse** button to provide the archive file name and location in the Restore from Archive text field.
5. Select **Restore** to restore the specified data.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673561-Viewing-the-Summary-Information-of-Archive-Files)
