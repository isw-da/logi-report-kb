---
title: "Chart Properties"
id: 4405664650263
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties
updated_at: 2022-01-27T20:36:06Z
---

# Chart Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661842327-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664651287-Chart-Label-Properties)

# Chart Properties

This topic describes the properties of a [Chart object](https://devnet.logianalytics.com/hc/en-us/articles/4405664369047-Working-with-Charts).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Page Report, Web Report, Library Component | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Alternative Text | Page Report, Web Report, Library Component | Specifies the alternate text of the image, which will be shown when the image cannot be displayed. This property applies only when the chart is exported to HTML as an image chart. Type a string to serve as the alternative text. Data type: String |
| Auto Scale in Number | Page Report, Web Report, Library Component | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   Data type: Boolean |
| Cache | Query Page Report | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Default for Filter | Page Report, Web Report | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean  Note icon In the same report, you can only set one data component's Default for Filter property to "true". |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Go to Detail | Query Page Report | Designer displays this property when the object is in the group header/footer panel of a banded object. You can use it to specify whether to show the detail information about the group when users select the object in Page Report Studio. For more information, see [Obtaining the Group Details in a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661346583-Obtaining-the-Group-Details-in-a-Banded-Object). Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set [Default for Filter](#DFilter) of the object to "true". Data type: Boolean |
| Logic Column | Page Report, Web Report, Library Component | Designer displays this property when the object is in a table. You can use it to specify whether to show the object in the next visible table cell in the same row when the column that holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When you set this property for several objects in the same row to "next visible column", and the columns holding these objects are all hidden, only the object in the rightmost column shows in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Column Number | Page Report, Web Report | Specifies the number of columns to determine the width of the object in the Excel output. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Number | Page Report, Web Report | Specifies the number of rows to determine the height of the object in the Excel output. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Platform (not available to organization chart) | | |
| Anti-aliasing | Page Report, Web Report, Library Component | Specifies whether to make the edges in the chart smooth. Data type: Boolean |
| Color When Null | Page Report, Web Report, Library Component | Specifies the color when the value is null. This property is available to heat map only and is applied when the heat map is colored only by a summary. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data Type: String |
| Color When Zero | Page Report, Web Report, Library Component | Specifies the color mapping to the zero value. Available to heat map only. It works when the heat map is colored only by a summary and the [Using Color When Zero](#UsingColorWhenZero) property is set to true. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data Type: String |
| End Color | Page Report, Web Report, Library Component | Specifies the end color of the gradient color. This property is available to heat map only and is applied when the heat map is colored only by a summary. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data type: String |
| Minimum Tick Mark Space | Page Report, Web Report, Library Component | Specifies the minimum space between two adjacent tick marks. Type a numeric value to change the space. Data type: Float |
| Pattern List | Page Report, Web Report, Library Component | Specifies the color pattern of the data markers in the same data series in the chart. Select Ellipsis button in the value cell to edit the pattern in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box). For heat maps, the Pattern List property works only when using single color and using groups as the color-by fields.  Data type: String |
| Reverse | Page Report, Web Report, Library Component | Specifies whether to reverse the start color and the end color. This property is available to heat map only and is applied when the heat map is colored only by a summary. Data type: Boolean |
| Show Legend | Page Report, Web Report, Library Component | Specifies whether to make the legend visible in a chart. Data type: Boolean |
| Start Color | Page Report, Web Report, Library Component | Specifies the start color of the gradient color. This property is available to heat map only and is applied when the heat map is colored only by a summary. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data type: String |
| Using Color When Zero | Page Report, Web Report, Library Component | Specifies whether to map the zero value to the color specified by the property [Color When Zero](#ColorWhenZero).  * If true and the minimum value < 0 < the maximum value, the gradient color will be from the [start color](#StartColor) to the color when zero first, and then from the color when zero to the [end color](#EndColor). * If false, the gradient color will be from the [start color](#StartColor) to the [end color](#EndColor) directly.   This property is available to heat map only and is applied when the heat map is colored only by a summary.  Data type: Boolean |
| Background | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color of the platform border. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| [Border End Caps](#EndCaps) | Page Report, Web Report, Library Component | Specifies the ending style of the platform border line. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](#Joint) | Page Report, Web Report, Library Component | Specifies the joint style of the platform border line. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Page Report, Web Report, Library Component | Specifies whether to show the platform border line in Outline Path. If the property is set to true, the platform border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Page Report, Web Report, Library Component | Specifies the line style of the platform border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width of the platform border. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Page Report, Web Report, Library Component | Specifies the transparency of the platform border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [Border Type](#BorderType) | Page Report, Web Report, Library Component | Specifies the border type of the platform. Choose an option from the drop-down list. Data type: Enumeration |
| Border Variable Dash | Page Report, Web Report, Library Component | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the [Format Platform dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664497047-Format-Platform-Dialog-Box#Dash) will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the [Format Platform dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664497047-Format-Platform-Dialog-Box#Dash) will take effect.   Data type: Boolean |
| Color | Page Report, Web Report, Library Component | Specifies the color of the platform background. Applied when [Fill Type](#Fill) of the platform background is set to color. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Fill Transparency | Page Report, Web Report, Library Component | Specifies the transparency of the platform background, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Page Report, Web Report, Library Component | Specifies the fill pattern for the platform background. Choose an option from the drop-down list. Can be none, color, texture, gradient or image. Data type: Enumeration |
| Gradient End Color | Page Report, Web Report, Library Component | Specifies the color of the point where the gradient ends. Applied when [Fill Type](#Fill) of the platform background is set to gradient. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Gradient End X | Page Report, Web Report, Library Component | Specifies the horizontal position where the gradient ends, measured in a percentage of the platform width. Applied when [Fill Type](#Fill) of the platform background is set to gradient. Data type: Integer |
| Gradient End Y | Page Report, Web Report, Library Component | Specifies the vertical position where the gradient ends, measured in a percentage of the platform height. Applied when [Fill Type](#Fill) of the platform background is set to gradient. Data type: Integer |
| Gradient Start Color | Page Report, Web Report, Library Component | Specifies the color of the point where the gradient begins. Applied when [Fill Type](#Fill) of the platform background is set to gradient. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Gradient Start X | Page Report, Web Report, Library Component | Specifies the horizontal position where the gradient begins, measured in a percentage of the platform width. Applied when [Fill Type](#Fill) of the platform background is set to gradient. Data type: Integer |
| Gradient Start Y | Page Report, Web Report, Library Component | Specifies the vertical position where the gradient begins, measured in a percentage of the platform height. Applied when [Fill Type](#Fill) of the platform background is set to gradient. Data type: Integer |
| Gradient Style | Page Report, Web Report, Library Component | Specifies the gradient style for the platform background, applied when [Fill Type](#Fill) of the platform background is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Image File | Page Report, Web Report, Library Component | Specifies the file name of the image, a portion of which will be displayed as the platform background. Applied when [Fill Type](#Fill) of the platform background is set to image. Type the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
| Image Height | Page Report, Web Report, Library Component | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when [Fill Type](#Fill) of the platform background is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
| Image Layout | Page Report, Web Report, Library Component | Specifies the layout style for the image that will be displayed as the platform background. Applied when [Fill Type](#Fill) of the platform background is set to image. Choose an option from the drop-down list.  * **tile** - Repeats the image over the entire area (default). * **center** - Displays the image in the center of the area. * **scaled** - Stretches the image to cover the entire area.   Data type: Enumeration |
| Image Width | Page Report, Web Report, Library Component | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when [Fill Type](#Fill) of the platform background is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
| Image X | Page Report, Web Report, Library Component | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when [Fill Type](#Fill) of the platform background is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
| Image Y | Page Report, Web Report, Library Component | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when [Fill Type](#Fill) of the platform background is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
| Inset Bottom | Page Report, Web Report, Library Component | Specifies the bottom position of the background area, measured in a percentage of the chart height, from the bottom edge of the chart. Data type: Float |
| Inset Left | Page Report, Web Report, Library Component | Specifies the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
| Inset Right | Page Report, Web Report, Library Component | Specifies the right position of the background area, measured in a percentage of the chart width, from the right edge of the chart. Data type: Float |
| Inset Top | Page Report, Web Report, Library Component | Specifies the top position of the background area, measured in a percentage of the chart height, from the top edge of the chart. Data type: Float |
| Radius | Page Report, Web Report, Library Component | Specifies the radius for the joint of the platform border line. Applied when [Border Joint](#BorderJoint) is set to joint round. Type a numeric value to change the radius. Data type: Float |
| Texture Background Color | Page Report, Web Report, Library Component | Specifies the background color of the texture. Applied when [Fill Type](#Fill) of the platform background is set to texture. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Texture Foreground Color | Page Report, Web Report, Library Component | Specifies the foreground color of the texture. Applied when [Fill Type](#Fill) of the platform background is set to texture. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Texture Style | Page Report, Web Report, Library Component | Specifies the texture style of the platform background. Applied when [Fill Type](#Fill) of the platform background is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Data (not available to organization chart) | | |
| For heat map | | |
| Color by Logarithm | Page Report, Web Report, Library Component | Specifies whether to calculate the color-by summary based on logarithm function. Available to heat map only. Choose an option from the drop-down list:  * **None** - Returns the real value of the field instead of any logarithmic value. * **log x** - Gets the logarithm of the field with base 10. * **ln x** - Gets the logarithm of the field with base e.   Data type: String |
| Size by Logarithm | Page Report, Web Report, Library Component | Specifies whether to calculate the size-by summary based on logarithm function. Available to heat map only. Choose an option from the drop-down list:  * **None** - Returns the real value of the field instead of any logarithmic value. * **log x** - Gets the logarithm of the field with base 10. * **ln x** - Gets the logarithm of the field with base e.   Data type: String |
| For other chart types | | |
| Category Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/4405661798039-Mapping-Data-Values-to-Different-Languages), which takes effect for category values shown on the category (X) axis and the hints of the data markers. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as "Category" (without the locale part).  Data type: String |
| [Category End Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Category End Offset specifies the ending offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
| Category Format | Page Report, Web Report, Library Component | Specifies the data format for the category axis (the X axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| Category Range Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/4405661798039-Mapping-Data-Values-to-Different-Languages), which takes effect for the special group values shown in the range of the category axis in a chart. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as "Category" (without the locale part).  Data type: String |
| [Category Start Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Category Start Offset specifies the starting offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
| Category Value Encoding | Page Report, Web Report, Library Component | Specifies the encoding format for values on the category axis. Choose an option from the drop-down list. Data type: String |
| Hint Percent Format | Page Report, Web Report, Library Component | Specifies the format for each hint percentage to the total. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| Hint Value Format | Page Report, Web Report, Library Component | Specifies the number format for the hint message. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| [Hyperlink](#HyperlinkDes) | Query Page Report, Web Report, Library Component | Specifies the hyperlink which refers to another report or a website to add to the data markers of the chart. Type the URL of the report or website in the value cell. Data type: String |
| [Hyperlink Target](#HyperlinkTarget) | Query Page Report, Web Report, Library Component | Specifies the target window or frame to display the content the Hyperlink property specifies. Choose an option from the drop-down list. Data type: String |
| Motion Bar Format | Page Report, Web Report, Library Component | Specifies the data format for the motion field values displayed on the motion bar. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| Overall Series | Page Report, Web Report, Library Component | Specifies whether to calculate the top or bottom N category values based on the series values. Data type: Boolean |
| Primary Data Format | Page Report, Web Report, Library Component | Specifies the data format for the primary value axis (the Y1 axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| Reverse Category | Page Report, Web Report, Library Component | Specifies whether to reverse the sequence of the category field value. Data type: Boolean |
| Reverse Series | Page Report, Web Report, Library Component | Specifies whether to reverse the sequence of the series field value. Data type: Boolean |
| Secondary Data Format | Page Report, Web Report, Library Component | Specifies the data format for the secondary value axis (the Y2 axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| Series Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/4405661798039-Mapping-Data-Values-to-Different-Languages), which takes effect for series values shown on the legend and the hints of the data markers. Not available to bubble chart. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as "Category" (without the locale part).  Data type: String |
| [Series End Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Series End Offset specifies the ending offset of the series.  Data type: Integer |
| Series Format | Page Report, Web Report, Library Component | Specifies the data format for the series axis (the Z axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box). Data type: String |
| [Series Start Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Series Start Offset specifies the starting offset of the series.  Data type: Integer |
| Series Value Encoding | Page Report, Web Report, Library Component | Specifies the encoding format for values on the series axis. Choose an option from the drop-down list. Data type: String |
| Sort Category | Page Report, Web Report, Library Component | Specifies the sorting order for the category field values. Choose an option from the drop-down list. Data type: Enumeration |
| Sort Series | Page Report, Web Report, Library Component | Specifies the sorting order for the series field values. Choose an option from the drop-down list. Data type: Enumeration |
| Swap Groups | Page Report, Web Report, Library Component | Specifies to display values from different data fields by switching data between the category and series axes, the category and value axes of a chart. By default, this property is set to false, which means no switch will take place in the chart. When it is set to true:  * If the chart has fields on all of its axes, data on the category and series axes will be switched. * If the chart has one field on the category axis and several on the value axis, data on the category and value axes will be switched.   Data type: Boolean  Note icon If the chart has only one field on the category axis and one on the value axis, even though you set the property to "true", there will be no switch take place on the two axes. |
| [X Hyperlink](#HyperlinkDes) | Query Page Report, Web Report, Library Component | Specifies the hyperlink which refers to another report or a website to add to the data labels on the X axis. Type the URL of the report or website in the value cell. Data type: String |
| [X Hyperlink Target](#HyperlinkTarget) | Query Page Report, Web Report, Library Component | Specifies the target window or frame to display the content the X Hyperlink property specifies. Choose an option from the drop-down list.  Data type: String |
| [Z Hyperlink](#HyperlinkDes) | Query Page Report, Web Report, Library Component | Specifies the hyperlink which refers to another report or a website to add to the data labels on the Z axis. Type the URL of the report or website in the value cell. Data type: String |
| [Z Hyperlink Target](#HyperlinkTarget) | Query Page Report, Web Report, Library Component | Specifies the target window or frame to display the content the Z Hyperlink property specifies. Choose an option from the drop-down list. Data type: String |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | A representation of the standard HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Title | Query Page Report | A representation of the standard HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| LongDesc | Query Page Report | A representation of the standard HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

## End Caps

The property can be set to one of the following:

* **butt** - Ends unclosed subpaths and dash segments with no added decoration.
* **round** - Ends unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square** - Ends unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

## Border Joint

The property can be set to one of the following:

* **miter** - Joins path segments by extending their outside edges until they meet.
* **round** - Joins path segments by rounding off the corner at a radius of half the line width.
* **bevel** - Joins path segments by connecting the outer corners of their wide outlines with a straight segment.
* **joint round** - Joins path segments by rounding off the corner at the specified radius. The value is supported for lines in the chart platform only.

## Border Type

The property can be set to one of the following:

* **none** - The platform has no visible border lines.
* **raised** - The platform has 3-D borders that appear as if they are raised off the page.
* **recess** - The platform has 3-D borders that appear as if they are pressed into the page.
* **shadow** - The platform has two shadowed borders, beneath and to the right of the platform.
* **solid** - The platform has single-line borders.

## Hyperlink, X Hyperlink, Z Hyperlink

You can use these properties to add a hyperlink, which refers to another report or a website, to the chart data markers, and to the data labels on the X and Z axes. For chart in a page report, you can also control the hyperlink with a formula, which is a good way to get the required data from another report.

For example, you have two reports, ReportA and ReportB, in the SampleReports.cat catalog. In ReportA, you group the data in a banded object by customer country and use a bar chart to illustrate the count of Customer\_ID in every group. ReportB shows the information of customer, such as ID, Name, and Annual Sales. Then you want to build a link between the two reports to get this result at runtime: run ReportA and select the bar of a country, then ReportB displays showing the data of the specific country only. To achieve it, take these steps:

1. In Designer, open ReportA.cls.
2. Create a formula, Link\_b. It might be:

   `string t="http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=ReportB.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8&jrs.authorization=YWRtaW46YWRtaW4%3D&";  
   string t1="jrs.param$PCOUNTRY=";  
   string url=t+t1+"@INNER"+"&jrs.result_type=1";  
   return url`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)Here are some tips for creating the formula to control the hyperlink properties:

   * You need to make sure that the paths of the catalog and the report in the URL correspond with their paths on Server. For more information about how to create the URL, see Running Reports via URL in the *Logi Report Server Guide*.
   * You can use the built-in parameter INNER to represent the category data, and OUTER for the series data.
   * If you want to use the formula to control the X HyperLink and Z HyperLink properties, you can use *@XDIM* and *@ZDIM* respectively instead of *@INNER* and *@OUTER*.
3. In the Report Inspector, set **Hyperlink** of the chart object to **Link\_b**.
4. Select the target window or frame to display the linked report from the value drop-down list of the **Hyperlink Target** property.
   1. **<Server Setting>**  
      Select to load the linked content according to setting on Server: for page report, it is specified by the Pop Up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab; for web report and library component, by the Target of Detail Table Report and Links option in the Profile > Configure Profile > Web Report Studio > Properties tab.
   2. **New Window**  
      Select to load the linked content into a new window. The window is not named.
   3. **Whole Window**  
      Select to load the linked content into the full browser window.
   4. **Same Frame**  
      Select to load the linked content into the same frame as the link.
   5. **Parent Frame**  
      Select to load the linked content into the parent frame of the frame that contains the link.
   6. **Other Frame**  
      Select to load the linked content into some other specified frame. Type the name of the frame you have defined in the value cell. If the frame name does not exist, Server loads the linked content into a new window.
5. Publish the two reports with the catalog to Server.
6. Run ReportA in Page Report Studio.
7. Point to a bar and select it. ReportB displays showing data of the specified country.
8. View the information of the other countries by selecting the corresponding bars in ReportA.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* After setting the Hyperlink, X Hyperlink, or Z Hyperlink property for a chart, if you also add another link to the data markers, the category axis, or series axis of the chart using the [Link](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports) feature, the link has higher priority over the hyperlink on the same chart element.
* Users can select the chart elements to open the specified hyperlinks at runtime only when you give the link action the highest [Click Priority](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Priority) (the link action has the highest priority by default).

## Start Offset(1st.Data.Set), End Offset(1st.Data.Set), Start Offset(2nd.Data.Set), and End Offset(2nd.Data.Set)

These four properties are used to control the data source range that appears in the chart.

For 2-level-group charts, record-level charts and all kinds of combination charts, Start Offset(1st.Data.Set) and End Offset(1st.Data.Set) are used to control the starting offset and ending offset of the data series; Start Offset(2ndDataSet) and End Offset(2nd Data.Set) are used to control the range of the categories.

For 1-level-group charts, Start Offset(2nd.Data.Set) and End Offset(2nd.Data.Set) are used to control the starting offset and ending offset of the categories; Start Offset(1st.Data.Set) and End Offset(1st.Data.Set) will not work because there is no series data in chart that contains only one group.

The range of the property values can be -1 (Default, Not Set) or an integer between 0 and Number of Data Series – 1 (or, Number of Categories - 1).

If the value is out of this range, the following rules will be applied to the default value:

| IF | THEN |
| --- | --- |
| Start Offset(1st.Data.Set) < 0 | Start Offset(1st.Data.Set) = 0 |
| Start Offset(1st.Data.Set) > max data number | Start Offset(1st.Data.Set) = max data number |
| End Offset(1st.Data.Set) < 0 | End Offset(1st.Data.Set) = max data number |
| End Offset(1st.Data.Set) > max data number | End Offset(1st.Data.Set) = max data number |
| Start Offset(1st.Data.Set) > End Offset(1st.Data.Set) and EndOffset(1st.Data.Set) >=0 | Start Offset(1st.Data.Set) = 0, End Offset(1st.Data.Set) = max data number |

Same rules apply to Start Offset(2nd.Data.Set) and End Offset(2nd.Data.Set).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* If values are set to be less than 0, it means the categories or series will be displayed without any offset.
* If values are set to be greater than 0 and the value of Category/Series Start Offset is greater than that of Category/Series End Offset, all of the categories or series will be displayed.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661842327-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664651287-Chart-Label-Properties)
