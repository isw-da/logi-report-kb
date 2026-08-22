---
title: "Dynamic Security"
id: 1500011463681
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463681-Dynamic-Security
updated_at: 2021-07-24T10:39:45Z
---

# Dynamic Security

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431662-Record-Level-and-Column-Level-Security) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431642-Select-N-Filter-Condition)

# Dynamic Security

Business view security, record level security and column level security of a catalog published to Logi JReport Server can be dynamically changed at runtime while keeping the current catalog untouched. The report security can be defined in the catalog and then exported to a .xml security file easily using Logi JReport Designer. Next the Logi JReport Server administrator can apply the security file as the default dynamic security to the catalog on the server. Then when end users run reports that use the catalog, the report security defined in the security file will be applied to replace that of the catalog.

Suppose that we have modified the security in SampleReports.cat and export the new security to the security file BISampleReports.security.xml. Then the server administrator can apply the security file as the default dynamic security to the catalog SampleReports.cat on the server.

![Dynamic Security](https://devnet.logianalytics.com/hc/article_attachments/4404909300247/rptscrty_dynamic.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431662-Record-Level-and-Column-Level-Security) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431642-Select-N-Filter-Condition)
