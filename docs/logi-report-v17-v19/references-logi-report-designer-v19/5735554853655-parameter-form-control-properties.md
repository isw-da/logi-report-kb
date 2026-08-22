---
title: "Parameter Form Control Properties"
id: 5735554853655
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735554853655-Parameter-Form-Control-Properties
updated_at: 2022-11-02T08:18:50Z
---

# Parameter Form Control Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533553303-Parameter-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585775383-Refresh-Object-Properties)

# Parameter Form Control Properties

This topic describes the properties of a [Parameter Form Control object](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type **W** in the value cell. Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
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
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports#Position) | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Title | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the title. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data type: String |
| Bold | Page Report, Web Report, Library Component | Specifies whether to apply bold formatting to the title. Data type: Boolean |
| Font Face | Page Report, Web Report, Library Component | Specifies the font face of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the title. Type an integer value to change the size. Data type: Integer |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the title. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.  Data type: String |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Page Report, Web Report, Library Component | Specifies whether to italicize the title. Data type: Boolean |
| Show Title | Page Report, Web Report, Library Component | Specifies whether to show the title of the parameter form control. It is meaningful to set all the other title properties when this property is "true". Data type: Boolean |
| Text | Page Report, Web Report, Library Component | Specifies the text you want to display as the title. Type a string to change the text. Data type: String |
| Underline | Page Report, Web Report, Library Component | Specifies whether to add a horizontal line under the title. Data type: Boolean |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab or web report's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true" and the object's [Position](#Position) property is not "static". |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Pattern | | |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** Select if you do not want to apply a pattern to the object. * **50%** Select to fill the object using 50%-transparency of the specified pattern color. * **horizontal** Select to fill the object with horizontal lines using the specified pattern color. * **vertical** Select to fill the object with vertical lines using the specified pattern color. * **grid** Select to fill the object with grids using the specified pattern color. * **diagonal** Select to fill the object with diagonal lines using the specified pattern color.   Data type: String |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533553303-Parameter-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585775383-Refresh-Object-Properties)
