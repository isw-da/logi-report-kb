---
title: "Data Source Properties"
id: 45190640944525
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190640944525-Data-Source-Properties
updated_at: 2026-04-30T15:15:25Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Data Source Properties

This topic describes the properties of a Data Source object in a catalog.

| Property Name | Description |
| --- | --- |
| Display Rounding Mode | Specifies the rounding mode for displaying numeric data values in the reports that you create in this data source. Choose an option from the drop-down list. Up Rounding mode to round away from zero. Down Rounding mode to round towards zero. Ceiling Rounding mode to round towards positive infinity. Floor Rounding mode to round towards negative infinity. Half Up Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round up. Half Down Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round down. Half Even Rounding mode to round towards the "nearest neighbor" unless both neighbors are equidistant, in which case, round towards the even neighbor. For more information about the rounding mode, go to docs.oracle.com/javase/10/docs/api/java/math/RoundingMode.html. Data Type: Enumeration |
| Is Default | Specifies whether the data source is the default data source for the catalog. One catalog must have one and only one default data source. Data type: Boolean |
| Name | Specifies the name of the data source. Data type: String |
| Pre-join | Specifies whether to apply the pre-join information that you define for the data source when building queries and defining join relationships in business views in the same data source. Data type: Boolean |
| Use Mapping Name Prefix | Specifies whether to automatically add table/imported SQL/stored procedure names as the prefix in the default mapping names of their columns when you add tables, importing SQLs, and stored procedures from database into the data source. By default, this property is "false", so when you add table1.column1 into the data source, its default mapping name depends on whether the mapping name "column1" already exists in the data source: if it exists, Designer applies "table1_column1" as the default mapping name of table1.column1; if it does not exist, Designer uses "column1". If you want to use "table1_column1" no matter whether "column1" exists, you can set this property to "true", then Designer always add the table names as the prefix of their columns. Data type: Boolean |
