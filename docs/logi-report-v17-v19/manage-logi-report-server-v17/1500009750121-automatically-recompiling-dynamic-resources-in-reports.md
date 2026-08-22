---
title: "Automatically Recompiling Dynamic Resources in Reports"
id: 1500009750121
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750121-Automatically-Recompiling-Dynamic-Resources-in-Reports
updated_at: 2021-07-25T07:18:58Z
---

# Automatically Recompiling Dynamic Resources in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements)

# This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Automatically Recompiling Dynamic Resources in Reports

When changes are made to business views, such as modifying mapping names of data columns, changing a referenced field, etc. dynamic formulas and aggregations in reports that were created based on those business views will need to be recompiled to work with the reports normally. This can now be accomplished directly in the Logi Report Server by administrators. There is no longer the need to download reports into Logi Report Designer, re-save the dynamic resources there, and then republish the reports back to the server. This is convenient and time-saving when there are many reports involved, especially when there is not a Logi Report Designer.

To recompile dynamic resources in reports upon changes in business views, take the following steps:

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Other** > **Batch Refresh Dynamic Resources** from the drop-down menu to open the following page.

   ![Batch Refresh Dynamic Resources](https://devnet.logianalytics.com/hc/article_attachments/4404936799127/mng_rsc_rcmpl.gif)
2. Select **Browse** to choose the catalog where the changed business views reside, from the server resource tree.
3. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404942502295/btn_chsr6.gif) to choose a folder in which there are reports that run with the above catalog, from the server resource tree. Each time you can recompile based on one catalog and one folder. If your server's workload and performance allows and you have enough time, you can choose a parent folder that contains all such folders, or simply choose the root directory of the server resource tree if you are not quite clear about where the reports are stored. Otherwise, start from a folder without a subfolder in it and do the work multiple times.
4. Select **OK** to start recompiling the dynamic resources in the reports that run with the specified catalog, in the specified folder (including its subfolders). The process might take a long while depending on the quantity of the dynamic resources to recompile and the reports to refresh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements)
