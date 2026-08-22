---
title: "Filter Control Properties"
id: 4405661853847
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661853847-Filter-Control-Properties
updated_at: 2022-01-27T20:35:51Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661852055-DBField-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661855895-Form-Properties)

# Filter Control Properties

This topic describes the properties of a [Filter Control object](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Filter).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). The properties of the object also vary for different [filter control types](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Type) (Text List, Drop-down List, Single Value Slider, and Range Slider) when you use it in library components. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Control Type | Page Report | Shows the type of the filter control. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Slider | | |
| Font Face | Slider in Library Component | Specifies the font face of the tick mark label text on the slider. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Slider in Library Component | Specifies the font size of the tick mark label text on the slider. Type an integer value to change the size. Data type: Integer |
| Format | Slider in Library Component | Specifies the format in which you want to display values of the object in the report. Choose an option from the drop-down list or type the format by yourself. Data type: String  Note icon If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. |
| Number Slider Unit Increment | Slider in Library Component | Specifies the increment between two pixels on the slider. Data type: Float |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Selection | Slider in Library Component | Specifies the color for the selected part on the slider bar. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String  Note icon This property takes effect only when the type of the filter control is Range Slider. |
| Slider Bar | Slider in Library Component | Specifies the color of the slider bar. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String  Note icon This property takes effect only when the type of the filter control is Range Slider. |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type **W** in the value cell. Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Item Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Item Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Border | | |
| Border Color | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Title (the properties of this group take effect for the Text List filter control type only) | | |
| Background | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the background color of the title. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Bold | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies whether to apply bold formatting to the title. Data type: Boolean |
| Font Face | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the font face of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the font size of the title. Type an integer value to change the size. Data type: Integer |
| Foreground | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the foreground color of the title. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Horizontal Alignment | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the horizontal justification of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies whether to italicize the title. Data type: Boolean |
| Map Name | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies whether to display the name of the DBField that you add to the filter control as its title. If you add more than one DBField to the filter control, Designer applies the name of the first displayed field you select in the field list as the title. Data type: Boolean |
| Show Title | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies whether to show the title of the filter control. It is meaningful to set all the other title properties when this property is "true". Data type: Boolean |
| Text | Page Report, Web Report, Text List and Drop-down List in Library Component | Designer enables this property when you set [Map Name](#MapName) to "false". You can use it to specify the text you want to display as the title. Type a string to change the text. Data type: String |
| Underline | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies whether to add a horizontal line under the title. Data type: Boolean |
| Text Format | | |
| Auto Scale in Number | Page Report, Web Report, Text List in Library Component | Designer displays this property when the fields bound with the object are Number data type. You can use it to specify whether to automatically scale the Number values that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   The option "auto" means that the property setting follows that of the object's parent data component.  Data type: Boolean |
| Bold | Page Report, Web Report, Text List in Library Component | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Font Face | Page Report, Web Report, Text List in Library Component | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Text List in Library Component | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Page Report, Web Report, Text List in Library Component | Specifies the format in which you want to display values of the object in the report. Choose an option from the drop-down list or type the format by yourself. Data type: String  Note icon   * If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. * If the object is Number data type and you set its Auto Scale in Number property to "true", Logi Report Engine applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the Auto Scale in Number property (for example, the values display in percentage), Logi Report Engine ignores the Auto Scale in Number property. |
| Italic | Page Report, Web Report, Text List in Library Component | Specifies whether to italicize the text in the object. Data type: Boolean |
| Underline | Page Report, Web Report, Text List in Library Component | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Title | Query Page Report | This property is mapped to the HTML attribute *title*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661852055-DBField-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661855895-Form-Properties)
