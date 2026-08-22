---
title: "Group Options Dialog Box Properties"
id: 5741459041175
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741459041175-Group-Options-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:35Z
---

# Group Options Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445636887-Group-Header-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429972759-Image-Properties)

# Group Options Dialog Box Properties

This topic describes how you can use the Group Options dialog box to [set the sort order of the group values and define the number of the group values to show](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report#GroupOptions) in the chart.

Server displays the dialog box after you select the Top N button ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/9905632725527/btn_wbrpt_topn.gif) above the Area box when the chart type is Heat Map in the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741422293143-Chart-Wizard-Properties#Map), [Insert Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459162391-Insert-Chart-Dialog-Box-Properties#Map), [Convert to Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449393815-Convert-to-Chart-Dialog-Box-Properties#Map), or [To Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741437074583-To-Chart-Dialog-Box-Properties#Map), or in the Bind Data screen of chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Map).

![Group Options dialog](https://devnet.logianalytics.com/hc/article_attachments/9905730412695/grpoptn.gif)

**Group Order**

Specify in which manner you want to sort the group values.

* **Ascend**  
   Select to sort the group values in the ascending order (A, B, C).
* **Descend**  
   Select to sort the group values in the descending order (C, B, A).
* **No Sort**  
   Select to sort the group values in the order you defined in the catalog.

**Group Selection**

Specify the number of group values you want to display in the chart.

* **Select**  
   Specify the Select N condition to define the number of the group values you want to display.
  + **All**  
     Select if you want to display all group values in the chart.
  + **Top N**  
     Select **Top N**, and then specify a number N in the field to the right, if you want to display the first N group values in the chart. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Top N condition.
  + **Bottom N**  
     Select **Bottom N**, and then specify a number N in the field to the right, if you want to display the last N group values in the chart. You can also select a parameter from the drop-down list, which returns an integer, and then specify a value for the parameter when viewing the report to dynamically define the Bottom N condition.
* **Based On**  
   Select **Based On**, and then you can select a field added to the value axis of the chart to sort the group values based on this field, or select **Custom Sort** to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties).
* **Remaining Groups In**  
   Enabled for Top N or Bottom N. Select this option, and then type a category name in the text box to include all the group values beyond the top/bottom N range.
* **Overall Series**  
  Not supported on group values.
* **Skip First**  
   Enabled for Top N or Bottom N. If you type a number M here, Server will skip the first M group values in the chart, and the Select N condition will take effect beginning with the M+1 value. The skipped values will be included in the remaining group together with all the group values beyond the top/bottom N range.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445636887-Group-Header-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429972759-Image-Properties)
