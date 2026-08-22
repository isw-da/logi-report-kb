---
title: "KPI Chart Paper Properties"
id: 4405661868183
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661868183-KPI-Chart-Paper-Properties
updated_at: 2022-01-27T20:35:30Z
---

# KPI Chart Paper Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661866903-KPI-Chart-Label-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661869207-Label-Properties)

# KPI Chart Paper Properties

This topic describes the properties of the Chart Paper object in a KPI chart.

| Property Name | Description |
| --- | --- |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner relative to its parent container, which Logi Report Engine applies when the KPI chart is not in static [position](https://devnet.logianalytics.com/hc/en-us/articles/4405661865751-KPI-Chart-Properties#Position) in its container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the KPI chart is not in static [position](https://devnet.logianalytics.com/hc/en-us/articles/4405661865751-KPI-Chart-Properties#Position) in its container. Type a numeric value to change the coordinate. Data type: Float |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style to apply to the object. You can specify the style in two ways:   * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the [Style Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup) property for the web report and there are styles in the style group that are applicable to the object.   Data type: String |
| Coordinate Paper | |
| Graph Position | Specifies the position of the paper contents relative to the paper background. Choose an option from the drop-down list. Data type: Enumeration |
| Reverse Painting Order | Specifies whether to reverse the order of graphic objects in a combo chart. Data type: Boolean |
| Scale X | Specifies the percentage for elongating or shortening the X axis. Type a numeric value to change the percentage. Data type: Float |
| Scale Y | Specifies the percentage for elongating or shortening the Y axis. Type a numeric value to change the percentage. Data type: Float |
| Shadow Contents | Specifies whether to add shadows to the chart. Data type: Boolean |
| Background | |
| Border Color | Specifies the color of the paper border. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#EndCaps) | Specifies the ending style of the paper border line. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Joint) | Specifies the joint style of the paper border line. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the paper border line in Outline Path. If the property is set to true, the paper border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Specifies the line style of the paper border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the paper border. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the transparency of the paper border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#BorderType) | Specifies the border type of the paper. Choose an option from the drop-down list. Data type: Enumeration |
| Border Variable Dash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option [Auto Adjust Dash](https://devnet.logianalytics.com/hc/en-us/articles/4405661580311-Format-Paper-Dialog-Box#Dash) in the Format Paper dialog box will take effect. * **false** - If selected, the dash size will be of fixed size, and the option [Fixed Dash Size](https://devnet.logianalytics.com/hc/en-us/articles/4405661580311-Format-Paper-Dialog-Box#Dash) in the Format Paper dialog box will take effect.   Data type: Boolean |
| Color | Specifies the color of the paper background. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to color. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specifies the transparency of the paper background, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specifies the fill pattern for the paper background. Choose an option from the drop-down list. Can be none, color, texture, gradient or image. Data type: Enumeration |
| Gradient End Color | Specifies the color of the point where the gradient ends. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the paper width. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the paper height. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the paper width. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the paper height. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the paper background. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Image File | Specifies the file name of the image, a portion of which will be displayed as the paper background. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to image. Type the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
| Image Height | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when [Fill Type](#BackgroundFillType) of the paper background is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
| Image Layout | Specifies the layout style for the image that will be displayed as the paper background. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to image. Choose an option from the drop-down list.  * **tile** - Repeats the image over the entire area (default). * **center** - Displays the image in the center of the area. * **scaled** - Stretches the image to cover the entire area.   Data type: Enumeration |
| Image Width | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when [Fill Type](#BackgroundFillType) of the paper background is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
| Image X | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when [Fill Type](#BackgroundFillType) of the paper background is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
| Image Y | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the paper background. They take effect when [Fill Type](#BackgroundFillType) of the paper background is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
| Inset Bottom | Specifies the bottom position of the background area, measured in a percentage of the paper height, from the bottom edge of the paper. Data type: Float |
| Inset Left | Specifies the left position of the background area, measured in a percentage of the paper width, from the left edge of the paper. Data type: Float |
| Inset Right | Specifies the right position of the background area, measured in a percentage of the paper width, from the right edge of the paper. Data type: Float |
| Inset Top | Specifies the top position of the background area, measured in a percentage of the paper height, from the top edge of the paper. Data type: Float |
| Texture Background Color | Specifies the background color of the texture. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style of the paper background. Applied when [Fill Type](#BackgroundFillType) of the paper background is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Graph | |
| Border Color | Specifies the line color for the border, not applying to line charts. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#EndCaps) | Specifies the ending style for the border, not applying to line charts. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Joint) | Specifies the line joint style for the border, not applying to line charts. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the border in outline form, not applying to line charts. If the property is set to true, the border will be shown in outline form; otherwise, in whole form. Data type: Boolean |
| Border Style | Specifies the line style for the border, not applying to line charts. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the thickness for the border, not applying to line charts. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the line transparency for the border, in percent, not applying to line charts. Type a numeric value to change the transparency. Data type: Integer |
| Border Variable Dash | Specifies whether to resize the dash automatically, not applying to line charts. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
| Show Border | Specifies whether to show the borders. Data type: Boolean |
| For bar/bench chart | |
| Bar Gap | Specifies the distance between each bar/bench in a category. Applies to clustered bar/bench charts only. Type a numeric value to change the gap. Data type: Integer |
| Bar Style | Specifies the style of the bars/benches. Choose an option from the drop-down list. It can be normal or cylinder, however, if you specify the style to be cylinder, it will take effect only when the property [Use Depth](#BarUseDepth) is set to true. Data type: Enumeration |
| Bar Width | Specifies the total width of the bars/benches in each category, measured in a percentage of the unit width. Type a numeric value to change the width. Data type: Integer |
| Data Label Type | Specifies in which way the data labels will be displayed around the bars/benches. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/4405661559447-Format-Bar-Dialog-Box#Show) is selected in the Format Bar dialog box. Choose an option from the drop-down list.  * **value** - Shows the value for each bar/bench. * **percent** - Shows the percentage of each bar/bench to the total. * **value and percent** - Shows the value and the percentage for each bar/bench.   Data type: Enumeration |
| Depth | Specifies the depth of the bars/benches when [Use Depth](#BarUseDepth) is set to true. Type a numeric value to change the depth. Data type: Float |
| Direction | Specifies the angle of the axis along the depth of the bars/benches. Type a numeric value to change the direction. Data type: Integer |
| Suppress Label When 0 | If true, the data label whose value is 0 will not be displayed. Data type: Boolean |
| Update Direction | Specifies the direction to paint the values when the chart is updated. Available to real time chart only. Choose an option from the drop-down list.  * **Default** - If it is a bench chart, paints the values from top to bottom, otherwise, from right to left. * **Reverse** - If it is a bench chart, paints the values from bottom to top, otherwise, from left to right.   Data type: Enumeration |
| Use Depth | Specifies whether to make the bars/benches visually three-dimensional. Data type: Boolean  Note icon If the chart is a combo chart composed by bars and areas/lines, when you set the depth properties for the bars, they will be applied to the areas/lines as well, and vice versa. |
| Vary Colors by Color List | Specifies whether to make the bar colors vary. It only takes effect on clustered bar/bench types and when the charts has no series field. Data type: Boolean |
| For line chart | |
| Area Pattern List | Specifies patterns for the areas which are formed by the chart axes and the lines. Select More button in the value cell and select the small squares in the color tray one by one to specify the patterns for the areas. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient.  Data type: String |
| Data Label Type | Specifies in which way the data labels will be displayed around the lines. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/4405661579287-Format-Line-Dialog-Box#Show) is selected in the Format Line dialog box. Choose an option from the drop-down list.  * **value** - Shows the value for each line node. * **percent** - Shows the percentage of each line node to the total. * **value and percent** - Shows the value and the percentage for each line node.   Data type: Enumeration |
| Depth | Specifies the depth of the lines when [Use Depth](#LineUseDepth) is set to true. Type a numeric value to change the depth. Data type: Float |
| Direction | Specifies the angle of the axis along the depth of the lines. Type a numeric value to change the direction. Data type: Integer |
| Ignore Null Value | Specifies whether to skip null data values in order to draw continuous lines.  * **true** - When a null data value appears, it is skipped and the line is drawn from the previous data value to the next data value directly. * **false** - When a null data value appears, draw it anyway and the line is broken at the point of the null data value.   Data type: Boolean |
| Smoothed Line | Specifies whether to draw the lines smoothly without the sharp joints. Data type: Boolean |
| Suppress Label When 0 | If true, the data label whose value is 0 will not be displayed. Data type: Boolean |
| Update Direction | Specifies the direction to paint the values when the chart is updated. Available to real time chart only. Choose an option from the drop-down list.  * **Default** - Paints the values from right to left. * **Reverse** - Paints the values from left to right.   Data type: Enumeration |
| Use Depth | Specifies whether to make the lines visually three-dimensional. Data type: Boolean  Note icon If the chart is a combo chart composed by lines and areas/bars, when you set the depth properties for the lines, they will be applied to the areas/bars as well, and vice versa. |
| For area chart | |
| Data Label Type | Specifies in which way the data labels will be displayed around the areas. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/4405661558167-Format-Area-Dialog-Box#Show) is selected in the Format Area dialog box. Choose an option from the drop-down list.  * **value** - Shows the value for each area node. * **percent** - Shows the percentage of each area node to the total. * **value and percent** - Shows the value and the percentage for each area node.   Data type: Enumeration |
| Depth | Specifies the depth of the areas when [Use Depth](#AreaUseDepth) is set to true. Type a numeric value to change the depth. Data type: Float |
| Direction | Specifies the angle of the axis along the depth of the areas. Type a numeric value to change the direction. Data type: Integer |
| Ignore Null Value | Specifies whether to skip null data values in order to draw continuous areas.  * **true** - When a null data value appears, it is skipped and the area is drawn from the previous data value to the next data value directly. * **false** - When a null data value appears, draw it anyway and the area is broken at the point of the null data value.   Data type: Boolean |
| Suppress Label When 0 | If true, the data label whose value is 0 will not be displayed. Data type: Boolean |
| Update Direction | Specifies the direction to paint the values when the chart is updated. Available to real time chart only. Choose an option from the drop-down list.  * **Default** - Paints the values from right to left. * **Reverse** - Paints the values from left to right.   Data type: Enumeration |
| Use Depth | Specifies whether to make the areas visually three-dimensional. Data type: Boolean  Note icon If the chart is a combo chart composed by areas and bars/lines, when you set the depth properties for the areas, they will be applied to the bars/lines as well, and vice versa. |
| Use Dropline | Specifies whether to show the lines that represent the data categories. Data type: Boolean |
| For pie chart | |
| Angle X | Specifies the rotation angle of the chart around the X axis, in degrees. Type a numeric value to change the rotation. Data type: Float |
| Angle Y | Specifies the rotation angle of the chart around the Y axis, in degrees. Type a numeric value to change the rotation. Data type: Float |
| Data Label Type | Specifies in which way the data labels will be displayed around the pie. Applied only when [Show Static Data Label](https://devnet.logianalytics.com/hc/en-us/articles/4405661581335-Format-Pie-Dialog-Box#Show) is selected in the Format Pie dialog box. Choose an option from the drop-down list.  * **value** - Shows the value for each pie section. * **category name** - Shows the category name for each pie section. * **percent** - Shows the percentage of each pie section to the total. * **value and percent** - Shows the value and the percentage for each pie section. * **category name, value**  - Shows the category name and value for each pie section. * **category name, percent**  - Shows the category name and percentage for each pie section. * **category name, value, percent**  - Shows the category name, value and percentage for each pie section.   Data type: Enumeration |
| Donut Hole | Specifies the radius percentage of the donut hole to the total pie circle. Applies to donut chart only. Data type: Float |
| Pie Gap | Specifies the distance between every two adjacent pie sections. Type a numeric value to change the gap. Data type: Float |
| Section Explode Gap | Specifies the distance between each pie section and the pie center. Type a numeric value to change the gap. Data type: Float |
| Show Pie/Donut Name | Specifies whether to show the name of the pie/donut. Data type: Boolean |
| Suppress Label When 0 | If true, the data label whose value is 0 will not be displayed. Data type: Boolean |
| For bullet chart | |
| Comparative Measure Color List | Specifies the fill effect of the comparative measures in the same data series. Select More button in the value cell to specify the effect. Data type: String |
| Comparative Measure Width | Specifies the width of the comparative measures. Type a numeric value to change the width. Data type: Integer |
| Featured Measure Width | Specifies the width of the featured measures. Type a numeric value to change the width. Data type: Integer |
| Graph Direction | Specifies the direction to draw the bullet chart, horizontally or vertically. Choose an option from the drop-down list. Data type: Enumeration |
| Qualitative Ranges Color List | Specifies the fill effect of the qualitative ranges in the same data series. Select More button in the value cell to specify the effect. Data type: String |
| Qualitative Ranges Width | Specifies the width of the qualitative ranges. Type a numeric value to change the width. Data type: Integer |
| Special Featured Measure Graph Type | Specifies the graph type for the featured measures when the value (Y) axis does not start from the value zero. Choose an option from the drop-down list. Data type: Enumeration |
| Vary Colors by Color List | Specifies whether to make colors for the featured measures vary. Data type: Boolean |
| Hint | |
| Category Name | Specifies the name of the category field to be displayed in the data marker hint. By default the display name of the category field is used in the hint to label the category value. You can customize the name to help users better understand the value. This property is available only when [Customize Category and Series Names](#CustomizeCategory) is set to true. Data type: String |
| Color | Specifies the color of the hint text. Applied when [Fill Type](#HintFillType) of the hint text is set to color. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Customize Category and Series Names | Specifies whether the names of the category and series fields in the data marker hint can be customized. Applied when [Show Category and Series](#ShowCategory) is set to true. Data type: Boolean |
| Fill Transparency | Specifies the transparency of the background, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specifies the fill pattern for the hint text. Choose an option from the drop-down list. Can be none, color, texture or gradient. Data type: Enumeration |
| [Font Effect](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#FontEffect) | Specifies the special effect for the hint text. Choose an option from the drop-down list. Data type: Integer |
| Font Face | Specifies the font face for the hint text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Rotation | Specifies the rotation angle of the hint text around its center, in degrees. The default value is 0. Type a numeric value to change the rotation. Data type: Float |
| Font Script | Specifies whether the hint text will be in superscript or subscript form, or neither of them. Choose an option from the drop-down list. Data type: Enumeration |
| Font Shearing | Specifies the shearing transformation of the hint text around its center. The default value is 0. Type a numeric value to change the shearing. Data type: Float |
| Font Size | Specifies the font size for the hint text. Type an integer value to change the size. Data type: Integer |
| Font Strikethrough | Specifies the style for the line by which the hint text is struck through. Choose an option from the drop-down list. Data type: Enumeration |
| Font Style | Specifies the font style for the hint text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Underline | Specifies the style of the horizontal line under the hint text. Choose an option from the drop-down list. When patterned line or bold patterned is selected, a line or bold line in the pattern of the text will be drawn. Data type: Enumeration  Critical icon Web Report Studio and JDashboard do not support underlining chart text so this property will be ignored when the chart runs in Web Report Studio or is used in a dashboard. |
| Gradient End Color | Specifies the color of the point where the gradient ends. Applied when [Fill Type](#HintFillType) of the hint text is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the hint width. Applies when [Fill Type](#HintFillType) of the hint text is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the hint height. Applied when [Fill Type](#HintFillType) of the hint text is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins. Applied when [Fill Type](#HintFillType) of the hint text is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the hint width. Applied when [Fill Type](#HintFillType) of the hint text is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the hint height. Applied when [Fill Type](#HintFillType) of the hint text is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the hint text. Applied when [Fill Type](#HintFillType) of the hint text is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Line Color | Specifies the color of the thin lines that are used to point to the static data labels. Applies to pie charts only. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Outline Color | Specifies the color for the hint text outline. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Outline End Caps](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#EndCaps) | Specifies the ending style for the hint text outline. Choose an option from the drop-down list. Data type: Enumeration |
| [Outline Joint](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Joint) | Specifies the joint style for the hint text outline. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Outlined | Specifies whether to show the hint text outline in outline form. If the property is set to true, the outline will be shown in outline form; otherwise, in whole form. Data type: Boolean |
| Outline Style | Specifies the style for the hint text outline. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Thickness | Specifies the thickness of the hint text outline. Type a numeric value to change the thickness. Data type: Float |
| Outline Transparency | Specifies the transparency for the hint text outline, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Outline Variable Dash | Specifies whether to resize the dash automatically. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
| Series Name | Specifies the name of the series field to be displayed in the data marker hint. By default the display name of the series field is used in the hint to label the series value. You can customize the name to help users better understand the value. This property is available only when [Customize Category and Series Names](#CustomizeCategory) is set to true. Data type: String |
| Show Category and Series | Specifies whether to include the category and series values in the data marker hint. Data type: Boolean |
| Show Tips | Specifies whether to show the hint that displays the values a data marker represents when you point to the data marker in Designer view mode, in HTML output, or at runtime. If this property is set to false, all the other hint properties will be ignored. Data type: Boolean |
| Texture Background Color | Specifies the background color of the texture. Applied when [Fill Type](#HintFillType) of the hint text is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture. Applied when [Fill Type](#HintFillType) of the hint text is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style for the hint text. Applied when [Fill Type](#HintFillType) of the hint text is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Threshold Line | |
| Fill Threshold1 | Specifies whether to fill the first threshold area with a semi-transparent color. Data type: Boolean |
| Fill Threshold2 | Specifies whether to fill the second threshold area with a semi-transparent color. Data type: Boolean |
| Fill Transparency | Specifies the transparency of the background, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Show Threshold Line1 | Specifies whether to show the first threshold line. Data type: Boolean |
| Show Threshold Line2 | Specifies whether to show the second threshold line. Data type: Boolean |
| Threshold Line Color1 | Specifies the color for the first threshold line. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Threshold Line Color2 | Specifies the color for the second threshold line. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Threshold Line Style](https://devnet.logianalytics.com/hc/en-us/articles/4405661845015-Chart-Paper-Properties#ThresholdLineStyle) | Specifies the style for the threshold lines. Choose an option from the drop-down list. Data type: Enumeration |
| Threshold Value1 | Specifies the value for the first threshold line. Data type: Float |
| Threshold Value2 | Specifies the value for the second threshold line. Data type: Float |
| MeanLine | |
| Color | Specifies the color of the mean line. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Node Style | Specifies the style of the nodes that represent the average values. Choose an option from the drop-down list. Data type: Enumeration |
| Show | Specifies whether to show a line that represents the average value of each category group. Not applies to bubble charts. Data type: Boolean |
| Type | Specifies the type of the mean line. Choose an option from the drop-down list. Data type: Enumeration |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) For combo chart, the graph properties will respectively apply to the corresponding chart types.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661866903-KPI-Chart-Label-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661869207-Label-Properties)
