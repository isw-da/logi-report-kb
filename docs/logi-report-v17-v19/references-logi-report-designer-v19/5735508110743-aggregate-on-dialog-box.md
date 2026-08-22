---
title: "Aggregate On Dialog Box"
id: 5735508110743
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735508110743-Aggregate-On-Dialog-Box
updated_at: 2022-11-02T08:20:18Z
---

# Aggregate On Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521846423-Advanced-Export-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513162391-Applet-Parameter-Dialog-Box)

# Aggregate On Dialog Box

You can use the Aggregate On dialog box to [calculate data using the field in the detail column](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables#Aggregate). This topic describes the options in the dialog box.

Designer displays the Aggregate On dialog box when you right-click a detail column in a table and select Aggregate On from the shortcut menu.

![Aggregate On dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933789042327/agrgton.gif)

Designer displays these options:

**Aggregate On**

This option shows the field bound with the detail column. The field is also the one on which the summary is based.

**Aggregate Function**

This drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you can use to compute the field in the detail column. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/7933688270615/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

**Group By**

If you select this option, you can select a group-by field from the drop-down list below, to which to apply the summary (if you do not select a field, the summary applies to the whole dataset); if you do not select this option, Designer creates a dynamic summary.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521846423-Advanced-Export-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513162391-Applet-Parameter-Dialog-Box)
