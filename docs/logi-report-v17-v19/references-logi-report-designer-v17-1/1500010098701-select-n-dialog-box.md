---
title: "Select N Dialog Box"
id: 1500010098701
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box
updated_at: 2021-07-23T19:15:59Z
---

# Select N Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060482-Select-Group-Position-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098721-Select-Pre-join-Dialog-Box)

# Select N Dialog Box

The Select N dialog box helps you to specify a number to [filter groups to be displayed in the report](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#SelectN), or a parameter which returns an integer to filter group dynamically when previewing the report. It appears when you select the Select N button in the Group screen of the banded/table wizard, or in the Display screen of the map wizard.

![Select N dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848494487/slctn.gif)

The following are details about options in the dialog box:

**In**

Indicates where the Select N condition will be applied.

**Select N**

Specifies the Select N condition to define groups that will be displayed while others are hidden.

* **All**  
   If selected, all groups in the report will be displayed.
* **Top N**  
   If selected, specify a number in the field below and the first N groups in the report will be displayed. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Top N condition.
* **Bottom N**  
   If selected, specify a number in the field below and the last N groups in the report will be displayed. You can also select a parameter from the drop-down list which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Bottom N condition.

**Other**

If the option is selected, all the other records that don't match the Select N condition will be displayed (which are by default hidden) in another group. Specify a name for this group as required.

This option is available only when the Select N condition is applied to a certain group.

**OK**

Accepts the changes and closes the dialog box.

**Cancel**

Discards the changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060482-Select-Group-Position-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098721-Select-Pre-join-Dialog-Box)
