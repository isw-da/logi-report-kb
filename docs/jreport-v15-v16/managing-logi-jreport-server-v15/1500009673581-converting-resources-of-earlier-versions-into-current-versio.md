---
title: "Converting Resources of Earlier Versions into Current Version"
id: 1500009673581
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673581-Converting-Resources-of-Earlier-Versions-into-Current-Version
updated_at: 2021-07-24T20:54:04Z
---

# Converting Resources of Earlier Versions into Current Version

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673661-Searching-for-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path)

# Converting Resources of Earlier Versions Into Current Version

If your Logi JReport Server contains resources earlier than V8 such as reports, visual analysis, library components, dashboards, catalogs, etc., during each server runtime lifecycle when you run such a resource for the first time, the Logi JReport Engine has to first convert the earlier version resource into a current version resource before running the resource. This may result in decreased performance. To avoid this, Logi JReport Server allows administrators to permanently convert resources earlier than V8 in the server resource tree to adapt to the current version.

You have the following two ways to convert resources:

* **Converting via the Administration UI**

  The converting UI is available to administrators only. It is used to convert all resources earlier than V8 in the My Reports folder or Public Reports folder. The converted resources are stored in the same directory.

  1. On the Logi JReport Administration page, select **Resources** on the system toolbar, then select **Converting** from the drop-down menu.
  2. Specify the folders which contain the resources you want to convert.
  3. Specify how to save the converted resources.
     + **Replace the Old Resource**  
        Replaces the old resources with the converted resources.
     + **Save as New Versions**  
        Saves the converted resources as new resource versions in the resource tree.
  4. When done, select **OK** to start converting.
* **Converting using tool**

  You can also use [rptconv.bat/rptconv.sh](https://devnet.logianalytics.com/hc/en-us/articles/1500009673341-Running-as-a-Standalone-Server#rptconv.bat) located in the `<install_root>\bin` directory to convert a resource and a type of resources or all resources earlier than V8 in a directory to current version.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673661-Searching-for-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path)
