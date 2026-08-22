---
title: "Recovering and Synchronizing In-memory Cubes"
id: 1500009673461
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673461-Recovering-and-Synchronizing-In-memory-Cubes
updated_at: 2021-07-24T20:54:05Z
---

# Recovering and Synchronizing In-memory Cubes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648982-Managing-Triggers)

# Recovering and Synchronizing In-Memory Cubes

If an in-memory cube is updating when the server shuts down, the cube will be disabled after the server restarts. Administrators need to enable the cube task in order for the cube to continue to update at the next scheduled time.

## Synchronizing In-Memory Cubes With Catalog Republish

After a catalog is republished, how the existing in-memory cubes based on the old business views in the catalog will be updated depends on the following conditions:

If no business view is modified, the existing in-memory cubes will be automatically applicable to the new catalog.

If a business view is modified, the in-memory cube based on the old business view will behave as follows:

* Before the next schedule time, the cube will be disabled for retrieving data to reports.
* When it is the next schedule time, data is fetched from the new business view to generate an updated cube:
  + If new parameters are added in the new business view, default values will be used until an administrator specifies values to them.
  + If old parameters are deleted from the new business view, the parameter values previously specified in the cube will be removed.
  + If parameters are changed and the previously specified values do not match the type, error messages will be given in the server error log and the cube is disabled for service.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648702-Viewing-and-Managing-the-Cube-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648982-Managing-Triggers)
