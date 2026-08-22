---
title: "Creating, Opening and Saving Catalogs"
id: 1500010063141
section: "Creating and Managing Catalogs - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs
updated_at: 2021-07-24T10:39:33Z
---

# Creating, Opening and Saving Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063161-Knowing-Catalogs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063181-Managing-the-Data-Resources-in-a-Catalog)

# Creating, Opening and Saving Catalogs

A report can only exist within a catalog folder that contains a catalog file. Therefore you must create and open a catalog before you create or edit a report.

A catalog is represented at the operating system level as a directory that contains the catalog file as well as the other report objects. A catalog folder must contain only one catalog file. You can use the operating system commands to copy and rename catalog files as long as you ensure you only have one catalog file per folder. A process you may use is to first create a base catalog with only connection information and tables used by all applications. You can then copy and rename this to create as many catalog folders and catalog files as you need for your reporting requirements.

Below is a list of the sections covered in this topic:

* [Creating a Catalog](#Create)
* [Adding Data Sources in a Catalog](#DataSource)
  + [Setting the Default Data Source for a Catalog](#Default)
* [Opening a Catalog](#Open)
* [Saving a Catalog](#Save)
  + [Sharing Catalog Files Among Multiple Report Developers](#Share)

## Creating a Catalog

1. Select **File** > **New Catalog**. The [New Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010031842-New-Catalog-Dialog) dialog appears.

   ![New Catalog dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909168151/nwctlg.gif)

   If necessary, Logi JReport Designer will prompt you to save changes to the current open catalog. Only one catalog can be open at a time.
2. In the Name field, enter the name for the catalog. The catalog name must include the extension (.cat or .cat.xml)
3. In the Data Source Name field, input the name for the data source that will be created along with the catalog (when creating a catalog, by default, a data source is created in the catalog at the same time). You can include spaces in the name but do not use special characters.
4. Specify the path to save the catalog in the Directory field. You can also select the button **![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif)** to browse to and select the directory in which to create the catalog. The directory you specify must not already contain a catalog file.
5. Select **OK** to create the catalog. The Catalog Manager displays, with a data source created for the catalog.

You can then [set up the required connections](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections) to connect the catalog data source with your databases. A data source in a catalog can be connected with multiple connections.

## Adding Data Sources in a Catalog

Logi JReport Designer supports the Multiple Data Sources feature, which means in one catalog you can add as many data sources as you need and connect them with many different types of data. However, if you want to mash up data that come from multiple connections into a single [query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) or [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010070641-Business-Views), the database connections must be all in the same data source in the catalog.

**To add another data source to a catalog:**

1. Do either of the following:
   * In the Catalog Manager, select a data source node, then select **New Data Source** on the Catalog Manager toolbar.
   * Select **Home** > **New** > **Data Source**.
   * Select **File** > **New** > **Data Source**.

   The [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010031882-New-Data-Source-Dialog) dialog appears.

   ![New Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909167895/nwdtsrc.gif)
2. In the Data Source Name text box, specify the name of the new data source.
3. From the Connection Type box, select the type of the first connection to create in the new data source.
4. Select **OK**. The corresponding connection wizard appears. [Set up the connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections) as required.

### Setting the Default Data Source for a Catalog

When a catalog contains multiple data sources, you need to specify which data source will be the default one for the catalog (by default, the data source that is created along with the catalog is the default data source of the catalog). To change the default data source, right-click the data source which you want to use as the default data source, then select **Set as Default** on the shortcut menu. A catalog must have one and only one default data source.

![Set Default Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404901348631/ctlg_crt_dftsc.gif)

## Opening a Catalog

You can open a catalog explicitly, by using the Open Catalog command, or you can open it implicitly, by [opening one of the reports in the catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010070901-Opening-Reports).

**To open a catalog explicitly:**

1. Select **File** > **Open Catalog**.

   If necessary, Logi JReport Designer will prompt you to save changes to the current open catalog. Only one catalog can be open at a time.
2. In the Open Catalog File dialog, browse to and select the catalog you want to open and then select the **Open** button.

   The Catalog Manager displays, listing the data resources in the specified catalog. You can [manage the resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010063181-Managing-the-Data-Resources-in-a-Catalog) using the manager.

## Saving a Catalog

To save a catalog, select **Save Catalog** on the Catalog Manager toolbar. The type, name and location were specified when you [created the catalog](#).

You can also select either of the following on the File menu tab to save a catalog:

* **Save Catalog**  
   Saves the open catalog.
* **Save Catalog As**  
   Saves the open catalog in the selected alternate format. Options are .cat or .cat.xml. The .cat.xml file can be in the same directory as the .cat file. When you open the catalog in Designer, you can select either the .cat or the .cat.xml version; however, only the open one will be updated. If you publish the report to Logi JReport Server, be sure to publish only the updated one as the out of date one will likely produce errors when the user runs the report with the outdated catalog. It is best practice to keep only one version of the catalog once you decide which format you will use to publish.

A directory can contain only one catalog file other than the .cat and .cat.xml of the same catalog. To merge multiple catalog files, see [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs).

### Sharing Catalog Files Among Multiple Report Developers

By default, the report file and resources referenced by this report are created and saved in the current catalog. You can also save a report or other resource to a catalog other than the one in which it is created. All the catalog resources related to this report will then be merged into the catalog in the specified folder. This can allow a team of report developers to share resources. Each report developer can work on a local version of the catalog, and then use the Save To command to have his catalog merged into a universal catalog. The universal catalog must have the same name as the current catalog. The Save To command saves not only the report files, but also the resources (query, formulas, and parameters) that are referenced by this report. When there is a conflict, the report developer must decide which version to keep or modify his catalog to rename the conflicting resources and try the Save To again.

For details about how to share catalog files, see [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs) and [Saving a Report to a Different Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010034882-Saving-Reports#SaveTo).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063161-Knowing-Catalogs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063181-Managing-the-Data-Resources-in-a-Catalog)
