---
title: "Group Header Panel Properties"
id: 1500009777801
section: "Banded Object Properties"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777801-Group-Header-Panel-Properties
updated_at: 2021-07-24T00:47:50Z
---

# Group Header Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749142-Group-Footer-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777781-Group-Panel-Properties)

# Group Header Panel Properties

This topic describes the properties of a Group Header Panel object in a banded object.

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
| Background | Specifies the background color and fill effect of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Others | |
| Cross Page | Specifies whether the panel can be split across a page break.  * If false, the panel will be shown in the next page when it spans a large space vertically and cannot be wholly shown in a page. * If true, the panel will be split across a page break when it exceeds the page height.   This property is applied only when running or exporting the report in the formats that support page layout such as PDF and RTF.  Data type: Boolean |
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
| Invisible | Specifies whether to show the object in the report. All formulas and calculations will still be performed if the property is set to true. You can also [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Formula) whether to show the object. Data type: Boolean |
| Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| [Merge to Next Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009777841-Banded-Page-Header-Properties#Panel) | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
| On New Page | Specifies whether the panel starts on a new page. This property is only applied if the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
| Record Location | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Remove Blank Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009777841-Banded-Page-Header-Properties#Panel) | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
| [Repeat](#Repeat) | Specifies whether to make the group header appear in every page. Data type: Boolean |
| [Repeat in Detail Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009777841-Banded-Page-Header-Properties#Panel) | Specifies whether to make the objects in the panel repeated in the detail panel in the exported Excel file. Data type: Boolean |
| Suppress | Specifies whether to show the object in the report. All formulas and calculations will be skipped if the property is set to true. You can also use a formula to dynamically control whether to show the object. Data type: Boolean  Note iconWhen you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress Blank Panel | Specifies whether a panel with no data is included in the report. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |

## Repeat

The default value for Repeat is false. For one detail panel which spans a large space vertically to be shown in several pages, Logi Report supports the Repeat property if you want to see the group header information in each page. When the Repeat property is set true and group headers are visible, the group headers will duplicate on every page.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* When a page split occurs in the bottom blank part of the detail panel (or margins in the detail panel) and the Cross Page property in the detail panel is set true, the output is: repeated group header + a slice of blank detail panel + group footer. It appears as though only group footers without any detail panel follow the repeated group header. In order to solve this problem, you can resize the detail panel.
* If you set the Repeat property to true in both outer group header and inner group header, Logi Report treats the two group headers as a completely repeated object.
* If you set the outer and inner group headers to be one completely repeated object, then when the page can only hold the group headers or has no enough space for the group headers, Server does not duplicate both outer and inner group headers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749142-Group-Footer-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777781-Group-Panel-Properties)
