---
title: "Tabular Row Group Properties"
id: 1500009612822
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612822-Tabular-Row-Group-Properties
updated_at: 2021-07-24T16:03:29Z
---

# Tabular Row Group Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635741-Tabular-Cell-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613022-Text-Box-Properties)

# Tabular Row Group Properties

This topic lists the properties of a Tabular Row Group object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties#ReportType): Query Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Others | | |
| Cross Page | Query Page Report, Web Report | Specifies whether the row can be split across a page break.  * If false, the row will be shown in the Next Topic when it spans a large space vertically and cannot be wholly shown in a page. * If true, the row will be split across a page break when it exceeds the page height.   This property is applied only when the report has page layout enabled.  Data type: Boolean |
| Fill Whole Page | Query Page Report, Web Report | Specifies whether to make the row extended to the bottom of the page, so that the next row starts on a new page. Data type: Boolean |
| [On New Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009612022-Group-Header-Panel-Properties#OnNewPage) | Query Page Report, Web Report | Specifies whether the row starts on a new page. This property is only applied if the report has page layout enabled. The default is false which means the panel starts on a new page only if the Previous Topic is filled. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009635741-Tabular-Cell-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613022-Text-Box-Properties)
