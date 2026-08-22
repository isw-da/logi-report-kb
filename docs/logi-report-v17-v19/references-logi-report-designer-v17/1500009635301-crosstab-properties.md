---
title: "Crosstab Properties"
id: 1500009635301
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009635301-Crosstab-Properties
updated_at: 2021-07-24T16:03:37Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612202-Contents-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612222-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)

# Crosstab Properties

This topic lists the properties of a Crosstab object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Displays the height of the object. This property is read only. |
| Width | Page Report, Web Report, Library Component | Displays the width of the object. This property is read only. |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Alternating Line Color | | |
| Direction | Page Report, Web Report, Library Component | Specifies whether the color defined by the property Pattern List will apply to the fields in the same rows or columns in the crosstab.  * **vertical** - The value of the property Pattern List will take effect on the fields in the same columns, except for the total columns. * **horizontal** - The value of the property Pattern List will take effect on the fields in the same rows, except for the total rows.   Data type: Enumeration |
| Pattern List | Page Report, Web Report, Library Component | Specifies the color patterns for the fields in the same rows or columns in the crosstab. Select Chooser button in the value cell to specify the patterns in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog. Data type: String |
| Show | Page Report, Web Report, Library Component | Specifies whether to enable alternating color for the crosstab. Only when it is set to true, the settings for the properties Direction and Pattern List can take effect. Data type: Boolean  **Note:** The setting of the alternating color can take effect only when all the aggregate fields in the crosstab have transparent background. |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Auto Scale in Number | Page Report, Web Report, Library Component | Specifies whether to automatically scale the values that are of the Number data type in the object when the values fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   Data type: Boolean |
| Cache | Query Page Report | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Current Column Block Index | Query Page Report | Specifies the horizontal index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| Current Row Block Index | Query Page Report | Specifies the vertical index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| Default for Filter | Page Report, Web Report | Specifies whether to show the data component as the default component in the Apply To drop-down list of the Filter dialog in Page/Web Report Studio. Data type: Boolean  **Note:** In the same report, only one data component's Default for Filter property can be set to true. |
| Enable Navigation | Web Report | Specifies whether to enable scrollbars on the crosstab when the parent container cannot fully display the data of the crosstab. When this property is set to true, you can further specify the height and width of the frame for holding the crosstab, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth).  For crosstabs in library components, the Enable Navigation property is invisible but its value is always true.  Data type: Boolean |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to show the data component in the Apply To drop-down list of the Filter dialog in Page/Web Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| Items per Column Block | Query Page Report | Specifies the number of columns of records in each data block. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| Items per Row Block | Query Page Report | Specifies the number of rows of records in each data block. The four properties work together to control the data of the crosstab to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.  Data type: Integer |
| Navigation Height | Web Report, Library Component | Specifies the height of the frame for holding the crosstab. Type a numeric value to specify the height. If no value is given here, Logi Report will calculate the height at runtime. This property takes effect only when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| Navigation Width | Web Report, Library Component | Specifies the width of the frame for holding the crosstab. Type a numeric value to specify the width. If no value is given here, Logi Report will calculate the width at runtime. This property takes effect only when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009613302-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#RecordLocation) | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When Empty | Query Page Report | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Has Border | Page Report, Web Report, Library Component | Specifies whether to show the cell borders. Data type: Boolean |
| Crosstab Property | | |
| Avoid Orphan Header | Query Page Report | Specifies whether to make the column header be together with the data. Sometimes the column header happens to be at the bottom of a page. To keep the column header together with the data in the Next Topic, set this property to true.  Data type: Boolean |
| Block Gap | Query Page Report | Specifies the space between each part if the crosstab is split into more than one part. Data type: Float |
| Boundary Value | Page Report, Web Report, Library Component | Specifies the number of columns in one aggregate cell when the crosstab is displayed horizontally, or rows when displayed vertically. Data type: Integer |
| Column Totals on Left | Page Report, Web Report, Library Component | Specifies whether to display the total columns on the left of the subtotals. Data type: Boolean |
| [Expand Data](#Expand) | Query Page Report | Specifies whether to enable Page Report Studio users to expand/collapse the column/row groups in the crosstab. Data type: Boolean |
| Horizontal Gap | Page Report, Web Report, Library Component | Specifies the space between the left/right edge of a crosstab cell and the contents in it. Data type: Float |
| Outside Aggregate Title | Query Page Report | Specifies to place the summary labels to the left of the row values if true, right of the row values if false. Data type: Boolean |
| [Repeat Aggregate](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Repeat) | Query Page Report | Specifies whether to repeat the crosstab for different aggregate fields. Data type: Boolean |
| Repeat Column Header | Query Page Report | Specifies whether to repeat column headings on every page. Data type: Boolean |
| Row Totals on Top | Page Report, Web Report, Library Component | Specifies whether to display the total rows on the top of the subtotals. Data type: Boolean |
| Suppress Column Header | Page Report, Web Report, Library Component | Specifies whether to suppress the column header in view mode. Data type: Boolean |
| Suppress Row Header | Page Report, Web Report, Library Component | Specifies whether to suppress the row header in view mode. Data type: Boolean |
| Use Table Style | Page Report, Web Report, Library Component | Specifies whether to add headers to the Total rows and columns. Data type: Boolean |
| Vertical Gap | Page Report, Web Report, Library Component | Specifies the space between the top/bottom edge of a crosstab cell and the contents in it. Data type: Float |
| Vertical Layout | Page Report, Web Report, Library Component | Indicates whether the aggregate fields are displayed vertically. The property is read only. |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| Summary | Query Page Report | It is mapped to the HTML attribute *[summary](http://www.w3.org/TR/html401/struct/tables.html#adef-summary)*. This attribute provides a summary of the object's purpose and structure. Data type: String |

## Expand Data, Expand Detail Data

For crosstabs in a page report, if they contain more than one column/row group level, you can specify whether or not to enable expanding and collapsing the column/row groups at runtime, and set the default expanding/collapsing state of groups in the outer level. This behavior is controlled by two properties: Expand Data and Expand Detail Data.

* **Expand Data**: A property on crosstab, and DBFields and formulas added into crosstab as column/row fields. This property on crosstab controls whether or not to enable end users to expand and collapse the column/row groups in the crosstab. When the property on a crosstab is enabled, you can use the property on DBFields and formulas in the crosstab to specify whether the corresponding column/row groups can be expanded and collapsed respectively.
* **Expand Detail Data**: A property on DBFields and formulas added into crosstab as column/row fields. It specifies whether or not to expand the details of specific column/row groups in a crosstab by default.

**Note:** These two properties work only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Mode) and do not apply on the innermost column/row group. After setting the two properties, if you further modify the crosstab layout, they may not take effect.

Suppose you have a crosstab which shows Product Type Name and Category as the column groups, Region, Country and State as the row groups, and displays summaries for Quantity.

1. In the Report Inspector, set the Expand Data property of the crosstab to **true**.
2. Set the Expand Data property of the DBField Country to **false**, and the Expand Detail Data property of the DBField Product Type Name to **false**.
3. Unselect **Page Layout** on the View menu tab to switch to continuous page mode.
4. When the report containing the crosstab is published to Logi Report Server and runs in Page Report Studio, you can select the buttons with a plus or minus sign to expand and collapse the details of the Region and Product Type Name groups. Since Expand Data of Country is false, the details of this group cannot be expanded; Expand Detail Data of Product Type Name is false so the details of this group are not expanded by default.

   ![Expand Crosstab Groups](https://devnet.logianalytics.com/hc/article_attachments/4404911644823/prpty_rpt_crstb.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612202-Contents-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612222-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)
