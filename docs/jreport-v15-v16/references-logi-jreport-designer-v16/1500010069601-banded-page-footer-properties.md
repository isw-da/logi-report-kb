---
title: "Banded Page Footer Properties"
id: 1500010069601
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069601-Banded-Page-Footer-Properties
updated_at: 2021-07-24T10:38:00Z
---

# Banded Page Footer Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069581-Banded-Page-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties)

# Banded Page Footer Properties

This topic lists the properties of a Banded Page Footer object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color and fill effect of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | | |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Label | Page Report, Web Report | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#RecordLocation) | Page Report, Web Report | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Show Bottom Line | Query Page Report | Specifies whether to include a horizontal line at the bottom of the panel. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
| Suppress | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress Blank Panel | Page Report, Web Report | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress on Last Page | Page Report, Web Report | If true, the footer panel on the last page will not be displayed. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Page Report, Web Report | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border lines of the object. Choose an option from the drop-down list.  * **miter** - Joins path segments by extending their outside edges until they meet. * **round** - Joins path segments by rounding off the corner at a radius of half the line width.   Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius for the border line joint of the object. This property takes effect only when [Border Joint](#BorderJoint) is set to round. Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069581-Banded-Page-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties)
