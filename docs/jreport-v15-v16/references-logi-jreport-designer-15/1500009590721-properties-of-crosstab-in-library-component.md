---
title: "Properties of Crosstab in Library Component"
id: 1500009590721
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590721-Properties-of-Crosstab-in-Library-Component
updated_at: 2021-07-24T05:54:21Z
---

# Properties of Crosstab in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590801-Properties-of-Page-Panel-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590821-Properties-of-DBField-in-Library-Component)

# Properties of Crosstab in Library Component

The same as in a web report crosstab, the [DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500009570142-Properties-of-DBField-in-Web-Report-Crosstab), [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009592041-Properties-of-Formula-Field-in-Web-Report-Crosstab) and [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009592061-Properties-of-Label-in-Web-Report-Crosstab) in a library component crosstab have different properties compared with in other library component containers.

The properties of a crosstab object in a library component are as follows:

| Property Name | Description |
| --- | --- |
| Geometry | |
| Height | Displays the height of the object. This property is read only. |
| Width | Displays the width of the object. This property is read only. |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Alternating Line Color | |
| Direction | Specifies whether the color defined by the property Pattern List will apply to the fields in the same rows or columns in the crosstab.  * **vertical** - The value of the property Pattern List will take effect on the fields in the same columns, except for the total columns. * **horizontal** - The value of the property Pattern List will take effect on the fields in the same rows, except for the total rows.   Data type: Enumeration |
| Enable | Specifies whether to enable setting alternating line color for the crosstab. Only when it is set to true, the settings for the properties Direction and Pattern List can take effect. Data type: Boolean  **Note:** The setting of the alternating line color function for crosstab can only take effect when all the aggregate fields in the crosstab have transparent background. |
| Pattern List | Specifies the color pattern for the fields in the same rows or columns in the crosstab. Select  in the value cell and select the small squares in the color tray one by one to specify the patterns. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
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
| Navigation Height | Specifies the height of the frame for holding the crosstab. Enter a numeric value to specify the height. If no value is given here, Logi JReport will calculate the height at runtime. Data type: Float |
| Navigation Width | Specifies the width of the frame for holding the crosstab. Enter a numeric value to specify the width. If no value is given here, Logi JReport will calculate the width at runtime. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Has Border | Specifies whether to show the cell borders. Data type: Boolean |
| Crosstab Property | |
| Boundary Value | Specifies the number of columns in one aggregate cell when the crosstab is displayed horizontally, or rows when displayed vertically. Data type: Integer |
| Column Totals on Left | Specifies whether to display the total columns on the left of the aggregates. Data type: Boolean |
| Horizontal Gap | Specifies the space between the left/right edge of a crosstab cell and the contents in it. Data type: Float |
| Row Totals on Top | Specifies whether to display the total rows on the top of the aggregates. Data type: Boolean |
| Suppress Column Header | Specifies whether to suppress the column header in view mode. Data type: Boolean |
| Suppress Row Header | Specifies whether to suppress the row header in view mode. Data type: Boolean |
| Use Table Style | Specifies whether to add headers to the Total rows and columns. Data type: Boolean |
| Vertical Gap | Specifies the space between the top/bottom edge of a crosstab cell and the contents in it. Data type: Float |
| Vertical Layout | Indicates whether the aggregate fields are displayed vertically. The property is read only. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590801-Properties-of-Page-Panel-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590821-Properties-of-DBField-in-Library-Component)
