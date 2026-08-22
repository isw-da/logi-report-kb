---
title: "Round Box Shape Properties"
id: 1500009612642
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612642-Round-Box-Shape-Properties
updated_at: 2021-07-24T16:03:30Z
---

# Round Box Shape Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635681-Report-Body-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612662-Shape-Map-Properties)

# Round Box Shape Properties

This topic lists the properties of a Round Box Shape object, which is supported in page reports only.

| Property Name | Description |
| --- | --- |
| General (only supported on round box shapes in page reports created using query resources) | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Bottom Attach Pos X | Specifies the horizontal coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Bottom Attach Pos Y | Specifies the vertical coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Top Attach Pos X | Specifies the horizontal coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Top Attach Pos Y | Specifies the vertical coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | |
| Export to Excel | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#RecordLocation) | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Bottom Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach) | Specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| [Bottom Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach) | Specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| [Top Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach) | Specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| [Top Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach) | Specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. Data type: Float |
| Round Box Property | |
| Border Color | Specifies the color of the object's border. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Style | Specifies the line style of the object's border. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width of the object's border. Type a numeric value to change the thickness. Data type: Float |
| Corner Factor | Specifies the relative radius of the object's corners. Data type: Float |
| Accessibility (only supported on round box shapes in page reports created using query resources) | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

**Note:** When a report is exported to an HTML or PS format file, round boxes in it cannot be shown. There is no such problem for PDF, RTF and other output formats.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635681-Report-Body-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612662-Shape-Map-Properties)
