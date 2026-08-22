---
title: "Multimedia Object (OLE Object)"
id: 1500009692182
section: "Web Report Object Property Reference"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692182-Multimedia-Object-OLE-Object
updated_at: 2021-11-03T06:56:39Z
---

# Multimedia Object (OLE Object)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692122-Label)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692162-Navigation-Control)

# Multimedia Object (OLE Object)

The properties of a multimedia object which is also called OLE object are:

| Property Name | Description |
| --- | --- |
| General | |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object, in inches. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object, in inches. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Enter a numeric value to change the position in inches. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Enter a numeric value to change the position in inches. Data type: Float |
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
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009719201-Making-Simple-Modifications-to-Components#Position) | Specifies the position of the object. Available when the object is directly contained in the report body or a tabular cell.  * **absolute** - The object's position will be decided by its X and Y property values. * **static** - The object will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.   Data type: Enumeration |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border in inches. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Object Settings | |
| Archive | Specifies the character string that can be used to implement your own archive functionality for the object. Data type: String |
| Class ID | Specifies the class identifier of the object. Data type: String |
| Code Base | Specifies the base path used to resolve relative URIs specified by the Class ID and Archive properties. When null, its default value is the base URI of the current report. Data type: String |
| Value Type | Specifies the MIME (Multipurpose Internet Mail Extensions) type of the object. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692122-Label)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692162-Navigation-Control)
