---
title: "Chart Paper Properties"
id: 5741484398615
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741484398615-Chart-Paper-Properties
updated_at: 2022-10-31T17:18:30Z
---

# Chart Paper Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464054423-Heat-Map-Rectangle-Properties)

# Chart Paper Properties

This topic describes the properties of the Chart Paper object.

| Property Name | Description |
| --- | --- |
| General | |
| Display Name | Specify the display name of the object. Data type: String |
| Instance Name | Server displays the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specify the height of the object, in inches. Type a numeric value to change the height. This property takes effect only when you set the [Placement](https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties#Placement) property for the chart legend to **customized**. Data type: Float |
| Width | Specify the width of the object, in inches. Type a numeric value to change the width. This property takes effect only when you set the [Placement](https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties#Placement) property for the chart legend to **customized**. Data type: Float |
| X | Specify the horizontal coordinate of the upper-left corner of the object, relative to its parent container. Type a numeric value to change the position in inches. This property takes effect only when you set the [Placement](https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties#Placement) property for the chart legend to **customized**. Data type: Float |
| Y | Specify the vertical coordinate of the upper-left corner of the object, relative to its parent container. Type a numeric value to change the position in inches. This property only takes effect when you set the [Placement](https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties#Placement) property for the chart legend to **customized**. Data type: Float |
| Coordinate Paper | |
| Graph Position | Select the position of the paper contents relative to the paper background. Data type: Enumeration |
| Reverse Painting Order | Select **true** if you want to reverse the order of graphic objects in a combo chart. Data type: Boolean |
| Scale X | Specify the percentage for elongating or shortening the X axis. Type a numeric value to change the percentage. Data type: Float |
| Scale Y | Specify the percentage for elongating or shortening the Y axis. Type a numeric value to change the percentage. Data type: Float |
| Others (available to org charts only) | |
| Layout Mode | Select how the org chart tree expands from the root node.  * **Top Down** The org chart tree expands from top to bottom. * **Bottom Up** The org chart tree expands from bottom to top. It is the reverse of the Top Down mode. * **Left Right** The org chart tree expands from left to right.   Data type: Enumeration |
| Graph for bar/bench/line/area chart | |
| Depth | Specify the depth of the bars/benches/lines/areas when you set [Use Depth](#BarUseDepth) to true. This property applies to 2D charts only. Type a numeric value to change the depth. Data type: Float |
| Direction | Specify the angle of the axis along the depth of the bars/benches/lines/areas. This property applies to 2D charts only. Type a numeric value to change the direction. Data type: Integer |
| Use Depth | Select **true** to make the bars/benches/lines/areas visually three-dimensional. This property applies to 2D charts only. Data type: Boolean  Note iconIf the chart is a combo chart composed by bars, areas, and lines, when you set the depth properties for one of the three types, they will apply to all the three types. |
| Background | |
| Border Color | Specify the color of the paper border. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style of the paper border line. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style of the paper border line. Data type: Enumeration |
| Border Style | Select the line style of the paper border. Data type: Enumeration |
| Border Thickness | Specify the width of the paper border, in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the paper border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderType) | Select the border type of the paper. Data type: Enumeration |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size.  Data type: Boolean |
| Color | Specify the color of the paper background. This property applies when [Fill Type](#BackgroundFillType) of the paper background is set to **Color**. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specify the transparency of the paper background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Select the fill pattern for the paper background.  * **None** No fill. * **Color** Select to fill with a specified color. * **More Effects** Specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741444679959-Fill-Effects-Dialog-Box-Properties)   Data type: Enumeration |
| Inset Bottom | Specify the bottom position of the background area, measured in a percentage of the paper height, from the bottom edge of the paper. Data type: Float |
| Inset Left | Specify the left position of the background area, measured in a percentage of the paper width, from the left edge of the paper. Data type: Float |
| Inset Right | Specify the right position of the background area, measured in a percentage of the paper width, from the right edge of the paper. Data type: Float |
| Inset Top | Specify the top position of the background area, measured in a percentage of the paper height, from the top edge of the paper. Data type: Float |
| Hint (unavailable to org chart) | |
| Category Name | Specify the name of the category field to display in the data marker hint. By default, Server uses the display name of the category field in the hint to label the category value. You can customize the name to help others better understand the value. This property only applies when the [Customize Category and Series Names](#CustomizeCategory) property value is **true**. Data type: String |
| Chart Value Names | Select the ellipsis button Select Values in the value cell to open the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457709079-Customize-Chart-Value-Names-Dialog-Box-Properties), and then specify the names of the chart value fields to display in the data marker hint. By default, Server uses the display names of the fields in the hint to label the chart values. This property only applies when the **Customize Chart Value Names** property value is **true**. Data type: String |
| Customize Category and Series Names | Select **true** to customize the names of the category and series fields in the data marker hint. Data type: Boolean |
| Customize Chart Value Names | Select **true** to customize the names of the chart value fields in the data marker hint. Data type: Boolean |
| Series Name | Specify the name of the series field to display in the data marker hint. By default, Server uses the display name of the series field in the hint to label the series value. You can customize the name to help others better understand the value. This property only applies when the [Customize Category and Series Names](#CustomizeCategory) property value is **true**. Data type: String |
| Show Tips | Select **true** to show the hint when you hover over a data marker in the chart, which displays the values the data marker represents. The hint is also available in the HTML output. If this property is false, Server ignores all the other hint properties. Data type: Boolean |
| Category (X) Axis (unavailable to pie, indicator, gauge, heat map, org, and KPI charts) | |
| Auto Major Unit | Select **true** to automatically define the interval unit between two adjacent major tick marks, or **false** to use the user defined [major interval unit](#Major). Data type: Boolean |
| Auto Maximum | Select **true** to automatically define the maximum value to label the tick marks, or **false** to use the user defined [maximum value](#Maximum). Data type: Boolean |
| Auto Minor Unit | Select **true** to automatically define the interval unit between two adjacent minor tick marks, or **false** to use the user defined [minor interval unit](#Minor). Data type: Boolean |
| Auto Minimum | Select **true** to automatically define the minimum value to label the tick marks, or **false** to use the user defined [minimum value](#Minimum). Data type: Boolean |
| Axis Color | Specify the color for the axis. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Axis End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the axis. Data type: Enumeration |
| [Axis Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the axis. Data type: Enumeration |
| Axis Style | Select the style for the axis. Data type: Enumeration |
| Axis Thickness | Specify the thickness for the axis. Type a numeric value to change the thickness. Data type: Float |
| Axis Transparency | Specify the transparency for the axis, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Axis Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Gridline Color | Specify the color for the gridlines. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Gridline End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the gridlines. Data type: Enumeration |
| [Gridline Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the gridlines. Data type: Enumeration |
| Gridline Style | Select the style for the gridlines. Data type: Integer |
| Gridline Thickness | Specify the thickness for the gridlines. Type a numeric value to change the thickness. Data type: Float |
| Gridline Transparency | Specify the transparency for the gridlines, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Gridline Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Increment | Specify the increased amount between two adjacent values on the axis. The default is to let Logi Report Designer determine the increased amount. This property applies to bubble charts which use the axis to show numeric data only. Data type: Integer |
| Label Axis Gap | Specify the distance between the labels and the axis. Type a numeric value to change the gap. Data type: Float |
| Label Color | Specify the color for the label text. This property applies when [Label Fill Type](#XLabelFillType) is set to **Color**. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Label Every N Tick Marks | Specify the frequency to label the tick marks. Type 1 to label every tick mark, type 2 to label every two tick marks, type 3 to label every three tick marks, and so on. Data type: Integer |
| Label Fill Transparency | Specify the transparency for the label text, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Label Fill Type | Select the fill pattern for the label text.  * **None** No fill. * **Color** Select to fill with a specified color.   Data type: Enumeration |
| Label Font Face | Select the font face for the label text. Data type: Enumeration |
| Label Font Orientation Automatically | Specify whether to adjust the rotation angle of the label text on the axis automatically.  * **true** Select to automatically adjust the rotation angle of the label text according to the length of the text, in degrees. If the text can completely display horizontally, the default rotation angle will be 0. If it cannot, the default rotation angle will be 30 anticlockwise. Server displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name. * **false** Select if you want to use the value of the **Label Font Rotation** property to determine the rotation angle of the label text.   Data type: Boolean |
| Label Font Rotation | Specify the rotation angle of the label text around its center, in degrees. Type a numeric value to change the rotation. Data type: Float |
| Label Font Size | Specify the font size for the label text. Type an integer value to change the size. Data type: Integer |
| Label Font Style | Select the font style for the label text. Data type: Enumeration |
| Label Position | Select whether to show the label text outside or inside the axis. This property takes effect only when the **Use Depth** property is **false**. Data type: Enumeration |
| Major Interval | Specify the interval between two adjacent major tick marks. Type a numeric value to change the interval. Data type: Float |
| Major Interval Unit | Select the interval unit between two adjacent major tick marks. Data type: Enumeration |
| Minor Interval | Specify the interval between two adjacent minor tick marks. Type a numeric value to change the interval. Data type: Float |
| Minor Interval Unit | Select the interval unit between two adjacent minor tick marks. Data type: Enumeration |
| Major Label Auto Scale in Number | Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.   The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).  Data type: Boolean |
| Major Tick Mark Length | Specify the length of the major tick marks. Type a numeric value to change the length. Data type: Float |
| Major Tick Mark Line Color | Specify the color of the major tick marks. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Major Tick Mark Line End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the major tick marks. Data type: Enumeration |
| [Major Tick Mark Line Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the major tick marks. Data type: Enumeration |
| Major Tick Mark Line Style | Select the line type for the major tick marks. Data type: Enumeration |
| Major Tick Mark Line Thickness | Specify the thickness of the major tick marks. Type a numeric value to change the thickness. Data type: Float |
| Major Tick Mark Line Transparency | Specify the color transparency of the major tick marks, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Major Tick Mark Line Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size.  This property applies when the **Major Tick Mark Line Style** property is not **Solid Line**.  Data type: Boolean |
| Major Tick Mark Type | Select the position of the major tick marks relative to the axis. Data type: Enumeration |
| Maximum | Specify the maximum value to label the tick marks. Data type: Float |
| Maximum Length | Server enables this property when you set [Truncate](#Truncate) to "true". You can use it to specify the maximum number of characters the major tick mark labels on the axis can display. When a label contains more characters than the specified number and is truncated, Server displays an ellipsis (…) for the cut-off part, and the ellipsis takes three characters out of the maximum length. However, when you set the property value to less than 4, Server displays the specified number of characters in the label with no ellipsis. |
| Maximum Value | Specify the maximum value of the data appearing on the X axis. This property applies to bubble charts which use the axis to show numeric data only. Data type: Float |
| Minimum | Specify the minimum value to label the tick marks. Data type: Float |
| Minimum Value | Specify the minimum value of the data appearing on the X axis. This property applies to bubble charts which use the axis to show numeric data only. Data type: Float |
| Minor Tick Mark Length | Specify the length of the minor tick marks. Type a numeric value to change the length. Data type: Float |
| Minor Tick Mark Type | Select the position of the minor tick marks relative to the axis. Data type: Enumeration |
| Number of Labels | Specify the number of tick mark labels you want to show. The default is to let Logi Report Designer determine the number of labels. Data type: Integer |
| Number of Tick Marks | Specify the number of tick marks you want to show. The default is to let Logi Report Designer determine the number. This property applies to bubble charts only. Data type: Integer |
| Number of Visible Values | Specify the number of data items you want to select on the scroll bar and display on the axis by default. This property is available to 2D scroll bar charts of bar, bench, line, area, and stock types. Data type: Integer |
| Percentage of Scrolling Area Height | Specify the height percentage the scroll bar occupies the whole size of the chart. This property is available to 2D scroll bar charts of bar, bench, line, area, and stock types. Data type: Float |
| Position Axis | Select the position where you want to display the data point and label on the X axis.  * **On Tick Marks** Select to align the data point and label with each tick mark on the X axis. * **Between Tick Marks** Select to display the data point and label between each two tick marks on the X axis.   Data type: Enumeration |
| Scrollable Chart | Specify whether to make the chart scrollable. If true, Server adds a scroll bar in the chart, with which you can control the visible value range on the axis. This property is available to 2D charts of bar, bench, line, and area types. Data type: Boolean |
| Show Axis | Select **true** to show the axis. Data type: Boolean |
| Show Axis Label Tips | Select **true** to show the complete label text when you hover over a label on the axis in the HTML or Web Report output. Data type: Boolean |
| Show Chart in Scrolling Area | Select **true** to show the thumbnail chart on the scroll bar. This property only applies when you set **Scrollable Chart** to **true** for 2D charts of bar, bench, line, and area types. Data type: Boolean |
| Show Gridline | Select **true** to show the gridlines perpendicular to the axis. Data type: Boolean |
| Show Tick Mark Labels | Select **true** to show the tick mark labels. Data type: Boolean |
| Truncate | Select **true** to truncate the major tick mark labels when the label text contains more characters than the number you specify to the [Maximum Length](#MaximumLength) property. Data type: Boolean |
| Use Best Effect | Select **true** to hide the label which overlaps the one in front of it. Data type: Boolean |
| Use Constant Interval | Select **true** to use a constant interval to label the tick marks. If true, Server increases the values of the tick marks continually on the axis based on the following properties, instead of just using the data values. Data type: Boolean |
| Value (Y) Axis (unavailable to pie, indicator, heat map, org, and KPI charts) | |
| Auto Scale in Number | Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.   The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).  Data type: Boolean |
| Auto Scale on Y Axis | Select **true** to recalculate the scale of Value (Y) Axis when the **Number of Visible Values** property value changes.  This property only applies when you set the **Scrollable Chart** property value to **true** for 2D charts of bar, bench, line, and area types.  Data type: Integer |
| Axis Color | Specify the color for the axis. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Axis End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the axis. Data type: Enumeration |
| [Axis Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the axis. Data type: Enumeration |
| Axis Style | Select the style for the axis. Data type: Enumeration |
| Axis Thickness | Specify the thickness for the axis. Type a numeric value to change the thickness. Data type: Float |
| Axis Transparency | Specify the transparency for the axis, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Axis Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Gridline Color | Specify the color for the gridlines. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Gridline End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the gridlines. Data type: Enumeration |
| [Gridline Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the gridlines. Data type: Enumeration |
| Gridline Style | Select the style for the gridlines. Data type: Enumeration |
| Gridline Thickness | Specify the thickness for the gridlines. Type a numeric value to change the thickness. Data type: Float |
| Gridline Transparency | Specify the transparency for the gridlines, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Gridline Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Increment | Specify the increased amount between two adjacent values on the axis. The default is to let Logi Report Designer determine the increased amount. Data type: Integer |
| Label Axis Gap | Specify the distance between the labels and the axis. Type a numeric value to change the gap. Data type: Float |
| Label Color | Specify the color for the label text. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. This property applies when you set the [Label Fill Type](#YLabelFillType) property value to **Color**.  Data type: String |
| Label Every N Tick Marks | Specify the frequency to label the tick marks. Type 1 to label every tick mark, type 2 to label every two tick marks, type 3 to label every three tick marks, and so on. Data type: Integer |
| Label Fill Transparency | Specify the transparency for the label text, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Label Fill Type | Select the fill pattern for the label text.  * **None** No fill. * **Color** Select to fill with a specified color.   Data type: Enumeration |
| Label Font Orientation Automatically | Specify whether to adjust the rotation angle of the label text on the axis automatically.  * **true** Select to automatically adjust the rotation angle of the label text according to the length of the text, in degrees. If the text can completely display horizontally, the default rotation angle will be 0. If it cannot, the default rotation angle will be 30 anticlockwise. Server displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name. * **false** Select to use the **Label Font Rotation** property value to determine the rotation angle of the label text.   Data type: Boolean |
| Label Font Face | Select the font face for the label text. Data type: Enumeration |
| Label Font Rotation | Specify the rotation angle of the label text around its center, in degrees. Type a numeric value to change the rotation. Data type: Float |
| Label Font Size | Specify the font size for the label text. Type an integer value to change the size. Data type: Integer |
| Label Font Style | Select the font style for the label text. Data type: Enumeration |
| Label Position | Select whether to show the label text outside or inside the axis. This property only takes effect when you set the **Use Depth** property value to **false**. Data type: Enumeration |
| Major Tick Mark Length | Specify the length of the major tick marks. Type a numeric value to change the length. Data type: Float |
| Major Tick Mark Line Color | Specify the color of the major tick marks. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Major Tick Mark Line End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style for the major tick marks. Data type: Enumeration |
| [Major Tick Mark Line Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style for the major tick marks. Data type: Enumeration |
| Major Tick Mark Line Style | Select the line type for the major tick marks. Data type: Enumeration |
| Major Tick Mark Line Thickness | Specify the thickness of the major tick marks. Type a numeric value to change the thickness. Data type: Float |
| Major Tick Mark Line Transparency | Specify the color transparency of the major tick marks, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Major Tick Mark Line Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size.  This property applies when the **Major Tick Mark Line Style** property is not **Solid Line**.  Data type: Boolean |
| Major Tick Mark Type | Select the position of the major tick marks relative to the axis. Data type: Enumeration |
| Maximum Value | Specify the maximum value of the data appearing on the Y axis. Data type: Float |
| Minimum Value | Specify the minimum value of the data appearing on the Y axis. Data type: Float |
| Minor Tick Mark Length | Specify the length of the minor tick marks. Type a numeric value to change the length. Data type: Float |
| Minor Tick Mark Type | Select the position of the minor tick marks relative to the axis. Data type: Enumeration |
| Number of Labels | Specify the number of tick mark labels you want to show. The default is to let Logi Report Designer determine the number of labels. Data type: Integer |
| Number of Tick Marks | Specify the number of tick marks you want to show. The default is to let Logi Report Designer determine the number. Data type: Integer |
| Show Axis | Select **true** to show the axis. Data type: Boolean |
| Show Axis Label Tips | Select **true** to show the complete label text when you hover over a label on the axis in the HTML or Web Report output. Data type: Boolean |
| Show Gridline | Select **true** to show the gridlines perpendicular to the axis. Data type: Boolean |
| Show Tick Mark Labels | Select **true** to show the tick mark labels. Data type: Boolean |
| Start Value | Specify the position where the axis label starts to show, applied when you set the [Use Start Value](#UseStartValue) property value to **true**. Data type: Float |
| Use Best Effect | Select **true** to hide the label which overlaps the one in front of it. Data type: Boolean |
| Use Start Value | Select **true** to set the start value of the axis. Data type: Boolean |
| Wall (unavailable to gauge, heat map and org chart) | |
| Border Color | Specify the color of the border of the wall. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#EndCaps) | Select the ending style of the wall border line. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/5741440046231-Chart-Properties#BorderJoint) | Select the joint style of the wall border line. Data type: Enumeration |
| Border Style | Select the line style of the wall borders. Data type: Enumeration |
| Border Thickness | Specify the width of the border, in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the wall borders, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Bound Color | Specify the color of the bound wall, applied when you set the [Bound Fill Type](#BoundFillType) property value to **Color**. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Bound Fill Transparency | Specify the transparency of the color schema to compound with the basic fill which you set in the wall area, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Bound Fill Type | Select the fill type of the bound wall.  * **None** No fill. The default value. * **Color** Select to fill with a specified color. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741444679959-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Color | Specify the color of the wall, applied when you set the [Fill Type](#FillType2) property value to **Color**. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specify the transparency of the background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Select the fill pattern for the wall.  * **None** No fill. * **Color** Select to fill with a specified color. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741444679959-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Show Wall | Select **true** to show the wall. Data type: Boolean |
| Threshold Line (unavailable to gauge, bubble, heat map and org charts) | |
| Fill Threshold1 | Select **true** to fill the first threshold area with a semi-transparent color. Data type: Boolean |
| Fill Threshold2 | Select **true** to fill the second threshold area with a semi-transparent color. Data type: Boolean |
| Fill Transparency | Specify the transparency of the background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Show Threshold Line1 | Select **true** to show the first threshold line. Data type: Boolean |
| Show Threshold Line2 | Select **true** to show the second threshold line. Data type: Boolean |
| Threshold Line Color1 | Specify the color for the first threshold line. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Threshold Line Color2 | Specify the color for the second threshold line. Choose a color or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Threshold Line Style | Select the style for the threshold lines.  * **Style1** Select to use two threshold areas (Threshold Line1 and Threshold Line2) to emphasize the data series that are higher than the first threshold line or lower than the second threshold line. * **Style2** Select to use a single threshold area (Threshold Line1) to emphasize the data series that are between the higher and the lower threshold lines.   A threshold line marks a specific data point that you specified. You usually use it for comparing with data series to see whether the data is higher or lower than this point. For example, if you want to see whether the production zones successfully accomplished their production tasks, you can set a threshold line to represent the goal output, and another to represent the lowest acceptable output quantity. Using the threshold lines, you can spot out of range zones at a glance.  Stock charts, radar charts, scatter charts, and bubble charts have no threshold lines.  Data type: Enumeration |
| Threshold Value1 | Specify the value for the first threshold line. Data type: Float |
| Threshold Value2 | Specify the value for the second threshold line. Data type: Float |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* For a combo chart, the graph properties respectively apply to the corresponding chart types.
* A combo chart may contain two value axes, namely, the Y1 and Y2 axes. The properties of the Y1 or Y2 axis are the same as those of the Y axis.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741476249751-Chart-Legend-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464054423-Heat-Map-Rectangle-Properties)
