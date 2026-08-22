---
title: "Query Column Properties"
id: 5735584906647
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735584906647-Query-Column-Properties
updated_at: 2022-11-02T08:09:50Z
---

# Query Column Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735584895639-Query-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735554081815-Query-Modifier-Properties)

# Query Column Properties

This topic describes the properties of a Column object in a query.

There are two types of the Column object in a query: table column and computed column. All the properties are read only for table columns, while some are editable for computed columns.

| Property Name | Description |
| --- | --- |
| Array | Specifies whether the column is an array type. Data type: Boolean |
| Column Name | Shows the name of the column in the raw database. |
| Currency | Shows whether to control the SQL type of the formulas and summaries which reference the column if the column is of the BigDecimal type.  * **true** Select to apply the BigDecimal type to the formulas and summaries and set their [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties#SQL) to 3. * **false** Select to apply normal data type to the formulas and summaries.   Data type: Boolean  Note icon Designer does not provide this property for a computed column. |
| Description | Specifies the description of the object. Data type: String |
| Display Width | Specifies the display width of the object, which takes effect when you insert the object into reports. Type a numeric value to change the width. If you do not set the display width, Designer applies a default width to it automatically. Data type: Float  Note icon After you set the Display Width property of an object and use the object while creating a data component with wizard, Designer may adjust its width according to the paper size. |
| Name | Shows the mapped name of the column in the catalog. |
| Nullable | Specifies the nullability for the values of the object. Choose an option from the drop-down list.  * **true** Select to indicate the object supports null values. * **false** Select to indicate the values of the object cannot be null. * **unknown** Select to indicate whether the values of the object can be null or not is unknown.   Data type: Enumeration |
| Precision | Specifies the precision for the values of the object. The default precision comes from data source metadata and defines the object's largest number of digits. The larger the precision is, the more memory it might take; however, the more accurate values you can get. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the values of the object. Data type: Integer |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties#SQL) | Specifies the SQL type of the object defined in Java. Choose an option from the drop-down list. Data type: Integer |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735584895639-Query-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735554081815-Query-Modifier-Properties)
