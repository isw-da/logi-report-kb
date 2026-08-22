---
title: "Filtering Reports"
id: 12480381681293
section: "Designing Your Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480381681293-Filtering-Reports
updated_at: 2026-02-25T23:47:35Z
source_host: docs-report.zendesk.com
---
# 
Filtering Reports

This topic introduces the different filters you can apply to narrow down data of your reports, and describes how you can apply a local filter in a report in detail.

This topic contains the following sections:

- Comparing the Filter Types

- Applying a Component Filter in a Page Report

## 
Comparing the Filter Types

To filter the data you want to display in a report, you can use the following filters:

- 
Query filter (including filter on SQL and filter on APE), which applies to all data components that use the query.

- 
Dataset filter, which applies to all data components that use the dataset in the report. 

- 
On-screen filter, that is the filter created via a filter control. It applies to the data components that use the same data source as the filter control in the report at runtime.

- 
Component filter on individual data component (Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI) defined via the component wizard or using the Edit Filter dialog box in a query-based page report. It applies to this specific data component and does not affect other components that use the same dataset in the page report.

Both query filters and dataset filters can be passed along to the database. They are much more efficient because only the filtered data is returned to Report Engine. The benefit of using a dataset filter instead of a query filter is that it only affects data components that use the dataset in a report. It still passes the filter to the database but does not change the catalog, thus it does not affect any other reports.  However, if you are using stored procedures, SOAP Web Service data sources, and other data sources, Report Engine may not be able to pass the filter to the database. 

Component filters are not passed to the database, so all data is returned and Report Engine filters the data locally. This consumes a lot more computer resources and can be very inefficient. In addition, for data share concern, component filters most often cannot be pushed down to the database even when you have enabled the Push Down Group Query feature.

You can push down on-screen filters in a page report tab or web report to the underlying database (by setting its Push Down On-screen Filter property to "true"  in the Report Inspector), to leverage query optimization capabilities at the database level to improve the overall performance at runtime, especially when the report applies big data. However, when a report only contains a small amount of data, you should not push down the filters, because too many accesses to the database also brings performance issues.

## 
Applying a Component Filter in a Page Report

- In a query-based page report, right-click the data component you want to filter and select Edit Filter. Designer display the Edit Filter dialog box.
    

 If you have applied a filter to the data component when creating it via the Filter screen of the component wizard, Designer automatically displays the filter conditions in the Edit Filter dialog box. You can remove or edit the conditions according to your requirements.

- 
Select Add Condition to add a condition line.
          

- From the field drop-down list, select the field on which the condition is based. The drop-down list contains all the DBFields in the query resource the data component uses, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource. You can select any field to filter. 

- Choose the operator with which to compose the condition from the operator drop-down list.

- From the value drop-down list, select the value or values of how to filter the field depending on the selected operator.
You can also type the values in the text box if you are familiar with the values. 
- When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

- When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
     If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement Trim(@Field) that transforms the spaces into empty string, then use the formula to replace the field itself in the condition.
    

- Repeat  the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
- To group some condition lines, select them and select Group, Designer then adds the selected condition lines  in one group and applies them as one line of filter expression (you can also group conditions and groups together).

- To take out any condition or group from a group, select it and select Ungroup.

- To adjust the priority of the condition lines, select it and select Up or Down.

- To delete a condition line, select it and select Delete.
            

- Select OK to create the filter for the data component.

- You cannot filter the following SQL type of data: Db.SQL_BINARY, Db.SQL_BLOB, Db.SQL_CLOB, Db.SQL_LONGVARCHAR, Db.SQL_LONGVARBINARY, Db.SQL_VARBINARY, and Db.SQL_OTHER. 

- When a data component uses an HDS as the data resource, Report Engine cannot apply the filter conditions you define in the Edit Filter dialog box for the data component when you run the report due to the specialty of HDS. Therefore, if you want to filter data components of this type, you need to use dataset filter.
