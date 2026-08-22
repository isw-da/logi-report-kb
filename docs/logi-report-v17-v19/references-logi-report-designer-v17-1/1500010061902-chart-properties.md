---
title: "Chart Properties"
id: 1500010061902
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties
updated_at: 2021-07-23T19:16:30Z
---

# Chart Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061882-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061922-Chart-Label-Properties)

# Chart Properties

This topic lists the properties of a Chart object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

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
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Alternative Text | Page Report, Web Report, Library Component | Specifies the alternate text of the image, which will be shown when the image cannot be displayed. This property applies only when the chart is exported to HTML as an image chart. Type a string to serve as the alternative text. Data type: String |
| Auto Scale in Number | Page Report, Web Report, Library Component | Specifies whether to automatically scale the values that are of the Number data type in the object when the values fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   Data type: Boolean |
| Cache | Query Page Report | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Default for Filter | Page Report, Web Report | Specifies whether to show the data component as the default component in the Apply To drop-down list of the Filter dialog box in Page/Web Report Studio. Data type: Boolean  Note icon In the same report, you can set only one data component's Default for Filter property to true. |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Go to Detail | Query Page Report | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. For more information, see [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010056722-Obtaining-Detailed-Information-from-a-Banded-Object). Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to show the data component in the Apply To drop-down list of the Filter dialog box in Page/Web Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| Logic Column | Page Report, Web Report, Library Component | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. This property is supported when the object is in a table. Choose an option from the drop-down list. Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Column Number | Page Report, Web Report | Specifies the number of columns which will be the object's width in the Excel or CSV output. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: String |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Row Number | Page Report, Web Report | Specifies the number of rows which will be the object's height in the Excel or CSV output. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Platform (not available to organization chart) | | |
| Anti-aliasing | Page Report, Web Report, Library Component | Specifies whether to make the edges in the chart smooth. Data type: Boolean |
| Color When Null | Page Report, Web Report, Library Component | Specifies the color when the value is null. This property is available to heat map only and is applied when the heat map is colored only by a summary. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data Type: String |
| Color When Zero | Page Report, Web Report, Library Component | Specifies the color mapping to the zero value. Available to heat map only. It works when the heat map is colored only by a summary and the [Using Color When Zero](#UsingColorWhenZero) property is set to true. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data Type: String |
| End Color | Page Report, Web Report, Library Component | Specifies the end color of the gradient color. This property is available to heat map only and is applied when the heat map is colored only by a summary. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data type: String |
| Minimum Tick Mark Space | Page Report, Web Report, Library Component | Specifies the minimum space between two adjacent tick marks. Type a numeric value to change the space. Data type: Float |
| Pattern List | Page Report, Web Report, Library Component | Specifies the color pattern of the data markers in the same data series in the chart. Select the ellipsis button Ellipsis button in the value cell to edit the pattern in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box). For heat maps, the Pattern List property works only when using single color and using groups as the color-by fields.  Data type: String |
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
| Border Variable Dash | Page Report, Web Report, Library Component | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the [Format Platform dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059282-Format-Platform-Dialog-Box#Dash) will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the [Format Platform dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059282-Format-Platform-Dialog-Box#Dash) will take effect.   Data type: Boolean |
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
| Category Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support), which takes effect for category values shown on the category (X) axis and the hints of the data markers. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| [Category End Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Category End Offset specifies the ending offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
| Category Format | Page Report, Web Report, Library Component | Specifies the data format for the category axis (the X axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| Category Range Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support), which takes effect for the special group values shown in the range of the category axis in a chart. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| [Category Start Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Category Start Offset specifies the starting offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
| Category Value Encoding | Page Report, Web Report, Library Component | Specifies the encoding format for values on the category axis. Choose an option from the drop-down list. Data type: String |
| Hint Percent Format | Page Report, Web Report, Library Component | Specifies the format for each hint percentage to the total. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| Hint Value Format | Page Report, Web Report, Library Component | Specifies the number format for the hint message. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| [Hyperlink](#HyperlinkDes) | Query Page Report, Web Report, Library Component | Specifies to add a hyperlink that refers to another report or a website to the data markers of the chart. Type the URL of the report or website in the value cell. Data type: String |
| [Hyperlink Target](#HyperlinkTarget) | Query Page Report, Web Report, Library Component | Specifies the target window or frame in which to display the content the [Hyperlink](#Hyperlink) property specifies. Choose an option from the drop-down list. Data type: String |
| Motion Bar Format | Page Report, Web Report, Library Component | Specifies the data format for the motion field values displayed on the motion bar. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| Overall Series | Page Report, Web Report, Library Component | Specifies whether to calculate the top or bottom N category values based on the series values. Data type: Boolean |
| Primary Data Format | Page Report, Web Report, Library Component | Specifies the data format for the primary value axis (the Y1 axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| Reverse Category | Page Report, Web Report, Library Component | Specifies whether to reverse the sequence of the category field value. Data type: Boolean |
| Reverse Series | Page Report, Web Report, Library Component | Specifies whether to reverse the sequence of the series field value. Data type: Boolean |
| Secondary Data Format | Page Report, Web Report, Library Component | Specifies the data format for the secondary value axis (the Y2 axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| Series Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support), which takes effect for series values shown on the legend and the hints of the data markers. Not available to bubble chart. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| [Series End Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Series End Offset specifies the ending offset of the series.  Data type: Integer |
| Series Format | Page Report, Web Report, Library Component | Specifies the data format for the series axis (the Z axis) to display the tick mark labels in the way you choose. Select Ellipsis button in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box). Data type: String |
| [Series Start Offset](#Offset) | Page Report, Web Report, Library Component | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Series Start Offset specifies the starting offset of the series.  Data type: Integer |
| Series Value Encoding | Page Report, Web Report, Library Component | Specifies the encoding format for values on the series axis. Choose an option from the drop-down list. Data type: String |
| Sort Category | Page Report, Web Report, Library Component | Specifies the sorting order for the category field values. Choose an option from the drop-down list. Data type: Enumeration |
| Sort Series | Page Report, Web Report, Library Component | Specifies the sorting order for the series field values. Choose an option from the drop-down list. Data type: Enumeration |
| Swap Groups | Page Report, Web Report, Library Component | Specifies to display values from different data fields by switching data between the category and series axes, the category and value axes of a chart. By default, this property is set to false, which means no switch will take place in the chart. When it is set to true:  * If the chart has fields on all of its axes, data on the category and series axes will be switched. * If the chart has one field on the category axis and several on the value axis, data on the category and value axes will be switched.   Data type: Boolean  Note icon If the chart has only one field on the category axis and one on the value axis, even though you set the property to "true", there will be no switch take place on the two axes. |
| [X HyperLink](#HyperlinkDes) | Query Page Report, Web Report, Library Component | Specifies to add a hyperlink that refers to another report or a website to the X axis labels. Type the URL of the report or website in the value cell. Data type: String |
| [X Hyperlink Target](#HyperlinkTarget) | Query Page Report, Web Report, Library Component | Specifies the target window or frame in which to display the content the [X Hyperlink](#XHyperlink) property specifies. Choose an option from the drop-down list.  Data type: String |
| [Z HyperLink](#HyperlinkDes) | Query Page Report, Web Report, Library Component | Specifies to add a hyperlink that refers to another report or a website to the Z axis labels. Type the URL of the report or website in the value cell. Data type: String |
| [Z Hyperlink Target](#HyperlinkTarget) | Query Page Report, Web Report, Library Component | Specifies the target window or frame in which to display the content the [Z Hyperlink](#ZHyperlink) property specifies. Choose an option from the drop-down list. Data type: String |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
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

## Hyperlink

This property is used to add a hyperlink, which refers to another report or a website, to the chart data markers. For chart in a page report, you can also control the hyperlink property with a formula, which will be a good way to get required data from another report.

For example, you have two reports ReportA and ReportB in the SampleReports.cat catalog. In ReportA, the data in a banded object is grouped by customer country and a bar chart is used to illustrate the count of Customer\_ID in every group. ReportB shows the information of customer, such as ID, Name, and Annual Sales. Then we build a link between the two reports. After publishing the reports to Server, run ReportA and select the bar of a country, ReportB will then appear, only showing the data of the specific country. The steps are:

1. In Designer, open ReportA.cls.
2. Create a new formula named "Link\_b". It might be:

   `string t="http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=ReportB.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8&jrs.authorization=YWRtaW46YWRtaW4%3D&";  
   string t1="jrs.param$PCOUNTRY=";  
   string url=t+t1+"@INNER"+"&jrs.result_type=1";  
   return url`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

   * Make sure that the paths of the catalog and the report in the URL are corresponding with their paths on Server.
   * The built-in parameter INNER is used for representing the category data. In addition, you can use OUTER for the series data.
   * For the X HyperLink and Z HyperLink properties, you can use @XDIM and @ZDIM respectively instead of @INNER and @OUTER.
3. In the Report Inspector, set the Hyperlink property of the chart platform to **Link\_b**.
4. Publish the two reports with the catalog to Server.
5. Run ReportA, point to a bar and select it, the corresponding records in ReportB will be displayed. You can also view the information of the other countries by selecting the corresponding bars in ReportA.

## Hyperlink Target

Specifies the target window or frame in which to display the linked content. Can be one of the following:

* **<Server Setting>**  
  Loads the linked content according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile page in Server.
* **New Window**  
  Loads the linked content into a new window. The window is not named.
* **Whole Window**  
  Loads the linked content into the full browser window.
* **Same Frame**  
  Loads the linked content into the same frame as the link.
* **Parent Frame**  
  Loads the linked content into the parent frame of the frame that contains the link.
* **Other Frame**  
  Loads the linked content into some other specified frame. If selected, you can also type the name of the frame you have defined in the text box. If the frame name does not exist, the linked content will be loaded into a new window.

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* If values are set to be less than 0, it means the categories or series will be displayed without any offset.
* If values are set to be greater than 0 and the value of Category/Series Start Offset is greater than that of Category/Series End Offset, all of the categories or series will be displayed.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061882-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061922-Chart-Label-Properties)
