---
title: "Properties of Label in Page Report Shape Map"
id: 1500009591561
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591561-Properties-of-Label-in-Page-Report-Shape-Map
updated_at: 2021-07-24T05:54:10Z
---

# Properties of Label in Page Report Shape Map

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591581-Properties-of-Summary-Field-in-Page-Report-Shape-Map)

# Properties of Label in Page Report Shape Map

You can set these properties globally for all the labels in a shape map, or respectively for the label in each specific shape map area, or for the one independently inserted in the shape map object.

The properties of a label object in a shape map of a page report are listed as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Use Global Setting | Specifies whether to apply the settings that you have set globally for all labels in the map to this object.  * **true** - If selected, the object will take the global settings, and all the properties for the object will become read only. * **false**- If selected, the properties for the object can be edited if required.   Data type: Boolean |
| Text Format | |
| [Auto Fit](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#Autofit) | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| [Maximum Width](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#Autofit) | Specifies the maximum width of the text displayed. Enter a numeric value to change the width. This property often works with the Auto Fit property. If Auto Fit = true and Maximum Width is not equal to 0, the text will extend until the width is this value.  Data type: Float |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Text | Specifies the text in the label. Enter a string to display as the label text. Data type: String |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Word Wrap](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#Autofit) | Specifies whether to wrap the text to the width. Data type: Boolean |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the object. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the object. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the object. * **50**% - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: Enumeration |
| Others | |
| Auto Connector | Specifies whether a line between the area and the object will be automatically drawn, when the object is dragged and dropped out of the area. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External Dir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591581-Properties-of-Summary-Field-in-Page-Report-Shape-Map)
