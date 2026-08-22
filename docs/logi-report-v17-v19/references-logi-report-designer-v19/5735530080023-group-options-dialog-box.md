---
title: "Group Options Dialog Box"
id: 5735530080023
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735530080023-Group-Options-Dialog-Box
updated_at: 2022-11-02T04:37:41Z
---

# Group Options Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735530070167-Group-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523560599-Horizontal-Banded-Wizard-Dialog-Box)

# Group Options Dialog Box

You can use the Group Options dialog box to [specify the sort order of the group values and define the number of the group values to show](https://devnet.logianalytics.com/hc/en-us/articles/5735498861207-Modifying-Charts#SelectN) in a heat map. This topic describes the options in the dialog box.

Designer displays the Group Options dialog box when you select Order/Select N in the Display screen of the chart wizard.

![Group Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898479392279/grpoptn.gif)

Designer displays these options:

**Group Order**

You can specify how to sort the group values in this box.

* **Ascend**  
  Select to sort values in an ascending order (A, B, C).
* **Descend**  
  Select to sort values in a descending order (C, B, A).
* **No Sort**  
  Select to sort values in the original order in database.

**Group Selection**

You can specify the number of the group values to display in the chart in this box.

* **Select**
  + **All**  
    Select to display all the group values in the chart.
  + **Top N**   
    Select and specify a number in the text box to display the first N group values in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Top N condition at runtime.
  + **Bottom N**  
    Select and specify a number in the text box to display the last N group values in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Bottom N condition at runtime.
* **Based On**  
  Select it and select a field that you have added to the value axis of the chart from the drop-down list to sort the group values based on this field. You can also select Custom Sort from the drop-down list to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box).
  + **Ascend**  
    Select to sort the group values based on the specified field in an ascending order.
  + **Descend**  
    Select to sort the group values based on the specified field in a descending order.
* **Remaining Groups In**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a character string in the text box to place all the group values beyond the top/bottom N range in this group.
* **Overall Series**  
  Designer does not enable this option for setting group values.
* **Skip First**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a number M in the text box to skip the first M group values in the chart, meaning the Select N condition takes effect beginning with the M+1 value. Designer includes the skipped values in the remaining group together with all the group values beyond the top/bottom N range.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735530070167-Group-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523560599-Horizontal-Banded-Wizard-Dialog-Box)
