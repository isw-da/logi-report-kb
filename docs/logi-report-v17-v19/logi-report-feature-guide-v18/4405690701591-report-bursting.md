---
title: "Report Bursting"
id: 4405690701591
section: "Logi Report Feature Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690701591-Report-Bursting
updated_at: 2022-01-27T07:59:58Z
---

# Report Bursting

![](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690700695-Quick-Start-a-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690702487-Report-Security-System)

# Report Bursting

Report bursting enables you to schedule and distribute a single page report to multiple users who each receive a subset of the results related only to them. This greatly reduces administrative burden and runtime load, because you don't have to run a report a million times in order to get a million results. You can also schedule a bursting task at a low-load time to reduce performance impact. Logi Report can distribute the bursting report results to any destination, including email, FTP, disk, and the versioning system and users in the security system of Server.

To create a bursting report, first the report designer needs to create a recipient query. The query should contain data fields that define recipients and a secondary data field that can be mapped to the bursting key which is the field distinguishing how the report data is to be split. The report data is therefore split by the bursting key and then distributed to the recipients in the query according to the mapping relationship.

In the following example, we define a bursting schema in a page report to split the report data according to regions and distribute the report to the versioning system of Server. After you publish the catalog and report to Server, we can schedule a task to distribute the bursting results.

![Bursting Report](https://devnet.logianalytics.com/hc/article_attachments/4420447045655/reportburst.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690700695-Quick-Start-a-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690702487-Report-Security-System)
