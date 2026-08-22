---
title: "Category Options Dialog Box Properties"
id: 5741434586391
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741434586391-Category-Options-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:19Z
---

# Category Options Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741434258071-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741449307031-Chart-Properties)

# Category Options Dialog Box Properties

This topic describes how you can use the Category Options dialog box to [set the sort order of the category values and define the number of the category values to show](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report#SlctN) in a chart.

Server displays the dialog box when you select the Top N button ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/9905632725527/btn_wbrpt_topn.gif) above the category box in the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741422293143-Chart-Wizard-Properties), [Insert Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459162391-Insert-Chart-Dialog-Box-Properties), [Convert to Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449393815-Convert-to-Chart-Dialog-Box-Properties), or [To Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741437074583-To-Chart-Dialog-Box-Properties), or in the Bind Data screen of chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Chart).

![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/9905620483479/ctgryoptn.gif)

**Category Order**

Specify the order in which you want to display data on the category axis of a chart.

* **Ascend**  
   Select to display data in an ascending order.
* **Descend**  
   Select to display data in a descending order.
* **No Sort**  
   Select to keep the data in their original order as you see in the catalog.

**Category Selection**

Specify the number of the category values that you want to display in the chart.

* **Select**  
   Specify the Select N condition to define the number of the category values you want to display.
  + **All**  
     Select to display all category values.
  + **Top N**  
     Select **Top N** and then specify a number N in the field to the right if you want to display the first N category values.
  + **Bottom N**  
     Select **Bottom N** and then specify a number N in the field to the right if you want to display the last N category values.
* **Based On**  
   Select and then you can select a field that you added to the value axis of the chart, to sort the category values based on this field, or select **Custom Sort** to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties).
* **Remaining Categories In**  
   Select and then type a character string in the text box, to group all the category values beyond the top/bottom N range. Server enables this property when you select **Top N** or **Bottom N** from the Select drop-down list.
* **Overall Series**  
   Select to calculate the top or bottom N category values based on the series values. Server enables this property when you select **Top N** or **Bottom N** from the **Select** drop-down list.
* **Skip First**  
   If you type a number M in the Skip First text box, Server will skip the first M category values in the chart, and the Select N condition will take effect beginning with M+1. Server includes the skipped values in the Remaining Categories group together with all the category values beyond the top/bottom N range.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741434258071-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741449307031-Chart-Properties)
