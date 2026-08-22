---
title: "Managing Tables in an XML Connection"
id: 1500009585461
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585461-Managing-Tables-in-an-XML-Connection
updated_at: 2021-07-24T05:55:41Z
---

# Managing Tables in an XML Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585441-Setting-Up-an-XML-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585161-MongoDB-Connections)

# Managing Tables in an XML Connection

A table contains fields mapped to attributes, simple elements, contents of complex elements, and other nodes in XML files. [Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) can be built on these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.

This document shows how to add more tables transformed from the XML data source into the Logi JReport catalog via the XML connection, organize the tables, and so on.

Below is a list of the sections covered in this topic:

> * [Adding Tables](#Add)
> * [Refreshing Tables](#Refresh)
> * [Organizing Tables](#Folder)
> * [Removing and Adding Columns to Tables](#Remove)

## Adding Tables

1. Do one of the following:
   * Right-click the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the XML connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the XML connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click [any folder](#Folder) in the Tables node of the XML connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the XML connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   The [Add Tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009564482-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893957911/addtbl_xml.gif)
2. Select the **Refresh** button. The tables contained in the schema that is transformed from the XML file will then be displayed in the Tables box.
3. Choose the required tables in the Tables box, and then select **Add**.

   To choose consecutive tables, select the first table, press and hold down the **SHIFT** key, and then select the last table. To choose tables that are not consecutive, press and hold down **CTRL**, and then select each table.
4. After adding the required tables, select **Done** to close the dialog.

## Refreshing Tables

The tables in your catalog are a temporary deposit to improve the performance when you design and test your report. Your data source keeps changing over the time; however, these will not be reflected automatically in your catalog. To synchronize your tables in the connection and data source, you can choose to refresh the table information using the Refresh command on the shortcut menu of the tables. When the refreshing job is done, a reporting dialog will be shown, summarizing the changes and operations that have been taken.

## Organizing tables

You can organize the tables in an XML connection by arranging them in different folders in the Catalog Manager.

**To add a folder:**

1. Do either of the following:
   * Right-click the **Tables** node, or any existing folder and select **New Folder** from the shortcut menu.
   * Selecting any existing table existing folder and select **New Folder** on the Catalog Manager toolbar.
2. A new folder is added to the Tables node, or in the selected folder. Type a name for the folder in the editing area, and then select outside to confirm the change.

**To move tables to a folder:**

1. Right-click the table you want to move and select **Move To**  from the shortcut menu.
2. In the Move Table dialog, select the folder to which the table will be moved, then select **OK**.

   ![Move Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889393559/cnctn_jdbc_obj_mvtbl.gif)

## Removing and Adding Columns to Tables

By default, when you add a table, you add all the columns that reside in the table; however, Logi JReport gives you the flexibility to remove columns in a table, leaving only the columns useful to your reports. To remove a column from a table, right-click the column and select **Delete** from the shortcut menu.

Also, you can add the columns back into a table after you have removed them. To do this:

1. Right-click the table to which you want to insert columns, then select **Add Columns**  from the shortcut menu.
2. In the Add Columns dialog, select the required columns from the Columns box and select **Add**.

   ![Add Columns dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893960727/cnctn_jdbc_obj_addclm.gif)

   There will be no available columns in the Columns box if you did not delete any in the table.
3. Select the **Done** button to close the Add Columns dialog.

**Tip:** If you want to add all the columns in a table at one time, you can also choose to refresh the table, which synchronizes the table in the catalog with the one in your XSD.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585441-Setting-Up-an-XML-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585161-MongoDB-Connections)
