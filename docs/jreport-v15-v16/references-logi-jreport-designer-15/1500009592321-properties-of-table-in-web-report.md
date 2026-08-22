---
title: "Properties of Table in Web Report"
id: 1500009592321
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592321-Properties-of-Table-in-Web-Report
updated_at: 2021-07-24T05:53:56Z
---

# Properties of Table in Web Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592301-Properties-of-Special-Field-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570542-Properties-of-Table-Header-in-Web-Report)

# Properties of Table in Web Report

A table may contains the following child objects: [Table Header](https://devnet.logianalytics.com/hc/en-us/articles/1500009570542-Properties-of-Table-Header-in-Web-Report), [Table Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009570502-Properties-of-Table-Group-in-Web-Report), [Table Footer,](https://devnet.logianalytics.com/hc/en-us/articles/1500009570482-Properties-of-Table-Footer-in-Web-Report) [Table Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009570462-Properties-of-Table-Column-in-Web-Report) and [Table Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500009570442-Properties-of-Table-Cell-in-Web-Report).

The properties of a table object in a web report are as follows:

| Property Name | Description |
| --- | --- |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Auto Expands | Specifies whether the objects in cells of the table will expand to their empty neighbouring cells horizontally when the actual size of the objects is bigger than the cells due to no enough column or page width for auto fit. This property requires that the property Auto Fit for the objects in the table cells is set to true. Data type: Boolean  **Note:** The property does not apply to horizontal tables. |
| Default for Filter | Specifies whether to show the data component as the default component in the Apply to drop-down list of the Filter dialog in Web Report Studio. Data type: Boolean  **Note:** In a web report, only one data component’s Default for Filter property can be set to true. |
| Enable Navigation | Specifies whether to enable page navigation on the table. If it is set to true, when the web report is opened in Web Report Studio, if the table contains more than one page, a page navigation bar specific for the table will be available right below it. You can use the bar to view the desired pages. When this property is set to true, you can further specify the height and width of the page for the table to display multiple pages, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). If later Web Report Studio users resize the table, the two properties will be reset to the resized values.  Data type: Boolean |
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
| Invisible for Filter Dialogs | Specifies whether to show the data component in the Apply to drop-down list of the Filter dialog in Web Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| Navigation Height | Specifies the height of the page for the table to display multiple pages. Enter a numeric value to specify the height. If no value is given here, Logi JReport will calculate the table page height at runtime. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| Navigation Width | Specifies the width of the page for the table to display multiple pages. Enter a numeric value to specify the width. If no value is given here, Logi JReport will calculate the table page width at runtime. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Split Overflow Columns | Specifies whether to display the overflow columns of the table on subsequent pages. The table object containing overflow columns on subsequent pages inherits the same Y value in its container, so that it keeps the same number of records as the table in the original page. However, its X value is reset to 0 for both static and absolute positions so as to show as many columns as possible. The height of each table row for overflow columns is the same as the corresponding row height in the original page. Data type: Boolean |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |

**Note:** Only these properties available to the table object in the Inspector panel of Web Report Studio can be rendered in Web Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592301-Properties-of-Special-Field-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570542-Properties-of-Table-Header-in-Web-Report)
