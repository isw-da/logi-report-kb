---
title: "UDS Column Properties"
id: 1500010100141
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100141-UDS-Column-Properties
updated_at: 2021-07-23T19:16:26Z
---

# UDS Column Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061622-User-Defined-Data-Source-UDS-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061602-User-Defined-Function-UDF-Properties)

# UDS Column Properties

This topic lists the properties of a Column object in a user-defined data source.

| Property Name | Description |
| --- | --- |
| General | |
| Array | Specifies whether the column is an array type or not. Data type: Boolean |
| Auto Group Index | Specifies the index of automatic group. The start index is 0, and if do not group by this field automatically, the index is -1. Data type: Integer |
| Column Index | Specifies the column index in the result set. Data type: Integer |
| Column Mapping Index | Specifies the column index in the result set. Data type: Integer |
| Column Name | Specifies the name of the column in the raw data source. Data type: String |
| Currency | Specifies whether to control the SQL type of formulas or summaries in which the BigDecimal type fields are imported.  * **true** - The formula or summary which is built with the BigDecimal type field will be BigDecimal type, and its [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500010061402-Formula-Properties#SQL) value will be set to 3. * **false** - The normal data type will be used for the formula or summary.   Data type: Boolean |
| Description | Specifies the description of the column. Data type: String |
| Display Width | Specifies the display width of the column. Type a numeric value to change the width. Data type: Float  Note icon   * If the Display Width value of a column is not set in the Catalog Manager, the column will be inserted in a report with the default width defined by Logi Report. * Assume that you have set the Display Width of a column, and used the column while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Length | Specifies the length of the column's value, in bytes. Data type: Integer |
| Name | Specifies the mapped name of the column in the catalog. Data type: String |
| [Nullable](https://devnet.logianalytics.com/hc/en-us/articles/1500010099941-HDS-Column-Properties#Nullable) | Specifies the nullability of the column's value. Choose an option from the drop-down list. Data type: Enumeration |
| Number Base | Specifies the number base of the column. Data type: Integer |
| Path String | Specifies the path of the column, which is used to identify the column in tree. Data type: String |
| Precision | Specifies the precision of the column's value. The default value comes from data source metadata and it specifies the column's largest number of digits. The larger the precision is, the more memory it might take, however, the more accurate values you will get. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the column's value. Data type: Integer |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500010061402-Formula-Properties#SQL) | Specifies the SQL type of the column defined in Java. Choose an option from the drop-down list. Data type: Integer |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the column according to the contents. Data type: Boolean |
| Auto Scale in Number | The property is available when the column is of the Number data type. It specifies whether to automatically scale the column values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale values.   The option "auto" means that the property setting follows that of the parent data container when the column is added in a report.  Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| Horizontal Alignment | Specifies the horizontal justification of the text in the column. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the column. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the column. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the column. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the column. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the column. Type a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the column, which takes effect when the column is inserted into a report. By default, no value is specified to the property, which means a height will be assigned to the column by Logi Report automatically. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the column, which takes effect when the column is inserted into a report. By default, no value is specified to the property, which means a height will be assigned to the column by Logi Report automatically. Type a numeric value to change the width. Data type: Float |
| Color | |
| Background | Specifies the background color of the column. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the column. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the column. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether or not to draw two shadowed borders, beneath and to the right of the column. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color with which to draw a pattern to fill the column. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#PatternStyle) | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Others | |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061622-User-Defined-Data-Source-UDS-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061602-User-Defined-Function-UDF-Properties)
