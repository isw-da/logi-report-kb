---
title: "Properties of Chart Legend in Page Report"
id: 1500009569482
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569482-Properties-of-Chart-Legend-in-Page-Report
updated_at: 2021-07-24T05:54:14Z
---

# Properties of Chart Legend in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591261-Properties-of-Heat-Map-Rectangle-Title-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569462-Properties-of-Chart-Label-in-Page-Report)

# Properties of Chart Legend in Page Report

The properties of a chart legend object in a page report are:

| Property | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. This property takes effect only when the [Placement](#Placement) property is set to customized. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. This property takes effect only when the [Placement](#Placement) property is set to customized. Data type: Float |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| Legend | |
| Auto Size | Specifies whether to resize the legend automatically. Data type: Boolean |
| Bottom Margin | Specifies the distance between the legend labels and the bottom border of the legend. Enter a numeric value to change the margin. Data type: Float |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500009589921-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| Label Format Source | Specifies the data format option for the chart legend labels. Choose an option from the drop-down list.  * **Axis Data Format**  - If selected, the data format of the legend labels will follow that of the axis data: if the chart has series axis, the legend label format will be the same as the series axis data format; if not, the category axis data format will be used to the legend labels. * **Legend Data Format** - If selected, the data format of the legend labels will be controlled by the property [Legend Data Format](#LegendDataFormat).   Not available to heat maps that are colored only by summaries.  Data type: Enumeration |
| Label Horizontal Spacing | Specifies the horizontal distance between two adjacent legend labels. Enter a numeric value to change the distance. Not available to heat maps that are colored only by summaries.  Data type: Float |
| Label Vertical Spacing | Specifies the vertical distance between two adjacent legend labels. Enter a numeric value to change the distance. Not available to heat maps that are colored only by summaries.  Data type: Float |
| Left Margin | Specifies the distance between the legend labels and the left border of the legend. Enter a numeric value to change the margin. Data type: Float |
| [Legend Data Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#DataFormat) | Specifies the data format of the legend labels, applied when [Label Format Source](#LabelFormatSource) is set to Legend Data Format. Select  in the value cell to specify the format in the [Data Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009565042-Data-Format-Dialog) dialog. Data type: String |
| Placement | Specifies the position of the legend to be on the left, right, top, bottom of the chart or customized by manually dragging on the chart. Choose an option from the drop-down list. Data type: Enumeration |
| Right Margin | Specifies the distance between the legend labels and the right border of the legend. Enter a numeric value to change the margin. Data type: Float |
| Secondary Placement | Specifies the position of the legend further based on the setting of the property Placement. Choose an option from the drop-down list. Data type: Enumeration |
| Show Scrollbar | Specifies whether to show a scrollbar on the legend to fully view the legend content when the content does not fit into the legend. Data type: Boolean |
| Show Tips | Specifies whether to show the corresponding data information when the mouse pointer points at a target in the chart legend in Designer view mode, in HTML result, or at server runtime. Data type: Boolean |
| Top Margin | Specifies the distance between the legend labels and the top border of the legend. Enter a numeric value to change the margin. Data type: Float |
| Truncate | Specifies whether to truncate the legend entry label text when the text overflow the labels. Data type: Boolean |
| Background | |
| Border Color | Specifies the color of the legend border. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style of the legend border line. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the joint style of the legend border line. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the legend border line in Outline Path. If the property is set to true, the legend border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Specifies the line style of the legend border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the legend border. Enter a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the transparency of the legend border, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#BorderType) | Specifies the border type of the legend. Choose an option from the drop-down list. Data type: Enumeration |
| Border Variable Dash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the [Format Legend](https://devnet.logianalytics.com/hc/en-us/articles/1500009565922-Format-Legend-Dialog-for-Page-Report-#Dash) dialog will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the [Format Legend](https://devnet.logianalytics.com/hc/en-us/articles/1500009565922-Format-Legend-Dialog-for-Page-Report-#Dash) dialog will take effect.   Data type: Boolean |
| Color | Specifies the color of the legend background, applied when the property Fill Type is set to color. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specifies the transparency of the legend background, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Fill Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FillType) | Specifies the fill pattern for the legend background. Choose an option from the drop-down list. Data type: Enumeration |
| Gradient End Color | Specifies the color of the point where the gradient ends, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the legend width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the legend height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the legend width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the legend height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the legend background, applied when the property Fill Type is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Image File | Specifies the file name of the image, a portion of which will be displayed as the legend background. Applied when the property Fill Type is set to image. Enter the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
| Image Height | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property Fill Type is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
| [Image Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#ImageLayout) | Specifies the layout style for the image that will be displayed as the legend background, applied when the property Fill Type is set to image. Choose an option from the drop-down list. Data type: Enumeration |
| Image Width | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property Fill Type is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
| Image X | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property Fill Type is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
| Image Y | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property Fill Type is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
| Inset Bottom | Specifies the bottom position of the background area, measured in a percentage of the legend height, from the bottom edge of the legend. Data type: Float |
| Inset Left | Specifies the left position of the background area, measured in a percentage of the legend width, from the left edge of the legend. Data type: Float |
| Inset Right | Specifies the right position of the background area, measured in a percentage of the legend width, from the right edge of the legend. Data type: Float |
| Inset Top | Specifies the top position of the background area, measured in a percentage of the legend height, from the top edge of the legend. Data type: Float |
| Texture Background Color | Specifies the background color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style of the legend background, applied when the property Fill Type is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Label | |
| Color | Specifies the color of the label, applied when the property Fill Type is set to color. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specifies the transparency of the background, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Fill Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FillType) | Specifies the fill pattern for the label. Choose an option from the drop-down list. Data type: Enumeration |
| [Font Effect](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontEffect) | Specifies the special effect for the label text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Face | Specifies the font face for the legend labels. Choose an option from the drop-down list. Data type: Enumeration |
| Font Rotation | Specifies the rotation angle of each legend label around its center, in degrees. The default value is 0. Enter a numeric value to change the rotation. Data type: Float |
| [Font Script](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontScript) | Specifies whether the label text will in superscript or subscript form, or neither of them. Choose an option from the drop-down list. Data type: Enumeration |
| Font Shearing | Specifies the shearing transformation of each legend label around its center. The default value is 0. Enter a numeric value to change the shearing. Data type: Float |
| Font Size | Specifies the font size for the legend labels. Enter an integer value to change the size. Data type: Integer |
| [Font Strikethrough](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontStrikethrough) | Specifies the style of the line by which the label texts are struck through. Choose an option from the drop-down list. Data type: Enumeration |
| Font Style | Specifies the font style for the legend labels. Choose an option from the drop-down list. Data type: Enumeration |
| [Font Underline](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FontUnderline) | Specifies the underline style for the legend labels. Choose an option from the drop-down list. Data type: Enumeration |
| Gradient End Color | Specifies the color of the point where the gradient ends, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the label text width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the label text height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the label text width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the label text height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the label, applied when the property Fill Type is set to gradient. The image fill type does not apply to the legend label. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Color | Specifies the color for the label text outline. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Outline End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style for the label text outline. Choose an option from the drop-down list. Data type: Enumeration |
| [Outline Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the joint style for the label text outline. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Outlined | Specifies whether to show the label text outline in outline form. If the property is set to true, the outline will be shown in outline form; otherwise, in whole form. Data type: Boolean |
| Outline Style | Specifies the style for the label text outline. Choose an option from the drop-down list. Data type: Enumeration |
| Outline Thickness | Specifies the thickness for the label text outline. Enter a numeric value to change the thickness. Data type: Float |
| Outline Transparency | Specifies the transparency for the label text outline, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Outline Variable Dash | Specifies whether to resize the dash automatically. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
| Percent Format | Specifies the format of the percentage values on the legend. Applied when [Show Percent](#ShowPercent) is set to true. Select  in the value cell to specify the format in the [Data Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009565042-Data-Format-Dialog) dialog. Data type: String |
| Reverse Labels | Specifies whether to reverse the order of the labels in the legend object. Data type: Boolean |
| Show Percent | Specifies whether to show the percentage of each entry value to the total on the legend. Applies to pie, bar and bench charts that have only one value axis. Data type: Boolean |
| Show Values | Specifies whether to show the values for the legend entries. Applies to pie, bar and bench charts that have only one value axis. Data type: Boolean |
| Text of Total Value | Specifies the text of the total value label on the legend. Applies to pie, bar and bench charts that have only one value axis. Data type: String |
| Texture Background Color | Specifies the background color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style for the label, applied when the property Fill Type is set to texture. Choose an option from the drop-down list. Data type: Enumeration |
| Value Format | Specifies the number format of the legend entry values. Applied when [Show Values](#ShowValue) is set to true. Select  in the value cell to specify the format in the [Data Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009565042-Data-Format-Dialog) dialog. Data type: String |
| Word Wrap | Specifies whether to enable the word wrap function for the label text, not applying to radar charts, bubble charts, scatter charts and gauge charts. If the text contains special characters (such as ",", "." and space), it will be broken at the position of one of the special characters. Data type: Boolean |
| Icon | |
| Border Color | Specifies the color of the icon borders. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style of the icon border line. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the joint style of the icon border line. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the icon border line in Outline Path. If the property is set to true, the icon border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Specifies the line style of the icon borders. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the icon borders. Enter a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the transparency of the icon borders, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Border Variable Dash | Specifies whether to resize the dash automatically. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
| Height | Specifies the height of the icon. Enter a numeric value to change the width. Data type: Float |
| Icon Alignment | Specifies the relative position of the icon to the legend. Choose an option from the drop-down list. Data type: Enumeration |
| Icon Text Gap | Specifies the distance between each legend label and icon. Enter a numeric value to change the gap. Data type: Float |
| Width | Specifies the width of the icon. Enter a numeric value to change the width. Data type: Float |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591261-Properties-of-Heat-Map-Rectangle-Title-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569462-Properties-of-Chart-Label-in-Page-Report)
