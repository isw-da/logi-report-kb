---
title: "Properties of Table Cell in Page Report"
id: 1500009591801
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591801-Properties-of-Table-Cell-in-Page-Report
updated_at: 2021-07-24T05:54:06Z
---

# Properties of Table Cell in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569902-Properties-of-Table-Column-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591881-Properties-of-Tabular-in-Page-Report)

# Properties of Table Cell in Page Report

The properties of a table cell object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
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
| Horizontal Alignment | Specifies the horizontal justification of the content in the table cell. Choose an option from the drop-down list. Data type: Enumeration  **Note:** When the Position property of the object in the table cell is set to absolute, this property does not take effect. |
| Joining Merge | Specifies whether to make all the sequential rows included in the cell vertically merged in the report results. It is meaningful to set the property only when the cell is merged with other cells in the same column. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Repeat | Specifies whether to repeat the content of the cell in every page of the report results when the cell is split into pages. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the content in the table cell. Choose an option from the drop-down list. Data type: Enumeration  **Note:** When the Position property of the object in the table cell is set to absolute, this property does not take effect. |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Accessibility | |
| Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
| Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
| Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569902-Properties-of-Table-Column-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591881-Properties-of-Tabular-in-Page-Report)
