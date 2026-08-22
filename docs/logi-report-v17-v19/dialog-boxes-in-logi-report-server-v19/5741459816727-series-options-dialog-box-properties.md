---
title: "Series Options Dialog Box Properties"
id: 5741459816727
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741459816727-Series-Options-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:43Z
---

# Series Options Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741446516119-Share-Report-Dialog-Box-Properties)

# Series Options Dialog Box Properties

This topic describes how you can use the Series Options dialog box to [set the sort order of the series values and define the number of the series values to show](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report#SlctN) in a chart.

Server displays the dialog box when you select the Top N button ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/9905632725527/btn_wbrpt_topn.gif) above the series box in the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741422293143-Chart-Wizard-Properties), [Insert Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459162391-Insert-Chart-Dialog-Box-Properties), [Convert to Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449393815-Convert-to-Chart-Dialog-Box-Properties), or [To Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741437074583-To-Chart-Dialog-Box-Properties), or the Bind Data screen of chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741437169815-Web-Report-Wizard-Properties#Chart).

![Series Options dialog](https://devnet.logianalytics.com/hc/article_attachments/9905717830935/seriesoptn.gif)

**Series Order**

Specify the order in which you want to display data on the series axis.

* **Ascend**  
   Select to display data in an ascending order.
* **Descend**  
   Select to display data in a descending order.
* **No Sort**  
   Select to keep the data in their original order as you see in the catalog.

**Series Selection**

Specify the number of the series values you want to display in the chart.

* **Select**  
   Specify the Select N condition to define the number of series values you want to display.
  + **All**  
     Select to display all series values.
  + **Top N**  
     Select and then specify a number N in the field to the right if you want to display the first N series values.
  + **Bottom N**  
     Select and then specify a number N in the field to the right if you want to display the last N series values.
* **Based On**  
   Select and then you can select a field that you added to the value axis of the chart to sort the series values based on this field, or select **Custom Sort** to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties).
* **Remaining Series In**  
   Select and then type a character string in the text box to group all the series values beyond the top/bottom N range. Server enables this property when you select Top N or Bottom N from the **Select** drop-down list.
* **Overall Series**  
   Not supported on series values.
* **Skip First**  
   If you type a number M in the Skip First text box, Server will skip the first M series values in the chart, and the Select N condition will take effect beginning with M+1. Server includes the skipped values in the Remaining Series group together with all the series values beyond the top/bottom N range.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741446516119-Share-Report-Dialog-Box-Properties)
