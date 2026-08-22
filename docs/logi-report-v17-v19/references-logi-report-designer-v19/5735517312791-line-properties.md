---
title: "Line Properties"
id: 5735517312791
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735517312791-Line-Properties
updated_at: 2022-11-02T08:18:40Z
---

# Line Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569072023-Label-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585626007-Multi-Value-Container-Properties)

# Line Properties

This topic describes the properties of a Line object that you can use in page reports and web reports.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry | | |
| Bottom Attach Pos X | Page Report, Web Report | Specifies the horizontal coordinate for the bottom end point of the line (or right end point if the line is horizontal) in the involved banded panel. When you exchange the top and bottom end points, this property applies to the bottom end point after the exchange.  Data type: Float |
| Bottom Attach Pos Y | Page Report, Web Report | Specifies the vertical coordinate for the bottom end point of the line (or right end point if the line is horizontal) in the involved banded panel. When you exchange the top and bottom end points, this property applies to the bottom end point after the exchange.  Data type: Float |
| Top Attach Pos X | Page Report, Web Report | Specifies the horizontal coordinate for the top end point of the line (or left end point if the line is horizontal) in the involved banded panel. When you exchange the top and bottom end points, this property applies to the top end point after the exchange.  Data type: Float |
| Top Attach Pos Y | Page Report, Web Report | Specifies the vertical coordinate for the top end point of the line (or left end point if the line is horizontal) in the involved banded panel. When you exchange the top and bottom end points, this property applies to the top end point after the exchange.  Data type: Float |
| CSS | | |
| Class | Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Record Location | Page Report, Web Report | Specifies the calculation point for the properties of the object that are controlled by formulas. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   See [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Suppress When No Records | Page Report, Web Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| [Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735554341911-Box-Properties#ExcelProperties) | | |
| Bottom Attach Column | Page Report, Web Report | Specifies the X coordinate for the lower right corner of the object in the Excel output, measured in cells. Data type: Float  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true". |
| Bottom Attach Row | Page Report, Web Report | Specifies the Y coordinate for the lower right corner of the object in the Excel output, measured in cells. Data type: Float  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true". |
| Top Attach Column | Page Report, Web Report | Specifies the X coordinate for the upper left corner of the drawing object in the Excel output, measured in cells. Data type: Float  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true". |
| Top Attach Row | Page Report, Web Report | Specifies the Y coordinate for the upper left corner of the drawing object in the Excel output, measured in cells. Data type: Float  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true". |
| Line Property | | |
| Enable Bottom Arrow | Page Report, Web Report | Specifies whether to use an arrow as the bottom end of the line (or right end if the line is horizontal). When you exchange the top and bottom ends, this property applies to the bottom end after the exchange. Data type: Boolean |
| Enable Top Arrow | Page Report, Web Report | Specifies whether to use an arrow as the top end of the line (or left end if the line is horizontal). When you exchange the top and bottom ends, this property applies the top end after the exchange. Data type: Boolean |
| Line Color | Page Report, Web Report | Specifies the color of the line. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Line Style | Page Report, Web Report | Specifies the style of the line. Choose an option from the drop-down list. Data type: Enumeration |
| Line Thickness | Page Report, Web Report | Specifies the width of the line. Type a numeric value to change the thickness. Data type: Float |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Title | Query Page Report | This property is mapped to the HTML attribute *title*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569072023-Label-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585626007-Multi-Value-Container-Properties)
