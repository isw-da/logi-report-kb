---
title: "Properties of KPI Chart in Library Component"
id: 1500009590881
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component
updated_at: 2021-07-24T05:54:19Z
---

# Properties of KPI Chart in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569222-Properties-of-KPI-Component-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569242-Properties-of-KPI-Chart-Paper-in-Library-Component)

# Properties of KPI Chart in Library Component

A KPI chart in a library component can have the following child objects: [Chart Paper](https://devnet.logianalytics.com/hc/en-us/articles/1500009569242-Properties-of-KPI-Chart-Paper-in-Library-Component) and Chart Label (the properties of a label in a KPI chart are [the same as those in a normal web report chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009570062-Properties-of-Chart-Label-in-Web-Report)).

The properties of a KPI chart object in a library component are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Alternative Text | Specifies the alternate text of the image, which will be shown when the image cannot be displayed. This property applies only when the chart is exported to HTML as an image chart. Enter a string to serve as the alternative text. Data type: String |
| Export to Applet | Specifies whether to include the object when exporting the library component to Applet. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the library component to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the library component to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the library component to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the library component to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the library component to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the library component to RTF. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| Platform | |
| Anti-aliasing | Specifies whether to make the edges in a chart smooth. Data type: Boolean |
| Minimum Tick Mark Space | Specifies the minimum space between two adjacent tick marks. Enter a numeric value to change the space. Data type: Float |
| Pattern List | Specifies patterns of the data markers. Select More button in the value cell and select the small squares in the color tray one by one to specify the patterns for the data markers. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient. Data type: String |
| Background | |
| Border Color | Specifies the color of the platform border. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Border End Caps](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#EndCaps) | Specifies the ending style of the platform border line. Choose an option from the drop-down list. Data type: Enumeration |
| [Border Joint](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#LineJoint) | Specifies the joint style of the platform border line. Choose an option from the drop-down list. Data type: Enumeration |
| Border Outlined | Specifies whether to show the platform border line in Outline Path. If the property is set to true, the platform border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
| Border Style | Specifies the line style of the platform border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the platform border. Enter a numeric value to change the thickness. Data type: Float |
| Border Transparency | Specifies the transparency of the platform border, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Border Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#BorderType) | Specifies the border type of the platform. Choose an option from the drop-down list. Data type: Enumeration |
| Border Variable Dash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the [Format Platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009587321-Format-Platform-Dialog#Dash) dialog will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the [Format Platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009587321-Format-Platform-Dialog#Dash) dialog will take effect.   Data type: Boolean |
| Color | Specifies the color of the platform background, applied when the property Fill Type is set to color. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Fill Transparency | Specifies the transparency of the platform background, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [Fill Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#FillType) | Specifies the fill pattern for the platform background. Choose an option from the drop-down list. Data type: Enumeration |
| Gradient End Color | Specifies the color of the point where the gradient ends, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient End X | Specifies the horizontal position where the gradient ends, measured in a percentage of the platform width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient End Y | Specifies the vertical position where the gradient ends, measured in a percentage of the platform height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Color | Specifies the color of the point where the gradient begins, applied when the property Fill Type is set to gradient. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Gradient Start X | Specifies the horizontal position where the gradient begins, measured in a percentage of the platform width. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Start Y | Specifies the vertical position where the gradient begins, measured in a percentage of the platform height. Applied when the property Fill Type is set to gradient. Data type: Integer |
| Gradient Style | Specifies the gradient style for the platform background, applied when the property Fill Type is set to gradient. Choose an option from the drop-down list. Data type: Enumeration |
| Image File | Specifies the file name of the image, a portion of which will be displayed as the platform background. Applied when Fill Type is set to image. Enter the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
| Image Height | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property Fill Type is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
| [Image Layout](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#ImageLayout) | Specifies the layout style for the image that will be displayed as the platform background, applied when the property Fill Type is set to image. Choose an option from the drop-down list. Data type: Enumeration |
| Image Width | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property Fill Type is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
| Image X | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property Fill Type is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
| Image Y | The four properties, Image X, Image Y, Image Width, and Image Height, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property Fill Type is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
| Inset Bottom | Specifies the bottom position of the background area, measured in a percentage of the chart height, from the bottom edge of the chart. Data type: Float |
| Inset Left | Specifies the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
| Inset Right | Specifies the right position of the background area, measured in a percentage of the chart width, from the right edge of the chart. Data type: Float |
| Inset Top | Specifies the top position of the background area, measured in a percentage of the chart height, from the top edge of the chart. Data type: Float |
| Radius | Specifies the radius for the joint of the platform border line. The property takes effect only when [Border Joint](#BorderJoint) is set to joint round. Enter a numeric value to change the radius. Data type: Float |
| Texture Background Color | Specifies the background color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Foreground Color | Specifies the foreground color of the texture, applied when the property Fill Type is set to texture. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Texture Style | Specifies the texture style of the platform background, applied when the property Fill Type is set to texture. Choose an option from the drop-down list. Data type: Enumeration |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569222-Properties-of-KPI-Component-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569242-Properties-of-KPI-Chart-Paper-in-Library-Component)
