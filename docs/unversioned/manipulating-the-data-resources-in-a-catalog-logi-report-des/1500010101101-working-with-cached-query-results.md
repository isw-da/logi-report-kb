---
title: "Working with Cached Query Results"
id: 1500010101101
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results
updated_at: 2021-07-23T19:16:45Z
---

# Working with Cached Query Results

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062662-Using-Query-Modifiers)

# Working with Cached Query Results

By default, when you run a report, Logi Report Engine fetches data from the database for the report, thus if you are offline and do not have a DBMS connection, you would not be able to load the report data. To help you avoid the inconvenience, Logi Report provides the Cached Query Result feature, which enables you to create cached result files for queries (and also [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures), [user-defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources), and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views) that function similarly as queries), save them somewhere in your machine, and apply them to your reports that use the queries. Then, when you view the reports, Logi Report Engine fetches data from the files as opposed to the database. This is very useful for working on the design of a report while you are offline. It is also helpful when you have problems with your reports and need to send the reports with data resources to Logi Analytics for reproducing the problems. This topic describes how you can create cached query results, apply them to reports, and generate data source drivers for cached query results.

This topic contains the following sections:

* [Creating Cached Query Results](#Create)
* [Applying Cached Query Results](#Apply)
* [Generating Data Source Drivers for Cached Query Results](#Manage)

## Creating Cached Query Results

You can create cached query results either in the Catalog Manager or in the Data panel.

* **Creating a cached query result file in the Catalog Manager**
  1. In the Catalog Manager, select the query for which you intend to create the cached query result file.
  2. Right-click the query, and select **Create Cached Query Result** from the shortcut menu.
  3. In the Save Cached Query Result dialog box, specify the file name with or without an extension and the folder where you want to save the result file. It is recommended to use an extension such as ".cqr" to help you identify the files. Designer does not provide a default extension.
  4. Select **Save** to save the cached query result file to the specified folder.
* **Creating a cached query result file in the Data panel**
  1. In the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010101501-Data-Panel), right-click the query and select **Create Cached Query Result** from the shortcut menu.
  2. In the Save Cached Query Result dialog box, specify the file name with or without an extension and the folder where you want to save the result file and then select **Save**.

## Applying Cached Query Results

To run a library component or a query-based page report using cached query result, you can set the [Data Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500010062082-Dataset-Properties#DataDriver) property on the [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) appropriately in the Report Inspector. You can specify the property value by inputting manually or selecting a [predefined data source driver](#Manage) from the drop-down list.

The input format is as follows: jrquery:/jet.universe.resultfile.UResultFileResultSet;*Fullpath\_of\_cached\_query\_result*

For example, if you save the cached query result to `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Cached` with the file name "test", the property value should be `jrquery:/jet.universe.resultfile.UResultFileResultSet;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Cached\test`.

However, the Data Driver property is not available to web reports and business view-based page reports . In order to apply cached query result to them, you can select the option **Use cached query result** in the Catalog category of the Options dialog box. Then whenever you preview a report in Designer, Designer displays a dialog box for you to choose a cached query result to run the report.

## Generating Data Source Drivers for Cached Query Results

When specifying the Data Driver property for a dataset, you may find it inconvenient to type in a property value that is long and complicated. To help you with this, Designer provides a tool for generating data source drivers for cached query results, which are then available in the Data Driver drop-down list for selection.

Assuming that you have created a cached query result file "orderstat\_cached" for the query OrderStat in the catalog file SampleReports.cat and saved it in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Cached`, to create a data source driver for the cached query result, follow the steps below:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, select **Data Source Drivers** on the toolbar. Designer displays the [Data Source Drivers dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058602-Data-Source-Drivers-Dialog-Box).

   ![Data Source Drivers dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856848151/dtsrcdrvr.gif)

   Designer lists all the added drivers in the **Data Source Drivers** box. If you want to remove a driver, select the driver and select the **Remove** button. To edit a driver, select the driver and select the **Edit** button.
3. Select the **New** button. Designer displays the [Data Source Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096121-Data-Source-Editor-Dialog-Box).

   ![Data Source Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856848535/dtsrcedtr.gif)
4. Type a name for the driver in the **Driver Name** text box. Here, we name it **OrderStat**.
5. Select the **URL** radio button and type the URL as follows:

   jrquery:/jet.universe.resultfile.UResultFileResultSet;*Fullpath\_of\_cached\_query\_result*

   In the example, the URL is `jrquery:/jet.universe.resultfile.UResultFileResultSet;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Cached\orderstat_cached`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you select the Driver radio button to specify the driver, you need to specify the class name and parameter of the driver as follows:
   * **Class Name**: jet.universe.resultfile.UResultFileResultSet
   * **Parameter**: Full path of the cached query result (`C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Cached\orderstat_cached` in this example)

   Then, Designer generates a URL according to the information you specify.
6. Select **OK** to add the driver.
7. Select **OK** in the Data Source Drivers dialog box to close it.
8. Now you can choose the driver from the Data Driver property's drop-down list directly without inputting the long value manually.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062662-Using-Query-Modifiers)
