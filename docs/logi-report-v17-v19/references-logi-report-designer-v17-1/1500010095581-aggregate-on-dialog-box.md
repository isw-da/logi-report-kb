---
title: "Aggregate On Dialog Box"
id: 1500010095581
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095581-Aggregate-On-Dialog-Box
updated_at: 2021-07-23T19:15:03Z
---

# Aggregate On Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058022-Advanced-Export-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095601-Applet-Parameter-Dialog-Box)

# Aggregate On Dialog Box

You can use the Aggregate On dialog box to [calculate data using the field in the detail column](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#Aggregate). This topic describes the options in the dialog box.

Designer displays the Aggregate On dialog box when you right-click a detail column in a table and select Aggregate On from the shortcut menu.

![Aggregate On dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848636567/agrgton.gif)

You see the following options in the dialog box:

**Aggregate On**

The option shows the field bound with the detail column. The field is also the one on which the summary is based.

**Aggregate Function**

The drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you can use to compute the field in the detail column. Select the function you need.

* **Distinct On**  
  Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

**Group By**

* If you select the option, you can select a group-by field from the drop-down list below, to which to apply the summary. If you do not select a field, the summary applies to the whole dataset.
* If you do not select the option, Designer creates a dynamic summary.

**OK**

Select to apply the settings to summarize the detail column data with the specified function.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058022-Advanced-Export-Settings-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095601-Applet-Parameter-Dialog-Box)
