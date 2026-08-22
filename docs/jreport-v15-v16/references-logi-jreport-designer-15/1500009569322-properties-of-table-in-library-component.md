---
title: "Properties of Table in Library Component"
id: 1500009569322
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569322-Properties-of-Table-in-Library-Component
updated_at: 2021-07-24T05:54:17Z
---

# Properties of Table in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569302-Properties-of-Parameter-Form-Control-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590961-Properties-of-Wrapper-in-Library-Component)

# Properties of Table in Library Component

A table can have some child object. Except for [Table Group](#Group), the properties of other child objects of a table in a library component are the same as those in a web report: [Table Header](https://devnet.logianalytics.com/hc/en-us/articles/1500009570542-Properties-of-Table-Header-in-Web-Report), [Table Group Header](https://devnet.logianalytics.com/hc/en-us/articles/1500009592361-Properties-of-Table-Group-Header-in-Web-Report), [Table Detail](https://devnet.logianalytics.com/hc/en-us/articles/1500009570522-Properties-of-Table-Detail-in-Web-Report), [Table Group Footer](https://devnet.logianalytics.com/hc/en-us/articles/1500009592341-Properties-of-Table-Group-Footer-in-Web-Report), [Table Footer,](https://devnet.logianalytics.com/hc/en-us/articles/1500009570482-Properties-of-Table-Footer-in-Web-Report) [Table Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009570462-Properties-of-Table-Column-in-Web-Report) and [Table Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500009570442-Properties-of-Table-Cell-in-Web-Report).

The properties of a table object in a library component are as follows:

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
| Navigation Height | Specifies the height of the page for the table to display multiple pages. Enter a numeric value to specify the height. If no value is given here, Logi JReport will calculate the table page height at runtime. Data type: Float |
| Navigation Width | Specifies the width of the page for the table to display multiple pages. Enter a numeric value to specify the width. If no value is given here, Logi JReport will calculate the table page width at runtime. Data type: Float |
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

## Table group

The properties of a table group object in a library component are:

| Property Name | Description |
| --- | --- |
| Others | |
| Current Block Index | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Current Block Index specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
| Expand Detail Data | Specifies whether to expand the groups to show the details when the report is opened in JDashboard. Only works in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Data type: Boolean |
| Items per Block | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Item per Block specifies the number of records in each data block.  Data type: Integer |
| Group Layout | |
| Keep Group Together | Specifies whether to keep the whole group together. Data type: Boolean |

**Note:** Only these table properties (including properties of the table child objects) available to the table related objects in the Inspector panel of Web Report Studio can be rendered in JDashboard.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569302-Properties-of-Parameter-Form-Control-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590961-Properties-of-Wrapper-in-Library-Component)
