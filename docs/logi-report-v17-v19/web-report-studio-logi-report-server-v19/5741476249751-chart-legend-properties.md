---
title: "Chart Legend Properties"
id: 5741476249751
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties
updated_at: 2022-10-31T17:18:52Z
---

# Chart Legend Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741484328727-Chart-Label-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741484398615-Chart-Paper-Properties)

# Chart Legend Properties

This topic describes the properties of the Chart Legend object.

| Property | Description |
| --- | --- |
| General | |
| Display Name | Specify the display name of the object. Data type: String |
| Instance Name | Server displays the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specify the height of the object, in inches. Type a numeric value to change the height. Data type: Float |
| Width | Specify the width of the object, in inches. Type a numeric value to change the width. Data type: Float |
| X | Specify the horizontal coordinate of the upper-left corner of the object, relative to its parent container. Type a numeric value to change the position in inches. Note icon This property takes effect only when you set the [Placement](#Placement) property to customized.  Data type: Float |
| Y | Specify the vertical coordinate of the upper-left corner of the object, relative to its parent container. Type a numeric value to change the position in inches. Note icon This property takes effect only when you set the [Placement](#Placement) property to customized.  Data type: Float |
| Legend | |
| Auto Size | Specify whether to resize the legend automatically. Data type: Boolean |
| Bottom Margin | Specify the distance between the legend labels and the bottom border of the legend, in inches. Type a numeric value to change the margin. Data type: Float |
| Label Format Source | Specify the data format option for the chart legend labels.  * **Axis Data Format** Select if you want the data format of the legend labels to follow that of the axis data: if the chart has series axis, the legend label format will be the same as the series axis data format; if not, the legend labels will use the category axis data format. * **Legend Data Format** Select if you want to control the data format of the legend labels by the [Legend Data Format](#LegendDataFormat) property.   Note icon This property is not available to heat maps that are colored only by summaries.  Data type: Enumeration |
| Label Horizontal Spacing | Specify the horizontal distance between two adjacent legend labels. Type a numeric value to change the distance. Note icon This property is not available to heat maps that are colored only by summaries.  Data type: Float |
| Label Vertical Spacing | Specify the vertical distance between two adjacent legend labels. Type a numeric value to change the distance. Note icon This property is not available to heat maps that are colored only by summaries.  Data type: Float |
| Left Margin | Specify the distance between the legend labels and the left border of the legend, in inches. Type a numeric value to change the margin. Data type: Float |
| Legend Data Format | Specify the data format of the legend labels. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457762839-Data-Format-Dialog-Box-Properties). Note icon This property applies when you set [Label Format Source](#LabelFormatSource) to Legend Data Format.  Data type: String |
| Placement | Specify the position of the legend to be on the left, right, top, bottom of the chart or customized by manually dragging in the chart. Choose an option from the drop-down list. Data type: Enumeration |
| Right Margin | Specify the distance between the legend labels and the right border of the legend, in inches. Type a numeric value to change the margin. Data type: Float |
| Secondary Placement | Specify the position of the legend further based on the setting of the [Placement](#Placement) property. Choose an option from the drop-down list. Data type: Enumeration |
| Show Scrollbar | Specify whether to display a scroll bar on the legend to fully view the legend contents when the contents do not fit into the legend. Data type: Boolean |
| Show Tips | Specify whether to show the corresponding data information when you hover over a legend entry in the chart. The tip is also available in the HTML output. Data type: Boolean |
| Top Margin | Specify the distance between the legend labels and the top border of the legend, in inches. Type a numeric value to change the margin. Data type: Float |
| Truncate | Specify whether to truncate the legend entry label text when the text overflow the labels. Data type: Boolean |
| Background | |
| Border Color | Specify the color of the legend border. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style of the legend border line. Data type: Enumeration |
| Border Style | Select the line style of the legend border. Data type: Enumeration |
| Border Thickness | Specify the width of the legend border, in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the legend border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderType) | Select the border type of the legend. Data type: Enumeration |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Color | Specify the color of the legend background. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Note icon This property applies when you set [Fill Type](#BackgroundFillType) of the legend background to Color.  Data type: String |
| Fill Transparency | Specify the transparency of the legend background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specify the fill pattern for the legend background.  * **None** No fill. The default value. * **Color** Select to fill with a specified color. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741444679959-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Inset Bottom | Specify the bottom position of the background area, measured in a percentage of the legend height, from the bottom edge of the legend. Data type: Float |
| Inset Left | Specify the left position of the background area, measured in a percentage of the legend width, from the left edge of the legend. Data type: Float |
| Inset Right | Specify the right position of the background area, measured in a percentage of the legend width, from the right edge of the legend. Data type: Float |
| Inset Top | Specify the top position of the background area, measured in a percentage of the legend height, from the top edge of the legend. Data type: Float |
| Label | |
| Auto Scale in Number | Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.   The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).  Data type: Boolean |
| Color | Specify the color of the label text. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Note icon This property applies when you set [Fill Type](#LabelFillType) of the label text to Color.  Data type: String |
| Fill Transparency | Specify the color transparency of the label text, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specify the fill pattern for the label text.  * **None** No fill. The default value. * **Color** Select to fill with a specified color.   Data type: Enumeration |
| Font Face | Select the font face for the label text. Data type: Enumeration |
| Font Rotation | Specify the rotation angle of each legend label around its center, in degrees. The default value is 0. Type a numeric value to change the rotation. Data type: Float |
| Font Size | Specify the font size for the label text. Type an integer value to change the size. Data type: Integer |
| Font Style | Select the font style for the label text. Data type: Enumeration |
| Outline Color | Specify the color for the label text outline. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Outline End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the label text outline. Data type: Enumeration |
| [Outline Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the label text outline. Data type: Enumeration |
| Percent Format | Specify the format of the percentage values on the legend. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457762839-Data-Format-Dialog-Box-Properties). Note icon This property applies when you set [Show Percent](#ShowPercent) to true.  Data type: String |
| Reverse Labels | Specify whether to reverse the order of the labels in the legend object. Data type: Boolean |
| Show All Labels | Specify whether to display zero values besides other values in the legend. Data type: Boolean |
| Show Percent | Specify whether to show the percentage of each entry value to the total on the legend. This property applies to pie, bar, and bench charts that have only one value axis. Data type: Boolean |
| Show Values | Specify whether to show the values for the legend entries. This property applies to pie, bar, and bench charts that have only one value axis. Data type: Boolean |
| Text of Total Value | Specify the text of the total value label on the legend. This property applies to pie, bar, and bench charts that have only one value axis. Data type: String |
| Value Format | Specify the number format of the legend entry values. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format](https://devnet.logianalytics.com/hc/en-us/articles/5741457762839-Data-Format-Dialog-Box-Properties) dialog box. Note icon This property applies when you set [Show Values](#ShowValue) to true.  Data type: String |
| Icon | |
| Border Color | Specify the color of the icon border. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style of the icon border line. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style of the icon border line. Data type: Enumeration |
| Border Style | Select the line style of the icon border. Data type: Enumeration |
| Border Thickness | Specify the width of the icon border in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the icon border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Height | Specify the height of the icon, in inches. Type a numeric value to change the width. Data type: Float |
| Icon Alignment | Select the relative position of the icon to the legend. Data type: Enumeration |
| Icon Text Gap | Specify the distance between each legend label and icon. Type a numeric value to change the gap. Data type: Float |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741484328727-Chart-Label-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741484398615-Chart-Paper-Properties)
