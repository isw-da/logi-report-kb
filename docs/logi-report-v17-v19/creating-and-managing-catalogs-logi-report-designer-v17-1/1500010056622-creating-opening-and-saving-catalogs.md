---
title: "Creating, Opening, and Saving Catalogs"
id: 1500010056622
section: "Creating and Managing Catalogs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs
updated_at: 2021-07-23T19:14:32Z
---

# Creating, Opening, and Saving Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094061-Knowing-About-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056642-Managing-the-Data-Resources-in-a-Catalog)

# Creating, Opening, and Saving Catalogs

A report can only exist within a catalog folder that contains a catalog file. Therefore, you must create and open a catalog before you create or edit a report. This topic describes how you can create, open, and save catalogs and add data sources in the catalogs.

This topic contains the following sections:

* [Creating a Catalog](#Create)
* [Adding Data Sources in a Catalog](#DataSource)
  + [Setting the Default Data Source for a Catalog](#Default)
* [Opening a Catalog](#Open)
* [Saving a Catalog](#Save)
  + [Sharing Catalog Files Among Multiple Report Developers](#Share)

## Creating a Catalog

1. Select **File** > **New Catalog**. Designer displays the [New Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097981-New-Catalog-Dialog-Box).

   ![New Catalog dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856907671/nwctlg.gif)

   Designer may prompt you to save changes to the current open catalog. You can open only one catalog at a time.
2. In the **Name** text box, type the name for the catalog. The name must include the extension (.cat or .cat.xml).
3. In the **Data Source Name** text box, type the name for the data source to be created along with the catalog (when you create a catalog, you create a data source in the catalog at the same time by default). You can include spaces in the name but do not use special characters.
4. In the **Directory** text box, specify the path to save the catalog. You can also select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to browse to and select the directory in which to create the catalog. The directory you specify must not already contain a catalog file.
5. Select **OK** to create the catalog. The Catalog Manager displays, with a data source created for the catalog.

You can then [set up the required connections](https://devnet.logianalytics.com/hc/en-us/articles/1500010057582-Connecting-to-Your-Data-Sources) to connect the catalog data source with your databases. You can connect a data source in a catalog with multiple connections.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Catalogs which support a large number of reports can become very large and difficult to maintain, so it is best to create a new catalog for each category of report types you create. For example, you may have reports for sales, accounts receivable, customer information, inventory management, and so on. If you include all of these types of reports in a single catalog, it becomes more difficult to maintain and keep track of which data objects belong to which group of reports. A better way is to create a separate catalog for each group of reports. You can use the operating system commands to copy and rename catalog files as long as you ensure you only have one catalog file per folder. A process you may use is to first create a base catalog with only connection information and tables used by all applications. You can then copy and rename this to create as many catalog folders and catalog files as you need for your reporting requirements.

## Adding Data Sources in a Catalog

Designer supports the Multiple Data Sources feature, which means in one catalog you can add as many data sources as you need and connect them with many different types of data. However, if you want to mash up data that come from multiple connections into a single [query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog) or [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views), the database connections must be all in the same data source in the catalog.

**To add another data source to a catalog:**

1. Do either of the following:
   * In the Catalog Manager, select a data source node, then select **New Data Source** on the Catalog Manager toolbar.
   * Select **Home** > **New** > **Data Source**.
   * Select **File** > **New** > **Data Source**.

   Designer displays the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059982-New-Data-Source-Dialog-Box).

   ![New Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848508055/nwdtsrc.gif)
2. In the **Data Source Name** text box, specify the name of the new data source.
3. In the **Connection Type** box, select the type of the first connection to create in the new data source.
4. Select **OK**. Designer displays the corresponding connection wizard. [Set up the connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010057582-Connecting-to-Your-Data-Sources) as required.

### Setting the Default Data Source for a Catalog

When a catalog contains multiple data sources, you need to specify which data source is the default one for the catalog (by default, the data source created along with the catalog is the default data source of the catalog). To change the default data source, right-click the data source which you want to use as the default data source, then select **Set as Default** on the shortcut menu. A catalog must have one and only one default data source.

![Set Default Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404848709399/ctlg_crt_dftsc.gif)

## Opening a Catalog

You can open a catalog explicitly by using the Open Catalog command, or you can open it implicitly by [opening one of the reports in the catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010062782-Opening-Reports).

**To open a catalog explicitly:**

1. Select **File** > **Open Catalog**.

   Designer may prompt you to save changes to the current open catalog. You can open only catalog at a time.
2. In the Open Catalog File dialog box, browse to and select the catalog you want to open and then select the **Open** button.

   The Catalog Manager displays, listing the data resources in the specified catalog. You can [manage the resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010056642-Managing-the-Data-Resources-in-a-Catalog) using the manager.

## Saving a Catalog

To save a catalog, select **Save Catalog** on the Catalog Manager toolbar. You have specified the type, name, and location when you created the catalog.

You can also select either of the following on the File menu tab to save a catalog:

* **Save Catalog**  
  Saves the open catalog.
* **Save Catalog As**  
  Saves the open catalog in the selected alternate format. Options are .cat or .cat.xml. The .cat.xml file can be in the same directory as the .cat file. When you open the catalog in Designer, you can select either the .cat or the .cat.xml version; however, Designer only updates the open one. If you publish the report to Server, be sure to publish only the updated one as the out of date one will likely produce errors when the user runs the report with the outdated catalog. It is best practice to keep only one version of the catalog once you decide which format you want to use to publish.

A directory can contain only one catalog file other than the .cat and .cat.xml of the same catalog. To merge multiple catalog files, see [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500010094081-Merging-Catalogs).

### Sharing Catalog Files Among Multiple Report Developers

By default, Designer saves the report file and resources referenced by this report in the current catalog. You can also save a report or other resource to a catalog other than the one in which you have created them. Designer then merges all the catalog resources related to this report into the catalog in the specified folder. This can enable a team of report developers to share resources. Each report developer can work on a local version of the catalog, and then use the **Save To** command to have his catalog merged into a universal catalog. The universal catalog must have the same name as the current catalog. The Save To command saves not only the report files, but also the resources (query, formulas, parameters, and so on) that are referenced by this report. When there is a conflict, the report developer must decide which version to keep or modify his catalog to rename the conflicting resources and try the Save To again.

For more information about how to share catalog files, see [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500010094081-Merging-Catalogs) and [Saving a Report to a Different Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010101381-Saving-Reports#SaveTo).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094061-Knowing-About-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056642-Managing-the-Data-Resources-in-a-Catalog)
