---
title: "Rectangle Properties"
id: 1500010069781
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069781-Rectangle-Properties
updated_at: 2021-07-24T10:37:58Z
---

# Rectangle Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034002-Node-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034022-Rectangle-Title-Properties)

# Rectangle Properties

This topic lists the properties of the Rectangle object in a heat map. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Group By | Query Page Report | Indicates the group-by field related to the rectangle. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | | |
| Link | Page Report, Web Report, Library Component | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports). Data type: String |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Separator | | |
| Color | Page Report, Web Report, Library Component | Specifies the color of the separator line. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Line Style | Page Report, Web Report, Library Component | Specifies the line style of separator. Choose an option from the drop-down list. Data type: Enumeration |
| Thickness | Page Report, Web Report, Library Component | Specifies the line width of the separator. Enter a numeric value to change the thickness. Data type: Float |
| Transparency | Page Report, Web Report, Library Component | Specifies the transparency of separators, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Page Report, Web Report, Library Component | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report, Web Report, Library Component | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034002-Node-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034022-Rectangle-Title-Properties)
