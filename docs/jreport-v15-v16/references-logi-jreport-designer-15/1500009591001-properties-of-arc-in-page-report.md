---
title: "Properties of Arc in Page Report"
id: 1500009591001
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591001-Properties-of-Arc-in-Page-Report
updated_at: 2021-07-24T05:54:17Z
---

# Properties of Arc in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590981-Properties-for-Objects-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report)

# Properties of Arc in Page Report

The properties of an arc object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Bottom Attach Pos X | Specifies the horizontal coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Bottom Attach Pos Y | Specifies the vertical coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Top Attach Pos X | Specifies the horizontal coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Top Attach Pos Y | Specifies the vertical coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Arc Property | |
| Arc Angle | Specifies the angle of the arc, in degrees. The value ranges from 0 to 360. As it gets closer to 360, the arc begins to take on an elliptical shape. Data type: Float |
| Border Color | Specifies the color of the object's border. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Style | Specifies the line style of the object's border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the object's border. Enter a numeric value to change the thickness. Data type: Float |
| Start Angle | Specifies the start angle of the arc, in degrees. The value ranges from 0 to 360. At 0, the vertex of the arc starts at 12:15 clock position. As it gets closer to 360, the arc travels in a counterclockwise motion. Data type: Float |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

**Note:** When a report is exported to an HTML/RTF/Excel format file, arcs in it cannot be shown. There is no such problem for PDF, PS, and other output formats.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590981-Properties-for-Objects-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report)
