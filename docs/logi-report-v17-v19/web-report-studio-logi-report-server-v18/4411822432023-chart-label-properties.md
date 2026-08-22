---
title: "Chart Label Properties"
id: 4411822432023
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411822432023-Chart-Label-Properties
updated_at: 2022-01-27T07:58:16Z
---

# Chart Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411830862103-Chart-Legend-Properties)

# Chart Label Properties

This topic describes the properties specific to a Chart Label object. For the other properties, see [Setting Web Report Object Properties Using the Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel).

| Property Name | Description |
| --- | --- |
| Label | |
| Bottom Margin | Specify the distance between the label text and the bottom border of the label, in inches. The four properties, Bottom Margin, Left Margin, Right Margin, and Top Margin, work together with the Text Alignment property. Type a numeric value to change the margin. Data type: Float |
| Color | Specify the color of the label text. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Note icon This property applies when you set [Fill Type](#LabelFillType) of the label text to Color.  Data type: String |
| Fill Transparency | Specify the color transparency of the label text, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specify the fill pattern for the label text.  * **None** No fill. The default value. * **Color** Select to fill with a specified color.   Data type: Integer |
| Font Face | Select the font face of the label text. Data type: Enumeration |
| Font Rotation | Specify the rotation angle of the label text around its center, in degrees. The default value is 0. Type a numeric value to change the rotation. Data type: Float |
| Font Size | Specify the font size of the label text. Type an integer value to change the size. Data type: Integer |
| Font Style | Select the font style for the label text. Data type: Enumeration |
| Left Margin | Specify the distance between the label text and the left border of the label, in inches. The four properties, Bottom Margin, Left Margin, Right Margin, and Top Margin, work together with the Text Alignment property. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Specify the distance between the label text and the right border of the label, in inches. The four properties, Bottom Margin, Left Margin, Right Margin, and Top Margin, work together with the Text Alignment property. Type a numeric value to change the margin. Data type: Float |
| Text | Specify the text of the label. Type a string to change the text. Data type: String |
| Text Alignment | Select the alignment style of the label text. It works together with the four properties, Bottom Margin, Left Margin, Right Margin, and Top Margin. Data type: Enumeration |
| Texture Background Color | Specify the background color of the texture. This property does not work on chart labels. Data type: String |
| Top Margin | Specify the distance between the label text and the top border of the label, in inches. The four properties, Bottom Margin, Left Margin, Right Margin, and Top Margin, work together with the Text Alignment property. Type a numeric value to change the margin. Data type: Float |
| Background | |
| Border Color | Specify the color of the label border. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties#EndCaps) | Select the ending style of the label border line. Data type: Enumeration |
| Border Style | Select the line style of the label border. Data type: Enumeration |
| Border Thickness | Specify the width of the label border, in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the label border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties#BorderType) | Select the border type of the label. Data type: Enumeration |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size.  Data type: Boolean |
| Color | Specify the color of the label background. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Note icon This property applies when you set [Fill Type](#BackgroundFillType) of the label background to Color.  Data type: String |
| Fill Transparency | Specify the transparency of the label background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specify the fill pattern for the label background.  * **None** No fill. The default value. * **Color** Select to fill with a specified color. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Inset Bottom | Specify the bottom position of the background area, measured in a percentage of the label height, from the bottom edge of the label. Data type: Float |
| Inset Left | Specify the left position of the background area, measured in a percentage of the label width, from the left edge of the label. Data type: Float |
| Inset Right | Specify the right position of the background area, measured in a percentage of the label width, from the right edge of the label. Data type: Float |
| Inset Top | Specify the top position of the background area, measured in a percentage of the label height, from the top edge of the label. Data type: Float |
| Icon | |
| Border Color | Specify the color of the icon border. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties#EndCaps) | Select the ending style of the icon border line. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties#BorderJoint) | Select the joint style of the icon border line. Data type: Enumeration |
| Border Outlined | Specify whether to show the icon border line in Outline Path. If the property to true, Server displays the icon border line in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Select the line style of the icon border. Data type: Enumeration |
| Border Thickness | Specify the width of the border in inches. Type a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specify the color transparency of the icon border, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Border Variable Dash | Select **true** to adjust the dash size automatically or **false** to use the fixed dash size. Data type: Boolean |
| Color | Specify the color of the icon background. Applied when [Fill Type](#IconFillType) of the icon is set to Color. Select a color from the drop-down list or select **Custom** to define a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String Data type: String |
| Fill Transparency | Specify the transparency of the icon background color, in percent. Type a numeric value to change the transparency. Data type: Integer |
| Fill Type | Specify the fill pattern for the icon.  * **None** No fill. The default value. * **Color** Select to fill with a specified color. * **More Effects** Select to specify either a gradient or an image as the fill effect in the [Fill Effects dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683816983-Fill-Effects-Dialog-Box-Properties).   Data type: Enumeration |
| Height | Specify the height of the icon, in inches. Type a numeric value to change the width. Data type: Float |
| Icon Alignment | Select the relative position of the icon to the label. Data type: Enumeration |
| Icon Style | Select the style of the icon attached to the label. Data type: Enumeration |
| Icon Text Gap | Specify the distance between the icon and the label. Data type: Float |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411830860823-Chart-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411830862103-Chart-Legend-Properties)
