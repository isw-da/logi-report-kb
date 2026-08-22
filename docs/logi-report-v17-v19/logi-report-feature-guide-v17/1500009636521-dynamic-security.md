---
title: "Dynamic Security"
id: 1500009636521
section: "Logi Report Feature Guide v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009636521-Dynamic-Security
updated_at: 2021-07-24T16:05:49Z
---

# Dynamic Security

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636541-Record-Level-Security-and-Column-Level-Security) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636561-Select-N-Filter-Condition)

# Dynamic Security

Logi Report Server administrators can create dynamic security policies for catalogs published to the server using security files, which contain catalog internal security definitions for Business View Security, Record Level Security, and Column Level Security. With dynamic security, administrators can change the security policies applied to a catalog at run time, without having to edit the security in Logi Report Designer and publish the catalog again.

In the following example, we suppose new security policies are added in the SampleReports.cat catalog file and we want them to be applied to the same catalog in the Public Reports\SampleReports folder in the Logi Report Server resource tree. So we export the security in Logi Report Designer to the security file SampleReports.security.xml, then we log onto the server as an administrator to apply the security file to the catalog to dynamically modify its security definitions.

![Dynamic Security](https://devnet.logianalytics.com/hc/article_attachments/4404904153495/rptscrty_dynamic.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636541-Record-Level-Security-and-Column-Level-Security) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636561-Select-N-Filter-Condition)
