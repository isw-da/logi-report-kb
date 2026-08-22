---
title: "Properties of KPI Chart Paper in Library Component"
id: 1500009569242
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569242-Properties-of-KPI-Chart-Paper-in-Library-Component
updated_at: 2021-07-24T05:54:19Z
---

# Properties of KPI Chart Paper in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590901-Properties-of-Label-in-Library-Component)

# Properties of KPI Chart Paper in Library Component

The properties of the chart paper in a KPI chart in a library component are as follows:

| Property Name | Description |
| --- | --- |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component#Position) property of the KPI chart is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component#Position) property of the KPI chart is set to static. Enter a numeric value to change the position. Data type: Float |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Coordinate Paper | |
| Graph Position | Specifies the position of the paper contents relative to the paper background. Choose an option from the drop-down list. Data type: Enumeration |
| Reverse Painting Order | Specifies whether to reverse the order of graphic objects in a combo chart. Data type: Boolean |
| Scale X | Specifies the percentage for elongating or shortening the X axis. Enter a numeric value to change the percentage. Data type: Float |
| Scale Y | Specifies the percentage for elongating or shortening the Y axis. Enter a numeric value to change the percentage. Data type: Float |
| Shadow Contents | Specifies whether to add shadows to all 2-D charts. Data type: Boolean |
| Background | |
| Border Color | Specifies the color of the paper border. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style of the paper border line. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the joint style of the paper border line. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the paper border line in Outline Path. If the property is set to true, the paper border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Specifies the line style of the paper border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the paper border. Enter a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the transparency of the paper border, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#BorderType) | Specifies the border type of the paper. Choose an option from the drop-down list. Data type: Enumeration |
| Border Variable Dash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the [Format Paper](https://devnet.logianalytics.com/hc/en-us/articles/1500009565982-Format-Paper-Dialog#Dash) dialog will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the [Format Paper](https://devnet.logianalytics.com/hc/en-us/articles/1500009565982-Format-Paper-Dialog#Dash) dialog will take effect.   Data type: Boolean |
| Color | Specifies the color of the paper background, applied when the property Fill Type is set to color. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specifies the transparency of the paper background, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Fill Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FillType) | Specifies the fill pattern for the paper background. Choose an option from the drop-down list. Data type: Enumeration |
| Gradient End Color | Specifies the color of the point where the gradient ends, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the paper width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the paper height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the paper width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the paper height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the paper background, applied when the property Fill Type is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Image File | Specifies the file name of the image, a portion of which will be displayed as the paper background. Applied when the property Fill Type is set to image. Enter the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
| Image Height | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when the property Fill Type is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
| [Image Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#ImageLayout) | Specifies the layout style for the image that will be displayed as the paper background, applied when the property Fill Type is set to image. Choose an option from the drop-down list. Data type: Enumeration |
| Image Width | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when the property Fill Type is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
| Image X | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when the property Fill Type is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
| Image Y | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when the property Fill Type is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
| Inset Bottom | Specifies the bottom position of the background area, measured in a percentage of the paper height, from the bottom edge of the paper. Data type: Float |
| Inset Left | Specifies the left position of the background area, measured in a percentage of the paper width, from the left edge of the paper. Data type: Float |
| Inset Right | Specifies the right position of the background area, measured in a percentage of the paper width, from the right edge of the paper. Data type: Float |
| Inset Top | Specifies the top position of the background area, measured in a percentage of the paper height, from the top edge of the paper. Data type: Float |
| Texture Background Color | Specifies the background color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style of the paper background, applied when the property Fill Type is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Graph | |
| Border | Specifies whether to show the borders. Data type: Boolean |
| Border Color | Specifies the line color for the border, not applying to 2-D line charts. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style for the border, not applying to 2-D line charts. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the line joint style for the border, not applying to 2-D line charts. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the border in outline form, not applying to 2-D line charts. If the property is set to true, the border will be shown in outline form; otherwise, in whole form. Data type: Boolean |
| Border Style | Specifies the line style for the border, not applying to 2-D line charts. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the thickness for the border, not applying to 2-D line charts. Enter a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the line transparency for the border, in percent, not applying to 2-D line charts. Enter a numeric value to change the transparency. Data type: Integer |
| Border Variable Dash | Specifies whether to resize the dash automatically, not applying to 2-D line charts. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
| Suppress Label When 0 | If true, the data label whose value is 0 will not be displayed. This property is available to these 2-D chart types: bar, bench, line, area and pie. Data type: Boolean |
| For bar/bench chart | |
| Bar Gap | Specifies the distance between each bar/bench in a category. Applies to 2-D clustered bar/bench charts only. Enter a numeric value to change the gap. Data type: Integer |
| Bar Style | Specifies the style of the bars/benches. Choose an option from the drop-down list. It can be normal or cylinder, however, if you specify the style to be cylinder, it will take effect only when the property [Use Depth](#Depth) is set to true. Data type: Enumeration |
| Bar Width | Specifies the total width of the bars/benches in each category, measured in a percentage of the unit width. Enter a numeric value to change the width. Data type: Integer |
| Depth | Specifies the depth of the bars/benches, applied when the value of the property Use Depth is set to true. Applies to 2-D bar/bench charts only. Enter a numeric value to change the depth. Data type: Float |
| Direction | Specifies the angle of the axis along the depth of the bars/benches. Applies to 2-D bar/bench charts only. Enter a numeric value to change the direction. Data type: Integer |
| Update Direction | Specifies the direction in which to paint the values when the chart is updated. Available to real time chart only. Choose an option from the drop-down list.  * **Default** - If it is a bench chart, paints the values from top to bottom, otherwise, from right to left. * **Reverse** - If it is a bench chart, paints the values from bottom to top, otherwise, from left to right.   Data type: Enumeration |
| Use Depth | Specifies whether to make the bars/benches visually three-dimensional. Applies to 2-D bar/bench charts only. Data type: Boolean  **Note:** If the chart is a combo chart composed by bars and areas/lines, when you set the depth properties for the bars, they will be applied to the areas/lines as well, and vice versa. |
| Value Label Type | Specifies in which way the value labels will be displayed around the bars/benches. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009587021-Format-Bar-Dialog-for-Web-Report-#Show) is checked in the Format Bar dialog. Choose an option from the drop-down list.  * **value** - Shows the value for each bar/bench. * **percent** - Shows the percentage of each bar/bench to the total. * **value and percent** - Shows the value and the percentage for each bar/bench.   Data type: Enumeration |
| Vary Colors by Color List | Specifies whether or not to make the bar colors vary. It only takes effect on clustered bar/bench types and when the charts has no series field. Data type: Boolean |
| For line chart | |
| Area Pattern List | Specifies patterns for the areas which are formed by the chart axes and the lines. Applies to 2-D lines only. Select More button in the value cell and select the small squares in the color tray one by one to specify the patterns for the areas. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient.  Data type: String |
| Depth | Specifies the depth of the lines, applied when the property Use Depth is set to true. Enter a numeric value to change the depth. Data type: Float |
| Direction | Specifies the angle of the axis along the depth of the lines. Enter a numeric value to change the direction. Data type: Integer |
| Ignore Null Value | Specifies whether to skip null data values in order to draw continuous lines.  * **true** - When a null data value appears, it is skipped and the line is drawn from the previous data value to the next data value directly. * **false** - When a null data value appears, draw it anyway and the line is broken at the point of the null data value.   Data type: Boolean |
| Smoothed Line | Specifies whether to draw the lines smoothly without the sharp joints. Applies to 2-D charts only. Data type: Boolean |
| Update Direction | Specifies the direction in which to paint the values when the chart is updated. Available to real time chart only. Choose an option from the drop-down list.  * **Default** - Paints the values from right to left. * **Reverse** - Paints the values from left to right.   Data type: Enumeration |
| Use Depth | Specifies whether to make the lines visually three-dimensional. Applies to 2-D line charts only. Data type: Boolean  **Note:** If the chart is a combo chart composed by lines and areas/bars, when you set the depth properties for the lines, they will be applied to the areas/bars as well, and vice versa. |
| Value Label Type | Specifies in which way the value labels will be displayed around the lines. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009565962-Format-Line-Dialog-for-Web-Report-#Show) is checked in the Format Line dialog. Available to 2-D line charts only. Choose an option from the drop-down list.  * **value** - Shows the value for each line node. * **percent** - Shows the percentage of each line node to the total. * **value and percent** - Shows the value and the percentage for each line node.   Data type: Enumeration |
| For area chart | |
| Depth | Specifies the depth of the areas, applied when the property Use Depth is set to true. Applies to 2-D area charts only. Enter a numeric value to change the depth. Data type: Float |
| Direction | Specifies the angle of the axis along the depth of the areas. Applies to 2-D area charts only. Enter a numeric value to change the direction. Data type: Integer |
| Ignore Null Value | Specifies whether to skip null data values in order to draw continuous areas.  * **true** - When a null data value appears, it is skipped and the area is drawn from the previous data value to the next data value directly. * **false** - When a null data value appears, draw it anyway and the area is broken at the point of the null data value.   Data type: Boolean |
| Update Direction | Specifies the direction in which to paint the values when the chart is updated. Available to real time chart only. Choose an option from the drop-down list.  * **Default** - Paints the values from right to left. * **Reverse** - Paints the values from left to right.   Data type: Enumeration |
| Use Depth | Specifies whether to make the areas visually three-dimensional. Applies to 2-D area charts only. Data type: Boolean  **Note:** If the chart is a combo chart composed by areas and bars/lines, when you set the depth properties for the areas, they will be applied to the bars/lines as well, and vice versa. |
| Use Dropline | Specifies whether to show the lines that represent the data categories. Applies to 2-D area charts only. Data type: Boolean |
| Value Label Type | Specifies in which way the value labels will be displayed around the areas. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009586981-Format-Area-Dialog-for-Web-Report-#Show) is checked in the Format Area dialog. Choose an option from the drop-down list.  * **value** - Shows the value for each area node. * **percent** - Shows the percentage of each area node to the total. * **value and percent** - Shows the value and the percentage for each area node.   Data type: Enumeration |
| For pie chart | |
| Angle X | Specifies the rotation angle of the chart around the X axis, in degrees. Enter a numeric value to change the rotation. Data type: Float |
| Angle Y | Specifies the rotation angle of the chart around the Y axis, in degrees. Enter a numeric value to change the rotation. Data type: Float |
| Donut Hole | Specifies the radius percentage of the donut hole to the total pie circle. Applies to donut chart only. Data type: Float |
| Pie Gap | Specifies the distance between every two adjacent pie sections. Enter a numeric value to change the gap. Data type: Float |
| Section Explode Gap | Specifies the distance between each pie section and the pie center. Enter a numeric value to change the gap. Data type: Float |
| Show Pie/Donut Name | Specifies whether to show the name of the pie/donut. Data type: Boolean |
| Value Label Type | Specifies in which way the value labels will be displayed around the pie. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009566002-Format-Pie-Dialog-for-Report-#Show) is checked in the Format Pie dialog. Choose an option from the drop-down list.  * **value** - Shows the value for each pie section. * **category name** - Shows the category name for each pie section. * **percent** - Shows the percentage of each pie section to the total. * **value and percent** - Shows the value and the percentage for each pie section. * **category name, value**  - Shows the category name and value for each pie section. * **category name, percent**  - Shows the category name and percentage for each pie section. * **category name, value, percent**  - Shows the category name, value and percentage for each pie section.   Data type: Enumeration |
| For bullet chart | |
| Comparative Measure Color List | Specifies the fill effect of the comparative measures in the same data series. Select More button in the value cell to specify the effect. Data type: String |
| Comparative Measure Width | Specifies the width of the comparative measures. Enter a numeric value to change the width. Data type: Integer |
| Featured Measure Width | Specifies the width of the featured measures. Enter a numeric value to change the width. Data type: Integer |
| Graph Direction | Specifies the direction to draw the bullet chart, horizontally or vertically. Choose an option from the drop-down list. Data type: Enumeration |
| Qualitative Ranges Color List | Specifies the fill effect of the qualitative ranges in the same data series. Select More button in the value cell to specify the effect. Data type: String |
| Qualitative Ranges Width | Specifies the width of the qualitative ranges. Enter a numeric value to change the width. Data type: Integer |
| Special Featured Measure Graph Type | Specifies the graph type for the featured measures when the value (Y) axis does not start from the value zero. Choose an option from the drop-down list. Data type: Enumeration |
| Vary Colors by Color List | Specifies whether or not to make colors for the featured measures vary. Data type: Boolean |
| Hint | |
| Color | Specifies the color of the hint text, applied when the property Fill Type is set to color. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specifies the transparency of the background, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Fill Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FillType) | Specifies the fill pattern for the hint text. Choose an option from the drop-down list. Data type: Enumeration |
| [Font Effect](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontEffect) | Specifies the special effect for the hint. Choose an option from the drop-down list. Data type: Integer |
| Font Face | Specifies the font face for the hint. Choose an option from the drop-down list. Data type: Enumeration |
| Font Rotation | Specifies the rotation angle of the hint around its center, in degrees. The default value is 0. Enter a numeric value to change the rotation. Data type: Float |
| [Font Script](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontScript) | Specifies whether the hint will be in superscript or subscript form, or neither of them. Choose an option from the drop-down list. Data type: Enumeration |
| Font Shearing | Specifies the shearing transformation of the hint around its center. The default value is 0. Enter a numeric value to change the shearing. Data type: Float |
| Font Size | Specifies the font size for the hint. Enter an integer value to change the size. Data type: Integer |
| [Font Strikethrough](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontStrikethrough) | Specifies the style for the line by which the hint text is struck through. Choose an option from the drop-down list. Data type: Enumeration |
| Font Style | Specifies the font style for the hint. Choose an option from the drop-down list. Data type: Enumeration |
| [Font Underline](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontUnderline) | Specifies the underline style for the hint. Choose an option from the drop-down list. Data type: Enumeration |
| Gradient End Color | Specifies the color of the point where the gradient ends, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the hint width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the hint height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the hint width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the hint height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the hint text, applied when the property Fill Type is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Line Color | Specifies the color of the thin lines that are used to point to the static data labels. Applies to pie charts only. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Outline Color | Specifies the color for the hint text outline. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Outline End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style for the hint text outline. Choose an option from the drop-down list. Data type: Enumeration |
| [Outline Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the joint style for the hint text outline. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Outlined | Specifies whether to show the hint text outline in outline form. If the property is set to true, the outline will be shown in outline form; otherwise, in whole form. Data type: Boolean |
| Outline Style | Specifies the style for the hint text outline. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Thickness | Specifies the thickness of the hint text outline. Enter a numeric value to change the thickness. Data type: Float |
| Outline Transparency | Specifies the transparency for the hint text outline, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Outline Variable Dash | Specifies whether to resize the dash automatically. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
| Show Category and Series | Specifies whether to include the category and series values in the hints of the data markers. Data type: Boolean |
| Show Tips | Specifies whether to show the hint that displays the value of a data marker when the mouse pointer points at the data marker in Designer view mode, in HTML result, or at runtime on Logi JReport Server. If this property is set to false, all the other hint properties will be ignored. Data type: Boolean |
| Texture Background Color | Specifies the background color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style for the hint text, applied when the property Fill Type is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Threshold Line | |
| Fill Threshold1 | Specifies whether to fill the first threshold area with a semi-transparent color. Data type: Boolean |
| Fill Threshold2 | Specifies whether to fill the second threshold area with a semi-transparent color. Data type: Boolean |
| Fill Transparency | Specifies the transparency of the background, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Show Threshold Line1 | Specifies whether to show the first threshold line. Data type: Boolean |
| Show Threshold Line2 | Specifies whether to show the second threshold line. Data type: Boolean |
| Threshold Line Color1 | Specifies the color for the first threshold line. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Threshold Line Color2 | Specifies the color for the second threshold line. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Threshold Line Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#ThresholdLineStyle) | Specifies the style for the threshold lines. Choose an option from the drop-down list. Data type: Enumeration |
| Threshold Value1 | Specifies the value for the first threshold line. Data type: Float |
| Threshold Value2 | Specifies the value for the second threshold line. Data type: Float |
| MeanLine | |
| Color | Specifies the color of the mean line. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Node Style | Specifies the style of the nodes that represent the average values. Choose an option from the drop-down list. Data type: Enumeration |
| Show | Specifies whether to show a line that represents the average value of each category group. Not applies to bubble charts. Data type: Boolean |
| Type | Specifies the type of the mean line. Choose an option from the drop-down list. Data type: Enumeration |

**Note:** For combo chart, the graph properties will respectively apply to the corresponding chart types.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590901-Properties-of-Label-in-Library-Component)
