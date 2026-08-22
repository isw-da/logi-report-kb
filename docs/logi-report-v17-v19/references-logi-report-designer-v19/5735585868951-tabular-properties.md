---
title: "Tabular Properties"
id: 5735585868951
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735585868951-Tabular-Properties
updated_at: 2022-11-02T08:18:56Z
---

# Tabular Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898557822615-Table-Group-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735546754199-Tabular-Cell-Properties)

# Tabular Properties

This topic describes the properties of a [Tabular object](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars) that you can use in query-based page reports and web reports.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry | | |
| Height | Query Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Query Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Query Page Report, Web Report | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Query Page Report, Web Report | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | | |
| Background | Query Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Query Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Query Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Auto Scale in Number | Query Page Report, Web Report | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.   Data type: Boolean |
| Export to CSV | Query Page Report, Web Report | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Query Page Report, Web Report | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Query Page Report, Web Report | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Query Page Report, Web Report | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Query Page Report, Web Report | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Query Page Report, Web Report | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Query Page Report, Web Report | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Query Page Report, Web Report | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Query Page Report, Web Report | Specifies whether to include the object in the XML output. Data type: Boolean |
| Horizontal Auto Size | Query Page Report, Web Report | Specifies whether to automatically expand the width of the object according to the size of its content. Data type: Boolean |
| Invisible | Query Page Report, Web Report | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports#Position) | Query Page Report, Web Report | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Query Page Report, Web Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Vertical Auto Size | Query Page Report, Web Report | Specifies whether to automatically expand the height of the object according to the size of its content. Data type: Boolean |
| Excel | | |
| Column Index | Query Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Row Index | Query Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | | |
| Anchor Display Value | Query Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Query Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898557822615-Table-Group-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735546754199-Tabular-Cell-Properties)
