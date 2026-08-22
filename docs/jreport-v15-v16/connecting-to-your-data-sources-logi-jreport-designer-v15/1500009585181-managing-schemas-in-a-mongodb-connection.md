---
title: "Managing Schemas in a MongoDB Connection"
id: 1500009585181
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585181-Managing-Schemas-in-a-MongoDB-Connection
updated_at: 2021-07-24T05:55:46Z
---

# Managing Schemas in a MongoDB Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564182-Setting-Up-a-MongoDB-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584781-HIVE-Connections)

# Managing Schemas in a MongoDB Connection

When a MongoDB connection is set up, the collection schemas in the MongoDB data source are transformed to relational schemas and can be used in Logi JReport. You can manage the schemas in the Logi JReport catalog as shown in this topic.

You can also manage the tables transformed from the MongoDB data source the same as you do with tables from an XML data source. For example, you can add more tables via the MongoDB connection into the Logi JReport catalog, remove undesired table columns, organizing the tables into folder and refreshing the tables. For details, see [Managing Tables in an XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585461-Managing-Tables-in-an-XML-Connection).

Below is a list of the sections covered in this topic:

> * [Adding Schemas](#Add)
> * [Refreshing Schemas](#Refresh)
> * [Renaming and Deleting Databases of Schemas](#Rename)

## Adding Schemas

To add relational schemas which are transformed from the collection schemas in a MongoDB data source to the Logi JReport catalog via a MongoDB connection, follow the steps below:

1. Right-click the **Schemas** node or an existing schema in the MongoDB connection and select **Add Collection**  from the shortcut menu to display the [Add Collection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585501-Add-Collection-Dialog) dialog.

   ![Add Collection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889392791/addclctn.gif)
2. Select the required collections in the schemas that are transformed from the collection schemas in the Schema box and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add them to the Added Schema box.
3. After adding the required collection schemas, select **OK** to close the dialog.

## Refreshing Schemas

The schemas in your catalog are a temporary cache of metadata to improve performance when you design and test your report. Your data source will probably change over the time; however, these changes will not be reflected automatically in your catalog. To refresh all of the collection schema metadata from the MongoDB database, you can choose to refresh the schema information using the Refresh command on the shortcut menu of the schema. When the refreshing job is done, a reporting dialog will be shown, summarizing the changes and operations that have been taken.

## Renaming and Deleting Databases of Schemas

* To rename the database of the schemas, right-click the database and select **Rename** from the shortcut menu, and then input the required database name in the text box.
  + If the renamed database exists in the MongoDB data source, it will connect to the new database.
  + If the renamed database does not exist in the MongoDB data source, no data will be retrieved.
* To delete the database of the schemas, right-click the database and select **Delete** from the shortcut menu.

**Tip:** If you want to add all the deleted or missing databases at one time, you can choose to refresh the schema, which refreshes all of the collection schema metadata from the MongoDB database.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564182-Setting-Up-a-MongoDB-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584781-HIVE-Connections)
