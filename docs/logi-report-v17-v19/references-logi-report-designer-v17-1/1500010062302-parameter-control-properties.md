---
title: "Parameter Control Properties"
id: 1500010062302
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062302-Parameter-Control-Properties
updated_at: 2021-07-23T19:16:39Z
---

# Parameter Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100721-Parameter-Field-Properties)

# Parameter Control Properties

This topic lists the properties of a Parameter Control object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Excel | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Border | | |
| Border Color | Query Page Report, Web Report, Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Border Thickness | Query Page Report, Web Report, Library Component | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Query Page Report, Web Report, Library Component | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Query Page Report, Web Report, Library Component | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Query Page Report, Web Report, Library Component | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Query Page Report, Web Report, Library Component | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Query Page Report, Web Report, Library Component | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Top Line | Query Page Report, Web Report, Library Component | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | | |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#PatternStyle) | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | | |
| Auto Scale in Number | Page Report, Web Report, Library Component | The property is available when the parameter added in the object is of the Number data type. It specifies whether to automatically scale the parameter values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   The option "auto" means that the property setting follows that of the object's parent data container.  Data type: Boolean |
| Bold | Page Report, Web Report, Library Component | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Page Report, Web Report, Library Component | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#Format) | Page Report, Web Report, Library Component | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  Note icon   * For the BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with the Auto Scale in Number property, for example the values are displayed in percentage, then the Auto Scale in Number property is ignored. |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Page Report, Web Report, Library Component | Specifies whether to make the text italic. Data type: Boolean |
| Underline | Page Report, Web Report, Library Component | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Others | | |
| Export as Text | Page Report, Web Report, Library Component | Specifies whether to export the parameter control as text. If this option is unselected, the parameter control will be exported as an image. When Export as Text is enabled, depending on the properties of the parameter bound in the parameter control, Logi Report will export the parameter control as follows:   * The selected values or text of the parameter will be exported as text while the icon or button for specifying the parameter value not exported. * If the parameter in the parameter control is of Boolean type, it is displayed as a checkbox in the parameter control, then when the checkbox is selected, it will be exported as Checkmark and if unselected as Checkbox.   Data Type: Boolean |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output of the report. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Parameter | Page Report, Web Report, Library Component | Specifies the value of the parameter. Data type: String |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | Query Page Report | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| Tag Name | Page Report, Web Report, Library Component | It specifies the header tag name of the object used for labeling the heading order of the object in the PDF output for accessibility.  When setting the property, you should make sure that the headers are nested properly following the rules below so that the heading tag sequence can be accepted by Adobe.   * If any heading tags are used, H1 should be the first. * The descending sequence of the headers should follow the downward order of the objects in the Report Inspector. * The descending sequence of the headers should proceed in strict numerical order and should not skip an intervening heading level. *H1 H2 H3* is permissible, while *H1 H3* is not.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100721-Parameter-Field-Properties)
