---
title: "Creating a Catalog"
id: 1500009562722
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog
updated_at: 2021-07-24T05:56:14Z
---

# Creating a Catalog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562742-Knowing-Catalogs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583221-Saving-a-Catalog)

# Creating a Catalog

A report can only exist within a catalog folder that contains a catalog file. Therefore you must create and open a catalog before you create or edit a report.

A catalog is represented at the operating system level as a directory that contains the catalog file (.cat or .cat.xml) as well as the other report objects. A catalog folder must contain only one catalog file. You can use the operating system commands to copy and rename catalog files as long as you ensure you only have one catalog file per folder. A process you may use is to first create a base catalog with only connection information and tables used by all applications. You can then copy and rename this to create as many catalog folders and catalog files as you need for your reporting requirements.

**To create a catalog:**

1. Select **File** > **New Catalog**. The [New Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009587941-New-Catalog-Dialog) dialog appears.

   ![New Catalog dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889327895/nwctlg.gif)

   If necessary, Logi JReport Designer will prompt you to save changes to the current open catalog. Only one catalog can be open at a time.
2. In the Name field, enter the name for the catalog. The catalog name must include the extension (.cat or .cat.xml)
3. In the Data Source Name field, input the name for the data source that will be created along with the catalog (when creating a catalog, by default, a data source is created in the catalog at the same time). You can include spaces in the name but do not use special characters.
4. Specify the path to save the catalog in the Directory field. You can also select the button **![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif)** to browse to and select the directory in which to create the catalog. The directory you specify must not already contain a catalog file.
5. Select **OK** to create the catalog. The Catalog Manager displays with a data source created for the catalog.

You can then [set up the required connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009563942-Connecting-to-Your-Data-Sources) to connect the catalog data source with your databases. A data source in a catalog can be connected with multiple connections. Logi JReport also supports the Multiple Data Sources feature, which means in one catalog you can add as many data sources as you need and connect them with many different types of data. However, if you want to mash up data that come from multiple connections into a single [query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) or [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562602-Creating-a-Business-View), the database connections must be all in the same data source in the catalog.

**To add another data source to a catalog:**

1. Do either of the following:
   * In the Catalog Manager, select a data source node, then select **New Data Source** on the Catalog Manager toolbar.
   * Select **Home** > **New** > **Data Source**.
   * Select **File** > **New** > **Data Source**.
2. In the New Data Source dialog, specify a name for the data source in the Data Source Name field, select the connection type, then select **OK**.

   ![New Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893864599/nwdtsrc.gif)
3. [Set up the first connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009563942-Connecting-to-Your-Data-Sources) in the data source according to your requirements.

When multiple data sources are created in a catalog, you need to specify which data source will be the default one for the catalog (by default, the data source that is created along with the catalog is the default data source of the catalog). To do this, right-click the data source which you want to use as the default data source, then select **Set as Default** on the shortcut menu. A catalog must have one and only one default data source.

![Set Default Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404894010775/ctlg_crt_deflt.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562742-Knowing-Catalogs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583221-Saving-a-Catalog)
