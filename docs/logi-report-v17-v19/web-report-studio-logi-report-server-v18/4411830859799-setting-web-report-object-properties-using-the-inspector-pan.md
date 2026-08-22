---
title: "Setting Web Report Object Properties Using the Inspector Panel"
id: 4411830859799
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel
updated_at: 2022-01-27T07:58:15Z
---

# Setting Web Report Object Properties Using the Inspector Panel

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690691607-Customizing-the-Web-Report-Studio-UI)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties)

# Setting Web Report Object Properties Using the Inspector Panel

You can update the properties of the web report objects in Web Report Studio using the Inspector panel. This topic describes how you can use all the properties.

For the properties specific to charts, see [Chart Properties](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties).

Keep in mind the following while browsing the properties:

* Some properties or property values are available to some objects.
* Some properties only show related information, and you cannot edit them.
* Some properties are in different categories for different objects.
* You can control some properties by a formula or expression. If you select a formula to control a property, Logi Report automatically generates an expression with the prefix @. Also, you must let Logi Report Engine know some properties before a page break, so that it can lay out the object. In a formula or expression, the special field **PageNumber** is the switch for setting the page break calculation time. If you use PageNumber in the formula or expression, then the calculation time will be after the page break, if you do not use PageNumber, the calculation time will be before the page break. For this reason, Logi Report will set the calculation time for controlling whether to mark the formula or expression as before page break or after page break. For most properties, you can control the property by formula or expression at any time without concern about the page break.

| Property Name | Description |
| --- | --- |
| General Properties | |
| Data Inherit | Server shows whether this object inherits the dataset from another object. This property is read only. |
| Display Name | Specify the display name of the object. Data type: String |
| Instance Name | Server shows the instance name of the object. This property is read only. |
| Reference | Server shows the instance name of the field if the label is related to a field. This property is read only. |
| Geometry Properties | |
| Autofit | Specify whether to automatically adjust the width of a vertical banded object or the height of a horizontal banded object according to the contents. Data type: Boolean |
| Height | Specify the height of the object, in inches. Type a numeric value to change the height. Data type: Float |
| Width | Specify the width of the object, in inches. Type a numeric value to change the width. Data type: Float |
| X | Specify the horizontal coordinate of the upper-left corner of the object, relative to its parent container. Type a numeric value to change the position in inches. Note icon This property is not available when the object is in a crosstab or the [Position](#Position) property value is static.  Data type: Float |
| Y | Specify the vertical coordinate of the upper-left corner of the object, relative to its parent container. Type a numeric value to change the position in inches. Note icon This property is not available when the object is in a crosstab or the [Position](#Position) property value is static.  Data type: Float |
| Bottom Attach Pos X | Specify the horizontal coordinate of the bottom (or right when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If you exchange the top and bottom end points, this property works on the bottom end point after the exchange. Data type: Float |
| Bottom Attach Pos Y | Specify the vertical coordinate of the bottom (or right when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If you exchange the top and bottom end points, this property works on the bottom end point after the exchange. Data type: Float |
| Top Attach Pos X | Specify the horizontal coordinate of the top (or left when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If you exchange the top and bottom end points, this property works on the top end point after the exchange. Data type: Float |
| Top Attach Pos Y | Specify the vertical coordinate of the top (or left when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If you exchange the top and bottom end points, this property works on the top end point after the exchange. Data type: Float |
| Color Properties | |
| Background | Specify the background color of the object. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| Fill Type | Specify the fill pattern for the object.  * **Color** Select to fill with a specified color. Then, specify the Background property. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Foreground | Specify the foreground color of the object. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| Text Format Properties | |
| Autofit | Select **true** if you want to expand the width and height of the object according to the contents. Note icon   * For performance concern, you should not set both Autofit and [Word Wrap](#WordWrap) to true when the object is in a crosstab. * For a table column, the Autofit property is in the Others category.   Data type: Boolean |
| Reduce Width When Autofit | Select **true** if you want to reduce the width of the object according to its content when you specify to automatically adjust its width (the object's Autofit being true) and the actual width of the content is smaller than that of the object. Note icon This property takes effect when you set Position of the object to absolute; but, it does not work if the Word Wrap property of the object is true.  Data type: Boolean |
| Auto Map Field Name | This property is available when the label is related to a field. Select **true** if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field. Server will ignore the [Text](#Text) property. Data type: Boolean |
| Auto Scale in Number | Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.   The value **auto** means that the setting follows that of the parent data container.  Data type: Boolean |
| Bold | Select **true** to make the text bold. Data type: Boolean |
| Font Face | Select the font of the text. Data type: Enumeration |
| Font Size | Specify the font size of the text. Type or select an integer value to change the size. Data type: Integer |
| Format | Specify the format in which you want to display the text. It varies with data type, and you can manually define it. Data type: String  Note icon   * For the BigDecimal data type, to avoid precision loss, you should type a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property value is true, the Format property applies to the integer part of the values after being scaled, but if the specified format conflicts with the Auto Scale in Number property, for example, the values display in percentage, then Server ignores the Auto Scale in Number property. |
| Format Locale | Specify the locale for displaying and formatting values of the object when its data type is locale sensitive, such as the date and time formats, and number and currency formats. Default is the locale of your JVM or the language of the NLS report. Choose an option from the drop-down list if you want to change the locale. Note icon When you use a formula or edit an expression to control the locale, the return value should be the two-letter language and country codes as defined by ISO-639 and ISO-3166 in the format *language\_country*, for example, de\_DE.  Data type: String |
| Horizontal Alignment | Select the horizontal justification of the text in the object. Data type: Enumeration |
| Ignore HTML Tag | Specify whether to ignore the HTML tag elements in the text at runtime and in the HTML output.  * Select **true** if you don't want Logi Report Engine to parse the HTML tag elements so they display exactly as what they are. * Select **false** if you want Logi Report Engine to transfer the HTML tag elements to the web browser so the web browser translates them into HTML.   Note icon The [Convert HTML Tag](#ConvertHTMLTag) property has higher priority than **Ignore HTML Tag**.  Data type: Boolean |
| Italic | Select **true** to make the text italic. Data type: Boolean |
| Strikethrough | Select **true** to add a strikethrough line to the text. Data type: Boolean |
| Text | Type the text of the label. Data type: String |
| Underline | Select **true** to underline the text. Data type: Boolean |
| Vertical Alignment | Select the vertical justification of the text in the object. Data type: Enumeration |
| Word Wrap | Select **true** to wrap the text to the object width. Note icon For performance concern, you should not set both [Autofit](#AutoFit) and Word Wrap to true when the object is in a crosstab.  Data type: Boolean |
| Border Properties | |
| Border Color | Specify the color of the border of the object. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| Border Thickness | Specify the width of the border in inches. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Select the line style of the bottom border of the object. Data type: Enumeration |
| Left Line | Select the line style of the left border of the object. Data type: Enumeration |
| Right Line | Select the line style of the right border of the object. Data type: Enumeration |
| Top Line | Select the line style of the top border of the object. Data type: Enumeration |
| Padding Properties | |
| Bottom Padding | Specify the space between the text and the bottom border of the object, in inches. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specify the space between the text and the left border of the object, in inches. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specify the space between the text and the right border of the object, in inches. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specify the space between the text and the top border of the object, in inches. Type a numeric value to change the padding. Data type: Float |
| Others Properties | |
| Cache | Specify whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Cache Section | Select **true** to cache the objects in the detail panel. Data type: Boolean  Note iconThe property does not work if there is crosstab, text object, or chart in the panel, because these objects contain child-DBFields. |
| CellPaddingBottom | Specify the space between the text and the bottom border of the filter control. Type a numeric value to change the padding. Data type: Float |
| CellPaddingTop | Specify the space between the text and the top border of the filter control. Type a numeric value to change the padding. Data type: Float |
| Cross Page | Select **true** if you want to split the panel across a page break when the panel exceeds the page height. Default is false. Server will display the panel in the next page, when the panel spans vertically beyond the page.  Note icon This property applies only when you enable the page layout of the report, and if you run or export the report in the formats that support page layout, such as PDF and RTF.  Data type: Boolean |
| Current Block Index | The two properties, Current Block Index and Items per Block, work together to control the data of the object to display in the continuous page mode. Use **Current Block Index** to specify the index of the data block you want to display. 0 means the first block index, 1 the second, and so on.  Data type: Integer |
| Display Null | Specify the text you want to display if the field value is null. Data type: String |
| Enable Navigation | Specify whether to enable page navigation for a table, or enable scrollbars for a crosstab or banded object, when the parent container cannot fully display its data. By default the property value is true. You can further specify the height and width of the frame for holding the object, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). If later you resize the object, Server will reset the two properties to use the resized values. If the table contains more than one page, a page navigation bar specific to the table will be available under it. You can use the bar to view the desired pages.  Data type: Boolean |
| Expand Detail Data | Specify whether to expand the groups to show the details when you open the report in Web Report Studio. This property only works in the continuous page mode. Data type: Boolean |
| Export as Text | Enable this property if you want to export the parameter control as text. Otherwise, Logi Report will export the parameter control as an image. When you enable this property, depending on the properties of the parameter in the parameter control, Logi Report will export the parameter control as follows:   * Logi Report will export the selected values or text of the parameter as text while it will not export the icon or button for specifying the parameter value. * If the parameter in the parameter control is of Boolean type, Logi Report displays it as a checkbox in the parameter control. Then when you select the checkbox, Logi Report will export it as Checkmark, or as Checkbox if you clear the checkbox.   Data Type: Boolean |
| Export to CSV | Specify whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specify whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specify whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specify whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specify whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specify whether to include the object when you open the report in Web Report Studio or in the Web Report Result. Data type: Boolean |
| Export to RTF | Specify whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specify whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specify whether to include the object when exporting the report to XML. Data type: Boolean |
| Field Type | Select another special field you want to substitute the current special field. Data type: Enumeration |
| Fill Whole Page | Select **true** to extend the row/panel to the bottom of the page, so that the next row/panel starts on a new page. Data type: Boolean |
| Horizontal Alignment | Select the horizontal justification of the contents in the object, or of the image in the container. Data type: Enumeration |
| Invisible | Select **true** to hide the object. Server will still perform all formulas and calculations. You can also [use a formula](https://devnet.logianalytics.com/hc/en-us/articles/4405690687511-Making-Simple-Modifications-to-Web-Report-Components#Formula) to control this property.  Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Items per Block | The two properties, Current Block Index and Items per Block, work together to control the data of the object to display in the continuous page mode. Use **Item per Block** to specify the number of records in each data block.  Data type: Integer |
| Label | Specify the text you want Server to pop up when you hover over the left edge of the panel. Data type: String |
| [Merge to Next Panel](#Panel) | Select **true** to merge the panel into the next panel in the Excel output. Data type: Boolean |
| Minimum Leaf Distance | Specify the minimum distance between two adjacent leaf nodes on the same level. For top-down and bottom-up layouts, it means horizontal distance. For left-right layout, it means vertical distance. Type a numeric value to specify the distance. Data type: Float |
| Minimum Level Distance | Specify the minimum distance between two adjacent levels. For top-down and bottom-up layouts, it means vertical distance. For left-right layout, it means horizontal distance. When running the report in the Web Report format, if the value of Minimum Level Distance is less than that of [Line Thickness](#LineThickness) on org chart line, the latter will replace the former. Data type: Float |
| Navigation Height | Specify the height of the frame for holding the object. Type a numeric value to specify the height. If you don't provide a value here, Logi Report will calculate the frame height. Note icon This property takes effect when [Enable Navigation](#EnableNavigation) is true.  Data type: Float |
| Navigation Width | Specify the width of the frame for holding the object. Type a numeric value to specify the width. If you don't provide a value here, Logi Report will calculate the frame width. Note icon This property takes effect when [Enable Navigation](#EnableNavigation) is true.  Data type: Float |
| On New Page | Select **true** to display the row/panel on a new page. Default is false, and the row/panel starts on a new page only if the previous page is filled. Note icon This property applies only when you enable the page layout of the report, and if you run or export the report in the formats that support page layout, such as PDF and RTF.  Data type: Boolean |
| Page Background | Specify the background color of the report page. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405690687511-Making-Simple-Modifications-to-Web-Report-Components#Position) | Specify the position of the object.  * **static** Select if you want to position the object at the location where you inserted it. Server will hide or disable the X, Y, and other position-related properties. The preceding objects in the same container will affect the position of the object. * **absolute** Select if you want to place the object at the position you specified by dragging or by setting its X and Y property values.   Data type: Enumeration  Note iconThis property only affects objects in a container, which is the report body, a table cell, or a tabular cell. |
| Record Location | Specify the calculation point for the properties of the object which you control by formulas.  * **Default** Select if you want to calculate the values of the properties in the default location where they are. * **Page Header** Select if you want to calculate the values of the properties in the page header. * **Page Footer** Select if you want to calculate the values of the properties in the page footer.   Data type: Enumeration |
| [Remove Blank Row](#Panel) | Select **true** to remove blank rows in the panel in the Excel output. Data type: Boolean |
| Remove Extra Quotes from First Line | Select **true** to remove the quotation marks and commas from the first line of the report's Text and CSV outputs. Data type: Boolean |
| Repeat | Specify whether to display the group header on every page. For one detail panel which spans a large space vertically to display in several pages, Logi Report supports the Repeat property if you want to see the group header information in each page. When the Repeat property is true and group header is visible, Server duplicates the group header on every page.  Note icon   * When a page split occurs in the bottom blank part of the detail panel (or margins in the detail panel) and the Cross Page property in the detail panel is true, the output is: repeated group header + a slice of blank detail panel + group footer. It appears as though only group footers without any detail panel follow the repeated group header. In order to solve this problem, you can resize the detail panel. * If you set the Repeat property to true in both outer group header and inner group header, Logi Report treats the two group headers as a completely repeated object. * If you set the outer and inner group headers to be one completely repeated object, then when the page can only hold the group headers or has no enough space for the group headers, Server does not duplicate both outer and inner group headers.   Data type: Boolean |
| [Repeat in Detail Panel](#Panel) | Select **true** to make the objects in the panel repeated in the detail panel in the Excel output. Data type: Boolean |
| Repeat on Pages | Specify whether to display the table header on every page of the report. Data type: Boolean |
| Shrink Footer | Specify whether to hide the group footer panel when collapsing a group. This property only works in the continuous page mode. Data type: Boolean |
| Split Overflow Columns | Select **true** to display a big table with many columns on multiple pages if one page cannot hold all the columns, instead of cutting the overflow columns off - the default behavior. When the property is true, the table object containing overflow columns on subsequent pages inherits the same Y value in its container, so that it keeps the same number of records as the table in the original page. However, Server resets its X value to 0 for both static and absolute positions, to show as many columns as possible. The height of each table row for overflow columns is the same as the corresponding row height in the original page.  Data type: Boolean |
| Suppress | Select **true** if you want to hide the object in the report. Server will skip all formulas and calculations. If you see the formula button Formula button in the value box, you can also [use a formula](https://devnet.logianalytics.com/hc/en-us/articles/4405690687511-Making-Simple-Modifications-to-Web-Report-Components#Property) to control this property. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress Aggregate | This property is available to labels (excluding summary labels) in a crosstab. Select **true** to hide the **Total** row or column. Data type: Boolean |
| Suppress Blank Panel | Select **true** to hide the panel if it contains no data. Data type: Boolean |
| Suppress Object Space If Not Exported | Select **true** to suppress the space for holding the objects in the report output if you don't include them for exporting. Data type: Boolean |
| Suppress When Empty | Select **true** to hide the object in the report when it contains no contents. Data type: Boolean |
| Suppress When No Records | Select **true** to hide the object in the report when no records return to its parent data component. Data type: Boolean |
| Tile Detail Panel | Select **true** to tile records in the detail panel. For a vertical banded object, you can tile each set of records in the detail panel when viewing the report if you set this property to true and set the detail panel's width/height equal to or less than 1/2 that of the banded object. The detail panel width determines the width of each record tile.  You will find this property is useful when you are making a mail-label format report. You can insert a blank banded object in a report, then in the Inspector panel, select the detail panel, and set the properties:  Tile Detail Panel = true Width = \*\*\* (The width of the detail panel. You can set this value according to the width of one column.)  Data type: Boolean  Note icon When the banded object's Autofit property is true, Server always treats the Tile Detail Panel property as false at runtime. |
| Tile Horizontal | If you set the Tile Detail Panel property of the detail panel to true, you can further specify the direction for tiling records in the detail panel.  * **true** Select if you want to tile records first in the row direction and then in the column. * **false** Select if you want to tile records first in the column direction and then in the row.   Data type: Boolean |
| To Bottom | Select **true** to move the banded object footer panel to the bottom of the page. Default is false, which means that the banded object footer displays at the end of the banded object. Data type: Boolean |
| Underlay | Select **true** if you want to layer the panel beneath the next panel in the banded object. You can use a panel layered beneath a subsequent panel to contain a background picture or watermark. Data type: Boolean  Note icon You cannot layer banded page header, page footer, or group footer panels beneath another panel. |
| Vertical Alignment | Select the vertical justification of the contents in the object, or of the image in the container. Data type: Enumeration |
| Alternating Line Color Properties | |
| Direction | Specify whether the color defined by the **Pattern List** property will apply to the fields in the same rows or columns in the crosstab. This property takes effect when the **Show** property is true.  * **Vertical** Select if you want the Pattern List property value to take effect on the fields in the same columns, except for the total columns. * **Horizontal** Select if you want the Pattern List property value to take effect on the fields in the same rows, except for the total rows.   Data type: Enumeration |
| Include Header and Footer | When the property is false, alternating color only applies to the table detail rows. Select **true** if you want to also apply alternating color to the footer, group headers, and group footers of the table. All table rows except the table header will use alternating color. It takes effect when the **Show** property is true.  Data type: Boolean |
| Pattern List | Specify the color patterns of the alternating color for the table rows. Select the ellipsis button Chooser button in the value cell to specify the patterns in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683801367-Color-List-Dialog-Box-Properties). This property takes effect when the **Show** property is true.  Data type: String |
| Show | Specify whether to enable setting alternating line color for the crosstab, or for the table rows. Data type: Boolean  Note icon   * The setting of the alternating line color function for crosstab can only take effect when all the aggregate fields in the crosstab have transparent background. * Alternating color works as the background color and will overwrite the table rows' own background color. * To make alternating color work in merged cells in group tables, you also need to set the background color of the merged cells to that of the alternating color. |
| Crosstab Property | |
| Column Totals on Left | Select **true** to display the Total columns on the left of the aggregates. Data type: Boolean |
| Row Totals on Top | Select **true** to display the Total rows on the top of the aggregates. Data type: Boolean |
| Suppress Column Header | Select **true** to suppress the column header of the crosstab. Data type: Boolean |
| Suppress Row Header | Select **true** to suppress the row header of the crosstab. Data type: Boolean |
| Excel Properties | |
| Columned | Select **true** if you want to improve the engine performance when exporting the report to CSV and Excel. Right after you set the Columned property to true from false each time, Logi Report will recalculate the values of the other Excel properties of the line objects in the report and reset the values to the defaults: Top Attach Column, Top Attach Row, Bottom Attach Column, and Bottom Attach Row. Server calculates the default values based on the position of each line object in the report. There is an exception: if both the Export to Excel and Export to CSV properties of a line object are false, Server will not recalculate the values of these properties and will preserve them as before.  When you set the Columned property to true:   * Server uses the columned method to export the report to Excel when you select **Column Format** in the export dialog box. * You can specify values for the Excel properties mentioned earlier of line objects instead of using the default, to well-align the line objects in the Excel output.   When the property is false, the specified values for the preceding Excel properties of the line objects in the report do not apply when you export the report to CSV or Excel.  Data type: Boolean |
| Column Index | Specify the X coordinate of the object relative to its parent container in the Excel and CSV outputs of the report, measured in cells. This property takes effect only when the Columned property of the web report is "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Specify the Y coordinate of the object relative to its parent container in the Excel and CSV outputs of the report, measured in cells. This property takes effect only when the Columned property of the web report is "true" and Position of the object is not "static". Data type: Integer |
| [Bottom Attach Column](#Attach) | Specify the X coordinate of the lower right corner of the object in the Excel output file, measured in cells. Data type: Float |
| [Bottom Attach Row](#Attach) | Specify the Y coordinate of the lower right corner of the object in the Excel output file, measured in cells. Data type: Float |
| [Top Attach Column](#Attach) | Specify the X coordinate of the upper-left corner of the object in the Excel output file, measured in cells. Data type: Float |
| [Top Attach Row](#Attach) | Specify the Y coordinate of the upper-left corner of the object in the Excel output file, measured in cells. Data type: Float |
| Group Layout Properties | |
| Keep Group Together | Select **true** to keep the whole group together. Data type: Boolean |
| Repeat While Group Footer | Select **true** if you want to repeat the group header when a page break occurs on the group footer, after you set the group header to be repeated. Data type: Boolean |
| Image Property | |
| Alternate Text | Specify the text that will display instead if Server cannot display the image. Data type: String |
| Disabled | Select **true** to disable the actions on the image. Data type: Boolean |
| Image Name | Specify the file name of the image. The image can be one on your local file system or retrieved using a URL. Data type: String |
| Maximum Scaling Ratio | Specify the maximum ratio up to which you can scale the image. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it. Data type: Float |
| Name | Specify the name of the image. Data type: String |
| Rotation | Specify the angle at which you want to rotate the image, in degrees. The following is the meaning of different values:  * 0 means no rotation. * A positive value means to rotate the image clockwise. * A negative value means to rotate the image anticlockwise.   Data type: Float |
| Scaling Mode | * **actual size** Select to show the image in its actual size. If the display area is smaller than the image, Server hides part of the image. * **fit image** Select if you want the image to fill the display area and keep the original perspective ratio under the limitation of Max Ratio. * **fit width** Select if you want the image to fit the display area width under the limitation of Max Ratio. * **fit height** Select if you want the image to fit the display area height, under the limitation of Max Ratio. * **customize** Select if you want to specify the width and height of the image in the size fields.   Note icon When you select fit height, fit image, or fit width, the image scales under the limitation of [Maximum Scaling Ratio](#Ratio).  Data type: Enumeration |
| Title | Specify the tip information about the image, which will display when you hover over the image in the Web Report result. Data type: String |
| Line Property | |
| Enable Bottom Arrow | Specify whether to use an arrow as the bottom (or right when the line is horizontal) end of the line. If you exchange the top and bottom ends, this property works on the bottom end after the exchange. Data type: Boolean |
| Enable Top Arrow | Specify whether to use an arrow as the top (or left when the line is horizontal) end of the line. If you exchange the top and bottom ends, this property works on the top end after the exchange. Data type: Boolean |
| Line Color | Specify the color of the line. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| Line Style | Select the style of the line. Data type: Enumeration |
| Line Thickness | Specify the thickness of the line. Type a numeric value to change the thickness. Data type: Float |
| Object Settings Properties | |
| Archive | Specify the character string that you can use to implement your own archive functionality for the object. Data type: String |
| Class ID | Specify the class identifier of the object. Data type: String |
| Code Base | Specify the base path you use to resolve relative URI specified by the Class ID and Archive properties. When null, its default value is the base URI of the current report. Data type: String |
| Value Type | Specify the MIME (Multipurpose Internet Mail Extensions) type of the object. Data type: String |
| Paper Properties | |
| Height | Specify the height of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values, but you can change the latter as desired. Type a numeric value to change the height. Data type: Float |
| Height Autofit | Specify whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Specify how to position the report page. The Orientation setting affects the Width and Height values.  * **Portrait** Select to position the page vertically. * **Landscape** Select to position the page horizontally.   Data type: Enumeration |
| Page Type | Specify the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Specify the width of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values, but you can change the latter as desired. Type a numeric value to change the width. Data type: Float |
| Width Autofit | Specify whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin Properties | |
| Bottom Margin | Specify the distance in inches or centimeters between the bottom page edge and the data area (the report for Banded Page Panel in a banded object). Type a numeric value to change the margin. Data type: Float |
| Left Margin | Specify the distance in inches or centimeters between the left page edge and the data area (the report for Banded Page Panel in a banded object). Type a numeric value to change the margin. Data type: Float |
| Right Margin | Specify the distance in inches or centimeters between the right page edge and the data area (the report for Banded Page Panel in a banded object). Type a numeric value to change the margin. Data type: Float |
| Top Margin | Specify the distance in inches or centimeters between the upper page edge and the data area (the report for Banded Page Panel in a banded object). Type a numeric value to change the margin. Data type: Float |
| Title Properties | |
| Background | Specify the background color of the title bar. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String  Data type: String |
| Bold | Select **true** to make the text bold in the title bar. Data type: Boolean |
| Font Face | Select the font of the text in the title bar. Data type: Enumeration |
| Font Size | Specify the font size of the text in the title bar. Type or select an integer value to change the size. Data type: Integer |
| Foreground | Specify the foreground color of the title bar. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| Horizontal Alignment | Select the horizontal justification of the text in the title bar. Data type: Enumeration |
| Italic | Select **true** to make the text italic in the title bar. Data type: Boolean |
| Map Name | Specify whether you want to display the name of the field you added to the filter control as the title in the title bar. Data type: Boolean |
| Show Title | Specify whether to show the title bar. It is meaningful to set all the other properties in [the Title category](#Title) when this property value is true. Data type: Boolean |
| Text | Type the text you want to display in the title bar. For a filter control, you can edit this property only when you set [Map Name](#MapName) to "false". Data type: String |
| Underline | Select **true** to underline the text in the title bar. Data type: Boolean |

## Merge to Next Panel, Repeat in Detail Panel, and Remove Blank Row

You can control panels of a banded object in the Excel output by setting the three properties:

* **Merge to Next Panel** controls whether to merge current panel to the next panel. It applies to the banded header, banded page header, group header, and group footer panels.
* **Repeat in Detail Panel** controls whether to repeat certain panel with the detail panel. It applies to the group header and banded page header panels.
* **Remove Blank Row** controls whether to remove blank rows in the panel. It applies to the banded page header, group header, and detail panels.

The three properties take effect only when you set the [Columned](#Columned) property of the web report to true. Server follows the operation order when the three properties work together: Merge to Next Panel > Repeat in Detail Panel > Remove Blank Row.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* Do not set **Merge to Next Panel** to true for the last group footer panel, because it will make the Excel output incorrect.
* Do not set **Merge to Next Panel** to true for the panel that contains crosstabs or subreports.
* When you specify to repeat a group header panel, if there is a chart in the panel, Server does not repeat the chart.
* If a banded object contains more than one group-by fields, that is to say, it has several group header panels, when you specify to repeat the first group header panel in the detail panel, Server will repeat it in the second group header panel as well.

## Bottom Attach Column, Bottom Attach Row, Top Attach Column, Top Attach Row

The four properties work together to control the position of a line in the Excel output file. They take effect when you set the [Columned](#Columned) property of the web report to true.

The first pair of the properties (Top Attach Column, Top Attach Row) locates a cell and uses its upper left corner as the upper-left corner of the line, while the second pair (Bottom Attach Column, Bottom Attach Row) locates another cell and uses its upper left corner as the lower right corner of the line.

For example, if you set the properties for an oval as:

Top Attach Column: 1, Top Attach Row: 2, Bottom Attach Column: 3, Bottom Attach Row: 4

Then, the upper left cell will be A2 and the lower right cell will be C4.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) The value you set for the Top Attach Column (Top Attach Row) property should be always larger than that for the Bottom Attach Column (Bottom Attach Row) property.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* If a table contains a merged cell that is across columns and there are absolutely positioned objects in the cell, when you exclude a column which is not the last column for this merged cell from the report output, Logi Report Engine recalculates the X coordinates of these objects that are in the excluded column and tries to display them in the output if space allows; however, this may result in that some objects get overlapped in their new position in the output.
* Because one cell in Excel can only contain one value, if you exclude a table column from the Excel output, Logi Report Engine is not able to display the value of a data field which is originally in the excluded column in the Excel output if the new position of the field is in a cell that already contains a value, even when the field satisfies the conditions as described earlier.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690691607-Customizing-the-Web-Report-Studio-UI)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties)
