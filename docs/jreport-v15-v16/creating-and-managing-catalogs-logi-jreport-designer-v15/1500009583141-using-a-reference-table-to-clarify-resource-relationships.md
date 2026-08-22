---
title: "Using a Reference Table to Clarify Resource Relationships"
id: 1500009583141
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583141-Using-a-Reference-Table-to-Clarify-Resource-Relationships
updated_at: 2021-07-24T05:56:14Z
---

# Using a Reference Table to Clarify Resource Relationships

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562782-Filtering-Resources) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources)

# Using a Reference Table to Clarify Resource Relationships

With the development of reports and catalogs, the relationships among the catalog resources may become increasingly complicated. You might be wondering if and where an SQL or a formula is used by a resource in a catalog or report. You might hesitate to rename or modify a resource because you don't exactly know what other resources are currently using it and, and if you change it what result it would cause.

To help you manage catalog resources, Logi JReport provides you with a tool - the reference table. Logi JReport monitors the resource reference information in the catalog and stores this information in the reference table. You can select the resource types that can be registered in the reference table. With the reference table, when you rename a resource object, Logi JReport Designer will scan the reference relationships between it and other resource objects. It will then prompt you to update the changes in the resources that reference the object, helping you reduce the risk of a missing resource causing a failure in another report.

Below is a list of the sections covered in this topic:

> * [Configuring the Reference Table](#Configure)
> * [Viewing a Resource Object's Referencing Relationships](#View)
> * [Refreshing and Exporting the Reference Table](#Refresh)

## Configuring the Reference Table

Before Logi JReport can start to monitor and record the resource reference information in the reference table, you must first have the reference table configured by choosing the resource types that are to be added to the table. Then Logi JReport will monitor the reference relationships among objects of these resource types and store the relationship information in the database.

**To configure the reference table:**

1. On the Catalog Manager toolbar, select **Configure Reference**. The [Reference Table Configuration](https://devnet.logianalytics.com/hc/en-us/articles/1500009586881-Filter-View-Dialog) dialog appears.

   ![Reference Table Configuration dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889323671/reftblconfig.gif)
2. Check the data sources you want Logi JReport to monitor in the Data Source box.
3. In the Catalog Resource Types box, check the resource types that are to be added to the reference table.

   In order to improve product performance and provide you with more flexibility, Logi JReport allows you to choose the resource types that you want to monitor by yourself. Logi JReport will then only monitor the referencing relationships between the resource types that you have selected. The resource types that have not been selected will not be monitored, even if they may have referencing relationships to the selected resource types. Therefore, if you are not sure whether the resource types you have selected hold all the possible reference relationships within themselves, it is recommended that you select as many resource types as possible to avoid incomplete information.

   For example, in the Reference Table Configuration dialog, selecting only the formula resource type means that for a formula, only the formulas referencing this formula will be recorded in the reference table, although other resources such as queries, summaries, and reports which are also using this formula will not be shown in the reference table. If you rename this formula, you will only be prompted to update the change in the formulas using it, and any other resources using it will be ignored.
4. Select **OK**. The referencing relationships between the resources of the checked types will then be monitored.

## Viewing a Resource Object's Referencing Relationships

After you have configured a reference table, you can view the referencing relationships for a specific resource object. To do this:

1. In the Data tab of the Catalog Manager, browse to the resource object with the reference relationships that you want to view.
2. Right-click the resource object and select **Reference Entities** on the shortcut menu.
3. The Reference Entities window appears, listing entities of the specified resource types that are using the selected resource object.

   ![Reference Entities dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889430295/ctlg_mng_crsrf.gif)

   **Tip:** In the Reference Entities window, you can right-click any of the query, formula, parameter or summary entity which uses the specified resource object to edit it, and right-click any report entity to open the report.

## Refreshing and Exporting the Reference Table

The reference table information is stored in a database, which provides reliable stability. However, in some circumstances you may need to refresh the reference table to retrieve the correct reference relationship information. To do this, on the Catalog Manager toolbar, select **Refresh Reference**.

You can also export the reference table information to a text file as follows: select **Export Reference** on the Catalog Manager toolbar, then in the Save Reference dialog, specify the location where you want to save the file and select **Save**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562782-Filtering-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources)
