---
title: "Managing Cached Report Data"
id: 1500009673381
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673381-Managing-Cached-Report-Data
updated_at: 2021-07-24T20:54:07Z
---

# Managing Cached Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673541-Migrating-Server-Data-from-One-Machine-to-Another)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673401-Creating-Cached-Report-Data-Automatically)

# Managing Cached Report Data

Cached report data (CRD) is a cached subset of data fetched from the database and is used as a substitute for the database for retrieving data for reports. This provides several benefits:

* Reports can be run from a specific point in time such as a month end report or quarter end report without going back to the DBMS to get the original data.
* Many users can run reports from data cached from a single data resource without impacting production DBMS users.
* Users running a report will all see the same view of the data, thus the data will not change minute by minute based on current DBMS updates.
* Cached report data can be scheduled for any time frame to simulate real time on-demand reporting for many users while not slowing down the production DBMS.

Cached report data can be created for data resources including queries, stored procedures, imported SQLs, user-defined data sources, hierarchical data sources, and parameters whose type is Bind with Single Column or Bind with Cascading Columns.

Administrators can either make cached report data created automatically (auto CRD) or schedule to have a cached data result created for a data resource and updated at a specific time or periodically (scheduled CRD).

* **Auto CRD**  
  Auto CRD are disabled for generation by default. Administrators can enable them and configure the maximum hard disk space for auto CRD and how long an auto CRD can be kept.
* **Scheduled CRD**  
  Using Logi JReport's scheduling mechanism, administrators are able to define when a cached data result for a data resource will be created and how it will be updated according to time. If a scheduled CRD is updating when the server shuts down, the CRD will continue with the update when the server restarts. The data before the shutdown will be maintained. Scheduled CRD have no version: once they are updated, only the latest are kept in the data resource.

The section contains the following topics:

* [Creating Cached Report Data Automatically](https://devnet.logianalytics.com/hc/en-us/articles/1500009673401-Creating-Cached-Report-Data-Automatically)
* [Scheduling Cached Report Data Results](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results)
* [Managing Scheduled CRD Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009648662-Managing-Scheduled-CRD-Tasks)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673541-Migrating-Server-Data-from-One-Machine-to-Another)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673401-Creating-Cached-Report-Data-Automatically)
