---
title: "Aggregate On Dialog"
id: 1500010064801
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064801-Aggregate-On-Dialog
updated_at: 2021-07-24T10:39:10Z
---

# Aggregate On Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029782-Advanced-Export-Settings-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064821-Applet-Parameter-Dialog)

# Aggregate On Dialog

The Aggregate On dialog helps you to [calculate data using the field in the detail column](https://devnet.logianalytics.com/hc/en-us/articles/1500010029302-Modifying-Tables#Aggregate). It appears when you right-click a detail column in a table and select Aggregate On from the shortcut menu.

![Aggregate On dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901294871/agrgton.gif)

**Aggregate On**

Displays the field bound with the detail column. The field is also the one on which the summary is based.

**Aggregate Function**

Specifies the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) to compute the field in the detail column. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.

**Group By**

* If checked, you can select a group-by field from the drop-down list below, to which the summary will be applied. If no field is selected, the summary will be applied to the whole dataset.
* If unchecked, a dynamic summary will be created.

**OK**

Summarizes the detail column data with the specified function and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029782-Advanced-Export-Settings-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064821-Applet-Parameter-Dialog)
