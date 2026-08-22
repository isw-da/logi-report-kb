---
title: "Crosstab Properties"
id: 4405664654871
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664654871-Crosstab-Properties
updated_at: 2022-01-27T20:38:10Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664653847-Contents-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664655767-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)

# Crosstab Properties

This topic describes the properties of a [Crosstab object](https://devnet.logianalytics.com/hc/en-us/articles/4405664392727-Working-with-Crosstabs).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. This property is read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Displays the height of the object. This property is read only. |
| Width | Page Report, Web Report, Library Component | Displays the width of the object. This property is read only. |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Alternating Line Color | | |
| Direction | Page Report, Web Report, Library Component | Specifies the direction to apply alternating color in the crosstab.  * **vertical** - Select to apply the alternating color to columns (excluding the total columns). * **horizontal** - Select to apply the alternating color to rows (excluding the total rows).   Data type: Enumeration |
| Pattern List | Page Report, Web Report, Library Component | Specifies the patterns for the alternating color you want to apply to the crosstab. Select the ellipsis Ellipsis button in the value cell to specify the color patterns in the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box). Data type: String |
| Show | Page Report, Web Report, Library Component | Specifies whether to use alternating color in the crosstab. Data type: Boolean  Note icon To apply alternating color in a crosstab, the aggregate fields in the crosstab should have transparent background. |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Auto Scale in Number | Page Report, Web Report, Library Component | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   Data type: Boolean |
| Cache | Query Page Report | Specifies whether to cache the dataset for this object in the [data buffer](https://devnet.logianalytics.com/hc/en-us/articles/4405664656919-Dataset-Properties#DataBuffer), so that other objects using the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Current Column Block Index | Query Page Report | You can use the four properties together to control the data of the crosstab you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode): Current Column Block Index, Current Row Block Index, Items per Column Block, and Items per Row Block. Current Column Block Index specifies the horizontal index of the data block. 0 means the first block index, 1 means the second, and so on. Data type: Integer |
| Current Row Block Index | Query Page Report | You can use the four properties together to control the data of the crosstab you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block. Current Row Block Index specifies the vertical index of the data block. 0 means the first block index, 1 means the second, and so on. Data type: Integer |
| Default for Filter | Page Report, Web Report | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean  Note icon In the same report, you can only set one data component's Default for Filter property to "true". |
| Enable Navigation | Web Report | Specifies whether to display scroll bars on the crosstab at runtime, if the parent container cannot fully display its data. When you set this property to "true", you can further specify the height and width of the frame for holding the crosstab via [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). Data type: Boolean |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Page Report, Web Report | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set [Default for Filter](#DFilter) of the object to "true". Data type: Boolean |
| Items per Column Block | Query Page Report | You can use the four properties together to control the data of the crosstab you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block. Items per Column Block specifies the number of the column records in each data block. Data type: Integer |
| Items per Row Block | Query Page Report | You can use the four properties together to control the data of the crosstab you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode): Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block. Items per Row Block specifies the number of the row records in each data block. Data type: Integer |
| Navigation Height | Web Report, Library Component | Specifies the height of the frame for holding the crosstab. Type a numeric value to specify the height. If you do not specify a value, Logi Report Engine calculates the height at runtime. Data type: Float  Note icon For a crosstab in a web report, this property takes effect when you set [Enable Navigation](#EnableNavigation) of the crosstab to "true". |
| Navigation Width | Web Report, Library Component | Specifies the width of the frame for holding the crosstab. Type a numeric value to specify the width. If you do not specify a value, Logi Report Engine calculates the width at runtime. Data type: Float  Note icon For a crosstab in a web report, this property takes effect when you set [Enable Navigation](#EnableNavigation) of the crosstab to "true". |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Record Location | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   For more information, see [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When Empty | Query Page Report | Specifies whether to suppress the object in the report when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Border | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Has Border | Page Report, Web Report, Library Component | Specifies whether to show cell borders in the crosstab. Data type: Boolean |
| Crosstab Property | | |
| Avoid Orphan Header | Query Page Report | Specifies whether to display the column headers together with the data. When you set this property to "true", if the column headers happen to be at the bottom of a page, Logi Report Engine displays them together with the data on the next page. Data type: Boolean |
| Block Gap | Query Page Report | Specifies the space between each part when the crosstab is split into more than one part. Type a numeric value to change the gap. Data type: Float |
| Boundary Value | Page Report, Web Report, Library Component | Specifies the number of columns in one aggregate cell when the crosstab displays horizontally, or the number of rows in one aggregate cell when the crosstab displays vertically. Type an integer value to change the number. Data type: Integer |
| Column Totals on Left | Page Report, Web Report, Library Component | Specifies whether to display the subtotal and grand total columns on the left of the detail aggregations. Data type: Boolean |
| [Expand Data](#Expand) | Query Page Report | Specifies whether to enable Page Report Studio users to expand/collapse the column/row groups in the crosstab. Data type: Boolean |
| Horizontal Gap | Page Report, Web Report, Library Component | Specifies the space between the left/right edge of a crosstab cell and the content in it. Type a numeric value to change the gap. Data type: Float |
| Outside Aggregate Title | Query Page Report | Specifies whether to place the aggregate field labels on the leftmost column when the aggregate layout is vertical, or on the topmost row of the crosstab when the aggregate layout is horizontal. Setting this property to "true" would make the labels of the aggregate fields far from their values. Data type: Boolean |
| [Repeat Aggregate](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#Repeat) | Query Page Report | Specifies whether to repeat the crosstab for different aggregate fields. Data type: Boolean |
| Repeat Column Header | Query Page Report | Specifies whether to display the column headers on every page when the crosstab spans more than one page. Data type: Boolean |
| Row Totals on Top | Page Report, Web Report, Library Component | Specifies whether to display the subtotal and grand total rows on the top of the detail aggregations. Data type: Boolean |
| Suppress Column Header | Page Report, Web Report, Library Component | Specifies whether to suppress the column headers in view mode. Data type: Boolean |
| Suppress Row Header | Page Report, Web Report, Library Component | Specifies whether to suppress the row headers in view mode. Data type: Boolean |
| Use Table Style | Page Report, Web Report, Library Component | Specifies whether to add labels to the Total rows and columns. Setting this property to "true" may make the row and column labels repeated too much. Data type: Boolean |
| Vertical Gap | Page Report, Web Report, Library Component | Specifies the space between the top/bottom edge of a crosstab cell and the content in it. Type a numeric value to change the gap. Data type: Float |
| Vertical Layout | Page Report, Web Report, Library Component | Shows whether the aggregate fields display vertically in the crosstab. This property is read only. |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Summary | Query Page Report | This property is mapped to the HTML attribute *summary*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

## Expand Data, Expand Detail Data

For crosstabs in a page report, if they contain more than one column/row group level, you can specify whether to enable expanding and collapsing the column/row groups at runtime, and set the default expanding/collapsing state of groups in the outer level. You can control this behavior by two properties: Expand Data and Expand Detail Data.

* **Expand Data**: A property on crosstab, and DBFields and formulas in crosstab as column/row fields. This property on crosstab controls whether to enable users to expand and collapse the column/row groups in the crosstab. When you enable the property on a crosstab, you can use the property on DBFields and formulas in the crosstab to specify whether to expand and collapse the corresponding column/row groups respectively.
* **Expand Detail Data**: A property on DBFields and formulas in crosstab as column/row fields. You can use it to specify whether to expand the details of specific column/row groups in a crosstab by default.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) These two properties work only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode) and do not apply to the innermost column/row group. After setting the two properties, if you further modify the crosstab layout, they may not take effect.

Suppose you have a crosstab which shows Product Type Name and Category as the column groups, Region, Country, and State as the row groups, and displays summaries for Quantity.

1. In the Report Inspector, set the **Expand Data** property of the crosstab to **true**.
2. Select the DBField **Country** and set its Expand Data property to **false**.
3. Set the **Expand Detail Data** property of **Product Type Name** to **false**.
4. Clear **Page Layout** on the **View** menu tab to switch to continuous page mode.
5. Publish the crosstab to Server and run it in Page Report Studio.
6. Select the icons with a plus or minus sign to expand and collapse the details of the Region and Product Type Name groups. Since Expand Data of Country is "false", you cannot expand the details of this group; Expand Detail Data of Product Type Name is "false" so the details of this group are not expanded by default.

   ![Expand Crosstab Groups](https://devnet.logianalytics.com/hc/article_attachments/4420542088599/prpty_rpt_crstb.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664653847-Contents-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664655767-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)
