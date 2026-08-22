---
title: "Rectangle Properties"
id: 9898540409239
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9898540409239-Rectangle-Properties
updated_at: 2022-11-02T04:10:38Z
---

# Rectangle Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898557772823-Org-Node-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540416279-Rectangle-Title-Properties)

# Rectangle Properties

This topic describes the properties of the Rectangle object in a heat map.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Group By | Query Page Report | Shows the group-by field of the object. When this property value is null, the object is grouped based on the whole dataset. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Link | Page Report, Web Report, Library Component | Specifies the target that you want to link the object to, which can be another report, a website, an email address, or a Blob data type field. Select the ellipsis Ellipsis button in the value cell to set the link target. See [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report). Data type: String |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the content in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Separator (for customizing the appearance of the line separating the rectangles) | | |
| Color | Page Report, Web Report, Library Component | Specifies the color of the separator. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Line Style | Page Report, Web Report, Library Component | Specifies the line style of separator. Choose an option from the drop-down list. Data type: Enumeration |
| Thickness | Page Report, Web Report, Library Component | Specifies the width of the separator. Type a numeric value to change the thickness. Data type: Float |
| Transparency | Page Report, Web Report, Library Component | Specifies the transparency of the separator, in percent. Type a numeric value to change the transparency. Data type: Integer |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | | |
| Anchor Display Value | Page Report, Web Report, Library Component | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report, Library Component | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898557772823-Org-Node-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540416279-Rectangle-Title-Properties)
