---
title: "Formula Properties"
id: 1500009568762
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568762-Formula-Properties
updated_at: 2021-07-24T05:54:26Z
---

# Formula Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568742-Data-Source-Security-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590421-Hierarchical-Data-Source-Properties)

# Formula Properties

The properties of a formula are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Description | Specifies the description of the formula. Data type: String |
| Display Width | Specifies the display width of the formula. Enter a numeric value to change the width. Data type: Float  **Notes:**   * If the Display Width value of a formula is not set in the Catalog Manager, the formula will be inserted in a report with the default width defined by Logi JReport. * Assume that you have set the Display Width of a formula, and used the formula while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Expression | Displays the whole statement of the formula. This property is read only. |
| Length | Specifies the length of the formula's returned value, in byte. Data type: Integer |
| Name | Specifies the name of the formula. Data type: String |
| Number Base | Specifies the number base of the formula. Data type: Integer |
| Precision | Specifies the precision of the formula's returned value. The default value comes from data source meta data and it specifies the value's largest number of digits. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point of the formula's returned value. Data type: Integer |
| [SQL Type](#SQL) | Specifies the SQL type of the formula defined in Java. Choose an option from the drop-down list. Data type: Integer |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the formula according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Format | Specifies the display format of the formula's returned value. The format varies with the formula's data type and can be defined manually. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the text in the formula. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the formula. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the formula. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the formula. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the formula. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the formula. Enter a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the formula, which takes effect when the formula is inserted into a report. Enter a numeric value to change the height. The default is 0 which means a proper height will be specified to the formula by Logi JReport automatically. Data type: Float |
| Width | Specifies the width of the formula, which takes effect when the formula is inserted into a report. Enter a numeric value to change the width. The default is 0 which means a proper width will be specified to the formula by Logi JReport automatically. Data type: Float |
| Color | |
| Background | Specifies the background color of the formula. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the formula. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the formula. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the formula. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the formula. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the formula. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether or not to draw two shadowed borders, beneath and to the right of the formula. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the formula. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color with which to draw a pattern to fill the formula. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the formula. * **50%** - The formula will be filled in the specified color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the specified color. * **vertical** - The pattern will be made of vertical lines of the specified color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the specified color. * **diagonal** - The pattern will be made of slash lines of the specified color.   Data type: Enumeration |
| Others | |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500009589921-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |

## SQL Type

| Option | Type | Option | Type |
| --- | --- | --- | --- |
| -7 | BIT | -6 | TINYINT |
| -5 | BIGINT | -4 | LONGVARBINARY |
| -3 | VARBINARY | -2 | BINARY |
| -1 | LONGVARCHAR | 1 | CHAR |
| 2 | NUMERIC | 3 | DECIMAL |
| 4 | INTEGER | 5 | SMALLINT |
| 6 | FLOAT | 7 | REAL |
| 8 | DOUBLE | 12 | VARCHAR |
| 16 | BOOLEAN | 91 | DATE |
| 92 | TIME | 93 | TIMESTAMP |
| 2003 | ARRAY | 2004 | BLOB |
| 2005 | CLOB |  |  |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568742-Data-Source-Security-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590421-Hierarchical-Data-Source-Properties)
