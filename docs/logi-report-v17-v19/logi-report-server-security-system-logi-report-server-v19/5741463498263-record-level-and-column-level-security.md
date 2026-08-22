---
title: "Record Level and Column Level Security"
id: 5741463498263
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741463498263-Record-Level-and-Column-Level-Security
updated_at: 2022-10-31T17:18:23Z
---

# Record Level and Column Level Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741469954327-Cached-Report-Bursting)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741455041943-Business-View-Security)

# Record Level and Column Level Security

The Record Level Security (RLS) and Column Level Security (CLS) of Logi Report allow you to control user access to different subsets of data and ensure that people only see what they need to see. This topic describes how you can use RLS and CLS.

RLS enables you to define which records are to be revealed to any given user, while CLS enables you to define which report column is revealed to any given user. This enables you to provide different users with accordingly different, but appropriate contents. No matter to whom you need to provide information, a plant manager or thousands of customers, Logi Report enables you to control access to information according to your requirements.

In Logi Report Designer, you can define two types of the RLS and CLS security policies: one is a security policy based on a catalog data source (data source scope security policy), and the other is a security policy based on a single report (report scope security policy).

* **Data source scope security**  
  You can build data source scope security policies, where each security policy refers to a catalog data source in the catalog. If you want to implement the same security policy in a group of reports, you can simply apply an existing security policy to the report, without having to repeatedly build security information for each report. Both RLS and CLS can be data source scope security.
* **Report scope security**   
  RLS can also be of report scope, based on the security information file. You can use the security information file to set the security policies for a report. Report scope security policy does not support CLS.

You can apply RLS simultaneously to both data source and report scopes. However, if you have already applied a report scope security policy to a report, it will override a data source scope security policy that you applied to the report. That is, report scope security policies have a higher priority than data source scope security policies.

After setting up the security policy for a report in Designer, you can then publish it to Server as normal. Then, when you sign in to the server as different users, you will find that Server applies the security settings to the report. That is, different users will only see the data they are supposed to see.

For more information, see Applying Record Level and Column Level Security in the *Logi Report Designer Guide*.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)Server may not recognize the users and roles that the report designer defined. If your security policies contain such users/roles, create these users and roles respectively in Server, and then in Designer, synchronize the security information with Server using the **Merge** option.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741469954327-Cached-Report-Bursting)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741455041943-Business-View-Security)
