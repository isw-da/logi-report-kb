---
title: "Group Options Dialog"
id: 1500009566322
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566322-Group-Options-Dialog
updated_at: 2021-07-24T05:55:08Z
---

# Group Options Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566302-Group-Filter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587521-Horizontal-Banded-Wizard-Dialog)

# Group Options Dialog

The Group Options dialog appears when you select the Order/Select N button in the Display screen of the chart wizard when the chart type is heat map. It helps you to [specify the sort order of the group values and define the number of the group values](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#SelectN) that will be displayed in a chart. [See the dialog](javascript:%20void(null)).

![Group Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893877783/grpoptn.gif)

The following are details about options in the dialog:

**Group Order**

Specifies in which manner to sort the group values.

* **Ascend**  
   Values will be sorted in an ascending order (A, B, C).
* **Descend**  
   Values will be sorted in a descending order (C, B, A).
* **No Sort**  
   Values will be sorted in the original order in database.

**Group Selection**

Specifies the number of group values that will be displayed in the chart.

* **Select**  
   Specifies the Select N condition to define the number of the group values that will be displayed.
  + **All**  
     If selected, all group values in the chart will be displayed.
  + **Top N**   
     If selected, specify a number in the field to the right and the first N group values in the chart will be displayed. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Top N condition.
  + **Bottom****N**  
     If selected, specify a number in the field to the right and the last N group values in the chart will be displayed. You can also select a parameter from the drop-down list which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Bottom N condition.
* **Based On**  
   If checked, the group values will be sorted by values of the summary selected with the direction specified. If unchecked, the group values will be sorted by the order specified in the Group Order box of the dialog.
* **Remaining Categories In**  
   Enabled only when Top N or Bottom N is selected from the Select drop-down list. Check this option and then type a character string in the text field to group all the group values beyond the top/bottom N range.
* **Overall Series**  
   Not supported on group values.
* **Skip First**  
  If you check the Skip First option and input a number M in the text field to the right, then the first M group values in the chart will be skipped and the Select N condition will take effect beginning with the M+1 value. The skipped values will be included in the remaining group together with all the group values beyond the top/bottom N range. Enabled when Top N or Bottom N is selected from the Select drop-down list.

**OK**

Accepts the changes and exits the dialog.

**Cancel**

Discards the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566302-Group-Filter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587521-Horizontal-Banded-Wizard-Dialog)
