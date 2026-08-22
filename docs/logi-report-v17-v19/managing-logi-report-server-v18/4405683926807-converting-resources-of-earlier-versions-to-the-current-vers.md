---
title: "Converting Resources of Earlier Versions to the Current Version"
id: 4405683926807
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683926807-Converting-Resources-of-Earlier-Versions-to-the-Current-Version
updated_at: 2022-01-27T07:59:38Z
---

# Converting Resources of Earlier Versions to the Current Version

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690643479-Getting-and-Using-Resources-From-a-Real-Path)

# Converting Resources of Earlier Versions to the Current Version

This topic describes how you can convert resources earlier than V8 to adapt to the current version using the Server Console or a tool.

If your Logi Report Server contains resources earlier than V8, such as reports, visual analysis, library components, dashboards, and catalogs, during each server runtime lifecycle when you run such a resource for the first time, Logi Report Engine has to first convert the earlier version resource to the current version resource before running the resource. This may result in decreased performance. To avoid this, Server enables administrators to permanently convert resources earlier than V8 in the server resource tree to adapt to the current version.

You can use the two ways to convert resources:

* **Converting resources via UI**

  The converting UI is available to administrators only. You can use it to convert the resources earlier than V8 in the My Reports folder or Public Reports folder. Server stores the converted resources in the same directory.

  1. On the system toolbar of the Server Console, navigate to **Administration** > **Other** > **Converting**. Server displays the Converting page.

     ![Converting Resources](https://devnet.logianalytics.com/hc/article_attachments/4420447188503/mng_rsc_cnvt.gif)
  2. Select the folders that contain the resources you want to convert.
  3. Specify how you want to save the converted resources.
     + **Replace the Old Resource**  
        Server replaces the old resources with the converted resources.
     + **Save as New Versions**  
        Select if you want to save the converted resources as new resource versions in the resource tree.
  4. Select **OK** to start converting.
* **Converting resources using a tool**

  You can also use [rptconv.bat/rptconv.sh](https://devnet.logianalytics.com/hc/en-us/articles/4405690640535-Running-Logi-Report-Server-as-a-Standalone-Server#rptconv.bat) in the `<install_root>\bin` directory to convert a resource, a type of resources, or all resources earlier than V8 in a directory to current version.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690643479-Getting-and-Using-Resources-From-a-Real-Path)
