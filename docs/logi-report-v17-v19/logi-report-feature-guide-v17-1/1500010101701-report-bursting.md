---
title: "Report Bursting"
id: 1500010101701
section: "Logi Report Feature Guide v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101701-Report-Bursting
updated_at: 2021-08-02T02:52:04Z
---

# Report Bursting

![](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101681-Quick-Start-a-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063102-Report-Security-System)

# Report Bursting

Report bursting enables you to schedule and distribute a single page report to multiple users who each receive a subset of the results related only to them. This greatly reduces administrative burden as well as runtime load since you don't have to run a report a million times in order to get a million results. You can also schedule a bursting task at a low-load time to reduce performance impact. Logi Report can distribute the bursting report results to any destination, including e-mail, FTP, disk, and the versioning system and users in the security system of Server.

To create a bursting report, first the report designer needs to create a recipient query. The query should contain data fields that define recipients and a secondary data field that can be mapped to the bursting key which is the field distinguishing how the report data is to be split. The report data is therefore split by the bursting key and then distributed to the recipients in the query according to the mapping relationship.

In the following example, we define a bursting schema in a page report to split the report data according to regions and distribute the report results to the versioning system of Server. After the catalog and report are published to Server, we can schedule a task to distribute the bursting results.

![Bursting Report](https://devnet.logianalytics.com/hc/article_attachments/4404856786583/reportburst.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101681-Quick-Start-a-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063102-Report-Security-System)
