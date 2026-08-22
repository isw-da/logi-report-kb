---
title: "Data Source Properties"
id: 5735553934359
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735553934359-Data-Source-Properties
updated_at: 2022-11-02T08:07:59Z
---

# Data Source Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532546071-Hierarchy-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties)

# Data Source Properties

This topic describes the properties of a [Data Source object](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#DataSource) in a catalog.

| Property Name | Description |
| --- | --- |
| Display Rounding Mode | Specifies the rounding mode for displaying numeric data values in the reports that you create in this data source. Choose an option from the drop-down list.  * **Up** Rounding mode to round away from zero. * **Down** Rounding mode to round towards zero. * **Ceiling** Rounding mode to round towards positive infinity. * **Floor**  Rounding mode to round towards negative infinity. * **Half Up**  Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round up. * **Half Down** Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round down. * **Half Even** Rounding mode to round towards the "nearest neighbor" unless both neighbors are equidistant, in which case, round towards the even neighbor.   For more information about the rounding mode, see <https://docs.oracle.com/javase/10/docs/api/java/math/RoundingMode.html>.  Data Type: Enumeration |
| Is Default | Specifies whether the data source is the default data source for the catalog. One catalog must have one and only one default data source. Data type: Boolean |
| Name | Specifies the name of the data source. Data type: String |
| Pre-join | Specifies whether to apply the pre-join information that you define for the data source when building queries and defining join relationships in business views in the same data source. Data type: Boolean |
| Use Mapping Name Prefix | Specifies whether to automatically add table/imported SQL/stored procedure names as the prefix in the default mapping names of their columns when you add tables, importing SQLs, and stored procedures from database into the data source. By default, this property is "false", so when you add table1.column1 into the data source, its default mapping name depends on whether the mapping name "column1" already exists in the data source: if it exists, Designer applies "table1\_column1" as the default mapping name of table1.column1; if it does not exist, Designer uses "column1". If you want to use "table1\_column1" no matter whether "column1" exists, you can set this property to "true", then Designer always add the table names as the prefix of their columns.  Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532546071-Hierarchy-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties)
