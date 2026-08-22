---
title: "Banded Object Properties"
id: 5735532848535
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735532848535-Banded-Object-Properties
updated_at: 2022-11-02T08:15:47Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735516870935-Arc-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557673239-Banded-Detail-Panel-Properties)

# Banded Object Properties

This topic describes the properties of a [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects) that you can use in page reports and web reports.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry | | |
| Auto Fit | Page Report, Web Report | Specifies whether to automatically adjust the width of a vertical banded object or the height of a horizontal banded object according to its content. Data type: Boolean |
| Height | Page Report, Web Report | Designer enables this property for a horizontal banded object. You can use it to specify the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Designer enables this property for a vertical banded object. You can use it to specify the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Auto Scale in Number | Page Report, Web Report | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.   Data type: Boolean |
| Cache | Page Report, Web Report | Specifies whether to cache the dataset for this object in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/5735517112983-Dataset-Properties#DataBuffer), so that other objects using the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Default for Filter | Page Report, Web Report | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean  Note icon In the same report, you can only set one data component's Default for Filter property to "true". |
| Enable Navigation | Web Report | Specifies whether to display scroll bars on the banded object in Web Report Studio, when the parent container cannot fully display its data. When you set this property to "true", you can further specify the height and width of the frame for holding the banded object via [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). Data type: Boolean |
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
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set [Default for Filter](#DFilter) of the object to "true". Data type: Boolean |
| Navigation Height | Web Report | Specifies the height of the frame for holding the banded object, when you set [Enable Navigation](#EnableNavigation) of the object to "true". Type a numeric value to change the height. If you do not specify a value, Logi Report Engine calculates the height at runtime. Data type: Float |
| Navigation Width | Web Report | Specifies the width of the frame for holding the banded object, when you set [Enable Navigation](#EnableNavigation) of the object to "true". Type a numeric value to change the width. If you do not specify a value, Logi Report Engine calculates the width at runtime. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports#Position) | Page Report, Web Report | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Record Location | Page Report, Web Report | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   See [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Suppress | Page Report, Web Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When Empty | Page Report, Web Report | Specifies whether to suppress the object in the report when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color for the border of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border of the object. Choose an option from the drop-down list.  * **miter** Select to join path segments by extending their outside edges until they meet. * **round** Select to join path segments by rounding off the corner at the specified [radius](#Radius).   Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius of the joint, when you set [Border Joint](#BorderJoint) of the object to "round". Type a numeric value to change the radius. Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735516870935-Arc-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557673239-Banded-Detail-Panel-Properties)
