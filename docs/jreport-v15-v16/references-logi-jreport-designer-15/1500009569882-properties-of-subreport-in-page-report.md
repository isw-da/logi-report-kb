---
title: "Properties of Subreport in Page Report"
id: 1500009569882
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569882-Properties-of-Subreport-in-Page-Report
updated_at: 2021-07-24T05:54:06Z
---

# Properties of Subreport in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569862-Properties-of-Special-Field-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591761-Properties-of-Summary-Field-in-Page-Report)

# Properties of Subreport in Page Report

The properties of a subreport object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| [Cache](#Cache) | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Embedded | If false, the page header and footer of the subreport will not be shown. Data type: Boolean |
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
| Maximum Page Number | Specifies the maximum number of pages in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataBuffer). Data type: Integer |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Records per Page | Specifies the number of records in each page in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataBuffer). Data type: Integer |
| Subreport Data Source Name | Displays the name of the data source used by the subreport. If nothing is displayed, the default data source will be used. This property is read only. |
| Subreport Query Name | Displays the name of the query used by the subreport. This property is read only. |
| Subreport Security Name | Displays the security name (record level security) used by the subreport. This property is read only. |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When Empty | Specifies whether to display the object in the report results when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [On New Sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File) | Specifies whether to put the subreport in a new sheet when exporting the report to Excel. Data type: Boolean |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Sheet Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File) | Specifies the name of the new sheet in which the subreport will be put. Make sure the name specified here isn't used by any other sheets. It is meaningful to specify the property value when the On New Sheet property is set to true.  Data type: String  **Note:** The characters "|", ":", "/", "?", "\", "\*", "]", "[" cannot be displayed in the sheet name in Excel and the last character in the sheet name cannot be single quotation mark ('). If any one of them is used when you specify the property, it will be replaced by "\_" in Excel. |
| Sheet Name Postfix | Specifies how to add postfix number to the sheets in which the subreport will be put when exporting the report to Excel. Choose an option from the drop-down list.  * **Add postfix number to every page** - Specifies to add the postfix number to every sheet for the subreport (Subreport1, Subreport2, Subreport3, Subreport4...). * **Add postfix number only to additional pages** - Specifies to add the postfix number to the subreport sheets starting from the second one (Subreport, Subreport1, Subreport2, Subreport3...).   It is meaningful to specify the property value when the On New Sheet property is set to true.  Data type: Enumeration |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## Cache

In a report, when the subreport needs to be run more than once, set the property Cache to true. The data of the subreport will be cached in the data buffer. When the subreport is run the next time, the sub-engine will retrieve the data from the data buffer instead of DBMS, and if sublink exists, it will also be calculated in the data buffer, thus improving the engine performance.

When a data buffer is defined in the sub-engine, the data buffer is divided into many pages and records are allocated in the pages. You can use the properties Records per Page and Maximum Page Number to set the number of the records in one page and the maximum number of pages in the data buffer. If enough physical memory is available and you know the total number of records in the subreport, to achieve better performance, you can set Records per Page approximate to the total number of records.

**Note:** The Cache property will not work in the following cases:

* When the parameter is displayed in the Parameters in subreport tab which is contained in the query of the subreport.
* When HDS is used by the subreport.
* When dynamic query is used by the subreport.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569862-Properties-of-Special-Field-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591761-Properties-of-Summary-Field-in-Page-Report)
