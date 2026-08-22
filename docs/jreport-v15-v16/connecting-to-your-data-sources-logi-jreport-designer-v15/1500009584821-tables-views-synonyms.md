---
title: "Tables/Views/Synonyms"
id: 1500009584821
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584821-Tables-Views-Synonyms
updated_at: 2021-07-24T05:55:49Z
---

# Tables/Views/Synonyms

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564002-DBMS-Objects-in-a-JDBC-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures)

# Tables/Views/Synonyms

Tables, views, and synonyms are mapped objects of the tables, views and synonyms in the raw database that a connection refers to. Mapped objects have mapped names that can be different from their names in the raw database. A catalog stores information about the real tables/views/synonyms mapped, such as the name, qualifier, and owner.

Since tables/views/synonyms are only mapped objects, they can be mapped and then re-mapped. That is, the information of the real tables/views/synonyms stored in a caytalog is changeable. This is useful when you are off-line from your database. You will still be able to see the table/view/synonym structure and generate reports; however, you cannot view the report since the catalog only stores a meta-data layer, not the database data. In addition, when changing the connection, for example, from an MySQL database to an Oracle database, you will only need to re-map all the tables/views/synonyms in the catalog as opposed to creating a new catalog.

[Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) can be built on tables, views and synonyms and a report is developed from a query (or something else which is functionally similar) or from a business view.

**Note:** Synonyms are supported for Oracle database only.

Below is a list of the sections covered in this topic:

> * [Adding Tables/Views/Synonyms to a Catalog](#Add)
> * [Refreshing Tables/Views/Synonyms](#Refresh)
> * [Organizing Tables/Views/Synonyms](#Folder)
> * [Removing and Adding Columns to Tables/Views/Synonyms](#Remove)
> * [Previewing the Column Data of Tables/Views/Synonyms](#Preview)

## Adding Tables/Views/Synonyms to a Catalog

1. In the Catalog Manager resource tree, do any of the following:
   * Right-click the JDBC connection and select **Add Tables**/**Views**/**Synonyms** from the shortcut menu.
   * Right-click the **Tables**/**Views**/**Synonyms** node of the JDBC connection and select **Add Tables**/**Views**/**Synonyms** from the shortcut menu.
   * Right-click an existing table/view/synonym in the JDBC connection if there is and select **Add Tables**/****Views****/****Synonyms**** from the shortcut menu.
   * Right-click [any folder](#Folder) in the Tables/Views/Synonyms node of the JDBC connection if you have already created some and select **Add Tables**/****Views****/****Synonyms**** from the shortcut menu.
   * Select the **Tables**/****Views****/****Synonyms**** node of the JDBC connection, or any existing table/view/synonym or folder in the connection and select **Add Tables**/**Views**/**Synonyms** on the Catalog Manager toolbar.

   The [Add Tables/Views/Synonyms](https://devnet.logianalytics.com/hc/en-us/articles/1500009585641-Add-Tables-Views-Synonyms-Dialog) dialog appears.

   ![Add Tables/Views/Synonyms dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889392407/addtbvwsynm.gif)
2. From the Database Catalogs drop-down list, select the required catalog, then specify a schema in the selected catalog from the Schemas box.
3. Check **Tables**/**Views**/**Synonyms** checkbox.
4. Select the **Refresh** button. The tables/views/synonyms contained in the selected schema will then be displayed in the box on the right of the Add Tables/Views/Synonyms dialog.
5. Check the **Show System Tables**/**Views**/**Synonyms** option if you want to have the system tables/views/synonyms available in the Tables/Views/Synonyms box.
6. Check **Show Tables**/**Views**/**Synonyms** **Already Added** to make the tables/views/synonyms that have been added to the connection available in the Tables/Views/Synonyms box if you want to add them again.
7. Choose the required tables in the Tables/Views/Synonyms box, and then select **Add**.

   To choose consecutive tables/views/synonyms, select the first table/view/synonym, press and hold down Shift, and then select the last table/view/synonym. To choose tables/views/synonyms that are not consecutive, press and hold down Ctrl, and then select each table/view/synonym.
8. Repeat steps 2 to 4 to add tables from other catalogs and schemas.
9. To add certain tables by name or by patterns in their name, select the **Table**/**View**/**Synonym** **Name Pattern** checkbox. The wildcard % will then be displayed in the text box.

   For example, if you want to add tables/views/synonyms beginning with AL, you can type AL% (case sensitive) in the text box, and select the Refresh button. All the tables/views/synonyms beginning with AL in the selected schema will then be displayed in the Tables/Views/Synonyms box. Choose the tables/views/synonyms that are required by selecting Add. They will then be added to the connection.
10. After adding the required tables/views/synonyms, select **Done** to close the dialog.

**Notes:**

* When you have added some tables/views/synonyms to a catalog, you can then set up pre-joins between them. For detailed information, see [Defining the join relationships between tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources).
* If you have selected schemas in the [Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#Schema) tab of the Get JDBC Connection Information dialog when setting up the connection, when you add tables/views/synonyms, by default only the selected schemas will be listed in the Schemas box of the Add Tables/Views/Synonyms dialog, however, you can check the Show All Schemas option to show all the schemas.
* When adding tables/views/synonyms, if the Show Tables/Views/Synonyms Already Added option is checked in the Add Tables/Views/Synonyms dialog, when you select the Add button to add a table/view/synonym that has already been added to the connection once, a dialog will be displayed, prompting you to give the new table/view/synonym a different name.

## Refreshing Tables/Views/Synonyms

The tables/views/synonyms in your catalog are a temporary deposit to improve the performance when you design and test your report. Your database keeps changing over the time. However, these will not be reflected automatically in your catalog. To synchronize your tables/views/synonyms in the connection and database, you can choose to refresh the tables/views/synonyms information using the Refresh command on their shortcut menu. Then when the refreshing job is done, a reporting dialog will be shown, summarizing the changes and operations that have been taken.

## Organizing Tables/Views/Synonyms

You can organize the tables/views/synonyms, which have been added to a catalog via a JDBC connection, by arranging them in different folders in the Catalog Manager.

**To add a folder:**

1. Do any of the following:
   * Right-click the **Tables**, **Views** or **Synonyms** node and select **New Folder** from the shortcut menu.
   * Right-click any existing folder and select **New Folder** from the shortcut menu.
   * Selecting any existing table, view, synonym or existing folder and select **New Folder** on the Catalog Manager toolbar.
2. A new folder is added to the Tables/Views node, or in the selected folder. Type a name for the folder in the editing area, and then select outside to confirm the change.

**To move tables/views/synonyms to a folder:**

1. Right-click the table/view/synonym you want to move and select **Move To**  from the shortcut menu.
2. In the Move Table/View/Synonym dialog, select the folder to which the table/view/synonym will be moved, then select **OK**.

   ![Move Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889393559/cnctn_jdbc_obj_mvtbl.gif)

## Removing and Adding Columns to Tables/Views/Synonyms

By default, when you add a table/view/synonym, you add all the columns present in the table/view/synonym. However, Logi JReport gives you the flexibility to remove columns in a table/view/synonym, leaving only the columns useful to your reports. Additionally, your database keeps changing over the time. You can add the columns to the table/view/synonym after you delete them or the database has been updated.

**To remove a column from a table/view/synonym:**

1. Select the column you want to remove.
2. Right-click the column and select **Delete** from the shortcut menu. This does not remove the column from the database, only from what is visible in Logi JReport Designer.

**To add columns to a table/view/synonym:**

1. Right-click the table/view/synonym to which you want to insert columns, then select **Add Columns**  from the shortcut menu.
2. In the Add Columns dialog, select the required columns from the Columns box and select **Add**.

   ![Add Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893960727/cnctn_jdbc_obj_addclm.gif)

   There will be no available columns in the Columns box if you do not delete any in the table/view/synonym before, or no updates have been made to the database. That is to say, you cannot add columns that do not belong to the table/view/synonym.
3. Select the **Done** button to add the columns to the table/view/synonym.

**Tip:** If you want to add all the columns in a table/view/synonym at the same time, you can also choose to refresh the table/view/synonym, which synchronizes the table/view/synonym in the catalog with the one in your database.

## Previewing the Column Data of Tables/Views/Synonyms

In the Catalog Manager, you can preview the data for a database column, which enables you to have a general idea about the field contents, field type, and other useful information related to this field.

**To preview the data of a column:**

1. Right-click the column with the data you want to preview, then on the shortcut menu, select **Browse Data**.
2. The data of this column is shown in a list in a dialog, which also includes other information including the field type, precision, scale and number of records.

   ![Browse Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893970967/cnctn_jdbc_obj_brsdt.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564002-DBMS-Objects-in-a-JDBC-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures)
