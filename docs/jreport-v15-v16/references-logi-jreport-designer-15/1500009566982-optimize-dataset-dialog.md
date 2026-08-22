---
title: "Optimize Dataset Dialog"
id: 1500009566982
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566982-Optimize-Dataset-Dialog
updated_at: 2021-07-24T05:54:59Z
---

# Optimize Dataset Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566962-Open-Report-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog)

# Optimize Dataset Dialog

The Optimize Dataset dialog appears when you select the Optimize Dataset button in the [Manage Datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500009587781-Manage-Datasets-Dialog) dialog. It helps you to [optimize the selected dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets#Optimize). [See the dialog](javascript:%20void(null)).

![Optimize Dataset dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889298967/optmzdtst.gif)

The following are details about options in this dialog:

**Data retrieved for the dataset**

Specifies the method used to retrieve data at runtime.

* **Only Columns Used in Report**  
   If checked, only data columns used in the current report are retrieved at runtime. This way ensures the best performance since the least data is involved in.
* **All Columns in Dataset**  
   If checked, all data columns defined in the dataset are retrieved at runtime.
* **All Columns in Query**  
   If checked, all data columns in the query that the dataset is based on are retrieved at runtime. The performance of this way is not as good as the other two.

**OK**

Applies the settings and closes the dialog.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566962-Open-Report-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog)
