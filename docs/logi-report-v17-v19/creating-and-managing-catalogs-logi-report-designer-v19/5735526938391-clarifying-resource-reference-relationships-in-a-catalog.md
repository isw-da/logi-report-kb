---
title: "Clarifying Resource Reference Relationships in a Catalog"
id: 5735526938391
section: "Creating and Managing Catalogs - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735526938391-Clarifying-Resource-Reference-Relationships-in-a-Catalog
updated_at: 2022-11-02T04:12:31Z
---

# Clarifying Resource Reference Relationships in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511752087-Editing-Pre-joins-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735498385175-Merging-Catalogs)

# Clarifying Resource Reference Relationships in a Catalog

With the development of reports and catalogs, the relationships between the catalog resources may become increasingly complicated. You might be wondering if and where a query or a formula is used by a resource in a catalog or report. You might hesitate to rename or edit a resource because you don't exactly know what other resources are currently using it and, if you change it what result it would cause. To help you manage catalog resources, Designer provides you with the tool - Reference Table. You can select the resource types you want to register in the reference table. Designer then monitors the reference information of the specified resource types in a catalog and stores this information in the reference table. This topic describes how you can configure the reference table and use it to help you clarify the reference relationships between resources in a catalog.

This topic contains the following sections:

* [Configuring the Reference Table for a Catalog](#Configure)
* [Viewing Reference Relationships in a Catalog](#View)
* [Refreshing the Reference Table](#Refresh)
* [Exporting the Reference Table](#Export)

## Configuring the Reference Table for a Catalog

Before Designer can start to monitor and record the resource reference information in the reference table, you must first configure the reference table by choosing the resource types you want to add to the table. Designer then monitors the reference relationships between resources of these types and stores the relationship information in the database.

**To configure the reference table for a catalog**

1. Open the catalog the resource reference relationships of which you want to clarify.
2. On the Catalog Manager toolbar, select **Configure Reference**. Designer displays the [Reference Table Configuration dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544168599-Reference-Table-Configuration-Dialog-Box).

   ![Reference Table Configuration dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898461089687/reftblcnfg.gif)
3. In the **Data Sources** box, select the data sources in the catalog you want Designer to monitor.
4. In the **Catalog Resource Types** box, select the resource types you want to add to the reference table. In order to improve product performance and provide you with more flexibility, Designer enables you to choose the resource types that you want to monitor by yourself. Designer only monitors the reference relationships between the resource types that you select. Designer does not monitor the resource types that you do not select, even if they may have reference relationships with the selected resource types. Therefore, if you are not sure whether the resource types you select hold all the possible reference relationships within themselves, you should select as many resource types as possible to avoid incomplete information.

   For example, in the Reference Table Configuration dialog box, selecting only the formula resource type means that for a formula, Designer only records the formulas referencing this formula in the reference table, other resources such as queries, summaries, and reports which are also using this formula will not be shown in the reference table. If you rename a formula, Designer only prompts you the formulas using it. Designer ignores any other resources using the formula.
5. Select **OK** to finish the configuration.

## Viewing Reference Relationships for a Catalog

After you have configured the reference table, Designer monitors the reference relationships between the resources of the selected types. You can right-click a specific resource in the Catalog Manager and select **Reference Entities** from the shortcut menu to view its reference relationships with other resources. The Reference Entities window lists all entities of the specified resource types that are using the selected resource.

![Reference Entities dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898519877911/ctlg_crsrf1.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) In the Reference Entities window, you can right-click any of the query, business view, formula, parameter, or summary entity to edit it, and right-click any report entity to open the report.

In addition, when you rename a resource, Designer scans the reference relationships between it and other resources, and prompts you whether to update all the resources that use it, in order to help you reduce the risk of a missing resource causing a failure in other resources. If you clear "Apply to all and save catalog" in the Warning dialog box, the impacted resources cannot work correctly.

![Reference Warning](https://devnet.logianalytics.com/hc/article_attachments/9898519897239/ctlg_crsrf2.gif)

## Refreshing the Reference Table

Designer stores the reference table information in a database, which provides reliable stability. However, in some circumstances, you may need to refresh the reference table to retrieve the correct reference relationship information. To do this, on the Catalog Manager toolbar, select **Refresh Reference**.

## Exporting the Reference Table

You can export the reference table information to a text file.

1. Select **Export Reference** on the Catalog Manager toolbar.
2. In the Save Reference dialog box, specify the location where you want to save the file and select **Save**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511752087-Editing-Pre-joins-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735498385175-Merging-Catalogs)
