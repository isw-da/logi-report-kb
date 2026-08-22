---
title: "Series Options Dialog Box"
id: 4405661699223
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661699223-Series-Options-Dialog-Box
updated_at: 2022-01-27T20:38:03Z
---

# Series Options Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661717911-Send-Message-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664566039-Set-Grids-Dialog-Box)

# Series Options Dialog Box

You can use the Series Options dialog box to [specify the sort order of the series values and define the number of the series values to show](https://devnet.logianalytics.com/hc/en-us/articles/4405664389143-Modifying-Charts#SelectN) in a chart. This topic describes the options in the dialog box.

Designer displays the Series Options dialog box when you select Order/Select N below the Series box in the Display screen of the chart wizard.

![Series Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542103703/seriesoptn.gif)

You see the following options in the dialog box:

**Series Order**

You can specify how to sort the series values in this box.

* **Ascend**  
  Select to sort values in an ascending order (A, B, C).
* **Descend**  
  Select to sort values in a descending order (C, B, A).
* **No Sort**  
  Select to keep the values in their original order in the database.

**Series Selection**

You can specify the number of the series values to display in the chart in this box.

* **Select**
  + **All**  
    Select to display all the series values in the chart.
  + **Top N**  
    Select and specify a number in the text box to display the first N series values in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Top N condition at runtime.
  + **Bottom N**  
    Select and specify a number in the text box to display the last N series values in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Bottom N condition at runtime.
* **Based On**  
  Select it and select a field that you have added to the value axis of the chart from the drop-down list to sort the series values based on this field. You can also select Custom Sort from the drop-down list to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664443927-Custom-Sort-Dialog-Box).
  + **Ascend**  
    Select to sort the series values based on the specified field in an ascending order.
  + **Descend**  
    Select to sort the series values based on the specified field in a descending order.
* **Remaining Series In**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a character string in the text box to group all the series values beyond the top/bottom N range.
* **Overall Series**  
  Designer does not enable this option for setting series values.
* **Skip First**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a number M in the text box to the right, Designer then skips the first M series values in the chart and the Select N condition takes effect beginning with M+1. Designer includes the skipped values in the remaining series group together with all the series values beyond the top/bottom N range.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661717911-Send-Message-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664566039-Set-Grids-Dialog-Box)
