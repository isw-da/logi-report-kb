---
title: "Category Options Dialog Box"
id: 1500010058442
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058442-Category-Options-Dialog-Box
updated_at: 2021-07-23T19:15:12Z
---

# Category Options Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058122-Business-View-Editor-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058462-Category-Property-Dialog-Box)

# Category Options Dialog Box

You can use the Category Options dialog box to [specify the sort order of the category values and define the number of the category values to show](https://devnet.logianalytics.com/hc/en-us/articles/1500010094661-Modifying-Charts#SelectN) in a chart. This topic describes the options in the dialog box.

Designer displays the Category Options dialog box when you select the Order/Select N button below the category box in the Display screen of the chart wizard.

![Category Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856984471/ctgryoptn.gif)

You see the following options in the dialog box:

**Category Order**

You can specify in which manner to sort the category values in this box.

* **Ascend**  
  Select to sort values in an ascending order (A, B, C).
* **Descend**  
  Select to sort values in a descending order (C, B, A).
* **No Sort**  
  Select to keep the values in their original order in the database.

**Category Selection**

You can specify the number of the category values to display in the chart in this box.

* **Select**
  + **All**  
    Select to display all the category values in the chart.
  + **Top N**  
    Select and specify a number in the text box to display the first N category values in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Top N condition at runtime.
  + **Bottom N**  
    Select and specify a number in the text box to display the last N category values in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Bottom N condition at runtime.
* **Based On**  
  Select and select a field that you have added to the value axis of the chart from the drop-down list to sort the category values based on this field. You can also select Custom Sort from the drop-down list to customize the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box).
  + **Ascend**  
    Select to sort the category values based on the specified field in an ascending order.
  + **Descend**  
    Select to sort the category values based on the specified field in a descending order.
* **Remaining Categories In**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a character string in the text box to group all the category values beyond the top/bottom N range.
* **Overall Series**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it to calculate the top or bottom N category values based on the series values.
* **Skip First**  
  Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a number M in the text box to the right, Designer then skips the first M category values in the chart and the Select N condition takes effect beginning with M+1. Designer includes the skipped values in the Remaining Categories group together with all the category values beyond the top/bottom N range.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058122-Business-View-Editor-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058462-Category-Property-Dialog-Box)
