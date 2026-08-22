---
title: "Detail Panel Properties"
id: 1500009777741
section: "Banded Object Properties"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777741-Detail-Panel-Properties
updated_at: 2021-07-24T00:47:49Z
---

# Detail Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749182-Banded-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749142-Group-Footer-Panel-Properties)

# Detail Panel Properties

This topic describes the properties of a Detail Panel object in a banded object.

| Property Name | Description |
| --- | --- |
| General | |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| Color | |
| Background | Specifies the background color and fill effect of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Others | |
| Cache Section | Specifies whether to cache the objects in the detail panel. Data type: Boolean  Note iconThe property does not work if there is crosstab, text object, chart, and so on in the panel, because these objects contain child-DBFields. |
| Cross Page | Specifies whether the panel can be split across a page break.  * If false, the panel will be shown in the next page when it spans a large space vertically and cannot be wholly shown in a page. * If true, the panel will be split across a page break when it exceeds the page height.   This property is applied only when running or exporting the report in the formats that support page layout such as PDF and RTF.  Data type: Boolean |
| Current Block Index | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in continuous page mode. Current Block Index specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
| Export to CSV | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when running the report in Web Report Studio. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Fill Whole Page | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
| Invisible | Specifies whether to show the object in the report. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Items per Block | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in continuous page mode. Item per Block specifies the number of records in each data block.  Data type: Integer |
| Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| On New Page | Specifies whether the panel starts on a new page. The default is false which means the panel starts on a new page only if the previous page is filled. This property is applied only when running or exporting the report in the formats that support page layout such as PDF and RTF. Data type: Boolean |
| Record Location | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Remove Blank Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009777841-Banded-Page-Header-Properties#Panel) | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
| Suppress | Specifies whether to show the object in the report. All formulas and calculations will be skipped if the property is set to true. You can also use a formula to dynamically control whether to show the object. Data type: Boolean  Note iconWhen you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress Blank Panel | Specifies whether a panel with no data is included in the report. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| [Tile Detail Panel](#TileDetailPanel) | Specifies whether to tile records in the detail panel. For a vertical banded object, you can make each set of records in the detail panel to be tiled when viewing the report if you set this property to true and set the detail panel's width/height equal to or less than 1/2 that of the banded object. The detail panel width defines the width of each record tile.  Data type: Boolean  Note iconWhen the banded object's Auto Fit property is true, Server always treats the Tile Detail Panel property as false at runtime. |
| Tile Horizontal | If the Tile Detail Panel property of the detail panel is set to true, you can further specify the direction for tiling records in the detail panel.  * **true** - Records will be tiled in the row direction and then in column. * **false** - Records will be tiled in the column direction and then in row.   Data type: Boolean |
| Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |

## Tile Detail Panel

You will find this property is useful when you are making a mail-label format report.

You can insert a blank banded object in a report, then in the Report Inspector, select the detail panel, and set properties as follows:

Tile Detail Panel = true  
Width = \*\*\* (The width of the detail panel. You can set this value according to the width of one column.)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749182-Banded-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749142-Group-Footer-Panel-Properties)
