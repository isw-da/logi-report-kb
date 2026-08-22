---
title: "Filtering Reports"
id: 4405664691735
section: "Creating Datasets and Designing Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664691735-Filtering-Reports
updated_at: 2022-01-27T20:34:54Z
---

# Filtering Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports)

# Filtering Reports

This topic introduces the different filters you can apply to narrow down the data of your reports, and describes how you can apply a local filter in a report in detail.

This topic contains the following sections:

* [Comparing the Filter Types](#Type)
* [Applying a Local Filter in a Report](#EditFilter)

## Comparing the Filter Types

To filter the data shown in a report, you can use the following filters:

* [Query filter](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog#FilterQuery) (including filter on [SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs) and filter on [APE](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs)), which applies to all data components that use the query.
* [Dataset filter](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets), which applies to the data components that use the dataset in the current report.
* Local filter on individual data component (Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI) defined via the component wizard or [using the Edit Filter dialog box](#EditFilter). It applies to this individual data component and does not affect other components that use the same dataset.
* On-screen filter, that is the filter created via a [filter control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Filter). It applies to the data components that use the same data source as the filter control in the current report.

Dataset filters are passed along to the Query Engine the same as query filters. The two levels of filters are much more efficient since only the filtered data is returned to Logi Report Engine. Local filters on individual components are not passed to the Query Engine so all data is returned to Logi Report Engine and the component filters out the unnecessary data. This may be very inefficient so always use dataset filters or query filters whenever possible. However, if you are using stored procedures, web services, and other data sources, Logi Report Engine may not be able to pass the filter to the Query Engine.

The advantage of using a dataset filter instead of a query filter is that it only affects data components that use the dataset in the current report. It still passes the filter to the database but does not change the catalog, thus it does not affect any other reports.

For data share concern, local filters most often cannot be pushed down to the database even though the [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/4405664629143-JDBC-Hive-Connection-Properties#PushDown) feature is enabled, thus all data is returned and Logi Report Engine filters the data locally which uses a lot more computer resources. To get better performance, it is better to define the filter at the other two levels.

## Applying a Local Filter in a Report

1. Right-click a data component in the report to which you want to apply the filter and select **Format Filter**. Designer display the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box).

   ![Edit Filer](https://devnet.logianalytics.com/hc/article_attachments/4420402333207/edtfltr.gif)
2. If the data component uses a business view, the **Filter** drop-down list is available, listing all the [predefined filters](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Filter) of the business view. You can select one from the drop-down list to apply, or select **User Defined** in the list to define a new filter by you own.

   If you have applied a filter to the data component when creating it via the Filter screen of the component wizard, Designer automatically displays the filter conditions in the Edit Filter dialog box. You can remove or edit the conditions according to your requirements.
3. Add the filter conditions. Based on the data resource type which the data component uses, a business view or a query resource, the way to format a filter for the data component varies.

   If the data component uses a business view, you can add filter condition for it in the same way as you [add conditions for a predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#AddCondition) in the business view. Besides, you can use [a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) as the value of a filter condition.

   **To add filter conditions for a data component using a query resource**

   1. Select **Add Condition** to add a condition line.

      ![Filter Condition Line](https://devnet.logianalytics.com/hc/article_attachments/4420410600343/rpt_fltr.gif)
   2. From the field drop-down list, select the field to be filtered. The drop-down list contains all the DBFields in the query resource the data component uses, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource. You can select any field to filter.
   3. From the operator drop-down list, set the operator with which to compose the filter expression.
   4. From the value drop-down list, select the value or values of how to filter the field depending on the selected operator.
      You can also type the values manually in the text box if you are familiar with the values.

      When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

      You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
   5. Repeat the preceding steps to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

      To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select **Up** or **Down**; to delete a condition line, select it and select **Delete**.
4. Select **OK** to create the filter for the data component.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg)

* You cannot filter the following SQL type of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.
* If a data component in a page report uses an HDS as the data resource, Logi Report Engine cannot apply the filter conditions you define in the Edit Filter dialog box for the data component when you run the report due to the [specialty of HDS](https://devnet.logianalytics.com/hc/en-us/articles/4405664411159-Developing-Reports-from-Hierarchical-Data-Sources). Therefore, if you want to apply local filters to data components of this type, you need to use the dataset filter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports)
