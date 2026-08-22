---
title: "Properties of Chart in Page Report"
id: 1500009591181
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591181-Properties-of-Chart-in-Page-Report
updated_at: 2022-01-13T20:14:04Z
---

# Properties of Chart in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591041-Properties-of-Banded-Column-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591201-Properties-of-Box-in-Page-Report)

# Properties of Chart in Page Report

The properties of a box object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Bottom Attach Pos X | Specifies the horizontal coordinate of the bottom right point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Bottom Attach Pos Y | Specifies the vertical coordinate of the bottom right point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Top Attach Pos X | Specifies the horizontal coordinate of the top left point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Top Attach Pos Y | Specifies the vertical coordinate of the top left point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| Bottom Attach Column | The four Excel properties, Top Attach Column, Top Attach Row, Bottom Attach Column and Bottom Attach Row, work together to control the position of a drawing object in the exported Excel file. Bottom Attach Column specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Bottom Attach Row | The four Excel properties, Top Attach Column, Top Attach Row, Bottom Attach Column and Bottom Attach Row, work together to control the position of a drawing object in the exported Excel file. Bottom Attach Row specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Top Attach Column | The four Excel properties, Top Attach Column, Top Attach Row, Bottom Attach Column and Bottom Attach Row, work together to control the position of a drawing object in the exported Excel file. Top Attach Column specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Top Attach Row | The four Excel properties, Top Attach Column, Top Attach Row, Bottom Attach Column and Bottom Attach Row, work together to control the position of a drawing object in the exported Excel file. Top Attach Row specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Box Property | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Style | Specifies the line style of the box border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the object's border. Enter a numeric value to change the thickness. Data type: Float |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591041-Properties-of-Banded-Column-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591201-Properties-of-Box-in-Page-Report)
