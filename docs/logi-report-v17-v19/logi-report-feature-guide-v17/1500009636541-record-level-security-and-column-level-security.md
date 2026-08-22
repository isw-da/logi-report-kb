---
title: "Record Level Security and Column Level Security"
id: 1500009636541
section: "Logi Report Feature Guide v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009636541-Record-Level-Security-and-Column-Level-Security
updated_at: 2021-07-24T16:05:43Z
---

# Record Level Security and Column Level Security

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613762-Cached-Report-Bursting) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636521-Dynamic-Security)

# Record Level Security and Column Level Security

Record Level Security (RLS) and Column Level Security (CLS) allow report designers to control end user access to different subsets of data and ensure that people only see what they are supposed to see: RLS is for defining which records are to be revealed to any given user, while CLS is for defining which report columns are revealed to any given user. This enables the report designers to provide different users with accordingly different, but appropriate contents.

RLS and CLS can be defined together in a data source security entry in a catalog and applied to different reports in the same catalog. RLS can also be defined on each page report that is created using query individually.

In the following examples, we suppose the Logi Report Server security system contains the user Cindy and the user has the necessary permissions to run reports in the Public Reports folder in the server resource tree.

First, we create a security entry in Data Source 1 of the SampleReport.cat catalog file to edit RLS to limit the user's permission to North America of the Assigned Region DBField, and use CLS to only allow the user to view the following report columns: Assigned Region, Name, and Employee Position. We then apply the security entry to a page report by setting it as value of the Security Policy Name property on the dataset of the report. After we publish the report and catalog to Logi Report Server, when the user Cindy logs onto the server and runs the report, she can only view the allowed data.

![Define Securities in Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404911571479/rptscrty_rls.gif)

Then we define RLS directly on another page report by setting the Record Security property on its dataset.

![Define Report Level Security on Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404911571863/rptscrty_rls_pg.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613762-Cached-Report-Bursting) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636521-Dynamic-Security)
