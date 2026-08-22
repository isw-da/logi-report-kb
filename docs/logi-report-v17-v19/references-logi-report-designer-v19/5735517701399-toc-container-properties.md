---
title: "TOC Container Properties"
id: 5735517701399
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735517701399-TOC-Container-Properties
updated_at: 2022-11-02T08:17:34Z
---

# TOC Container Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533827351-Text-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585983511-TOC-Properties)

# TOC Container Properties

When you insert the TOC Page object in a page report tab or web report, Designer automatically creates the TOC Container object in the Report Inspector to represent the table of contents generated via the TOC Page object. You can edit properties of the object to customize the font style, indentation, line spacing, and so on of the entries in the TOC. This topic describes the properties of the TOC Container object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Title | Page Report, Web Report | Specifies the text you want to display as the title of the TOC. Data type: String |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Page Report, Web Report | Specifies the foreground color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Font | | |
| Bold | Page Report, Web Report | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Font Face | Page Report, Web Report | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Italic | Page Report, Web Report | Specifies whether to italicize the text in the object. Data type: Boolean |
| Strikethrough | Page Report, Web Report | Specifies whether to draw a line through the text in the object. Data type: Boolean |
| Underline | Page Report, Web Report | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Others | | |
| Item Indentation | Page Report, Web Report | Specifies the indentation for entries in the TOC. Data type: Float |
| Leader | Page Report, Web Report | Specifies the character that leads each entry and its commencing page number in the TOC. The leader does not display when you set Show Page Numbers to "false". Data type: String |
| Line Spacing | Page Report, Web Report | Specifies the line spacing between two entries in the TOC. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports#Position) | Page Report, Web Report | Shows the position of the TOC in the report. Read only. |
| Show Page Numbers | Page Report, Web Report | Specifies whether to show the commencing page number of the entries in the TOC. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533827351-Text-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735585983511-TOC-Properties)
