---
title: "Banded Object Properties"
id: 1500010061722
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties
updated_at: 2021-07-23T19:16:27Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100181-Arc-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100201-Banded-Footer-Properties)

# Banded Object Properties

This topic lists the properties of a Banded Object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Indicates whether the dataset for this object is inherited from another object. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Auto Fit | Page Report, Web Report | Specifies whether to automatically adjust the width of a vertical banded object or the height of a horizontal banded object according to the contents. Data type: Boolean |
| Height | Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Enabled when it is a horizontal banded object. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Enabled when it is a vertical banded object. Data type: Float |
| X | Page Report, Web Report | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report | The property can be used in two ways:  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Auto Scale in Number | Page Report, Web Report | Specifies whether to automatically scale the values that are of the Number data type in the object when the values fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   Data type: Boolean |
| Cache | Page Report, Web Report | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Default for Filter | Page Report, Web Report | Specifies whether to show the data component as the default component in the Apply To drop-down list of the Filter dialog box in Page/Web Report Studio. Data type: Boolean  Note icon In the same report, you can only set one data component's Default for Filter property to true. |
| Enable Navigation | Web Report | Specifies whether to enable scrollbars on the banded object when the parent container cannot fully display the data of the crosstab. When this property is set to true, you can further specify the height and width of the frame for holding the banded object, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth).  Data type: Boolean |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV output of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel output of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text output of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML output of the report. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to show the data component in the Apply To drop-down list of the Filter dialog box in Page/Web Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| Navigation Height | Web Report | Specifies the height of the frame for holding the banded object. Type a numeric value to specify the height. If no value is given here, Logi Report will calculate the height at runtime. This property takes effect only when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| Navigation Width | Web Report | Specifies the width of the frame for holding the banded object. Type a numeric value to specify the width. If no value is given here, Logi Report will calculate the width at runtime. This property takes effect only when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Page Report, Web Report | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#RecordLocation) | Page Report, Web Report | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress When Empty | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| [Column Index](#Index) | Query Page Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](#Index) | Query Page Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border lines of the object. Choose an option from the drop-down list.  * **miter** - Joins path segments by extending their outside edges until they meet. * **round** - Joins path segments by rounding off the corner at a radius of half the line width.   Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius for the border line joint of the object. This property takes effect only when [Border Joint](#BorderJoint) is set to round. Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute [*id*](http://www.w3.org/TR/html401/struct/global.html#adef-id). This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute [*lang*](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang). This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## Column Index & Row Index

The two properties together provide a way for you to control the position of an object in the Excel and CSV outputs of a page report tab or web report.

However, Logi Report has default values for them which are calculated based on the position of each object in the report. You can find the default values of the two properties right after you set the Columned property at the page report tab or web report level to true.

To make the specified values take effect when exporting a page report tab or web report to CSV or Excel, the following is necessary for both export formats:

* First set the Columned property of the page report tab or web report to true, and then specify values to the two properties of the objects in the report.

**More requirements for preview as Excel:**

* Make sure that the Export to Excel property of the objects is set to true.

**More requirements for Excel exporting:**

* Make sure that the Export to Excel property of the objects is set to true.
* When exporting the report to Excel, make sure Column Format is selected in the Export to Excel dialog box.

**More requirements for CSV exporting:**

* Make sure that the Export to CSV property of the object is set to true.
* When exporting the report to Text via dialog box, do select the Delimited Format option.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Preview as Text cannot support the specified values because the default setting of Delimited Format is unselected and it is unconfigurable.

### TOC

Some objects in a report can be set up to show in a table of contents. Then when previewing the report in Logi Report format, exporting it to PDF or HTML, or running it in Page Report Studio for a page report, you can use the TOC tree to locate the objects.

**To show an object in the TOC tree:**

1. Set its TOC Anchor property to **true**.
2. Specify the display value for the anchor by setting the Anchor Display Value property.

Logi Report also enables you to specify [properties of the TOC tree](https://devnet.logianalytics.com/hc/en-us/articles/1500010100961-TOC-Properties), including its CSS style, colors, and fonts as you want.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100181-Arc-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100201-Banded-Footer-Properties)
