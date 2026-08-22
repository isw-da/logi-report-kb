---
title: "Chart Properties"
id: 4411830860823
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties
updated_at: 2022-01-27T07:58:16Z
---

# Chart Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411822432023-Chart-Label-Properties)

# Chart Properties

This topic describes the properties specific to a Chart object, including a KPI Chart object. For the other properties, see [Setting Web Report Object Properties Using the Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel).

Select the following links to view the topics:

* [Chart Label Properties](https://devnet.logianalytics.com/hc/en-us/articles/4411822432023-Chart-Label-Properties)
* [Chart Legend Properties](https://devnet.logianalytics.com/hc/en-us/articles/4411830862103-Chart-Legend-Properties)
* [Chart Paper Properties](https://devnet.logianalytics.com/hc/en-us/articles/4411830863127-Chart-Paper-Properties)
* [Heat Map Rectangle Properties](https://devnet.logianalytics.com/hc/en-us/articles/4411822431127-Heat-Map-Rectangle-Properties)

| Property Name | Description |
| --- | --- |
| Platform | |
| Minimum Tick Mark Space | Specify the minimum space between two adjacent tick marks. Type a numeric value to change the space. Data type: Float |
| Show Legend | Specify whether to make the legend visible in a chart. Unavailable to KPI charts. Data type: Boolean |
| Background | |
| Border Color | Specify the color of the platform border. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Border End Caps](#EndCaps) | Select the ending style of the platform border line. Data type: Enumeration |
| [Border Joint](#BorderJoint) | Select the joint style of the platform border line. Data type: Enumeration |
| Border Style | Select the line style of the platform border. Data type: Enumeration |
| Border Thickness | Specify the width of the platform border, in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the platform border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [Border Type](#BorderType) | Select the border type of the platform. Data type: Enumeration |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size.  Data type: Boolean |
| Color | Specify the color of the platform background. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Note icon This property applies when you set [Fill Type](#FillType) of the platform background to Color.  Data type: String |
| Fill Transparency | Specify the transparency of the platform background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specify the fill pattern for the platform background.  * **None** No fill. The default value. * **Color** Select to fill with a specified color. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Inset Bottom | Specify the bottom position of the background area, measured in a percentage of the chart height, from the bottom edge of the chart. Data type: Float |
| Inset Left | Specify the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
| Inset Right | Specify the right position of the background area, measured in a percentage of the chart width, from the right edge of the chart. Data type: Float |
| Inset Top | Specify the top position of the background area, measured in a percentage of the chart height, from the top edge of the chart. Data type: Float |
| Radius | Specify the radius for the joint of the platform border line. Type a numeric value to change the radius. Note icon The property takes effect only when you set [Border Joint](#BorderJoint) to joint round.  Data type: Float |
| Data | |
| [Category End Offset](#SettingDataRange) | The four properties work together to control the range of the data to display on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Use Category End Offset to specify the ending offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
| Category Format | Specify the data format for the category axis (the X axis) to display the tick mark labels in the way you choose. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| [Category Start Offset](#SettingDataRange) | The four properties work together to control the range of the data to display on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Use Category Start Offset to specify the starting offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
| Hint Percent Format | Specify the format for each hint percentage to the total. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| Hint Value Format | Specify the number format for the hint message. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| Hyperlink | Specify to add a hyperlink that refers to another report or a website to the data markers of the chart. Type the URL of the report or website in the value cell. For more information, see [Running Reports via URL](https://devnet.logianalytics.com/hc/en-us/articles/4405690694295-Running-Reports-via-URL). Data type: String |
| Hyperlink Target | Specify the target window or frame in which you want to display the contents the Hyperlink property specifies.  * **<Server Setting>**  Select to load the linked file according to the setting of [Pop Up New Window for Links](https://devnet.logianalytics.com/hc/en-us/articles/4405683964951-Customizing-Page-Report-Studio-Profile#Link). * **New Window** Select to load the linked file into a new window. The window is not named. * **Whole Window** Select to load the linked file into the full browser window. * **Same Frame** Select to load the linked file into the same frame as the link. * **Parent Frame** Select to load the linked file into the parent frame of the frame that contains the link. * **Other Frame** Select to load the linked file into some other specified frame. Then, you can also directly type the name of the frame you have defined in the text box. If the frame name does not exist, Server will load the linked file into a new window.   Data type: String |
| Motion Bar Format | Specify the data format for the motion field values displayed on the motion bar. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| Overall Series | Specify whether to calculate the top or bottom N category values based on the series values. Data type: Boolean |
| Primary Data Format | Specify the data format for the primary value axis (the Y1 axis) to display the tick mark labels in the way you choose. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| Reverse Category | Specify whether to reverse the sequence of the category field value. Data type: Boolean |
| Reverse Series | Specify whether to reverse the sequence of the series field value. Data type: Boolean |
| Secondary Data Format | Specify the data format for the secondary value axis (the Y2 axis) to display the tick mark labels in the way you choose. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| [Series End Offset](#SettingDataRange) | The four properties work together to control the range of the data to display on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Use Series End Offset to specify the ending offset of the series.  Data type: Integer |
| Series Format | Specify the data format for the series axis (the Z axis) to display the tick mark labels in the way you choose. Select the ellipsis button Select Values in the value cell to specify the format in the [Data Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683807895-Data-Format-Dialog-Box-Properties). Data type: String |
| [Series Start Offset](#SettingDataRange) | The four properties work together to control the range of the data being displayed on a chart: Category Start Offset, Category End Offset, Series Start Offset, and Series End Offset. Use Series Start Offset to specify the starting offset of the series.  Data type: Integer |
| Sort Category | Select the sorting order for the category field values. Data type: Enumeration |
| Sort Series | Select the sorting order for the series field values. Data type: Enumeration |
| Swap Groups | Specify to display values from different data fields by switching data between the category and series axes, or the category and value axes of a chart. By default, this property is false, which means no switch will take place in the chart. When it is true:  * If the chart has fields on all of its axes, Server will switch the data on the category and series axes. * If the chart has one field on the category axis and several on the value axis, Server will switch the data on the category and value axes.   Note icon If the chart has only one field on the category axis and one on the value axis, even though the property value is true, there will be no switch taking place on the two axes. |
| X HyperLink | Specify to add a hyperlink that refers to another report or a website to the X axis labels. Type the URL of the report or website in the value cell. For more information, see [Running Reports via URL](https://devnet.logianalytics.com/hc/en-us/articles/4405690694295-Running-Reports-via-URL). Data type: String |
| X Hyperlink Target | Specify the target window or frame in which you want to display the contents the X Hyperlink property specifies.  * **<Server Setting>** Select to load the linked file according to the setting of [Pop Up New Window for Links](https://devnet.logianalytics.com/hc/en-us/articles/4405683964951-Customizing-Page-Report-Studio-Profile#Link). * **New Window** Select to load the linked file into a new window. The window is not named. * **Whole Window** Select to load the linked file into the full browser window. * **Same Frame** Select to load the linked file into the same frame as the link. * **Parent Frame** Select to load the linked file into the parent frame of the frame that contains the link. * **Other Frame** Select to load the linked file into some other specified frame. Then, you can also directly type the name of the frame you have defined in the text box. If the frame name does not exist, Server will load the linked file into a new window.   Data type: String |

## Border Type

Specify the border type of an object. Can be one of the following:

* **None**  
   The object has no visible border lines.
* **Raised**  
   The object has 3D borders as if they are raised off the page.
* **Recess**  
   The object has 3D borders as if they are pressed into the page.
* **Shadow**  
   The object has two shadowed borders, beneath and to the right of the object.
* **Solid**  
   The object has single-line borders.

## Border End Caps

Specify the ending style of the border line. Can be one of the following:

* **Butt**  
   End unclosed subpaths and dash segments with no added decoration.
* **Round**  
   End unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **Square**  
   End unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

## Border Joint

Specify the joint style. Can be one of the following:

* **Miter**  
   Join path segments by extending their outside edges until they meet.
* **Round**  
   Join path segments by rounding off the corner at a radius of half the line width.
* **Bevel**  
   Join path segments by connecting the outer corners of their wide outlines with a straight segment.
* **Joint Round**  
   Join path segments by rounding off the corner at the specified radius. Available only for chart platform.

## Start Offset(1st.Data.Set), End Offset(1st.Data.Set), Start Offset(2nd.Data.Set), and End Offset(2nd.Data.Set)

Use these four properties to control the data source range in the chart.

For 2-level-group charts, record-level charts, and all kinds of combination charts, use Start Offset(1st.Data.Set) and End Offset(1st.Data.Set) to control the starting offset and ending offset of the data series; use Start Offset(2ndDataSet) and End Offset(2nd Data.Set) to control the range of the categories.

For 1-level-group charts, use Start Offset(2nd.Data.Set) and End Offset(2nd.Data.Set) to control the starting offset and ending offset of the categories; Start Offset(1st.Data.Set) and End Offset(1st.Data.Set) will not work because there is no series data in the chart that contains only one group.

The range of the property values can be -1 (Default, Not Set) or an integer between 0 and Number of Data Series – 1 (or, Number of Categories - 1).

If the value is out of this range, the following rules will apply to the default value:

| IF | THEN |
| --- | --- |
| Start Offset(1st.Data.Set) < 0 | Start Offset(1st.Data.Set) = 0 |
| Start Offset(1st.Data.Set) > max data number | Start Offset(1st.Data.Set) = max data number |
| End Offset(1st.Data.Set) < 0 | End Offset(1st.Data.Set) = max data number |
| End Offset(1st.Data.Set) > max data number | End Offset(1st.Data.Set) = max data number |
| Start Offset(1st.Data.Set) > End Offset(1st.Data.Set) and EndOffset(1st.Data.Set) >=0 | Start Offset(1st.Data.Set) = 0, End Offset(1st.Data.Set) = max data number |

Same rules apply to Start Offset(2nd.Data.Set) and End Offset(2nd.Data.Set).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411822432023-Chart-Label-Properties)
