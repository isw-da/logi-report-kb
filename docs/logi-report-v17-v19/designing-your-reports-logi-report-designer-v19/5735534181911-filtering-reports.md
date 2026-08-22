---
title: "Filtering Reports"
id: 5735534181911
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports
updated_at: 2022-11-02T08:22:58Z
---

# Filtering Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report)

# Filtering Reports

This topic introduces the different filters you can apply to narrow down data of your reports, and describes how you can apply a local filter in a report in detail.

This topic contains the following sections:

* [Comparing the Filter Types](#Type)
* [Applying a Component Filter in a Page Report](#EditFilter)

## Comparing the Filter Types

To filter the data you want to display in a report, you can use the following filters:

* [Query filter](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#FilterQuery) (including filter on [SQL](https://devnet.logianalytics.com/hc/en-us/articles/5735507746711-Using-Imported-SQLs) and filter on [APE](https://devnet.logianalytics.com/hc/en-us/articles/5735512889367-Using-Imported-APEs)), which applies to all data components that use the query.
* [Dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report), which applies to all data components that use the dataset in the report.
* On-screen filter, that is the filter created via a [filter control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Filter). It applies to the data components that use the same data source as the filter control in the report at runtime.
* Component filter on individual data component (Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI) defined via the component wizard or [using the Edit Filter dialog box](#EditFilter) in a query-based page report. It applies to this specific data component and does not affect other components that use the same dataset in the page report.

Both query filters and dataset filters can be passed along to the database. They are much more efficient because only the filtered data is returned to Logi Report Engine. The benefit of using a dataset filter instead of a query filter is that it only affects data components that use the dataset in a report. It still passes the filter to the database but does not change the catalog, thus it does not affect any other reports. However, if you are using stored procedures, SOAP Web Service data sources, and other data sources, Logi Report Engine may not be able to pass the filter to the database.

Component filters are not passed to the database, so all data is returned and Logi Report Engine filters the data locally. This consumes a lot more computer resources and can be very inefficient. In addition, for data share concern, component filters most often cannot be pushed down to the database even when you have enabled the [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/5735516614679-JDBC-Hive-Connection-Properties#PushDown) feature.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")You can push down on-screen filters in a page report tab or web report to the underlying database (by setting its Push Down On-screen Filter property to "true" in the Report Inspector), to leverage query optimization capabilities at the database level to improve the overall performance at runtime, especially when the report applies big data. However, when a report only contains a small amount of data, you should not push down the filters, because too many accesses to the database also brings performance issues.

## Applying a Component Filter in a Page Report

1. In a query-based page report, right-click the data component you want to filter and select **Edit Filter**. Designer display the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box).

   ![Edit Filer](https://devnet.logianalytics.com/hc/article_attachments/9898474463383/edtfltr.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you have applied a filter to the data component when creating it via the Filter screen of the component wizard, Designer automatically displays the filter conditions in the Edit Filter dialog box. You can remove or edit the conditions according to your requirements.
2. Select **Add Condition** to add a condition line.
3. From the field drop-down list, select the field on which the condition is based. The drop-down list contains all the DBFields in the query resource the data component uses, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource. You can select any field to filter.
4. Choose the operator with which to compose the condition from the operator drop-down list.
5. From the value drop-down list, select the value or values of how to filter the field depending on the selected operator.
   You can also type the values in the text box if you are familiar with the values.
   * When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
   * When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
     If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement `Trim(@Field)` that transforms the spaces into empty string, then use the formula to replace the field itself in the condition.
6. Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
   * To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
   * To take out any condition or group from a group, select it and select **Ungroup**.
   * To adjust the priority of the condition lines, select it and select **Up** or **Down**.
   * To delete a condition line, select it and select **Delete**.
7. Select **OK** to create the filter for the data component.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* You cannot filter the following SQL type of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.
* When a data component uses an HDS as the data resource, Logi Report Engine cannot apply the filter conditions you define in the Edit Filter dialog box for the data component when you run the report due to the [specialty of HDS](https://devnet.logianalytics.com/hc/en-us/articles/5735527967639-Developing-Reports-from-Hierarchical-Data-Sources). Therefore, if you want to filter data components of this type, you need to use dataset filter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report)
