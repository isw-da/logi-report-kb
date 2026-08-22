---
title: "Report Bursting"
id: 1500011431722
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431722-Report-Bursting
updated_at: 2021-07-24T10:39:45Z
---

# Report Bursting

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011463721-Quick-Start-a-Web-Report) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431702-Report-Security-System)

# Report Bursting

Report bursting enables you to schedule and distribute a single page report to multiple users who each receive a subset of the results related only to them. This greatly reduces administrative burden as well as runtime load since you don't have to run a report a million times in order to get a million results. A bursting task can also be scheduled at a low-load time. Bursting report results can be distributed to any destination, including e-mail, FTP, disk, Logi JReport’s versioning system, and users in the Logi JReport Server security system.

To create a bursting report, first the report designer needs to create a recipient query. The query should contain data fields that define recipients and a secondary data field that can be mapped to the bursting key which is the field which distinguishes how the report data is to be split. The report data is therefore split by the bursting key and then distributed to the recipients in the query according to the mapping relationship.

Then the report designer can create a page report using a query resource or business view that contains the bursting key, and define a bursting schema in the report as follows:

* Map the bursting key to a data field in the recipient query.
* Set a data field in the recipient query as the recipient.

For more information about bursting reports, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010070801-Creating-Bursting-Reports).

In the following example, we will define a bursting schema in a page report, publish it to Logi JReport Server, and schedule a task to distribute the bursting results.

![Bursting Report](https://devnet.logianalytics.com/hc/article_attachments/4404909300759/reportburst.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011463721-Quick-Start-a-Web-Report) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431702-Report-Security-System)
