---
title: "Properties of Banded Object in Page Report"
id: 1500009569342
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report
updated_at: 2021-07-24T05:54:17Z
---

# Properties of Banded Object in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591001-Properties-of-Arc-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591081-Properties-of-Banded-Header-Panel-in-Page-Report)

# Properties of Banded Object in Page Report

A banded object can have the following child objects: [Banded Header Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009591081-Properties-of-Banded-Header-Panel-in-Page-Report), [Banded Page Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009569362-Properties-of-Banded-Page-Panel-in-Page-Report), [Banded Footer Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009591061-Properties-of-Banded-Footer-Panel-in-Page-Report) and [Banded Column Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009591021-Properties-of-Banded-Column-Group-in-Page-Report).

The properties of a banded object in a page report are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Enabled when it is a horizontal banded object. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Enabled when it is a vertical banded object. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways:  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Default for Filter | Specifies whether to show the data component as the default component in the Apply to drop-down list of the Filter dialog in Page Report Studio. Data type: Boolean  **Note:** In a page report tab, only one data component’s Default for Filter property can be set to true. |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to show the data component in the Apply to drop-down list of the Filter dialog in Page Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When Empty | Specifies whether to display the object in the report results when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Column Index](#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Specifies the joint style for the border lines of the object. Choose an option from the drop-down list.   * **miter** - Joins path segments by extending their outside edges until they meet. * **round** - Joins path segments by rounding off the corner at a radius of half the line width.   Data type: Enumeration |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Radius | Specifies the radius for the border line joint of the object. This property takes effect only when [Border Joint](#BorderJoint) is set to round. Data type: Integer |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute [*id*](http://www.w3.org/TR/html401/struct/global.html#adef-id). This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| Language | It is mapped to the HTML attribute [*lang*](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang). This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## Column Index & Row Index

The two properties together provide a way for you to control the position of an object in the exported CSV or Excel file by specifying values to them.

However, Logi JReport has default values for them which is calculated based on the position of each object in the report. You can find the default values of the two properties right after you set the Columned property at the report tab level to true.

To make the specified values take effect when exporting the report to CSV or Excel, the following is necessary for both exporting formats:

* First set the Columned property in report tab level to true, and then specify values to the two properties of the component.

**More requirements for preview as Excel**:

* Make sure that the Export to Excel property of the component is set to true.

**More requirements for Excel exporting**:

* Make sure that the Export to Excel property of the component is set to true.
* When exporting the report to Excel, make sure Column Format is selected in the Export to Excel dialog.

**More requirements for CSV exporting**:

* Make sure that the Export to CSV property of the component is set to true.
* When exporting the report to Text via dialog, do check the Delimited Format option.

**Note:** Preview as Text cannot support the specified values for the default setting of Delimited Format is unchecked and it is unconfigurable.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591001-Properties-of-Arc-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591081-Properties-of-Banded-Header-Panel-in-Page-Report)
