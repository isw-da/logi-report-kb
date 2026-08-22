---
title: "Query Column Properties"
id: 1500009590561
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590561-Query-Column-Properties
updated_at: 2021-07-24T05:54:23Z
---

# Query Column Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568942-Query-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590541-Query-Modifier-Properties)

# Query Column Properties

There are two kinds of columns in a query: table columns and computed columns, the properties of which are listed as follows. Note that, all the properties are read only for table columns, and some are editable for computed columns.

The properties of a query column are as follows:

| Property Name | Description |
| --- | --- |
| Array | Specifies whether the column is an array type or not. Data type: Boolean |
| Column Name | Indicates the name of the column in the raw database. This property is read only. |
| Currency | Displays whether to control the SQL type of formulas or summaries in which the BigDecimal type fields are imported.  * **true** - The formula or summary which is built with the BigDecimal type field will be BigDecimal type, and its [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009568762-Formula-Properties#SQL) value will be set to 3. * **false** - The normal data type will be used for the formula or summary.   Data type: Boolean |
| Description | Specifies the description of the column. Data type: String |
| Display Width | Specifies the display width of the column. Data type: Float  **Notes:**   * If the Display Width value of a column is not set in the Catalog Manager, the column will be inserted in a report with the default width defined by Logi JReport. * Assume that you have set the Display Width of a column, and used the column while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Expression | Specifies the statement of the formula. Available to computed column only. Data type: String |
| Name | Shows the display name of the column. This property is read only. |
| [Nullable](https://devnet.logianalytics.com/hc/en-us/articles/1500009568782-HDS-Column-Properties#Nullable) | Specifies the nullability of the column's value. Data type: Enumeration |
| Precision | Specifies the precision of the column's value. The default value comes from data source meta data and it specifies the column's largest number of digits. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the column's value. Data type: Integer |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009568762-Formula-Properties#SQL) | Specifies the SQL type of the column defined in Java. Choose an option from the drop-down list. Data type: Integer |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568942-Query-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590541-Query-Modifier-Properties)
