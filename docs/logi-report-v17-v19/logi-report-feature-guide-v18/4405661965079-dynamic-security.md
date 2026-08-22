---
title: "Dynamic Security"
id: 4405661965079
section: "Logi Report Feature Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661965079-Dynamic-Security
updated_at: 2022-01-27T20:35:02Z
---

# Dynamic Security

![](https://devnet.logianalytics.com/hc/article_attachments/4420394628247/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661966103-Record-Level-Security-and-Column-Level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420402298007/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661967127-Select-N-Filter-Condition)

# Dynamic Security

The Server administrators can create dynamic security policies for catalogs published to Server using security files, which contain catalog internal security definitions for Business View Security, Record Level Security, and Column Level Security. With dynamic security, administrators can change the security policies applied to a catalog at runtime, without having to edit the security in Designer and publish the catalog again.

In the following example, we suppose new security policies are added in the SampleReports.cat catalog file and we want them to be applied to the same catalog in the Public Reports\SampleReports folder in Server resource tree. So we export the security in Designer to the security file SampleReports.security.xml, then we sign in to the Server Console as an administrator to apply the security file to the catalog to dynamically modify its security definitions.

![Dynamic Security](https://devnet.logianalytics.com/hc/article_attachments/4420402304535/rptscrty_dynamic.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4420394628247/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661966103-Record-Level-Security-and-Column-Level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420402298007/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661967127-Select-N-Filter-Condition)
