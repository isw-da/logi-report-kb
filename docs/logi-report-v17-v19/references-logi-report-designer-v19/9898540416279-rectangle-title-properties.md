---
title: "Rectangle Title Properties"
id: 9898540416279
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9898540416279-Rectangle-Title-Properties
updated_at: 2022-11-02T08:18:25Z
---

# Rectangle Title Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540409239-Rectangle-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735517073687-Configuration-Properties)

# Rectangle Title Properties

This topic describes the properties of the Rectangle Title object in a heat map.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Reference | Query Page Report | Shows the instance name of the field when the rectangle title is related to a field. Read only. |
| Text Format | | |
| Bold | Page Report, Web Report, Library Component | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Convert HTML Tag | Query Page Report | Specifies whether to parse the HTML tag elements that are included in the text of the object as the web browser translates them into HTML in the report. Data type: Boolean  Note icon   * This property has higher priority than the Ignore HTML Tag property. * This property does not work when you view or export the report in the Page Report Result or Logi Report Result format. |
| Font Face | Page Report, Web Report, Library Component | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Page Report, Web Report, Library Component | Specifies the format in which you want to display group values in the rectangle title. Choose an option from the drop-down list or type the format by yourself. Data type: String |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Ignore HTML Tag | Page Report, Web Report, Library Component | Specifies whether to ignore the HTML tag elements that are included in the text of the object at runtime and in HTML output, so they display exactly as what they are. When you set this property to "false", Logi Report Engine transfers the HTML tag elements to the web browser and they are translated into HTML by the web browser. Data type: Boolean |
| Italic | Page Report, Web Report, Library Component | Specifies whether to italicize the text in the object. Data type: Boolean |
| Maximum Width | Query Page Report | Specifies the maximum width of the text you want to display in the object. Type a numeric value to change the width. Data type: Float |
| Strikethrough | Page Report, Web Report, Library Component | Specifies whether to draw a line through the text in the object. Data type: Boolean |
| Underline | Page Report, Web Report, Library Component | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Page Report, Web Report, Library Component | Specifies whether to wrap the text according to the width of the object. Data type: Boolean |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type **W** in the value cell. Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Excel | | |
| Column Index | Query Page Report | Specifies the X coordinate of the object relative to its parent container in the Excel output, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true". |
| Row Index | Query Page Report | Specifies the Y coordinate of the object relative to its parent container in the Excel output, measured in cells. Data type: Integer  Note icon This property takes effect when you set the page report tab's [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property to "true". |
| Padding | | |
| Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report, Library Component | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report, Library Component | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report, Library Component | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Shadow | Page Report, Web Report, Library Component | Specifies whether to add a drop shadow effect to the border. Data type: Boolean |
| Shadow Color | Page Report, Web Report, Library Component | Specifies the color of the border shadow. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Pattern | | |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** Select if you do not want to apply a pattern to the object. * **50%** Select to fill the object using 50%-transparency of the specified pattern color. * **horizontal** Select to fill the object with horizontal lines using the specified pattern color. * **vertical** Select to fill the object with vertical lines using the specified pattern color. * **grid** Select to fill the object with grids using the specified pattern color. * **diagonal** Select to fill the object with diagonal lines using the specified pattern color.   Data type: String |
| Others | | |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | | |
| Anchor Display Value | Query Page Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Query Page Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External AccessKey | Query Page Report | This property is mapped to the HTML attribute *accesskey*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External Dir | Query Page Report | This property is mapped to the HTML attribute *dir*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External TabIndex | Query Page Report | This property is mapped to the HTML attribute *tabindex*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: Integer |
| External Title | Query Page Report | This property is mapped to the HTML attribute *title*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| HrefLang | Query Page Report | This property is mapped to the HTML attribute *hreflang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). You can use it to specify the base language of the resource designated by a link on the object, such as the target you define via the [Link](#Link) property. Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| LongDesc | Query Page Report | This property is mapped to the HTML attribute *longdesc*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540409239-Rectangle-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735517073687-Configuration-Properties)
