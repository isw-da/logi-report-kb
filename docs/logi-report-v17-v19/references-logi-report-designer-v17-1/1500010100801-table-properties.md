---
title: "Table Properties"
id: 1500010100801
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100801-Table-Properties
updated_at: 2021-07-23T19:16:41Z
---

# Table Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100781-Summary-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062422-Table-Cell-Properties)

# Table Properties

This topic lists the properties of a Table object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Alternating Line Color | | |
| Include Header and Footer | Page Report, Web Report, Library Component | Specifies whether to apply alternating color to the footer, group headers and group footers of the table. By default it is true and all table rows except the table header in the displayed result will use alternating color. When it is false, alternating color will be applied to the table detail rows only. Data type: Boolean |
| Pattern List | Page Report, Web Report, Library Component | Specifies the color pattern of the alternating color for the table rows. Select the ellipsis button Ellipsis button in the value cell to specify the pattern in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box). Data type: String |
| Show | Page Report, Web Report, Library Component | Specifies whether to enable alternating color for the table rows in the displayed report result. Alternating color works as the background color and will overwrite the table rows' own background color. Only when it is set to true, the settings for the properties Include Header and Footer and Pattern List can take effect. Data type: Boolean  Note icon To make alternating color work in merged cells in group tables, you need also set the background color of the merged cells to that of the alternating color. |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Auto Expands | Page Report, Web Report, Library Component | Specifies whether the objects in cells of the table will expand to their empty neighbouring cells horizontally when the actual size of the objects is bigger than the cells due to no enough column or page width for auto fit. This property requires that the property Auto Fit for the objects in the table cells is set to true. Data type: Boolean  Note icon The property does not apply to horizontal tables. |
| Auto Scale in Number | Page Report, Web Report, Library Component | Specifies whether to automatically scale the values that are of the Number data type in the object when the values fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   Data type: Boolean |
| Cache | Query Page Report | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Default for Filter | Page Report, Web Report | Specifies whether to show the data component as the default component in the Apply To drop-down list of the Filter dialog box in Page/Web Report Studio. Data type: Boolean  Note icon In the same report, you can set only one data component's Default for Filter property to true. |
| Enable Navigation | Web Report | Specifies whether to enable page navigation on the table. If it is set to true, when the web report is opened in Web Report Studio, if the table contains more than one page, a page navigation bar specific for the table will be available right below it. You can use the bar to view the desired pages. When this property is set to true, you can further specify the height and width of the page for the table to display multiple pages, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). If later Web Report Studio users resize the table, the two properties will be reset to the resized values.  For tables in library components, the Enable Navigation property is invisible but its value is always true.  Data type: Boolean |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output of the report. Data type: Boolean |
| Horizontal | Query Page Report | Specifies whether to show the table in horizontal style. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to show the data component in the Apply To drop-down list of the Filter dialog box in Page/Web Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| Navigation Height | Web Report, Library Component | Specifies the height of the page for the table to display multiple pages. Type a numeric value to specify the height. If no value is given here, Logi Report will calculate the table page height at runtime. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| Navigation Width | Web Report, Library Component | Specifies the width of the page for the table to display multiple pages. Type a numeric value to specify the width. If no value is given here, Logi Report will calculate the table page width at runtime. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#RecordLocation) | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Split Overflow Columns | Page Report, Web Report, Library Component | Set this property to "true" to display a big table with many columns on multiple pages if one page cannot hold all the columns, instead of cutting the overflow columns off - the default behavior. When the property is "true", the table object containing overflow columns on subsequent pages inherits the same Y value in its container, so that it keeps the same number of records as the table in the original page. However, its X value is reset to 0 for both static and absolute positions so as to show as many columns as possible. The height of each table row for overflow columns is the same as the corresponding row height in the original page.  Data type: Boolean |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress When Empty | Query Page Report | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Page Report, Web Report, Library Component | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report, Web Report, Library Component | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Summary | Query Page Report | It is mapped to the HTML attribute *[summary](http://www.w3.org/TR/html401/struct/tables.html#adef-summary)*. This attribute provides a summary of the object's purpose and structure. Data type: String |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) For the Table object in web reports and library components, only the properties available in the Web Report Studio Inspector panel can be rendered in Web Report Studio and JDashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100781-Summary-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062422-Table-Cell-Properties)
