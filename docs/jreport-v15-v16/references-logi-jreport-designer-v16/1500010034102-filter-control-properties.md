---
title: "Filter Control Properties"
id: 1500010034102
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034102-Filter-Control-Properties
updated_at: 2021-07-24T10:37:57Z
---

# Filter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034142-Form-Properties)

# Filter Control Properties

This topic lists the properties of a Filter Control object, which is supported in all the [report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

The following properties of the Filter Control object vary for different report types. The properties also vary for different [filter control types](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Type) (Text List, Single Value Slider and Range Slider) when used in library components.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Control Type | Page Report | Shows the type of the filter control. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Slider | | |
| Font Face | Slider in Library Component | Specifies the font of the tick mark label text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Slider in Library Component | Specifies the font size of the tick mark label text. Enter an integer value to change the size. Data type: Integer |
| [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties#Format) | Slider in Library Component | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Notes:**   * For the BigDecimal data type, to avoid precision loss, you should enter a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with the Auto Scale in Number property, for example the values are displayed in percentage, then the Auto Scale in Number property is ignored. |
| Number Slider Unit Increment | Slider in Library Component | Specifies the increment between two pixels on the slider. Data type: Float |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Selection | Slider in Library Component | Specifies the color of the selected part on the slider bar. This property takes effect only when the type of the filter control is Range Slider. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Slider Bar | Slider in Library Component | Specifies the color of the slider bar. This property takes effect only when the type of the filter control is Range Slider. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | | |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Item Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Item Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Excel | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Border | | |
| Border Color | Page Report, Web Report, Text List in Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Border Thickness | Page Report, Web Report, Text List in Library Component | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Text List in Library Component | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Text List in Library Component | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Text List in Library Component | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Title | | |
| Background | Page Report, Web Report, Text List in Library Component | Specifies the background color of the title bar. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Bold | Page Report, Web Report, Text List in Library Component | Specifies whether to make the text bold in the title bar. Data type: Boolean |
| Font Face | Page Report, Web Report, Text List in Library Component | Specifies the font of the text in the title bar. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Text List in Library Component | Specifies the font size of the text in the title bar. Enter an integer value to change the size. Data type: Integer |
| Foreground | Page Report, Web Report, Text List in Library Component | Specifies the foreground color of the title bar. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Horizontal Alignment | Page Report, Web Report, Text List in Library Component | Specifies the horizontal justification of the text in the title bar. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Page Report, Web Report, Text List in Library Component | Specifies whether to make the text italic in the title bar. Data type: Boolean |
| Map Name | Page Report, Web Report, Text List in Library Component | Specifies whether to use the name of the DBField added to the filter control as the text displayed in the title bar. Data type: Boolean |
| Show Title | Page Report, Web Report, Text List in Library Component | Specifies whether to show the title bar. It is meaningful to set all the other properties in [the Title category](#Title) when this property is set to true. Data type: Boolean |
| Text | Page Report, Web Report, Text List in Library Component | Specifies the text displayed in the title bar. This property can be edited only when [Map Name](#MapName) is set to false. Enter a string to change the text. Data type: String |
| Underline | Page Report, Web Report, Text List in Library Component | Specifies whether to underline the text in the title bar. Data type: Boolean |
| Text Format | | |
| Auto Scale in Number | Page Report, Web Report, Text List in Library Component | The property is available when the field added in the object is of the Number data type. It specifies whether to automatically scale the field values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   The option "auto" means that the property setting follows that of the object's parent data container.  Data type: Boolean |
| Bold | Page Report, Web Report, Text List in Library Component | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Page Report, Web Report, Text List in Library Component | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Text List in Library Component | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties#Format) | Page Report, Web Report, Text List in Library Component | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Notes:**   * For the BigDecimal data type, to avoid precision loss, you should enter a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with the Auto Scale in Number property, for example the values are displayed in percentage, then the Auto Scale in Number property is ignored. |
| Italic | Page Report, Web Report, Text List in Library Component | Specifies whether to make the text italic. Data type: Boolean |
| Underline | Page Report, Web Report, Text List in Library Component | Specifies whether to underline the text. Data type: Boolean |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | Query Page Report | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034142-Form-Properties)
