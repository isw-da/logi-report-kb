---
title: "Query Column Properties"
id: 1500009611742
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611742-Query-Column-Properties
updated_at: 2021-07-24T16:03:44Z
---

# Query Column Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634861-Query-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611722-Query-Modifier-Properties)

# Query Column Properties

This topic lists the properties of a Column object in a query.

There are two types of the Column object in a query: table column and computed column. All the properties are read only for table columns, while some are editable for computed columns.

| Property Name | Description |
| --- | --- |
| Array | Specifies whether the column is an array type or not. Data type: Boolean |
| Column Name | Indicates the name of the column in the raw database. This property is read only. |
| Currency | Displays whether to control the SQL type of formulas or summaries in which the BigDecimal type fields are imported.  * **true** - The formula or summary which is built with the BigDecimal type field will be BigDecimal type, and its [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009611622-Formula-Properties#SQL) value will be set to 3. * **false** - The normal data type will be used for the formula or summary.   Data type: Boolean |
| Description | Specifies the description of the column. Data type: String |
| Display Width | Specifies the display width of the column. Data type: Float  **Notes:**   * If the Display Width value of a column is not set in the Catalog Manager, the column will be inserted in a report with the default width defined by Logi Report. * Assume that you have set the Display Width of a column, and used the column while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Expression | Specifies the statement of the formula. Available to computed column only. Data type: String |
| Name | Shows the display name of the column. This property is read only. |
| [Nullable](https://devnet.logianalytics.com/hc/en-us/articles/1500009634681-HDS-Column-Properties#Nullable) | Specifies the nullability of the column's value. Data type: Enumeration |
| Precision | Specifies the precision of the column's value. The default value comes from data source metadata and it specifies the column's largest number of digits. The larger the precision is, the more memory it might take, however, the more accurate values you will get. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the column's value. Data type: Integer |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009611622-Formula-Properties#SQL) | Specifies the SQL type of the column defined in Java. Choose an option from the drop-down list. Data type: Integer |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634861-Query-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611722-Query-Modifier-Properties)
