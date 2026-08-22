---
title: "Category Options"
id: 1500009689722
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009689722-Category-Options
updated_at: 2021-11-03T06:57:26Z
---

# Category Options

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715641-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009689502-Chart-Properties)

# Category Options

The Category Options dialog helps you to [set the sort order of the category values and define the number of the category values to show](https://devnet.logianalytics.com/hc/en-us/articles/1500009719181-Inserting-Components#SlctN) in the chart. This dialog appears when you select the Top N button ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/4412139502103/btn_wbrpt_topn.gif) above the category box in the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009689522-Chart-Wizard), [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009690342-Insert-Chart) dialog, [Convert to Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009689562-Convert-to-Chart) dialog, or [To Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009717161-To-Chart) dialog, or in the Bind Data screen of chart in the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009717201-Web-Report-Wizard#Chart).

![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131392919/ctgryoptn.gif)

**Category Order**

Specifies in which order data on the category axis of a chart will be displayed.

* **Ascend**  
   Lists data in an ascending order.
* **Descend**  
   Lists data in a descending order.
* **No Sort**  
   Keeps the data in their original order in database.

**Category Selection**

Specifies the number of the category values that will be displayed in the chart.

* **Select**  
   Specifies the Select N condition to define the number of the category values that will be displayed.
  + **All**  
     If selected, all category values will be displayed.
  + **Top N**   
     If selected, specify a number in the field to the right and the first N category values will be displayed.
  + **Bottom****N**  
     If selected, specify a number in the field to the right and the last N category values will be displayed.
* **Based On**  
   If checked, select a field added to the value axis of the chart to sort the category values based on this field, or select Custom Sort to customize the sort manner in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog.
* **Remaining Categories In**  
   Enabled when Top N or Bottom N is selected from the Select drop-down list. Check this option and then type a character string in the text box to group all the category values beyond the top/bottom N range.
* **Overall Series**  
   Specifies whether to calculate the top or bottom N category values based on the series values. Enabled when Top N or Bottom N is selected from the Select drop-down list.
* **Skip First**  
   If you input a number M in the Skip First text box, the first M category values in the chart will be skipped and the Select N condition will take effect beginning with M+1. The skipped values will be included in the Remaining Categories group together with all the category values beyond the top/bottom N range.

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Discards the changes and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715641-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009689502-Chart-Properties)
