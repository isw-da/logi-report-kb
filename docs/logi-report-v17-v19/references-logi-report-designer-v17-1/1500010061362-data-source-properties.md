---
title: "Data Source Properties"
id: 1500010061362
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061362-Data-Source-Properties
updated_at: 2021-07-23T19:16:21Z
---

# Data Source Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099881-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061382-Data-Source-Security-Properties)

# Data Source Properties

This topic lists the properties of a Data Source object in a catalog.

| Property Name | Description |
| --- | --- |
| [Display Rounding Mode](#Round) | Specifies the rounding mode for displaying numeric data values in reports that are created on this data source. Choose an option from the drop-down list.  * **Up** -   Rounding mode to round away from zero. Always increments the digit prior to a non-zero discarded fraction. * **Down** -   Rounding mode to round towards zero. Never increments the digit prior to a discarded fraction (that is, truncates). * **Ceiling** -   Rounding mode to round towards positive infinity. If the result is positive, behaves as for Up; if negative, behaves as for Down. * **Floor** -   Rounding mode to round towards negative infinity. If the result is positive, behaves as for Down; if negative, behaves as for Up. * **Half up** -   Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round up. Behaves as for Up if the discarded fraction is >= 0.5; otherwise, behaves as for Down. * **Half down** -   Rounding mode to round towards "nearest neighbor" unless both neighbors are equidistant, in which case round down. Behaves as for Up if the discarded fraction is > 0.5; otherwise, behaves as for Down. * **Half even** -   Rounding mode to round towards the "nearest neighbor" unless both neighbors are equidistant, in which case, round towards the even neighbor. Behaves as for Half up if the digit to the left of the discarded fraction is odd; behaves as for Half down if it's even.   For more information about the rounding mode, refer to <http://docs.oracle.com/javase/7/docs/api/java/math/RoundingMode.html>.  Data Type: Enumeration |
| Is Default | Specifies whether the data source is the default data source for the current catalog. One catalog must have one and only one default data source. Data type: Boolean |
| Name | Specifies the name of the data source. Data type: String |
| Pre-join | Specifies whether or not to apply the pre-join information defined on the data source when building a query or defining join relationships in business views in the same data source. Data type: Boolean |
| Use Mapping Name Prefix | Specifies whether to automatically add table/imported SQL/stored procedure names as the prefix before column names in the default mapping names when adding tables, importing SQLs and stored procedures from DBMS into the data source. By default the property is false, so when table1.column1 is added into the data source, its default mapping name depends on whether the mapping name "column1" already exists in the data source: if it exists, table1\_column1 will be used as the default mapping name of table1.column1; if it does not exist, column1 will be used. If you want to use "table1\_column1" no matter whether "column1" exists, you can set this property to true, then table names will always be added as the prefix of columns.  Data type: Boolean |

## Display Rounding Mode

| Input number | Input rounded to one digit with Up rounding | Input rounded to one digit with Down rounding | Input rounded to one digit with Ceiling rounding | Input rounded to one digit with Floor rounding | Input rounded to one digit with Half up rounding | Input rounded to one digit with Half down rounding | Input rounded to one digit with Half even rounding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.5 | 6 | 5 | 6 | 5 | 6 | 5 | 6 |
| 2.5 | 3 | 2 | 3 | 2 | 3 | 2 | 2 |
| 1.6 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| 1.1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| 1.0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| -1.0 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| -1.1 | -2 | -1 | -1 | -2 | -1 | -1 | -1 |
| -1.6 | -2 | -1 | -1 | -2 | -2 | -2 | -2 |
| -2.5 | -3 | -2 | -2 | -3 | -3 | -2 | -2 |
| -5.5 | -6 | -5 | -5 | -6 | -6 | -5 | -6 |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099881-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061382-Data-Source-Security-Properties)
