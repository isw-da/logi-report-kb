---
title: "Banded Page Header Properties"
id: 1500009612062
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612062-Banded-Page-Header-Properties
updated_at: 2021-07-24T16:03:39Z
---

# Banded Page Header Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635101-Banded-Page-Footer-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635121-Group-Panel-Properties)

# Banded Page Header Properties

This topic lists the properties of a Banded Page Header object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties#ReportType): Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color and fill effect of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Page Report, Web Report | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Label | Page Report, Web Report | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| [Merge to Next Panel](#Panel) | Page Report, Web Report | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#RecordLocation) | Page Report, Web Report | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Remove Blank Row](#Panel) | Page Report, Web Report | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
| [Repeat in Detail Panel](#Panel) | Page Report, Web Report | Specifies whether to make the objects in the panel repeated in the detail panel in the exported Excel file. Data type: Boolean |
| Show Bottom Line | Query Page Report | Specifies whether to include a horizontal line at the bottom of the panel. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
| Suppress | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress Blank Panel | Page Report, Web Report | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Page Report, Web Report | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border lines of the object. Choose an option from the drop-down list.  * **miter** - Joins path segments by extending their outside edges until they meet. * **round** - Joins path segments by rounding off the corner at a radius of half the line width.   Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius for the border line joint of the object. This property takes effect only when [Border Joint](#BorderJoint) is set to round. Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## Merge to Next Panel, Repeat in Detail Panel, Remove Blank Row

You can control panels of a banded object in the exported Excel file by settings the three properties:

* Merge to Next Panel controls whether to merge current panel to the next panel. It applies to the banded header, banded page header, group header, and group footer panels.
* Repeat in Detail Panel controls whether to repeat certain panel with the detail panel. It applies to the group header and banded page header panels.
* Remove Blank Row controls whether to remove blank rows in the panel. It applies to the banded page header, group header, and detail panels.

The three properties take effect only when the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property of the page report tab containing the banded object or the web report is set to true, and there is an operation order when those three properties work together: Merge to Next Panel > Repeat in Detail Panel > Remove Blank Row.

Suppose there is a page report tab containing a standard banded object which displays the fields Customer Name, Annual Sales, and is grouped by Customer\_Country and Customer\_Region.

![Standard banded report](https://devnet.logianalytics.com/hc/article_attachments/4404911645207/prpty_rpt_bdobj_pg_hd_pnl1.gif)

Then we set the Columned property of the report tab to true and Merge to Next Panel of the first group header panel to true as well, save the report tab and export it to Excel. We can see that the two group panels are merged into one and fields in the two panels are put in one cell in the exported Excel file.

![Exported Excel file with merged panels](https://devnet.logianalytics.com/hc/article_attachments/4404904202519/prpty_rpt_bdobj_pg_hd_pnl2.gif)

In order to improve the layout of the Excel result, now we specify the Column Index and Row Index properties of the objects as follows:

![Specify the Column Index and Row Index properties of the objects](https://devnet.logianalytics.com/hc/article_attachments/4404904202775/prpty_rpt_bdobj_pg_hd_pnl3.gif)

| Object | Column Index | Row Index |
| --- | --- | --- |
| A | 3 | 1 |
| B | 4 | 1 |
| C | 1 | 1 |
| D | 2 | 1 |
| E | 3 | 1 |
| F | 4 | 1 |

Save the report tab and export it to Excel again. Fields in the Excel file are shown more clearly this time.

![Excel result with improved result](https://devnet.logianalytics.com/hc/article_attachments/4404911645463/prpty_rpt_bdobj_pg_hd_pnl4.gif)

**Notes:**

* When two or more objects in the to be merged panels have the same Column Index and Row Index property values, after merging the panels, in the exported Excel file, the objects will be merged into one cell, and they will be located in the cell based on this rule: the object whose X/Y property value is smaller than others will be put to front, and Y has higher priority than X.
* Do not set Merge to Next Panel to true for the last group footer panel, because it will make the exported Excel file incorrect.
* Do not set Merge to Next Panel to true for the panel that contains crosstab or subreport.
* When the objects in the group header/banded page header panel have the same Row Index and Column Index property values with those in the detail panel, and you specify to repeat the group header/banded page header panel in the detail panel, in the exported Excel file, the repeated objects will be put in the same cells with the ones in the detail panel based on this rule: the object whose X/Y property value is smaller than others will be put to front, and Y has higher priority than X.
* When you specify to repeat a group header panel, if there is a chart in the panel, the chart cannot be repeated.
* If a banded object contains more than one group-by fields, that is to say, it has several group header panels, when you specify to repeat the first group header panel in the detail panel, it will be repeated in the second group header panel as well.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635101-Banded-Page-Footer-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635121-Group-Panel-Properties)
