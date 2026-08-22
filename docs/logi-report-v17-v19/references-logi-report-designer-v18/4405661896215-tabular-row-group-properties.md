---
title: "Tabular Row Group Properties"
id: 4405661896215
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661896215-Tabular-Row-Group-Properties
updated_at: 2022-01-27T20:36:14Z
---

# Tabular Row Group Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661895191-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664679063-Text-Box-Properties)

# Tabular Row Group Properties

This topic describes the properties of a Tabular Row Group object that you can use in query-based page reports and web reports.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Others | | |
| Cross Page | Query Page Report, Web Report | Specifies whether the row can be split across a page break.  * **true** - Select to split the row across a page break when it exceeds the page height. * **false** - Select to display the row on the next page when it spans a large space vertically and cannot completely show on a page.   This property cannot take effect if you disable [Page Layout](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode) for the report, meaning, the report is in continuous page mode.  Data type: Boolean |
| Fill Whole Page | Query Page Report, Web Report | Specifies whether to extend the row to the page bottom in the report, so that the next row starts on a new page. Data type: Boolean |
| On New Page | Query Page Report, Web Report | Specifies whether to start the row on a new page in the report. Default (the property being "false") is starting the row on a new page only when the previous page is filled. This property cannot take effect if you disable [Page Layout](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode) for the report, meaning, the report is in continuous page mode. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661895191-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664679063-Text-Box-Properties)
