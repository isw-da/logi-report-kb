---
title: "Automatically Recompiling Dynamic Resources in Reports"
id: 1500009748722
section: "Managing Resources"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748722-Automatically-Recompiling-Dynamic-Resources-in-Reports
updated_at: 2021-07-24T00:47:56Z
---

# Automatically Recompiling Dynamic Resources in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements)

# Automatically Recompiling Dynamic Resources in Reports

This topic describes how you can recompile dynamic formulas and aggregations in reports upon changes of business views, on Logi Report Server as an administrator.

When you made changes to business views, such as modifying mapping names of data columns, and changing a referenced field, you need to recompile dynamic formulas and aggregations in reports that you created based on those business views, to work with the reports normally. You can achieve this directly on Server if you are an administrator. There is no longer the need to download reports into Logi Report Designer, re-save the dynamic resources there, and then republish the reports back to Server. This is convenient and time-saving when there are many reports involved, especially when you do not have a Designer at hand.

To recompile dynamic resources in reports upon changes in business views, take the following steps:

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Other** > **Batch Refresh Dynamic Resources** from the drop-down menu. Server displays the following page.

   ![Batch Refresh Dynamic Resources](https://devnet.logianalytics.com/hc/article_attachments/4404880289943/mng_rsc_rcmpl.gif)
2. Select **Browse** to choose the catalog where the changed business views reside, from the server resource tree.
3. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404885412247/btn_chsr6.gif) to choose a folder in which there are reports that run with the above catalog, from the server resource tree. Each time you can recompile based on one catalog and one folder. If your server's workload and performance enables and you have enough time, you can choose a parent folder that contains all such folders, or simply choose the root directory of the server resource tree if you are not quite clear about where the reports are. Otherwise, start from a folder without a subfolder in it and do the work multiple times.
4. Select **OK** to start recompiling the dynamic resources in the reports that run with the specified catalog, in the specified folder (including its sub folders). The process might take a long while depending on the quantity of the dynamic resources to recompile and the reports to refresh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements)
