---
title: "Export Page Setting Object"
id: 1500009750881
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750881-Export-Page-Setting-Object
updated_at: 2021-07-25T07:18:45Z
---

# Export Page Setting Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750841-Page-Footer-Panel)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750901-Parameter-Control)

# Export Page Setting Object

When you clear the Auto option for an export format and select OK in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009749201-Page-Setup#Export) tab of the Page Setup dialog box, an export page setting object is added in the Inspector tree for this specific export format. By defining the properties of an export page setting object, you can customize the page properties for the exported result of the corresponding export format. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi Report Server.

| Property Name | Description |
| --- | --- |
| Paper | |
| Height | Specifies the height of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Type a numeric value to change the height. Data type: Float |
| Height Auto Fit | Specifies whether to dynamically calculate the page height according to the height of the contents within the page. Data type: Boolean |
| Orientation | Specifies how to position the report page. The Orientation setting affects the Width and Height values. Choose an option from the drop-down list.  * **Portrait** - The page is positioned vertically. * **Landscape** - The page is positioned horizontally.   Data type: Enumeration |
| Page Type | Specifies the report page dimensions. Choose a size from the drop-down list. Data type: Enumeration |
| Width | Specifies the width of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Type a numeric value to change the width. Data type: Float |
| Width Auto Fit | Specifies whether to dynamically calculate the page width according to the width of the contents within the page. Data type: Boolean |
| Margin | |
| Bottom Margin | Specifies the distance in inches or centimeters between the bottom page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Left Margin | Specifies the distance in inches or centimeters between the left page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Right Margin | Specifies the distance in inches or centimeters between the right page edge and the data area. Type a numeric value to change the margin. Data type: Float |
| Top Margin | Specifies the distance in inches or centimeters between the top page edge and the data area. Type a numeric value to change the thickness. Data type: Float |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750841-Page-Footer-Panel)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750901-Parameter-Control)
