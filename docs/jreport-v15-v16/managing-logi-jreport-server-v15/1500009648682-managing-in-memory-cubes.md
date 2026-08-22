---
title: "Managing In-memory Cubes"
id: 1500009648682
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648682-Managing-In-memory-Cubes
updated_at: 2021-07-24T20:54:06Z
---

# Managing In-memory Cubes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648662-Managing-Scheduled-CRD-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes)

# Managing In-Memory Cubes

In-memory cubes are cached data of business views. They are created by caching pre-computed aggregation functions called measures. Reports and visualizations use the cube data to improve performance.

The generating and updating of in-memory cubes are achieved by scheduling cube tasks. In-memory cubes are similar to scheduled reports that can be run immediately, run once at a specific time or run periodically to select the data from the DBMS and store it in Logi JReport Server. After an in-memory cube is created and ready for use, all web reports, library components, and visual analyses that use the same business view as the in-memory cube will automatically use the cube rather than go to the database for the data. By applying in-memory cubes, your reporting performance will be greatly improved.

The following topics shows how to create, use and manage in-memory cubes as follows:

* [Creating In-Memory Cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes)
* [Viewing and Managing the Cube Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks)
* [Recovering and Synchronizing In-Memory Cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009673461-Recovering-and-Synchronizing-In-memory-Cubes)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648662-Managing-Scheduled-CRD-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes)
