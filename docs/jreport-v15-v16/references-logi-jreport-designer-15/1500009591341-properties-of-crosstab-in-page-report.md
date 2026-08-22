---
title: "Properties of Crosstab in Page Report"
id: 1500009591341
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591341-Properties-of-Crosstab-in-Page-Report
updated_at: 2021-07-24T05:54:13Z
---

# Properties of Crosstab in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591361-Properties-of-Column-Row-Compound-Group-and-Summary-Area)

# Properties of Crosstab in Page Report

A crosstab can have the following child objects: [Column Compound Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009591361-Properties-of-Column-Row-Compound-Group-and-Summary-Area), [Row Compound Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009591361-Properties-of-Column-Row-Compound-Group-and-Summary-Area) and [Summary Area](https://devnet.logianalytics.com/hc/en-us/articles/1500009591361-Properties-of-Column-Row-Compound-Group-and-Summary-Area), the properties of which are all the same.

The properties of a crosstab object in a page report are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Displays the height of the object. This property is read only. |
| Width | Displays the width of the object. This property is read only. |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Alternating Line Color | |
| Direction | Specifies whether the color defined by the property Pattern List will apply to the fields in the same rows or columns in the crosstab.  * **vertical** - The value of the property Pattern List will take effect on the fields in the same columns, except for the total columns. * **horizontal** - The value of the property Pattern List will take effect on the fields in the same rows, except for the total rows.   Data type: Enumeration |
| Enable | Specifies whether to enable setting alternating line color for the crosstab. Only when it is set to true, the settings for the properties Direction and Pattern List can take effect. Data type: Boolean  **Note:** The setting of the alternating line color function for crosstab can only take effect when all the aggregate fields in the crosstab have transparent background. |
| Pattern List | Specifies the color pattern for the fields in the same rows or columns in the crosstab. Select  in the value cell and select the small squares in the color tray one by one to specify the patterns. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Current Column Block Index | Specifies the horizontal index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| Current Row Block Index | Specifies the vertical index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
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
| Items per Column Block | Specifies the number of columns of records in each data block. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| Items per Row Block | Specifies the number of rows of records in each data block. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When Empty | Specifies whether to display the object in the report results when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Has Border | Specifies whether to show the cell borders. Data type: Boolean |
| Crosstab Property | |
| Avoid Orphan Header | Specifies whether to make the column header be together with the data. Sometimes the column header happens to be at the bottom of a page. To keep the column header together with the data in the next page, set this property to true.  Data type: Boolean |
| Block Gap | Specifies the space between each part if the crosstab is split into more than one part. Data type: Float |
| Boundary Value | Specifies the number of columns in one aggregate cell when the crosstab is displayed horizontally, or rows when displayed vertically. Data type: Integer |
| Column Totals on Left | Specifies whether to display the total columns on the left of the aggregates. Data type: Boolean |
| [Expand Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab) | Specifies whether to enable Page Report Studio users to expand/collapse dimensions in the crosstab. This property works only in [continuous page mode.](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode) Data type: Boolean |
| Horizontal Gap | Specifies the space between the left/right edge of a crosstab cell and the contents in it. Data type: Float |
| Outside Aggregate Title | Specifies to place the summary labels to the left of the row values if true, right of the row values if false. Data type: Boolean |
| [Repeat Aggregate](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout#Repeat) | Specifies whether to repeat the crosstab for different aggregate fields. Data type: Boolean |
| Repeat Column Header | Specifies whether to repeat column headings on every page. Data type: Boolean |
| Row Totals on Top | Specifies whether to display the total rows on the top of the aggregates.  Data type: Boolean |
| Suppress Column Header | Specifies whether to suppress the column header in view mode. Data type: Boolean |
| Suppress Row Header | Specifies whether to suppress the row header in view mode. Data type: Boolean |
| Use Table Style | Specifies whether to add headers to the Total rows and columns. Data type: Boolean |
| Vertical Gap | Specifies the space between the top/bottom edge of a crosstab cell and the contents in it. Data type: Float |
| Vertical Layout | Indicates whether the aggregate fields are displayed vertically. The property is read only. |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| Summary | It is mapped to the HTML attribute *[summary](http://www.w3.org/TR/html401/struct/tables.html#adef-summary)*. This attribute provides a summary of the object's purpose and structure. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591361-Properties-of-Column-Row-Compound-Group-and-Summary-Area)
