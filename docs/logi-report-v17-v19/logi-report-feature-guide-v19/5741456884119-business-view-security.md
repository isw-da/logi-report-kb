---
title: "Business View Security"
id: 5741456884119
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741456884119-Business-View-Security
updated_at: 2022-10-31T17:18:45Z
---

# Business View Security

![](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741491635863-Report-Security-System)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741485725463-Cached-Report-Bursting)

# Business View Security

Business view security enables report designers to limit user access to the data and to the specific members of groups in business views. By defining which members of a group object in a business view are available to which users, groups, or roles existing in the security system of Server, you can create different report results for each user, role, and group. When a user accesses any report created using the specified business view at runtime, Server checks the user, and the group and role of the user and merges the data in the report the user is authorized to see and displays the permitted result to the user.

In the following example, we suppose the security system contains the user Manager\_NA who is the manager of the North America region, and the user has the necessary permissions to run the sample reports in the Public Reports\SampleReports folder in the resource tree of Server. In Designer we first define a security policy on the WorldWideSalesBV business view in the SampleReports.cat catalog file to limit the manager's data access permission to that of North America only, and then we publish the catalog to the Public Reports\SampleReports folder in Server to update its business view security. Then when the manager logs onto the Server Console with the username **Manager\_NA** and runs the sample reports that use WorldWideSalesBV, he will only be able to view data about North America in the reports.

![](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741491635863-Report-Security-System)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741485725463-Cached-Report-Bursting)
