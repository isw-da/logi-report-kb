---
title: "Creating a Business View"
id: 1500009562602
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562602-Creating-a-Business-View
updated_at: 2021-07-24T05:56:16Z
---

# Creating a Business View

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562622-Editing-a-Business-View)

# Creating a Business View

This topic demonstrates how to create a business view.

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog), then do either of the following:
   * In the Catalog Manager, expand the data source in which you want to create the business view, then select the **Business Views**  node or any existing business view in the data source and select **New Business View**  on the Catalog Manager toolbar, or right-click the **Business Views**  node in the data source and select **New Business View**  from the shortcut menu.
   * Select **Home** > **New** > **Business View**  or **File** > **New** > **Business View**, specify the data source in which the business view will be created, then select **OK**.
2. In the Enter Business View Name dialog, provide a name for the business view and select **OK**. The [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009585621-Add-Tables-Views-Queries-Dialog) dialog is then displayed.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893821975/addtbvwqy.gif)
3. In the left box, expand the resource nodes to add the resources based on which to create the business view to the right box, then select **OK**.

   If the catalog data source is connected with multiple connections, you can mash up multiple data resources for the business view that come from all these connections, including tables, views, synonyms, queries, imported SQLs, stored procedures and user defined data sources. When a query, imported SQL, stored procedure or user defined data source is added, it will be added as a single table with all of its columns. When two resources (for example, a table and a view) use the same name, they cannot be added at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

   If the current catalog data source contains JDBC connections, the Include Added Tables/Views option is available. Check it if you want to show the tables, views and synonyms in the resource tree in the left box, which have already been added to the right box. You can then add the tables, views and synonyms of the JDBC connections for the business view as many times as you want by providing different names for the tables, views and synonyms each time you add them.
4. If more than one data resource is added for the business view, the Query Editor appears, in which you can edit the data resources you select for the business view in the same way you would do for a query. You can:
   * Select the columns in each table that you want to use for the business view. However, for tables from MongoDB connections, you cannot select all columns by selecting \*. The PrimaryKey and ForeignKey columns in such table cannot be selected to a business view.
   * [Add or delete the tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009570762-Adding-and-Deleting-Tables-in-a-Query) used for creating the business view.
   * [Set up joins between the tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query).
   * [Create formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009570702-Adding-Formula-Fields-to-a-Query) to use in the business view.
   * [Add filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query) to narrow data used in the business view.

   When done, select the **OK** button at the bottom of the Query Editor to apply the changes. If needed you can also select **Menu** > **Query** > **Save As** to save the data resources as a query.
5. The [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009564622-Business-View-Editor-Dialog) appears. All the resources you have selected for the business view, and the formulas and summaries in the current catalog data source that are valid for the selected resources are listed in the Resource Objects panel on the left of the editor.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404893953303/bvedtr.gif)
6. [Add elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements) to the business view based on the available resources.
7. [Define hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/1500009583021-Defining-Hierarchies) on the business view to allow end users to drill report data to particular groups.
8. [Create predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters) on the business view for users to choose when using the business view to create reports.
9. [Modify the joins between the resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009562682-Modifying-the-Joins-Between-Data-Resources) the business view uses.
10. [Configure security for the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security) if necessary.
11. Select **Save** on the toolbar to save the business view.
12. Select **Menu** > **File** > **Close** to close the window. The business view will now have been added to the catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562622-Editing-a-Business-View)
