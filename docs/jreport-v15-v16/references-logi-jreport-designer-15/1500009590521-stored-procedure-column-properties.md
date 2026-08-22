---
title: "Stored Procedure Column Properties"
id: 1500009590521
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590521-Stored-Procedure-Column-Properties
updated_at: 2021-07-24T05:54:24Z
---

# Stored Procedure Column Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568902-Stored-Procedure-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590581-Summary-Properties)

# Stored Procedure Column Properties

The properties of a stored procedure column are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Array | Specifies whether the column is an array type or not. Data type: Boolean |
| Column Index | Specifies the column index in the result set. Data type: Integer |
| Column Name | Specifies the name of the column in the raw data source. Data type: String |
| Currency | Specifies whether to control the SQL type of formulas or summaries in which the BigDecimal type fields are imported.  * **true** - The formula or summary which is built with the BigDecimal type field will be BigDecimal type, and its [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009568762-Formula-Properties#SQL) value will be set to 3. * **false** - The normal data type will be used for the formula or summary.   Data type: Boolean |
| Description | Specifies the description of the column. Data type: String |
| Display Width | Specifies the display width of the column. Enter a numeric value to change the width. Data type: Float  **Notes:**   * If the Display Width value of a column is not set in the Catalog Manager, the column will be inserted in a report with the default width defined by Logi JReport. * Assume that you have set the Display Width of a column, and used the column while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Length | Specifies the length of the column's value, in bytes. Data type: Integer |
| Name | Specifies the mapped name of the column in the Logi JReport catalog. Data type: String |
| [Nullable](https://devnet.logianalytics.com/hc/en-us/articles/1500009568782-HDS-Column-Properties#Nullable) | Specifies the nullability of the column's value. Choose an option from the drop-down list. Data type: Enumeration |
| Number Base | Specifies the number base of the column. Data type: Integer |
| Precision | Specifies the precision of the column's value. The default value comes from data source meta data and it specifies the column's largest number of digits. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the column's value. Data type: Integer |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009568762-Formula-Properties#SQL) | Specifies the SQL type of the column defined in Java. Choose an option from the drop-down list. Data type: Integer |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the column according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Format | Specifies the display format of the column's value. The format varies with the column's data type and can be defined manually. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the text in the column. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the column. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the column. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the column. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the column. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the column. Enter a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the column, which takes effect when the column is inserted into a report. By default, no value is specified to the property, which means a height will be assigned to the column by Logi JReport automatically. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the column, which takes effect when the column is inserted into a report. By default, no value is specified to the property, which means a height will be assigned to the column by Logi JReport automatically. Enter a numeric value to change the width. Data type: Float |
| Color | |
| Background | Specifies the background color of the column. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the column. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the column. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether or not to draw two shadowed borders, beneath and to the right of the column. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the column. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color with which to draw a pattern to fill the column. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the column. * **50%** - The column will be filled in the specified color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the specified color. * **vertical** - The pattern will be made of vertical lines of the specified color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the specified color. * **diagonal** - The pattern will be made of slash lines of the specified color.   Data type: Enumeration |
| Others | |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500009589921-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568902-Stored-Procedure-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590581-Summary-Properties)
