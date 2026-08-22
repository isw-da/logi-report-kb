---
title: "Cached Query Results"
id: 1500009570622
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results
updated_at: 2021-07-24T05:53:54Z
---

# Cached Query Results

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592561-Query-Modifiers)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager)

# Cached Query Results

By default, when you run a report, Logi JReport Engine fetches data from the database using the JDBC driver. For reports that are built on queries (and also [imported SQL files](https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures) and [user defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009564222-User-Defined-Data-Sources)), Logi JReport Designer enables you to create cached result files and save them somewhere in your machine. Then, when you view these reports, you can choose to use the data from the cached query result file as opposed to the database. This is very useful for working on the design of a report while you are off-line and do not have a DBMS connection. Additionally, it is helpful when you need to send data and reports to Jinfonet Support for assistance.

Below is a list of the sections covered in this topic:

> * [Creating a Cached Query Result for a Query](#Create)
> * [Managing Cached Query Results](#Manage)

## Creating a Cached Query Result for a Query

Logi JReport Designer provides you with two ways to create cached query results, the first is with the Catalog Manager and the second is with the Data panel.

* **Creating a cached query result file in the Catalog Manager**
  1. In the Catalog Manager, select the query for which you intend to create the cached query result file.
  2. Right-click the query, and select **Create Cached Query Result** from the shortcut menu.
  3. In the Save Cached Query Result dialog, specify the file name with or without an extension and the folder where you want to save the result file. It is recommended to use an extension such as .cqr to help you identify the files. Logi JReport does not provide a default extension.
  4. Select **Save** and the cached query result file will be saved to the specified folder.
* **Creating a cached query result file in the Data panel** (available to page reports only)
  1. In the [Data panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel), right-click the query on which the report is built and select **Create Cached Query Result** from the shortcut menu.
  2. In the Save Cached Query Result dialog, specify the file name with or without an extension and the folder where you want to save the result file and then select **Save**.

Then, you can set the [Data Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataDriver) property on the dataset created from the query appropriately in the Report Inspector to make a report run using cached query result.

**Note:** If you check the option "Use cached query result" in the Catalog category of the Options dialog, whenever you view a report in Logi JReport Designer, a dialog will prompt you to choose a cached query result to run the report.

## Managing Cached Query Results

When specifying the Data Driver property for a dataset, you may find it inconvenient to input a property value that is long and complicated. To help you with this, Logi JReport Designer provides a tool for managing your cached query results, the Data Source Drivers.

Assume that a cached query result file orderstat\_cached for the query OrderStat in the catalog file SampleReports.cat has been created and saved in `C:\Logi JReport\Designer\Cached`. To use the Data Source Drivers, follow the steps below:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `C:\Logi JReport\Designer\Demo\Reports\SampleReports`.
2. In the Catalog Manager, select **Data Source Drivers** on the toolbar. The [Data Source Drivers](https://devnet.logianalytics.com/hc/en-us/articles/1500009565122-Data-Source-Drivers-Dialog) dialog appears.

   ![Data Source Drivers dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893824791/dtsrcdrvr.gif)

   All the added drivers will be listed in the Data Source Drivers box. If you want to remove a driver, select the driver and select the Remove button. To edit a driver, select the driver and select the Edit button.
3. Select the **New** button, and the [Data Source Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586281-Data-Source-Editor-Dialog) appears.

   ![Data Source Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893825047/dtsrcedtr.gif)
4. Enter a name for the driver in the Driver Name box. Here, we name it **OrderStat**.
5. Check the **URL** radio button and input the URL as follows:

   jrquery:/jet.universe.resultfile.UResultFileResultSet;*Fullpath\_of\_cached\_query\_result*

   In the example, the URL is `jrquery:/jet.universe.resultfile.UResultFileResultSet;C:\Logi JReport\Designer\Cached\orderstat_cached`

   **Note:** If you check the Driver radio button to specify the driver, you will need to input the class name and parameter of the driver as follows:
   * **Class Name**: jet.universe.resultfile.UResultFileResultSet
   * **Parameter**: Full path of the cached query result (`C:\Logi JReport\Designer\Cached\orderstat_cached` in this example)

   Then, a URL will be generated according to your input information.
6. Select **OK** to add the driver.
7. Select **OK** in the Data Source Drivers dialog to close it.
8. Now you can choose the driver from the Data Driver property's drop-down list directly without inputting the long value manually.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592561-Query-Modifiers)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager)
