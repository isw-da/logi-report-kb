---
title: "Logi JReport v15 Release Notes"
id: 1500009648542
section: "Release Notes for Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648542-Logi-JReport-v15-Release-Notes
updated_at: 2021-07-24T20:54:09Z
---

# Logi JReport v15 Release Notes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648562-Logi-JReport-v15-Enhancements)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673261--Logi-JReport-Server-Guide-v15-Product-Overview)

# Logi JReport v15 Release Notes

This topic describes the feature enhancements, resolved issues and any known issues for Logi JReport in this release.

## Feature Enhancements

| Item | Case # | Description |
| --- | --- | --- |
| 1 | 159511 | Array parameter values returned from formula. |
| 2 | 163160 | Fast responding when filtering large values in on-screen filter. |
| 3 | 163454 | Chart animation on Bar, Bench, Pie, Donut, Line, and Area. |
| 4 | 163155 | Distinct records for MongoDB. |
| 5 | 160204 | Mouse hover to show tips while highlighting the selected chart elements (bar, pie slice. etc.) |
| 6 | 109704 | Sortable on-screen filter values in Web Report Studio. |
| 7 | 116790 | Optionally linking to detail report or drill down in any level of the hierarchy. |
| 8 | 159184 | Easier selecting and moving objects in Logi JReport Designer. |
| 9 | 159172 | Direct database connections (Oracle, SQL Server and MySQL) on Logi JReport Designer Welcome Page. |
| 10 | 163831 | Performance improvements in fetching database table list. |
| 11 | 162803 | "Comments" support in Imported SQL. |
| 12 | 160234 | Parameters and constant level formulas for join conditions. |
| 13 | 161016 | Pagination and search capabilities on Logi JReport Server user console. |
| 14 | 142857 | Page Report Creation using business views in Designer. |
| 15 | 158498 | Alternative default of horizontal or vertical crosstab aggregations in Ad Hoc Page Reports. |
| 16 | 166648 | Two screen/monitor display for Logi JReport Designer. |
| 17 | 70009 | Optimized performance of running dynamic queries from business views with enabled pre-joins. |
| 18 | 72929 | Optimized crosstab performance with huge data in Page Report. |
| 19 | 73116 | Enabled passing parameters to Visual Analysis via URL. |
| 20 | 73116 | Custom authentication for Visual Analysis. |
| 21 | 73253 | Enabled using on-the-fly formulas (dynamic formulas) in aggregations for Web Report. |
| 22 | 73432 | Enhanced Custom Measure to enable using formula in another formula. |
| 23 | 73462 | Enabled the go-to-detail action from a chart in Web Report that uses dynamic aggregations. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Resolved Issues

| Item | Case # | Issue |
| --- | --- | --- |
| 1 | 72390 | Removable temporary files in the temp folder for integrated Logi JReport server. |
| 2 | 73095 | Solved "access denied" error when configuring “schedule to e-mail” for tenant users. |
| 3 | 73201 | Recovered background running tasks after upgraded. |
| 4 | 73241 | Solved the jet.exception.UserException error when the property “Underlay” is set on a detail panel of a banded object. |
| 5 | 73253 | Enabled saving formulas with summaries in Logi JReport Designer. |
| 6 | 73309 | Solved a java.lang.IllegalArgumentException when viewing a page report without any data returned. |
| 7 | 73311 | Function DateTimeToDate() can return value correctly now. |
| 8 | 73328 | Solved the "Failed to activate Quartz Scheduler" issue with Logi JReport Server after upgraded. |
| 9 | 73333 | Solved the chart axis label translation failure when inserting a web report component into dashboard. |
| 10 | 73346 | Log message enhancements with enabled NLS. |
| 11 | 73430 | Tenant users can save/publish dashboards and reports to Public Report and Public Components folders now. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Known Issues

**JDK 9 is not supported for Logi JReport 15**

As a newly released JDK version, JDK 9 is currently not supported for the installation of Logi JReport 15 products.

**Summary field disappears from design view when deleting table column**

If a summary is inserted in the GroupFooterPanel of a table, when you delete a column from the table, or unmerge the cell of the group footer row, sometimes you may find the summary field disappears from design view, however, from the report structure tree in the Report Inspector, you can still find the object. You can reset its coordinate related properties so as to make the summary field display again.

**Report data gets cut off in PDF result**

When you export a report to PDF format, if the report contains a large amount of data but its page mode was specified to be continuous page mode, or its page size was set to be larger than 200 inches, you will find that in the PDF result some data of the report are cut off. This is because in one PDF page, the data displayed can be no larger than 200 inches.

**Unsupported go-to action temporarily when using dynamic formula on chart**

When you perform the go-to action on a chart which uses a dynamic formula as its shown value, and the formula contains group information, you will get exceptions. This is a limitation in current version. We will resolve the issue in future release.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648562-Logi-JReport-v15-Enhancements)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673261--Logi-JReport-Server-Guide-v15-Product-Overview)
