---
title: "Aggregate On Dialog"
id: 1500009607262
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607262-Aggregate-On-Dialog
updated_at: 2021-07-24T16:05:00Z
---

# Aggregate On Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629901-Advanced-Export-Settings-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607282-Applet-Parameter-Dialog)

# Aggregate On Dialog

The Aggregate On dialog helps you to [calculate data using the field in the detail column](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables#Aggregate). It appears when you right-click a detail column in a table and select Aggregate On from the shortcut menu.

![Aggregate On dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916819479/agrgton.gif)

**Aggregate On**

Displays the field bound with the detail column. The field is also the one on which the summary is based.

**Aggregate Function**

Specifies the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) to compute the field in the detail column. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Group By**

* If the option is selected, you can select a group-by field from the drop-down list below, to which the summary will be applied. If no field is selected, the summary will be applied to the whole dataset.
* If the option is unselected, a dynamic summary will be created.

**OK**

Summarizes the detail column data with the specified function and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629901-Advanced-Export-Settings-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607282-Applet-Parameter-Dialog)
