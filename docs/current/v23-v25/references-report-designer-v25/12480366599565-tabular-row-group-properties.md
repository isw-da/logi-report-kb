---
title: "Tabular Row Group Properties"
id: 12480366599565
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480366599565-Tabular-Row-Group-Properties
updated_at: 2026-02-25T23:47:49Z
source_host: docs-report.zendesk.com
---
# 
Tabular Row Group Properties

This topic describes the properties of a Tabular Row Group object that you can use in query-based page reports and web reports.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Others |  |  |
| Cross Page | Query Page Report, Web Report | Specifies whether the row can be split across a page break. Default is to split the row across a page break when it exceeds the page height. When you set this property to "false", Designer displays the row on the next page when it spans a large space vertically and cannot completely show on a page.Data type: Boolean This property cannot take effect if you disable Page Layout for the report, meaning, the report is in continuous page mode. |
| Fill Whole Page | Query Page Report, Web Report | Specifies whether to extend the row to the page bottom in the report, so that the next row starts on a new page. Data type: Boolean |
| On New Page | Query Page Report, Web Report | Specifies whether to start the row on a new page in the report. Default (the property being "false") is starting the row on a new page only when the previous page is filled. This property cannot take effect if you disable Page Layout for the report, meaning, the report is in continuous page mode. Data type: Boolean |
