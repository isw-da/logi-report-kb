---
title: "Properties of KPI Component in Library Component"
id: 1500009569222
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569222-Properties-of-KPI-Component-in-Library-Component
updated_at: 2021-07-24T05:54:19Z
---

# Properties of KPI Component in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569202-Properties-of-Image-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component)

# Properties of KPI Component in Library Component

A KPI component can have a child object: [KPI Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component).

The properties of a KPI component in a library component are as follows:

| Property Name | Description |
| --- | --- |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color in the [Pick a Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009567042-Pick-a-Color-Dialog#Color) dialog. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color in the [Pick a Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009567042-Pick-a-Color-Dialog#Color) dialog. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Padding | |
| Bottom Padding | Specifies the space between the contents and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the contents and the left border of the object. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the contents and the right border of the object. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the contents and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| Others | |
| Export to Applet | Specifies whether to include the object when exporting the library component to Applet. Data type: Boolean |
| Export to CSV | Specifies whether to include the object when exporting the library component to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the library component to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the library component to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the library component to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the library component to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the library component to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the library component to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the library component to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the library component to XML. Data type: Boolean |
| Horizontal Alignment | Specifies the horizontal justification of the contents in the KPI component. Choose an option from the drop-down list. Data type: Enumeration |
| Invisible | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Vertical Alignment | Specifies the vertical justification of the contents in the KPI component. Choose an option from the drop-down list. Data type: Enumeration |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569202-Properties-of-Image-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590881-Properties-of-KPI-Chart-in-Library-Component)
