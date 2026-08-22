---
title: "Dynamic Security"
id: 5741507416215
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741507416215-Dynamic-Security
updated_at: 2022-10-31T17:18:47Z
---

# Dynamic Security

![](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741498879511-Record-Level-Security-and-Column-Level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741507464855-Select-N-Filter-Condition)

# Dynamic Security

The Server administrators can create dynamic security policies for catalogs published to Server using security files, which contain catalog internal security definitions for Business View Security, Record Level Security, and Column Level Security. With dynamic security, administrators can change the security policies applied to a catalog at runtime, without having to edit the security in Designer and publish the catalog again.

In the following example, we suppose new security policies are added in the SampleReports.cat catalog file and we want them to be applied to the same catalog in the Public Reports\SampleReports folder in Server resource tree. So we export the security in Designer to the security file SampleReports.security.xml, then we sign in to the Server Console as an administrator to apply the security file to the catalog to dynamically modify its security definitions.

![](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741498879511-Record-Level-Security-and-Column-Level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741507464855-Select-N-Filter-Condition)
