---
title: "Subreport Properties"
id: 1500009635721
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009635721-Subreport-Properties
updated_at: 2021-07-24T16:03:30Z
---

# Subreport Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612722-Special-Field-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612682-Summary-Field-Properties)

# Subreport Properties

This topic lists the properties of a Subreport object, which is supported in page reports.

| Property Name | Description |
| --- | --- |
| General (available for page reports created using query resources) | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | |
| [Cache](#Cache) | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Embedded | If false, the page header and footer of the subreport will not be shown. Data type: Boolean |
| Export to CSV | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Maximum Page Number | Specifies the maximum number of pages in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009612242-Dataset-Properties#DataBuffer). Data type: Integer |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009613302-Editing-Reports#Position) | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#RecordLocation) | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Records per Page | Specifies the number of records in each page in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009612242-Dataset-Properties#DataBuffer). Data type: Integer |
| Subreport Data Source Name | Displays the name of the data source used by the subreport. If nothing is displayed, the default data source will be used. This property is read only. |
| Subreport Query Name | Displays the name of the query used by the subreport. This property is read only. |
| Subreport Security Name | Displays the security name (record level security) used by the subreport. This property is read only. |
| Suppress | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When Empty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | The property is available for page reports created using query resources. It specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [On New Sheet](#Sheet) | Specifies whether to put the subreport in a new sheet in the Excel result of the report. Data type: Boolean |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | The property is available for page reports created using query resources. It specifies the Y coordinate of the object relative to its parent container in the Excel/CSV result of the report, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Sheet Name | Specifies the name of the new sheet in which the subreport will be put in the exported Excel file. Make sure the name specified here isn't used by any other sheets. It is meaningful to specify the property value when [On New Sheet](#OnNewSheet) is set to true.  Data type: String  **Note:** The characters "|", ":", "/", "?", "\", "\*", "]", "[" cannot be displayed in the sheet name in Excel and the last character in the sheet name cannot be single quotation mark ('). If any one of them is used when you specify the property, it will be replaced by "\_" in Excel. |
| Sheet Name Postfix | Specifies how to add postfix number to the sheets in which the subreport will be put in the exported Excel file. Choose an option from the drop-down list.  * **Add postfix number to every page** - Specifies to add the postfix number to every sheet for the subreport (Subreport1, Subreport2, Subreport3, Subreport4...). * **Add postfix number only to additional pages** - Specifies to add the postfix number to the subreport sheets starting from the second one (Subreport, Subreport1, Subreport2, Subreport3...).   It is meaningful to specify the property value when [On New Sheet](#OnNewSheet) is set to true.  Data type: Enumeration |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility (available for page reports created using query resources) | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## Cache

In a report, when the subreport needs to be run more than once, set the property Cache to true. The data of the subreport will be cached in the data buffer. When the subreport is run the next time, the sub-engine will retrieve the data from the data buffer instead of DBMS, and if sublink exists, it will also be calculated in the data buffer, thus improving the engine performance.

When a data buffer is defined in the sub-engine, the data buffer is divided into many pages and records are allocated in the pages. You can use the properties Records per Page and Maximum Page Number to set the number of the records in one page and the maximum number of pages in the data buffer. If enough physical memory is available and you know the total number of records in the subreport, to achieve better performance, you can set Records per Page approximate to the total number of records.

**Note:** The Cache property will not work in the following cases:

* When parameters are used in the subreport.
* When HDS is used by the subreport.
* When dynamic query is used by the subreport.

## On New Sheet

This property is used to specify where the subreport will be put in the Excel result of the report.

* If you want to put the subreport in the same worksheet together with the primary report, set the value to false.
* If you want to put the subreport in a new worksheet in the Excel result, set the property value to true, then specify a name for the new worksheet in the Sheet Name property's value cell.

When On New Sheet is true, in the Excel result file you will find that the primary report is exported into the first worksheet, and there are some links on it. You can select the links to go to the subreport in the second worksheet of the Excel file.

**Note:** If the subreport are cut into several pages, that is to say you have defined some [page settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages) on the subreport, the links in the primary report will be subreport1\_0, subreport1\_1, subreport1\_2, and so on. You can select the link to see the corresponding part you want.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612722-Special-Field-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612682-Summary-Field-Properties)
