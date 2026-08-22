---
title: "Body Properties"
id: 4405661841175
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661841175-Body-Properties
updated_at: 2022-01-27T20:38:05Z
---

# Body Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661838487-Group-Header-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661842327-Box-Properties)

# Body Properties

This topic describes the properties of the Body object in a library component.

The Body object in library components resembles the Report Body object in page reports and web reports. It works as a flow layout container to hold the components in a library component.

| Property Name | Description |
| --- | --- |
| Border | |
| Bottom Border Color | Shows the color for the bottom border of the object. This property is read only. Data type: String |
| Bottom Border Thickness | Shows the thickness for the bottom border of the object. This property is read only. Data type: Float |
| Bottom Line | Shows the line style for the bottom border of the object. This property is read only. Data type: Enumeration |
| Left Border Color | Shows the color for the left border of the object. This property is read only. Data type: String |
| Left Border Thickness | Shows the thickness for the left border of the object. This property is read only. Data type: Float |
| Left Line | Shows the line style for the left border of the object. This property is read only. Data type: Enumeration |
| Right Border Color | Shows the color for the right border of the object. This property is read only. Data type: String |
| Right Border Thickness | Shows the thickness for the right border of the object. This property is read only. Data type: Float |
| Right Line | Shows the line style for the right border of the object. This property is read only. Data type: Enumeration |
| Top Border Color | Shows the color for the top border of the object. This property is read only. Data type: String |
| Top Border Thickness | Shows the thickness for the top border of the object. This property is read only. Data type: Float |
| Top Line | Shows the line style for the top border of the object. This property is read only. Data type: Enumeration |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Padding | |
| Bottom Padding | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Margin | |
| Bottom Margin | Specifies the distance between the object and the bottom border of the library component contents. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Specifies the distance between the object and the left border of the library component contents. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Specifies the distance between the object and the right border of the library component contents. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Specifies the distance between the object and the top border of the library component contents. Type a numeric value to change the margin. Data type: Float |
| Others | |
| Auto Scale in Number | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661838487-Group-Header-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661842327-Box-Properties)
