---
title: "Aggregate On Dialog Box"
id: 4405661457431
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661457431-Aggregate-On-Dialog-Box
updated_at: 2022-01-27T20:35:13Z
---

# Aggregate On Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664427671-Advanced-Export-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664429463-Applet-Parameter-Dialog-Box)

# Aggregate On Dialog Box

You can use the Aggregate On dialog box to [calculate data using the field in the detail column](https://devnet.logianalytics.com/hc/en-us/articles/4405664405527-Modifying-Tables#Aggregate). This topic describes the options in the dialog box.

Designer displays the Aggregate On dialog box when you right-click a detail column in a table and select Aggregate On from the shortcut menu.

![Aggregate On dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402539671/agrgton.gif)

You see the following options in the dialog box:

**Aggregate On**

This option shows the field bound with the detail column. The field is also the one on which the summary is based.

**Aggregate Function**

This drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) that you can use to compute the field in the detail column. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box).

**Group By**

If you select this option, you can select a group-by field from the drop-down list below, to which to apply the summary (if you do not select a field, the summary applies to the whole dataset); if you do not select this option, Designer creates a dynamic summary.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664427671-Advanced-Export-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664429463-Applet-Parameter-Dialog-Box)
