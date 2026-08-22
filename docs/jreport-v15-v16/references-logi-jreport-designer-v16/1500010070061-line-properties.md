---
title: "Line Properties"
id: 1500010070061
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070061-Line-Properties
updated_at: 2021-07-24T10:37:54Z
---

# Line Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070101-Multi-value-Container-Properties)

# Line Properties

This topic lists the properties of a Line object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Bottom Attach Pos X | Page Report, Web Report | Specifies the horizontal coordinate of the bottom (or right when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If the top and bottom end points are exchanged, this property works on the bottom end point after the exchange. Data type: Float |
| Bottom Attach Pos Y | Page Report, Web Report | Specifies the vertical coordinate of the bottom (or right when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If the top and bottom end points are exchanged, this property works on the bottom end point after the exchange. Data type: Float |
| Top Attach Pos X | Page Report, Web Report | Specifies the horizontal coordinate of the top (or left when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If the top and bottom end points are exchanged, this property works on the top end point after the exchange. Data type: Float |
| Top Attach Pos Y | Page Report, Web Report | Specifies the vertical coordinate of the top (or left when the line is horizontal) end point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. If the top and bottom end points are exchanged, this property works on the top end point after the exchange. Data type: Float |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | | |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#RecordLocation) | Page Report, Web Report | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress When No Records | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| [Bottom Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010069701-Box-Properties#Attach) | Page Report, Web Report | Specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| [Bottom Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010069701-Box-Properties#Attach) | Page Report, Web Report | Specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| [Top Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010069701-Box-Properties#Attach) | Page Report, Web Report | Specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| [Top Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010069701-Box-Properties#Attach) | Page Report, Web Report | Specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| Line Property | | |
| Enable Bottom Arrow | Page Report, Web Report | Specifies whether to use an arrow as the bottom (or right when the line is horizontal) end of the line. If the top and bottom ends are exchanged, this property works on the bottom end after the exchange. Data type: Boolean |
| Enable Top Arrow | Page Report, Web Report | Specifies whether to use an arrow as the top (or left when the line is horizontal) end of the line. If the top and bottom ends are exchanged, this property works on the top end after the exchange. Data type: Boolean |
| Line Color | Page Report, Web Report | Specifies the color of the line. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Line Style | Page Report, Web Report | Specifies the style of the line. Choose an option from the drop-down list. Data type: Enumeration |
| Line Thickness | Page Report, Web Report | Specifies the thickness of the line. Enter a numeric value to change the thickness. Data type: Float |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | Query Page Report | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

**Note:** When a report is exported to HTML, the lines in it should be vertical or horizontal lines, otherwise they cannot be shown properly in the HTML result files. You should make sure that Top Attach Pos X = Bottom Attach Pos X or Top Attach Pos Y= Bottom Attach Pos Y. There is no such problem for PDF, PS, RTF and other output formats.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070101-Multi-value-Container-Properties)
