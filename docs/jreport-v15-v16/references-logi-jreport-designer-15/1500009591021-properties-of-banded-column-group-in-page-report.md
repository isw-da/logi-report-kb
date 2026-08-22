---
title: "Properties of Banded Column Group in Page Report"
id: 1500009591021
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591021-Properties-of-Banded-Column-Group-in-Page-Report
updated_at: 2021-07-24T05:54:17Z
---

# Properties of Banded Column Group in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591061-Properties-of-Banded-Footer-Panel-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591041-Properties-of-Banded-Column-in-Page-Report)

# Properties of Banded Column Group in Page Report

If you open a table-style report created by Logi JReport Designer of a version lower than 8, you may find that the table is actually a banded object, and the columns of the table are organized as a banded column group which may contain one or more columns. The banded column group is displayed as BandedColumnInfos in the Report Inspector by default. A banded column object can have the following child object: [Banded Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009591041-Properties-of-Banded-Column-in-Page-Report).

The properties of a banded column group object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Column Widths | Specifies the column width values. Type the width values delimited by comma. If you want to use the Width property of a column, leave its place blank. Data type: String |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Page Report Result | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Pattern | Specifies the style group for the columns. Data type: String |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. The X and Y properties are ignored. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Show Columns | Specifies the columns to be shown in the report result. Type the column mapping names delimited by comma. For example: Shipping Cost, Ship Date, Ship Via, Payment Received. Data type: String |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Show Border | Specifies whether to show the border. Data type: Boolean |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute [*id*](http://www.w3.org/TR/html401/struct/global.html#adef-id). This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| Language | It is mapped to the HTML attribute [*lang*](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang). This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591061-Properties-of-Banded-Footer-Panel-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591041-Properties-of-Banded-Column-in-Page-Report)
