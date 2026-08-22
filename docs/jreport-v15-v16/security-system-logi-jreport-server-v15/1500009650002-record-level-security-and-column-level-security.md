---
title: "Record-Level Security and Column-Level Security"
id: 1500009650002
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650002-Record-Level-Security-and-Column-Level-Security
updated_at: 2021-07-24T20:53:40Z
---

# Record-Level Security and Column-Level Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674901-Cached-Report-Bursting)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674881-Business-View-Security)

# Record-Level Security and Column-Level Security

The record-level security (RLS) and column-level security (CLS) of Logi JReport Designer allow you to control user access to different subsets of data and ensure that people only see what they are supposed to see: record-level security allows you to define which records are to be revealed to any given user, while column-level security allows you to define which report column is revealed to any given user. This enables you to provide different users with accordingly different, but appropriate contents. No matter to whom you need to provide information, a plant manager or thousands of customers, Logi JReport Designer allows you to control access to information according to your requirements.

Logi JReport Designer have two types of the security policies, one is a security policy based on a catalog data source (data source scope security policy), and the other is a security policy based on a single report (report scope security policy).

* **Data source scope security**  
   You can build data source scope security policies: where each security policy refers to a catalog data source in the catalog. If you want to implement the same security policy in a group of reports, you can simply apply an existing security policy to the report, without having to repeatedly build security information for each report. Both RLS and CLS can be data source scope security.
* **Report scope security**   
   Additionally, record-level security can be of report scope, based on the security information file. That is, you can use the security information file to set the security policies for a report. Report scope security policy doesn't support column-level security.

Record-level security can be applied simultaneously to both data source and report scopes. However, if a report scope security policy has already been applied to a report, it will override a data source scope security policy applied to the report. That is, report scope security policies have a higher priority than data source scope security policies.

After setting up the security policy for a report in Logi JReport Designer, you can then publish it to Logi JReport Server as normal. Then, when you log onto the server as different users, you will find that the security settings are applied to the report. That is, different users will only see the data they are supposed to see.

See also "Record-level and Column-level Security" in the *Logi JReport Designer User's Guide* for details about how to set up record-level/column-level security policies and apply them to reports in Logi JReport Designer.

**Note:** The report designer defined users and roles may not be recognized by Logi JReport Server. If your security policies contain such users/roles, create these users and roles respectively in Logi JReport Server, and then in Logi JReport Designer, synchronize the security information with Logi JReport Server using the Merge option.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674901-Cached-Report-Bursting)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674881-Business-View-Security)
