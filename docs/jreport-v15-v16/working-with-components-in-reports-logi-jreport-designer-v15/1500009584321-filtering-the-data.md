---
title: "Filtering the Data"
id: 1500009584321
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data
updated_at: 2021-07-24T05:55:57Z
---

# Filtering the Data

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584301-Managing-Cells-Columns-and-Rows-in-a-Table)

# Filtering the Data

This topic introduces how to filter the data in a table.

Below is a list of the sections covered in this topic:

> * [Filter Levels](#FilterLevel)
> * [Adding Filter Conditions to a Table](#Table)

## Filter Levels

There are 3 levels of filters in Logi JReport:

* [Query filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009592541-Using-a-Query-to-Filter-Multiple-Queries) (including [filter on SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files#Filter)), which applies to all data components that use the query.
* [Dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets), which applies to the data components that use the dataset in the current report.
* Local filter on individual data component defined using the report wizard or by right-clicking a data component and using the Edit Filter dialog. It applies to this individual data component and does not affect other components that use the same dataset.

Dataset filters are passed along to the Query Engine the same as query filters. The two levels of filters are much more efficient since only the filtered data is returned to Logi JReport. Local filters on individual components are not passed to the Query Engine so all data is returned to Logi JReport and the component filters out the unnecessary data. This may be very inefficient so always use dataset filters or query filters whenever possible. However if you are using stored procedures, web services and other data sources, Logi JReport may not be able to pass the filter to the Query Engine.

The advantage of using a dataset filter instead of a query filter is that it only affects data components that use the dataset in the current report. It still passes the filter to the database but does not change the catalog thus does not affect any other reports.

For data share concern, local filters most often cannot be pushed down to the database even though the [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009590441-JDBC-HIVE-Connection-Properties#PushDown) feature is enabled, thus all data is returned and Logi JReport filters the data locally which will use a lot more computer resources. To get better performance, it is better to define the filter at the other two levels.

## Adding Filter Conditions to a Table

To add filter conditions to a table, that is to apply a local filter on a table, follow the steps below:

1. Right-click the table and select **Format Filter** to display the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

   ![Edit Filer dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893926423/edtfltr.gif)
2. If the table is created using a business view, the Filter drop-down list is available, listing all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters) of the business view. You can select one from the drop-down list to apply, or select **User Defined** in the list to define a new filter as required.
3. Select the **Add Condition** button to add a condition line.
4. In the field drop-down list, specify the field on which the filter will be based.

   For a table created on a query, you can filter on any DBField in the query, or a parameter or valid formula that is in the same catalog data source as the query. For a table created on a business view, you can only filter on a group or detail object in the business view.
5. From the operator drop-down list, set the operator with which to compose the filter expression.
6. In the value text field, specify the value of how to filter the field. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

   For a table created on a business view, you can use the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009584241-Special-Fields#UserName) or a parameter to define the value dynamically. When the available parameters cannot meet your requirement, you can also create a [local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the filter. For the usage of parameters in filter conditions, see the example in [Dynamically Filtering Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries).
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to create the filter.

   Then when you preview the table, only data satisfying the specified filter conditions are shown.

**Note:** The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584301-Managing-Cells-Columns-and-Rows-in-a-Table)
