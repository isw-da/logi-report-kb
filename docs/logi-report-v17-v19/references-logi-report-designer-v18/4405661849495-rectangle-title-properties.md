---
title: "Rectangle Title Properties"
id: 4405661849495
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661849495-Rectangle-Title-Properties
updated_at: 2022-01-27T20:36:14Z
---

# Rectangle Title Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661848343-Rectangle-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664652823-Configuration-Properties)

# Rectangle Title Properties

This topic describes the properties of the Rectangle Title object in a heat map.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Reference | Query Page Report | Shows the instance name of the field if the title is related to a field. This property is read only. |
| Text Format | | |
| Bold | Page Report, Web Report, Library Component | Specifies whether to make the text bold. Data type: Boolean |
| Convert HTML Tag | Query Page Report | Specifies whether to parse the HTML tag elements that are included in the text of the object as the web browser translates them into HTML in the report. Data type: Boolean  Note icon   * This property has higher priority than Ignore HTML Tag. * This property does not work when you view or export the report in the Page Report Result or Logi Report Result format. |
| Font Face | Page Report, Web Report, Library Component | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| Format | Page Report, Web Report, Library Component | Indicates the data format depending on the data type of the group field. |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Ignore HTML Tag | Page Report, Web Report, Library Component | Specifies whether to ignore the HTML tag elements that are included in the text of the object at runtime and in HTML output, so they display exactly as what they are. When you set this property to "false", Logi Report Engine transfers the HTML tag elements to the web browser and they are translated into HTML by the web browser. Data type: Boolean |
| Italic | Page Report, Web Report, Library Component | Specifies whether to make the text italic. Data type: Boolean |
| Maximum Width | Query Page Report | Specifies the maximum width of the text displayed. Type a numeric value to change the width. Data type: Float |
| Strikethrough | Page Report, Web Report, Library Component | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Page Report, Web Report, Library Component | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Page Report, Web Report, Library Component | Specifies whether to wrap the text to the width. Data type: Boolean |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Enabled when it is a horizontal banded object. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type **W** in the value cell. Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Excel | | |
| Column Index | Query Page Report | Specifies the X coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab to "true". Data type: Integer |
| Row Index | Query Page Report | Specifies the Y coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab to "true". Data type: Integer |
| Padding | | |
| Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Page Report, Web Report, Library Component | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Page Report, Web Report, Library Component | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | | |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Pattern Style | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** Select if you do not want to apply a pattern to the object. * **50%** Select to fill the object using 50%-transparency of the specified pattern color. * **horizontal** Select to fill the object with horizontal lines using the specified pattern color. * **vertical** Select to fill the object with vertical lines using the specified pattern color. * **grid** Select to fill the object with grids using the specified pattern color. * **diagonal** Select to fill the object with diagonal lines using the specified pattern color.   Data type: String |
| Others | | |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | | |
| Anchor Display Value | Query Page Report | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Query Page Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External AccessKey | Query Page Report | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External Dir | Query Page Report | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * **LTR** - Left-to-right text or table. * **RTL** - Right-to-left text or table.   Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | Query Page Report | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Type an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | Query Page Report | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | Query Page Report | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | Query Page Report | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661848343-Rectangle-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664652823-Configuration-Properties)
