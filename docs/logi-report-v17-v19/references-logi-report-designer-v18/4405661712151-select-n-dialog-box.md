---
title: "Select N Dialog Box"
id: 4405661712151
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661712151-Select-N-Dialog-Box
updated_at: 2022-01-27T20:36:13Z
---

# Select N Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664573847-Select-Group-Position-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661713175-Select-Pre-join-Dialog-Box)

# Select N Dialog Box

You can use the Select N dialog box to specify the Select N condition to [filter the records or groups in a data component](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#SelectN). This topic describes the options in the dialog box.

Designer displays the Select N dialog box when you select Select N in the Group screen of the banded/table wizard, or in the Display screen of the map wizard.

![Select N dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556130071/slctn.gif)

You see the following options in the dialog box:

**In**

This option shows where to apply the Select N condition, the whole object or a specific group.

**Select N**

Specify the Select N condition.

* **All**  
  Select to display all the records, or all the groups in the specified group level in the data component.
* **Top N**  
  Select and specify a number in the text box below to display the first N records, or the first N groups in the specified group level in the data component. You can also select a parameter which returns an integer from the drop-down list to dynamically define the Top N condition.
* **Bottom N**  
  Select and specify a number in the text box below to display the last N records, or the last N groups in the specified group level in the data component. You can also select a parameter which returns an integer from the drop-down list to dynamically define the Bottom N condition.

**Other**

Designer enables this option when you use the dialog box for defining the Select N condition for a specific group level. Select it to display all the other groups of this group level that don't match the Select N condition (which are by default hidden) in another group. Specify the name for this group in the text box.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664573847-Select-Group-Position-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661713175-Select-Pre-join-Dialog-Box)
