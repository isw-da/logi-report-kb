---
title: "Navigation Control"
id: 1500009692162
section: "Navigation Control"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692162-Navigation-Control
updated_at: 2021-11-03T06:56:42Z
---

# Navigation Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692182-Multimedia-Object-OLE-Object-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718461-Navigation-Item)

# Navigation Control

The properties of a navigation control are as follows. A navigation control has a child object: [Navigation Item](https://devnet.logianalytics.com/hc/en-us/articles/1500009718461-Navigation-Item).

| Property Name | Description |
| --- | --- |
| General | |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object, in inches. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object, in inches. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Enter a numeric value to change the position in inches. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the[Position](#Position)property is set to static. Enter a numeric value to change the position in inches. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Others | |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object in Web Report Studio or when the report is opened in Web Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show or hide the object. All formulas and calculations will still be performed if the property is set to true. You can also [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009719201-Making-Simple-Modifications-to-Components#Formula) whether or not to show the object. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009719201-Making-Simple-Modifications-to-Components#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border in inches. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692182-Multimedia-Object-OLE-Object-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718461-Navigation-Item)
