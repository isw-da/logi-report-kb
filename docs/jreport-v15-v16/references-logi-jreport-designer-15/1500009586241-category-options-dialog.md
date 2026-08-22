---
title: "Category Options Dialog"
id: 1500009586241
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586241-Category-Options-Dialog
updated_at: 2021-07-24T05:55:30Z
---

# Category Options Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564982-Category-Property-Dialog)

# Category Options Dialog

The Category Options dialog appears when you select the Order/Select N button below the category box in the Display screen of the chart wizard. It helps you to [specify the sort order of the category values and define the number of the category values](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#SelectN) that will be displayed in a chart. [See the dialog](javascript:%20void(null)).

![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893932823/ctgryoptn.gif)

The following are details about options in the dialog:

**Category Order**

Specifies in which manner to sort the category values.

* **Ascend**  
   Values will be sorted in an ascending order (A, B, C).
* **Descend**  
   Values will be sorted in a descending order (C, B, A).
* **No Sort**  
   Values will be sorted in the original order in database.

**Category Selection**

Specifies the number of the category values that will be displayed in the chart.

* **Select**Specifies the Select N condition to define the number of the category values that will be displayed.
  + **All**  
     If selected, all category values in the chart will be displayed.
  + **Top N**   
     If selected, specify a number in the field to the right and the first N category values in the chart will be displayed. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Top N condition.
  + **Bottom****N**  
     If selected, specify a number in the field to the right and the last N category values in the chart will be displayed. You can also select a parameter from the drop-down list which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Bottom N condition.
* **Based On**If checked, the category values will be sorted by values of the summary selected with the direction specified. If unchecked, the category values will be sorted by the order specified in the Category Order box of the dialog.
* **Remaining Categories In**  
   Enabled only when Top N or Bottom N is selected from the Select drop-down list. Check this option and then type a character string in the text field to group all the category values beyond the top/bottom N range.
* **Overall Series**  
   Specifies whether to calculate the top or bottom N category values based on the series values. Enabled when Top N or Bottom N is selected from the Select drop-down list.
* **Skip First**  
   If you check the Skip First option and input a number M in the text field to the right, then the first M category values in the chart will be skipped and the Select N condition will take effect beginning with M+1. The skipped values will be included in the Remaining Categories group together with all the category values beyond the top/bottom N range. Enabled when Top N or Bottom N is selected from the Select drop-down list.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Discards the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564982-Category-Property-Dialog)
