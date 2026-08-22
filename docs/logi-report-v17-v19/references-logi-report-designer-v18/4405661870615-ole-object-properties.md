---
title: "OLE Object Properties"
id: 4405661870615
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661870615-OLE-Object-Properties
updated_at: 2022-01-27T20:36:15Z
---

# OLE Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664665111-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661877783-Oval-Shape-Properties)

# OLE Object Properties

This topic describes the properties of an OLE Object, that is, a [multimedia object](https://devnet.logianalytics.com/hc/en-us/articles/4405661390743-Working-with-Multimedia-Objects) that you can use in page reports and web reports.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Page Report, Web Report | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Record Location | Page Report, Web Report | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   For more information, see [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Suppress | Query Page Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Query Page Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Object Settings | | |
| Access Key | Page Report, Web Report | Specifies the accelerator key for the object. Data type: String |
| Alternate Text | Page Report, Web Report | Specifies the text you want to show instead when the object cannot display.  Data type: String |
| Archive | Page Report, Web Report | Specifies the character string that can be used to implement your own archive functionality for the object. Data type: String |
| Class ID | Page Report, Web Report | Specifies the class identifier of the object. Data type: String |
| Code Base | Page Report, Web Report | Specifies the base path used to resolve relative URIs specified by the Class ID and Archive properties. Logi Report Engine applies the base URI of the current report when the property value is null. Data type: String |
| Declare | Page Report, Web Report | Specifies whether to make the current object definition a declaration only. The object must be instantiated by a subsequent object definition referring to this declaration. Data type: Boolean |
| Horizontal Space | Page Report, Web Report | Specifies the horizontal margin for the object. Data type: Float |
| Name | Page Report, Web Report | Specifies the name of the object. Data type: String |
| Stand By | Page Report, Web Report | Specifies the message you want to display while the object is being loaded. Data type: String |
| Tab Index | Page Report, Web Report | Specifies the index that defines the tab order for the object. Data type: Integer |
| Title | Page Report, Web Report | Specifies the tool tip information of the object, which displays when you hover over the object in HTML output or at runtime. Data type: String |
| Use Map | Page Report, Web Report | Specifies the URL, often with a bookmark extension (#name), to use as a client-side image map. Data type: String |
| Value Type | Page Report, Web Report | Specifies the MIME (Multipurpose Internet Mail Extensions) type of the object. Data type: String |
| Vertical Space | Page Report, Web Report | Specifies the vertical margin for the object. Data type: Float |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664665111-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661877783-Oval-Shape-Properties)
