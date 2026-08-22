---
title: "Setting Filter Options for an Object"
id: 1500009570942
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object
updated_at: 2021-07-24T05:53:48Z
---

# Setting Filter Options for an Object

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592881-Enabling-Sort-and-Filter-on-Labels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592921-Page-Report-Manager)

# Setting Filter Options for an Object

In Page Report Studio, when you right-click a field (including DBField, formula and summary) or a [filterable](https://devnet.logianalytics.com/hc/en-us/articles/1500009592881-Enabling-Sort-and-Filter-on-Labels) label in a banded object or table, you will find the Filter submenu. This submenu can list items such as Remove Filter, Top N, Bottom N, and More. With these menu items you can easily filter the records. While if you do not want to show some of the four items for a field or filterable label, you can set the filter options in Logi JReport Designer as follows.

1. Select the field or label and locate its Filter Options property in the Report Inspector.
2. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) to bring out the Filter Options dialog.

   ![Filter Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889290263/fltroptn.gif)
3. Check the items you want to show on the Filter submenu of the field in Page Report Studio, and then select **OK**.
4. The properties value will be generated, equal to sum of values of those selected items. The items and corresponding values when checked are as follows:

   Remove Filter: 1  
    Top N: 2  
    Bottom N: 4  
    More: 8  
    Default: 16
5. After saving the page report and publishing it to Logi JReport Server, you will see the effect.

**Note:** In the Filter Options dialog, only when Default is deselected will the remaining four checkboxes be enabled. If you check Default, they will be disabled, but their values will still affect the Filter Options property value. If Default is checked (Filter Options >= 16), which items will be displayed on the Filter submenu in Page Report Studio will be determined by settings in the Page Report Studio profile on Logi JReport Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592881-Enabling-Sort-and-Filter-on-Labels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592921-Page-Report-Manager)
