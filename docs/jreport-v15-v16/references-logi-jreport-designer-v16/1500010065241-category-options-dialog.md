---
title: "Category Options Dialog"
id: 1500010065241
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065241-Category-Options-Dialog
updated_at: 2021-07-24T10:39:02Z
---

# Category Options Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065261-Category-Property-Dialog)

# Category Options Dialog

The Category Options dialog helps you to [specify the sort order of the category values and define the number of the category values to show](https://devnet.logianalytics.com/hc/en-us/articles/1500010063621-Modifying-Charts#SelectN) in a chart. It appears when you select the Order/Select N button below the category box in the Display screen of the chart wizard.

![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901274391/ctgryoptn.gif)

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

* **Select**  
   Specifies the Select N condition to define the number of the category values that will be displayed.
  + **All**  
     If selected, all category values in the chart will be displayed.
  + **Top N**  
     If selected, specify a number in the field to the right and the first N category values in the chart will be displayed. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Top N condition.
  + **Bottom N**  
     If selected, specify a number in the field to the right and the last N category values in the chart will be displayed. You can also select a parameter from the drop-down list which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Bottom N condition.
* **Based On**  
   If checked, select a field added to the value axis of the chart to sort the category values based on this field, or select Custom Sort to customize the sort manner in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010065201-Custom-Sort-Dialog) dialog.
  + **Ascend**  
     Sorts the category values based on the select field in an ascending order.
  + **Descend**  
     Sorts the category values based on the select field in a descending order.
* **Remaining Categories In**  
   Enabled only when Top N or Bottom N is selected from the Select drop-down list. Check this option and then type a character string in the text box to group all the category values beyond the top/bottom N range.
* **Overall Series**  
   Specifies whether to calculate the top or bottom N category values based on the series values. Enabled when Top N or Bottom N is selected from the Select drop-down list.
* **Skip First**  
   If you check the Skip First option and input a number M in the text box to the right, then the first M category values in the chart will be skipped and the Select N condition will take effect beginning with M+1. The skipped values will be included in the Remaining Categories group together with all the category values beyond the top/bottom N range. Enabled when Top N or Bottom N is selected from the Select drop-down list.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Discards the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065261-Category-Property-Dialog)
