---
title: "Parameter Control"
id: 1500009750901
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750901-Parameter-Control
updated_at: 2021-07-25T07:18:45Z
---

# Parameter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750881-Export-Page-Setting-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724002-Parameter-Field)

# Parameter Control

The properties of Parameter Control object are:

| Property Name | Description |
| --- | --- |
| General | |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object, in inches. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object, in inches. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the[Position](#Position)property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Text Format | |
| Auto Scale in Number | The property is available when the parameter added in the object is of the Number data type. It specifies whether to automatically scale the parameter values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   The option "auto" means that the property setting follows that of the object's parent data container.  Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Notes:**   * For the BigDecimal data type, to avoid precision loss, you should type a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property is true, the Format property applies to the integer part of the values after scaled, but if the specified format conflicts with the Auto Scale in Number property, for example, the values are displayed in percentage, then the Auto Scale in Number property is ignored. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border in inches. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Padding | |
| Bottom Padding | Specifies the space between the text of the parameter control and its bottom border. Data type: Float |
| Left Padding | Specifies the space between the text of the parameter control and its left border. Data type: Float |
| Right Padding | Specifies the space between the text of the parameter control and its right border. Data type: Float |
| Top Padding | Specifies the space between the text of the parameter control and its top border. Data type: Float |
| Others | |
| Export as Text | Specifies whether to export the parameter control as text. If this option is unselected, the parameter control will be exported as an image. When Export as Text is enabled, depending on the properties of the parameter bound in the parameter control, Logi Report will export the parameter control as follows:   * The selected values or text of the parameter will be exported as text while the icon or button for specifying the parameter value not exported. * If the parameter in the parameter control is of Boolean type, Report Server displays it as a check box in the parameter control. Then when the check box is selected, it will be exported as Checkmark and if unselected as Checkbox.   Data Type: Boolean |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object in Web Report Studio or when the report is opened in Web Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show or hide the object. All formulas and calculations will still be performed if the property is set to true. You can also [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Formula) whether or not to show the object. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750881-Export-Page-Setting-Object)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724002-Parameter-Field)
