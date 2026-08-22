---
title: "Table/View/Synonym Column Properties"
id: 5735554133527
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735554133527-Table-View-Synonym-Column-Properties
updated_at: 2022-11-02T08:09:54Z
---

# Table/View/Synonym Column Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735554128919-Table-View-Synonym-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516825495-User-Defined-Data-Source-Properties)

# Table/View/Synonym Column Properties

This topic describes the properties of a Column object in a table/view/synonym.

| Property Name | Description |
| --- | --- |
| General | |
| Array | Specifies whether the column is an array type. Data type: Boolean |
| Column Name | Specifies the name of the column in the raw database. Data type: String  Note icon Designer does not provide this property when the table column is in a MongoDB/JSON/Elasticsearch connection. |
| Column Type | Designer displays this property when the table column is in a MongoDB/JSON/Elasticsearch connection. It shows the type of the column and is read only. |
| Currency | Specifies whether to control the SQL type of the formulas and summaries which reference the column if the column is of the BigDecimal type.  * **true** Select to apply the BigDecimal type to the formulas and summaries and set their [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties#SQL) to 3. * **false** Select to apply the normal data type to the formulas and summaries.   Data type: Boolean |
| Description | Specifies the description of the object. Data type: String |
| Display Width | Specifies the display width of the object, which takes effect when you insert the object into reports. Type a numeric value to change the width. If you do not set the display width, Designer applies a default width to it automatically. Data type: Float  Note icon After you set the Display Width property of an object and use the object while creating a data component with wizard, Designer may adjust its width according to the paper size. |
| Element Name | When the table column is in a MongoDB connection, you can use this property to specify the mapped element name in a document. If the column is mapped from an element of an embedded document element, the name is a path from the embedded document element. For the PrimaryKey and ForeignKey columns, the name is blank. Designer uses "\" as an escaped char. If the element name contains "." and "\", Designer records them as "\." and "\\". When the table column is in a JSON/Elasticsearch connection, this property is read only. It shows the mapped element name in the metadata; for the Primary Key and Foreign Key columns, the name is blank.  Data type: String |
| Name | Specifies the mapped name of the object in the catalog. Data type: String |
| Nullable | Shows the nullability for the values of the column. Read only. |
| Precision | Specifies the precision for the values of the object. The default precision comes from data source metadata and defines the object's largest number of digits. The larger the precision is, the more memory it might take; however, the more accurate values you can get. Data type: Integer |
| Scale | Specifies the number of digits to the right of the decimal point for the values of the object. Data type: Integer |
| [SQL Type](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties#SQL) | Specifies the SQL type of the object defined in Java. Choose an option from the drop-down list. Data type: Integer |
| Text Format | |
| Auto Fit | Specifies whether to automatically adjust the width and height of the object according to its content. Data type: Boolean |
| Auto Scale in Number | Designer displays this property when the object is Number data type. You can use it to specify whether to automatically scale values of the object that fall into the two ranges:  * When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.   The option "auto" means that the property setting follows that of the parent data component when you use the object in a report.  Data type: Boolean |
| Bold | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Font Face | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Specifies the format in which you want to display values of the object in reports. Choose an option from the drop-down list or type the format by yourself. Data type: String  Note icon If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to italicize the text in the object. Data type: Boolean |
| Strikethrough | Specifies whether to draw a line through the text in the object. Data type: Boolean |
| Underline | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text according to the width of the object. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the object, which takes effect when you insert the object into reports. If you do not set the height, Designer assigns a proper height to the object automatically. Data type: Float |
| Width | Specifies the width of the object, which takes effect when you insert the object into reports. If you do not set the width, Designer assigns a proper width to the object automatically. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to add a drop shadow effect to the border. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** Select if you do not want to apply a pattern to the object. * **50%** Select to fill the object using 50%-transparency of the specified pattern color. * **horizontal** Select to fill the object with horizontal lines using the specified pattern color. * **vertical** Select to fill the object with vertical lines using the specified pattern color. * **grid** Select to fill the object with grids using the specified pattern color. * **diagonal** Select to fill the object with diagonal lines using the specified pattern color.   Data type: String |
| Others | |
| Data Mapping File | Specifies the data mapping file (without the locale part) you want to apply to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/5735553821719-Mapping-Data-Values-to-Different-Languages). For example, if the data mapping file is Product\_de\_DE.properties, type **Product** in the value cell. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735554128919-Table-View-Synonym-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516825495-User-Defined-Data-Source-Properties)
