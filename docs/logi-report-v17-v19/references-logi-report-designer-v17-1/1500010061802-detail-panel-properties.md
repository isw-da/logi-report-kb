---
title: "Detail Panel Properties"
id: 1500010061802
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061802-Detail-Panel-Properties
updated_at: 2021-07-23T19:16:29Z
---

# Detail Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061782-Group-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061822-Group-Footer-Panel-Properties)

# Detail Panel Properties

This topic lists the properties of a Detail Panel object in a banded object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report and Web Report.

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
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Page Report, Web Report | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Cache Section | Page Report, Web Report | Specifies whether to cache the objects in the detail panel. Data type: Boolean  Note icon The property doesn't work if there is crosstab, text object, chart, and so on in the panel, because these objects contain child-DBFields. |
| Cross Page | Page Report, Web Report | Specifies whether the panel can be split across a page break.  * If false, the panel will be shown in the Next Topic when it spans a large space vertically and cannot be wholly shown in a page. * If true, the panel will be split across a page break when it exceeds the page height.   This property is applied only when the report has page layout enabled.  Data type: Boolean |
| Current Block Index | Page Report, Web Report | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages#Mode). Current Block Index specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV output of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel output of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text output of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML output of the report. Data type: Boolean |
| Fill Whole Page | Page Report, Web Report | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Items per Block | Page Report, Web Report | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages#Mode). Item per Block specifies the number of records in each data block.  Data type: Integer |
| Label | Page Report, Web Report | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| [On New Page](https://devnet.logianalytics.com/hc/en-us/articles/1500010100261-Group-Header-Panel-Properties#OnNewPage) | Page Report, Web Report | Specifies whether the panel starts on a new page. This property is applied only when the report has page layout enabled. The default is false which means the panel starts on a new page only if the Previous Topic is filled. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#RecordLocation) | Page Report, Web Report | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Remove Blank Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010061842-Banded-Page-Header-Properties#Panel) | Page Report, Web Report | Specifies whether to remove blank rows in the panel in the Excel output. Data type: Boolean |
| Show Bottom Line | Query Page Report | Specifies whether to include a horizontal line at the bottom of the panel. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
| Suppress | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress Blank Panel | Page Report, Web Report | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| [Tile Detail Panel](#TileDetailPanel) | Page Report, Web Report | Specifies whether to tile records in the detail panel. For a vertical/horizontal banded object, you can make each set of records in the detail panel to be tiled when viewing the report if you set this property to true and set the detail panel's width/height equal to or less than 1/2 that of the banded object. The detail panel width/height defines the width/height of each record tile.  Data type: Boolean  Note icon If you set the banded object's Auto Fit property to "true", Logi Report Engine always treats the Tile Detail Panel property as "false" at runtime. |
| Tile Horizontal | Page Report, Web Report | If the Tile Detail Panel property of the detail panel is set to true, you can further specify the direction for tiling records in the detail panel.  * **true** - Records will be tiled in the row direction and then in column. * **false** - Records will be tiled in the column direction and then in row.   Data type: Boolean |
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
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## Tile Detail Panel

You will find this property is useful when you are making a mail-label format report.

You can insert a blank banded object in a report, then in the Report Inspector, select the detail panel, and set properties as follows:

Tile Detail Panel = true  
 Width = \*\*\* (The width of the detail panel. You can set this value according to the width of one column.)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061782-Group-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061822-Group-Footer-Panel-Properties)
