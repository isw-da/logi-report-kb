---
title: "Category Options Dialog Box"
id: 5735522351383
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735522351383-Category-Options-Dialog-Box
updated_at: 2022-11-02T04:35:19Z
---

# Category Options Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735508509719-Category-Property-Dialog-Box)

# Category Options Dialog Box

You can use the Category Options dialog box to [specify order of the categories and define the number of the categories to display](https://devnet.logianalytics.com/hc/en-us/articles/5735498861207-Modifying-Charts#SelectN) in a chart. This topic describes the options in the dialog box.

Designer displays the Category Options dialog box when you select Order/Select N below the Category box in the Display screen of the chart wizard.

![Category Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898515608343/ctgryoptn.gif)

Designer displays these options:

**Category Order**

You can specify how to sort the categories in this box.

* **Ascend**  
  Select to sort values in an ascending order (A, B, C).
* **Descend**  
  Select to sort values in a descending order (C, B, A).
* **No Sort**  
  Select to keep the values in their original order in the database.

**Category Selection**

You can specify the number of the categories to display in the chart in this box.

* **Select**
  + **All**  
    Select to display all categories in the chart.
  + **Top N**  
    Select and specify a number in the text box to display the first N categories in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Top N condition at runtime.
  + **Bottom N**  
    Select and specify a number in the text box to display the last N categories in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Bottom N condition at runtime.
* **Based On**  
  Select it and select a field that you have added to the value axis of the chart from the drop-down list to sort the categories based on this field. You can also select **Custom Sort** from the drop-down list to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box).
  + **Ascend**  
    Select to sort the categories based on the specified field in an ascending order.
  + **Descend**  
    Select to sort the categories based on the specified field in a descending order.
* **Remaining Categories In**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a character string in the text box to group all categories beyond the top/bottom N range.
* **Overall Series**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it to calculate the top or bottom N categories based on series.
* **Skip First**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a number M in the text box to the right, Designer then skips the first M categories in the chart and the Select N condition takes effect starting from M+1. Designer includes the skipped categories in the remaining category group together with all the categories beyond the top/bottom N range.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735508509719-Category-Property-Dialog-Box)
