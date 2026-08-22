---
title: "Clearing Invalid Nodes from the Server Database"
id: 1500009673521
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673521-Clearing-Invalid-Nodes-from-the-Server-Database
updated_at: 2021-07-24T20:54:04Z
---

# Clearing Invalid Nodes from the Server Database

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673561-Viewing-the-Summary-Information-of-Archive-Files)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673541-Migrating-Server-Data-from-One-Machine-to-Another)

# Clearing Invalid Nodes From the Server Database

When resources, such as folders, catalogs, and reports, have been published using a [real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path), there is a possibility to produce invalid nodes. Also, after running a report and saving the result to the versioning system or scheduling reports which are saved in the versioning system, either of the following operations will generate invalid nodes:

* Cancel or change the real path setting.
* Publish a resource to replace an existing real path resource.

The invalid nodes are generated in the realm database. They are links to files in the history folder that no longer exist. To clear them:

1. On the Logi JReport Administration page, select **Data** on the system toolbar and then select **Realm DB** from the drop-down menu to open the Data - Realm DB page.
2. Select the **Realm DB Check** tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926694807/mng_data_clear.gif)
3. Select a realm from the Select Realm drop-down list at the top right corner.
4. Select the **Check** button. All invalid resource nodes are then listed.
5. Check the checkbox on the header of the first column to specify whether you want to select all or unselect all. Otherwise, you can check the corresponding checkbox to select the invalid nodes that you want to delete.
6. Select **Delete** button to delete all selected nodes.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673561-Viewing-the-Summary-Information-of-Archive-Files)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673541-Migrating-Server-Data-from-One-Machine-to-Another)
