---
title: "Converting Resources of Earlier Versions into Current Version"
id: 1500009750061
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750061-Converting-Resources-of-Earlier-Versions-into-Current-Version
updated_at: 2021-07-25T07:18:59Z
---

# Converting Resources of Earlier Versions into Current Version

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path)

# Converting Resources of Earlier Versions into Current Version

If your Logi Report Server contains resources earlier than V8 such as reports, visual analysis, library components, dashboards, catalogs, etc., during each server runtime lifecycle when you run such a resource for the first time, Logi Report Engine has to first convert the earlier version resource into a current version resource before running the resource. This may result in decreased performance. To avoid this, Logi Report Server allows administrators to permanently convert resources earlier than V8 in the server resource tree to adapt to the current version.

You have the following two ways to convert resources:

* **Converting via UI**

  The converting UI is available to administrators only. It is used to convert all resources earlier than V8 in the My Reports folder or Public Reports folder. The converted resources are stored in the same directory.

  1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Other** > **Converting** from the drop-down menu to display the Converting page.

     ![Converting Resources](https://devnet.logianalytics.com/hc/article_attachments/4404936800919/mng_rsc_cnvt.gif)
  2. Specify the folders which contain the resources you want to convert.
  3. Specify how to save the converted resources.
     + **Replace the Old Resource**  
        Replaces the old resources with the converted resources.
     + **Save as New Versions**  
        Saves the converted resources as new resource versions in the resource tree.
  4. When done, select **OK** to start converting.
* **Converting using tool**

  You can also use [rptconv.bat/rptconv.sh](https://devnet.logianalytics.com/hc/en-us/articles/1500009749961-Running-as-a-Standalone-Server#rptconv.bat) located in the `<install_root>\bin` directory to convert a resource and a type of resources or all resources earlier than V8 in a directory to current version.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path)
