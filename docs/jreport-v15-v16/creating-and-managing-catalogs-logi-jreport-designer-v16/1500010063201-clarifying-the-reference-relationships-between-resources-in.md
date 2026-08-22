---
title: "Clarifying the Reference Relationships Between Resources in a Catalog"
id: 1500010063201
section: "Creating and Managing Catalogs - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063201-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog
updated_at: 2021-07-24T10:39:31Z
---

# Clarifying the Reference Relationships Between Resources in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028522-Editing-Pre-joins-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs)

# Clarifying the Reference Relationships Between Resources in a Catalog

With the development of reports and catalogs, the relationships between the catalog resources may become increasingly complicated. You might be wondering if and where a query or a formula is used by a resource in a catalog or report. You might hesitate to rename or edit a resource because you don't exactly know what other resources are currently using it and, if you change it what result it would cause.

To help you manage catalog resources, Logi JReport provides you with the tool - Reference Table. You can select the resource types you want to register in the reference table. Logi JReport then monitors the reference information of the specified resource types in a catalog and stores this information in the reference table.

Below is a list of the sections covered in this topic:

* [Configuring the Reference Table](#Configure)
* [Viewing Reference Relationships](#View)
* [Refreshing the Reference Table](#Refresh)
* [Exporting the Reference Table](#Export)

## Configuring the Reference Table

Before Logi JReport can start to monitor and record the resource reference information in the reference table, you must first have the reference table configured by choosing the resource types you want to add to the table. Logi JReport then monitors the reference relationships between resources of these types and store the relationship information in the database.

**To configure the reference table:**

1. Open the catalog the resource reference relationships of which you want to clarify.
2. On the Catalog Manager toolbar, select **Configure Reference**. The [Reference Table Configuration](https://devnet.logianalytics.com/hc/en-us/articles/1500010067561-Reference-Table-Configuration-Dialog) dialog appears.

   ![Reference Table Configuration dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901185047/reftblcnfg.gif)
3. Check the data sources in the catalog you want Logi JReport to monitor in the Data Sources box.
4. In the Catalog Resource Types box, check the resource types that are to be added to the reference table.

   In order to improve product performance and provide you with more flexibility, Logi JReport allows you to choose the resource types that you want to monitor by yourself. Logi JReport only monitors the reference relationships between the resource types that you have selected. The resource types that have not been selected will not be monitored, even if they may have reference relationships to the selected resource types. Therefore, if you are not sure whether the resource types you have selected hold all the possible reference relationships within themselves, it is recommended that you select as many resource types as possible to avoid incomplete information.

   For example, in the Reference Table Configuration dialog, selecting only the formula resource type means that for a formula, only the formulas referencing this formula will be recorded in the reference table, other resources such as queries, summaries, and reports which are also using this formula will not be shown in the reference table. If you rename a formula, you will only be prompted with the formulas using it, and any other resources using it will be ignored.
5. Select **OK** to finish the configuration.

## Viewing Reference Relationships

After you have configured the reference table, the reference relationships between the resources of the checked types will be monitored. You can right-click a specific resource in the Catalog Manager and select **Reference Entities** from the shortcut menu to view its reference relationships with other resources. The Reference Entities window lists all entities of the specified resource types that are using the selected resource.

![Reference Entities dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909292183/ctlg_crsrf1.gif)

**Tip:** In the Reference Entities window, you can right-click any of the query, business view, formula, parameter or summary entity to edit it, and right-click any report entity to open the report.

In addition, when you rename a resource, Logi JReport Designer will scan the reference relationships between it and other resources, and prompt you whether to update all the resources that use it, helping you reduce the risk of a missing resource causing a failure in other resources. If you uncheck the Apply to all and save catalog option in the Warning dialog, the impacted resources cannot work correctly.

![Reference Warning](https://devnet.logianalytics.com/hc/article_attachments/4404909292567/ctlg_crsrf2.gif)

## Refreshing the Reference Table

The reference table information is stored in a database, which provides reliable stability. However, in some circumstances you may need to refresh the reference table to retrieve the correct reference relationship information. To do this, on the Catalog Manager toolbar, select **Refresh Reference**.

## Exporting the Reference Table

You can also export the reference table information to a text file as follows: select **Export Reference** on the Catalog Manager toolbar, then in the Save Reference dialog, specify the location where you want to save the file and select **Save**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028522-Editing-Pre-joins-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs)
