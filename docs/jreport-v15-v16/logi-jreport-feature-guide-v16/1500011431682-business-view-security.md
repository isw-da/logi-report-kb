---
title: "Business View Security"
id: 1500011431682
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431682-Business-View-Security
updated_at: 2021-07-24T10:39:45Z
---

# Business View Security

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431702-Report-Security-System) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463701-Cached-Report-Bursting)

# Business View Security

Business view security enables report designers to limit user access to the data and to the specific members of groups in business views. By defining which members of a group are available to which users, groups, or roles, report results are created for each user, role and group. When a user accesses a report, Logi JReport checks the user, group and role of the user and merges the data in the report the user is authorized to see and displays it to the user.

When defining business view security, it is recommended to import users from Logi JReport Server. In the following example, we will create a user directly to simplify the process. Suppose that there is a server user named Manager\_NA who is the manager of the North America region. We will limit his data access permission to that of North America in the WorldWideSalesBV. Then we publish a report showing data in all the regions using WorldWideSalesBV to Logi JReport Server, log into the server as the user Manager\_NA, and run the report. The report will be filtered to show only data about North America.

![Define Security](https://devnet.logianalytics.com/hc/article_attachments/4404909300503/rptscrty_bv.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431702-Report-Security-System) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463701-Cached-Report-Bursting)
