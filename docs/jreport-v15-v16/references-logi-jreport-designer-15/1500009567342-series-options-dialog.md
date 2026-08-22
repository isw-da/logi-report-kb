---
title: "Series Options Dialog"
id: 1500009567342
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009567342-Series-Options-Dialog
updated_at: 2021-07-24T05:54:52Z
---

# Series Options Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588741-Send-Message-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588581-Set-Grids-Dialog)

# Series Options Dialog

The dialog appears when you select the Order/Select N button below the series box in the Display screen of the chart wizard. It helps you to [specify the sort order of the series values and define the number of the series values](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#SelectN) that will be displayed in a chart. [See the dialog](javascript:%20void(null)).

![Series Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893856535/seriesoptn.gif)

The following are details about options in the dialog:

**Series Order**

Specifies in which manner to sort the series values.

* **Ascend**  
  Values will be sorted in an ascending order (A, B, C).
* **Descend**  
  Values will be sorted in a descending order (C, B, A).
* **No Sort**  
  Values will be sorted in the original order in database.

**Series Selection**

Specifies the number of series values that will be displayed in the chart.

* **Select**  
  Specifies the Select N condition to define the number of the series values that will be displayed.
  + **All**  
    If selected, all series values in the chart will be displayed.
  + **Top N**   
    If selected, specify a number in the field to the right and the first N series values in the chart will be displayed. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Top N condition.
  + **Bottom****N**  
    If selected, specify a number in the field to the right and the last N series values in the chart will be displayed. You can also select a parameter from the drop-down list which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Bottom N condition.
* **Based On**  
  If checked, the series values will be sorted by values of the summary selected with the direction specified. If unchecked, the series values will be sorted by the order specified in the Series Order box of the dialog.
* **Remaining Series In**  
  Enabled only when Top N or Bottom N is selected from the Select drop-down list. Check this option and then type a character string in the text field to group all the series values beyond the top/bottom N range.
* **Overall Series**  
  Not supported on series values.
* **Skip First**  
  If you check the Skip First option and input a number M in the text field to the right, then the first M series values in the chart will be skipped and the Select N condition will take effect beginning with M+1. The skipped values will be included in the Remaining Series group together with all the series values beyond the top/bottom N range. Enabled when Top N or Bottom N is selected from the Select drop-down list.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Discards the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588741-Send-Message-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009588581-Set-Grids-Dialog)
