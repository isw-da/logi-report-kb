---
title: "Table Cell Properties"
id: 4405661897239
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661897239-Table-Cell-Properties
updated_at: 2022-01-27T20:38:06Z
---

# Table Cell Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661892887-Table-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661898263-Table-Column-Properties)

# Table Cell Properties

This topic describes the properties of a Table Cell object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. This property is read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
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
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the content in the cell. Choose an option from the drop-down list.  Data type: Enumeration  Note icon This property does not take effect, when the Position property of the object in the cell is "absolute". |
| Joining Merge | Page Report, Web Report, Library Component | Specifies whether to merge all the sequential rows included in the cell vertically in the report. Data type: Boolean |
| Record Location | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   For more information, see [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Repeat | Page Report, Web Report, Library Component | Specifies whether to repeat the content of the cell on every page of the report, when the cell is split into pages. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the content in the cell. Choose an option from the drop-down list. Data type: Enumeration  Note icon This property does not take effect, when the Position property of the object in the cell is "absolute". |
| Excel | | |
| Merged Cell | Page Report, Web Report, Library Component | Specifies whether the cell is also a merged cell in the Excel output, when it displays with its sequential cells as a merged cell in the report. This property takes effect when you [export the report to Excel using Report Format](https://devnet.logianalytics.com/hc/en-us/articles/4405661753751-Exporting-to-Excel#Format). Data type: Boolean |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| Abbr | Query Page Report | This property is mapped to the HTML attribute *abbr*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Axis | Query Page Report | This property is mapped to the HTML attribute *axis*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Headers | Query Page Report | This property is mapped to the HTML attribute *headers*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Scope | Query Page Report | This property is mapped to the HTML attribute *scope*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Choose an option from the drop-down list to specify the set of data cells for which the current header cell provides header information in the accessible HTML output.  * **none** Select it if you do not want to generate this attribute in the output. * **Column** Select it if you want the current header cell to provide header information for the rest of the column that contains it. * **Row** Select it if you want the current header cell to provide header information for the rest of the row that contains it.   Data type: Enumeration |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) For the Table Cell object in web reports and library components, Logi Report Engine can only render the properties that are available in the Web Report Studio Inspector panel at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661892887-Table-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661898263-Table-Column-Properties)
