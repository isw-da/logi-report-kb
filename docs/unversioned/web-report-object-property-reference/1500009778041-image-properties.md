---
title: "Image Properties"
id: 1500009778041
section: "Web Report Object Property Reference"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778041-Image-Properties
updated_at: 2021-07-24T00:47:45Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778021-Formula-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778061-KPI-Properties)

# Image Properties

This topic describes the properties of an Image object.

| Property Name | Description |
| --- | --- |
| General | |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object, in inches. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object, in inches. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
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
| Horizontal Alignment | Specifies the horizontal alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Invisible | Specifies whether to show or hide the object. All formulas and calculations will still be performed if the property is set to true. You can also [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Formula) whether to show the object. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Position) | Specifies the position of the object. Available when the object is directly contained in the report body or a tabular cell.  * **absolute** - The object's position will be decided by its X and Y property values. * **static** - The object will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.   Data type: Enumeration |
| Vertical Alignment | Specifies the vertical alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Image Property | |
| Alternate Text | Specifies the text that will be displayed instead if the image cannot be displayed. Data type: String |
| Disabled | Specifies whether to disable the actions on the image. Data type: Boolean |
| Image Name | Specifies the file name of the image. The image can be one on your local file system or retrieved using a URL. Data type: String |
| Maximum Scaling Ratio | Specifies the maximum ratio up to which the image can be scaled. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it. Data type: Float |
| Name | Specifies the name of the image. Data type: String |
| Rotation | Specifies the angle at which to rotate the image, in degrees. The following is the meaning of different values:  * 0 - No rotation. * positive value - Rotates the image clockwise. * negative value - Rotates the image anticlockwise.   Data type: Float |
| Scaling Mode | * **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off. * **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio. * **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio. * **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio. * **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.   When you select fit height, fit image, or fit width, the image scales under the limitation of [Maximum Scaling Ratio](#Ratio).  Data type: Enumeration |
| Title | Specifies the tip information about the image, which will be displayed when you hover the mouse pointer over the image in Web Report result. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778021-Formula-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778061-KPI-Properties)
