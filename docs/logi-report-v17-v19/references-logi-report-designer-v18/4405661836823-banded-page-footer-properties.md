---
title: "Banded Page Footer Properties"
id: 4405661836823
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661836823-Banded-Page-Footer-Properties
updated_at: 2022-01-27T20:35:30Z
---

# Banded Page Footer Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661835799-Banded-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661839511-Banded-Page-Header-Properties)

# Banded Page Footer Properties

This topic describes the properties of a Banded Page Footer object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. This property is read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color or fill effect of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
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
| Label | Page Report, Web Report | Specifies the tool tip you want to display for the panel when you hover over the left edge of the panel in the design area. Type a string to change the label. Data type: String |
| Record Location | Page Report, Web Report | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   For more information, see [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Show Bottom Line | Query Page Report | Specifies whether to add a horizontal line at the bottom of the panel in the report. Data type: Boolean |
| Suppress | Page Report, Web Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress Blank Panel | Page Report, Web Report | Specifies whether to suppress the panel in the report when it contains no data. Data type: Boolean |
| Suppress on Last Page | Page Report, Web Report | Specifies whether to display the panel on the last page. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Page Report, Web Report | Specifies whether to layer the panel beneath the next panel in the banded object. This property is read only for the banded page footer panel, meaning, the panel cannot be underlaid. Data type: Boolean |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border lines of the object. Choose an option from the drop-down list.  * **miter** Select to join path segments by extending their outside edges until they meet. * **round** Select to join path segments by rounding off the corner at a radius of half the line width.   Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius for the joint of the border lines. This property takes effect when you set Border Joint of the object to "round". Type a numeric value to change the radius. Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661835799-Banded-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661839511-Banded-Page-Header-Properties)
