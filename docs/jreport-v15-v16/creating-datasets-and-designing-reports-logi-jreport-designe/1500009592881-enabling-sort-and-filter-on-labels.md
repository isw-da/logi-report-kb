---
title: "Enabling Sort and Filter on Labels"
id: 1500009592881
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592881-Enabling-Sort-and-Filter-on-Labels
updated_at: 2021-07-24T05:53:47Z
---

# Enabling Sort and Filter on Labels

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570962-Predefining-Sort-and-Filter-Conditions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object)

# Enabling Sort and Filter on Labels

By default, the Sort and Filter shortcut menu items are only available on fields (including DBField, formula and summary) in banded objects or tables in Page Report Studio. Logi JReport provides you with the option to enable the two menu items on labels in the banded objects or tables by binding them with fields.

1. Select a label in a banded object or table.
2. In the Report Inspector, locate the Bind Column property in the Others category.
3. All the fields used in the banded object or table are listed in the property's value drop-down list. Select one to bind with the label.
4. If you want to display the sort and filter buttons beside the label in Page Report Studio which provide another easy way for sorting and filtering, go on set the Sortable and Filterable properties of the label to true.
5. Save the report and publish it to Logi JReport Server.
6. Run the report in Page Report Studio and you can then right-click the label or the proper button beside the label to sort or filter the records of the bound field.

   ![Report run in Page Report Studio](https://devnet.logianalytics.com/hc/article_attachments/4404889290007/rpt_pgrpt_dhtml_label.gif)

When a label is bound with a field, you can further specify the options that will be displayed on its Filter submenu. For details, see [Setting Filter Options for an Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570962-Predefining-Sort-and-Filter-Conditions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object)
