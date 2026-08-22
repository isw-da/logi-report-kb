---
title: "Record-level Security and Column-level Security"
id: 1500009718801
section: "Report Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718801-Record-level-Security-and-Column-level-Security
updated_at: 2021-11-03T06:56:32Z
---

# Record-level Security and Column-level Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718781-Cached-Report-Bursting)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692582-Business-View-Security)

# Record Level and Column Level Security

The Record Level Security (RLS) and Column Level Security (CLS) of Logi JReport allow you to control user access to different subsets of data and ensure that people only see what they are supposed to see: RLS allows you to define which records are to be revealed to any given user, while CLS allows you to define which report column is revealed to any given user. This enables you to provide different users with accordingly different, but appropriate contents. No matter to whom you need to provide information, a plant manager or thousands of customers, Logi JReport allows you to control access to information according to your requirements.

In Logi JReport Designer, you can define two types of the RLS and CLS security policies: one is a security policy based on a catalog data source (data source scope security policy), and the other is a security policy based on a single report (report scope security policy).

* **Data source scope security**  
   You can build data source scope security policies, where each security policy refers to a catalog data source in the catalog. If you want to implement the same security policy in a group of reports, you can simply apply an existing security policy to the report, without having to repeatedly build security information for each report. Both RLS and CLS can be data source scope security.
* **Report scope security**   
  RLS can also be of report scope, based on the security information file. That is, you can use the security information file to set the security policies for a report. Report scope security policy doesn't support CLS.

RLS can be applied simultaneously to both data source and report scopes. However, if a report scope security policy has already been applied to a report, it will override a data source scope security policy applied to the report. That is, report scope security policies have a higher priority than data source scope security policies.

After setting up the security policy for a report in Logi JReport Designer, you can then publish it to Logi JReport Server as normal. Then, when you log onto the server as different users, you will find that the security settings are applied to the report. That is, different users will only see the data they are supposed to see.

See also Record Level and Column Level Security in the *Logi JReport Designer User's Guide* for details about how to set up the security policies and apply them to reports in Logi JReport Designer.

**Note:** The report designer defined users and roles may not be recognized by Logi JReport Server. If your security policies contain such users/roles, create these users and roles respectively in Logi JReport Server, and then in Logi JReport Designer, synchronize the security information with Logi JReport Server using the Merge option.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718781-Cached-Report-Bursting)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692582-Business-View-Security)
