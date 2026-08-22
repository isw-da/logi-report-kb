---
title: "Export Page Setting Object Properties"
id: 4405664667799
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664667799-Export-Page-Setting-Object-Properties
updated_at: 2022-01-27T20:38:10Z
---

# Export Page Setting Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661878807-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664666007-Page-Footer-Panel-Properties)

# Export Page Setting Object Properties

When you clear the Auto option for an export format and select OK in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box) tab of the Page Setup dialog box, Designer adds an export page setting object in the Report Inspector tree for this specific export format. By defining the properties of an export page setting object, you can [customize the page properties for the output of the corresponding export format](https://devnet.logianalytics.com/hc/en-us/articles/4405664595479-Exporting-Reports#Page). This topic describes the properties of an Export Page Setting Object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Paper | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the page. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Page Report, Web Report, Library Component | Specifies how to position the report page. Choose an option from the drop-down list.  * **portrait** - Select to position the page vertically. * **landscape** - Select to position the page horizontally.   Data type: Enumeration |
| Page Type | Page Report, Web Report, Library Component | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Page Report, Web Report, Library Component | Specifies the width of the page. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin | | |
| Bottom Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the bottom edge of the page. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the left edge of the page. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the right edge of the page. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Page Report, Web Report, Library Component | Specifies the distance between the report data and the top edge of the page. Type a numeric value to change the thickness. Data type: Float |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* Designer changes the values for the Height and Width properties automatically when you change Orientation or Page Type. After you select a paper type and edit either Height or Width, Designer changes the paper type to "custom size" automatically.
* Server also applies the page properties that you specify for any export format when users advanced run and schedule to run the report in this format at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661878807-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664666007-Page-Footer-Panel-Properties)
