---
title: "Series Options Dialog Box Properties"
id: 1500009747962
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:14Z
---

# Series Options Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748042-Select-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747982-Share-Report-Dialog-Box-Properties)

# Series Options Dialog Box Properties

This topic describes how you can use the Series Options dialog box to [set the sort order of the series values and define the number of the series values to show](https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report#SlctN) in a chart.

Server displays the dialog box when you select the Top N button ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif) above the series box in the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009775021-Chart-Wizard-Properties), [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009747582-Insert-Chart-Dialog-Box-Properties) dialog box, [Convert to Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009746782-Convert-to-Chart-Dialog-Box-Properties) dialog box, or [To Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009748162-To-Chart-Dialog-Box-Properties) dialog box, or the Bind Data screen of chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties#Chart).

![Series Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880340119/seriesoptn.gif)

**Series Order**

Specifies in which order data on the series axis will be displayed.

* **Ascend**  
   Lists data in an ascending order.
* **Descend**  
   Lists data in a descending order.
* **No Sort**  
   Keeps the data in their original order in database.

**Series Selection**

Specifies the number of the series values that will be displayed in the chart.

* **Select**  
   Specifies the Select N condition to define the number of series values that will be displayed.
  + **All**  
     If selected, all series values will be displayed.
  + **Top N**   
     If selected, specify a number in the field to the right and the first N series values will be displayed.
  + **Bottom** **N**  
     If selected, specify a number in the field to the right and the last N series values will be displayed.
* **Based On**  
   If the option is selected, you can select a field added to the value axis of the chart to sort the series values based on this field, or select Custom Sort to customize the sort manner in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box.
* **Remaining Series In**  
   Enabled when Top N or Bottom N is selected from the Select drop-down list. Select this option and then type a character string in the text box to group all the series values beyond the top/bottom N range.
* **Overall Series**  
   Not supported on series values.
* **Skip First**  
   If you type a number M in the Skip First text box, the first M series values in the chart will be skipped and the Select N condition will take effect beginning with M+1. The skipped values will be included in the Remaining Series group together with all the series values beyond the top/bottom N range.

**OK**

Accepts the changes and closes the dialog box.

**Cancel**

Discards the changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the selection and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748042-Select-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747982-Share-Report-Dialog-Box-Properties)
