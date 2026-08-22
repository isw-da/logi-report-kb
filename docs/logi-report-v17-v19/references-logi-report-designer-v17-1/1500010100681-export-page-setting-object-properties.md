---
title: "Export Page Setting Object Properties"
id: 1500010100681
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100681-Export-Page-Setting-Object-Properties
updated_at: 2021-07-23T19:16:38Z
---

# Export Page Setting Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062242-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100661-Page-Footer-Panel-Properties)

# Export Page Setting Object Properties

This topic lists the properties of an Export Page Setting Object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

When you clear the Auto option for an export format and select OK in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) tab of the Page Setup dialog box, an export page setting object is added in the Report Inspector tree for this specific export format. By defining the properties of an export page setting object, you can customize the page properties for the exported result of the corresponding export format. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Server.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Paper | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the page. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Page Report, Web Report, Library Component | Specifies how to position the report page. The Orientation setting affects the Width and Height values. Choose an option from the drop-down list.  * **portrait** - The page is positioned vertically. * **landscape** - The page is positioned horizontally.   Data type: Enumeration |
| Page Type | Page Report, Web Report, Library Component | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Page Report, Web Report, Library Component | Specifies the width of the page. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Page Report, Web Report, Library Component | Specifies whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin | | |
| Bottom Margin | Page Report, Web Report, Library Component | Specifies the distance between the bottom page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Page Report, Web Report, Library Component | Specifies the distance between the left page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Page Report, Web Report, Library Component | Specifies the distance between the right page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Page Report, Web Report, Library Component | Specifies the distance between the top page edge and the data area. Type a numeric value to change the thickness. Data type: Float |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062242-Page-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100661-Page-Footer-Panel-Properties)
