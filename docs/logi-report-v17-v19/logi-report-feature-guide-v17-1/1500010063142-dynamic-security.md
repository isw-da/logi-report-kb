---
title: "Dynamic Security"
id: 1500010063142
section: "Logi Report Feature Guide v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063142-Dynamic-Security
updated_at: 2021-08-02T02:54:23Z
---

# Dynamic Security

![](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063162-Record-Level-Security-and-Column-Level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063182-Select-N-Filter-Condition)

# Dynamic Security

The Server administrators can create dynamic security policies for catalogs published to Server using security files, which contain catalog internal security definitions for Business View Security, Record Level Security, and Column Level Security. With dynamic security, administrators can change the security policies applied to a catalog at runtime, without having to edit the security in Designer and publish the catalog again.

In the following example, we suppose new security policies are added in the SampleReports.cat catalog file and we want them to be applied to the same catalog in the Public Reports\SampleReports folder in Server resource tree. So we export the security in Designer to the security file SampleReports.security.xml, then we log onto the Server Console as an administrator to apply the security file to the catalog to dynamically modify its security definitions.

![Dynamic Security](https://devnet.logianalytics.com/hc/article_attachments/4404848361367/rptscrty_dynamic.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063162-Record-Level-Security-and-Column-Level-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063182-Select-N-Filter-Condition)
