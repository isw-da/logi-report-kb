---
title: "Subreport Properties"
id: 5735533660951
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735533660951-Subreport-Properties
updated_at: 2022-11-02T08:18:54Z
---

# Subreport Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569369879-Special-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585818519-Summary-Field-Properties)

# Subreport Properties

This topic describes the properties of a [Subreport object](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports) that you can use in page reports only.

| Property Name | Description |
| --- | --- |
| General **(available when the object is in a query-based page report)** | |
| Class Type | Shows the class type of the object. Read only. |
| Data Inherit | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Shows the dataset the object applies. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the [Style Group](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) property for the page report tab and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | |
| Cache | Specifies whether to cache the dataset for this object in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/5735517112983-Dataset-Properties#DataBuffer), so that other objects using the same dataset can share the data rather than perform their own SQL query. Data type: Boolean  When you need to run the subreport in a report more than once, you can set the Cache property to "true". Data of the subreport is then cached in the data buffer, so the next time when you run the subreport, Logi Report Engine retrieves data from the data buffer instead of from database, and if the subreport contains sublinks, Logi Report Engine also calculates them in the data buffer.  Note icon This property does not take effect when the subreport contains parameters, uses HDS, or applies dynamic query. |
| Embedded | When this property is "false" (the default behavior), the page header and footer of the subreport do not display in the report. Data type: Boolean |
| Export to CSV | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Maximum Page Number | Specifies the maximum number of pages for the subreport in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/5735517112983-Dataset-Properties#DataBuffer). Type a numeric value to change the number. Data type: Integer |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports#Position) | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Record Location | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   See [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Records per Page | Specifies the number of records in each page for the subreport in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/5735517112983-Dataset-Properties#DataBuffer). Type a numeric value to change the number. Data type: Integer |
| Subreport Data Source Name | Shows the name of the data source the subreport applies. The property value is blank when the subreport applies the default data source. Read only. |
| Subreport Query Name | Shows the name of the query the subreport uses. Read only. |
| Subreport Security Name | Shows the name of the [data source security entry](https://devnet.logianalytics.com/hc/en-us/articles/5735527007767-Working-with-RLS-and-CLS-at-Data-Source-Scope) the subreport applies. Read only. |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When Empty | Specifies whether to suppress the object in the report when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| Column Index | Designer displays this property when the object is in a query-based page report. You can use it to specify the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Customize Subreport Index Format | Designer enables this property when you set On New Sheet to "true". You can use it to specify whether to enable customizing text format of the subreport links inside the primary report in the Excel output. Data type: Boolean |
| On New Sheet | Specifies whether to put the subreport in separate sheet in the Excel output. Default is to put the subreport in the same sheet together with the primary report. When you set this property to "true", Logi Report Engine exports the subreport in separate sheet and applies the name you specify via the Sheet Name property to the sheet. In the Excel output, the primary report is in the first sheet and there are links in it. You can select any link to go to the corresponding subreport in separate sheet and customize the text format of the links. When the subreport is divided into several pages, that is, you have defined [page settings](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages) in the subreport, the links in the primary report are subreport1\_0, subreport1\_1, subreport1\_2, and so on. You can select the links to view the corresponding part too.  Data type: Boolean  Note icon This property takes effect when you [export the primary report to Excel using Report Format](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel#Format). |
| Row Index | Designer displays this property when the object is in a query-based page report. You can use it to specify the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Sheet Name | Specifies the name of the new sheet in which to put the subreport in the Excel output, when you set On New Sheet to "true". You should make sure no other sheets apply this name. Data type: String  Note icon Excel does not support using the following characters in the sheet name: "|", ":", "/", "?", "\", "\*", "]", "[", and the single quotation mark (') as the last character in the sheet name. If you use any one of them in the value of the property, Excel replaces it by "\_". |
| Sheet Name Postfix | Specifies how to add postfix number to the sheets containing the subreport in the Excel output, when you set On New Sheet to "true". Choose an option from the drop-down list.  * **Add postfix number to every page** Select to add the postfix number to every sheet for the subreport (Subreport1, Subreport2, Subreport3, Subreport4...). * **Add postfix number only to additional pages** Select to add the postfix number to the subreport sheets starting from the second one (Subreport, Subreport1, Subreport2, Subreport3...).   Data type: Enumeration |
| Designer enables the following index properties when you set [Customize Subreport Index Format](#IndexFormat) to "true". | |
| Subreport Index Background | Specifies the background color of the subreport links in the Excel output. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Subreport Index Bold | Specifies whether to apply bold formatting to the subreport links in the Excel output. Data type: Boolean |
| Subreport Index Font Face | Specifies the font face of the subreport index in the Excel output. Choose an option from the drop-down list. Data type: Enumeration |
| Subreport Index Font Size | Specifies the font size of the subreport links in the Excel output. Type an integer value to change the size. Data type: Integer |
| Subreport Index Foreground | Specifies the foreground color of the subreport links in the Excel output. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Subreport Index Italic | Specifies whether to italicize the subreport index in the Excel links. Data type: Boolean |
| Subreport Index Underline | Specifies whether to add a horizontal line under the subreport links in the Excel output. Data type: Boolean |
| Border | |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | |
| Anchor Display Value | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML)**(available when the object is in a query-based page report)** | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569369879-Special-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585818519-Summary-Field-Properties)
