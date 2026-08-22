---
title: "Summary Properties"
id: 1500010069401
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069401-Summary-Properties
updated_at: 2021-07-24T10:38:03Z
---

# Summary Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069301-Stored-Procedure-Column-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069421-Table-View-Synonym-Properties)

# Summary Properties

This topic lists the properties of a Summary object in a catalog.

| Property Name | Description |
| --- | --- |
| General | |
| Description | Specifies the description of the summary. Data type: String |
| Display Width | Specifies the display width of the summary. Enter a numeric value to change the width. Data type: Float  **Notes:**   * If the Display Width value of a summary is not set in the Catalog Manager, the summary will be inserted in a report with the default width defined by Logi JReport. * Assume that you have set the Display Width of a summary, and used the summary while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Expression | Displays the statement of the summary. This property is read only. |
| Function | Specifies the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) of the summary. Data type: String |
| Group By | Specifies the criteria (break-by group) that the summary will be performed. Data type: String |
| Length | Specifies the length of the summary's value, in bytes. Data type: Integer |
| Name | Specifies the name of the summary. Data type: String |
| Number Base | Specifies the number base of the summary. Data type: Integer |
| Precision | Specifies the precision of the summary's value. The default value comes from data source metadata and it specifies the value's largest number of digits. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the summary's value. Data type: Integer |
| Special Function | If the group-by field is of Numeric, String, Date or Time type, you can further define to calculate the summary by specifying a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Function). Data type: String |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/1500010069121-Formula-Properties#SQL) | Specifies the SQL type of the summary defined in Java. Choose an option from the drop-down list. Data type: Integer |
| Summary On | Specifies the field on which the summary performs. Data type: String |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the summary according to the contents. Data type: Boolean |
| Auto Scale in Number | The property is available when the summary is of the Number data type. It specifies whether to automatically scale the summary values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale values.   The option "auto" means that the property setting follows that of the parent data container when the summary is added in a report.  Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties#Format) | Specifies the display format of the summary's value. The format varies with the summary's data type and can be defined manually. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the text in the summary. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the summary. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the summary. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the summary. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the summary. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the summary. Enter a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the summary, which takes effect when the summary is inserted into a report. Enter a numeric value to change the height. The default is 0 which means a proper height will be specified to the summary by Logi JReport automatically. Data type: Float |
| Width | Specifies the width of the summary, which takes effect when the summary is inserted into a report. Enter a numeric value to change the width. The default is 0 which means a proper width will be specified to the summary by Logi JReport automatically. Data type: Float |
| Color | |
| Background | Specifies the background color of the summary. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the summary. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the summary. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the summary. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the summary. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the summary. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether or not to draw two shadowed borders, beneath and to the right of the summary. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the summary. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color with which to draw a pattern to fill the summary. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties#PatternStyle) | Specifies the style of the pattern. Choose an option from the drop-down list.     Data type: Enumeration |
| Others | |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010033362-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069301-Stored-Procedure-Column-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069421-Table-View-Synonym-Properties)
