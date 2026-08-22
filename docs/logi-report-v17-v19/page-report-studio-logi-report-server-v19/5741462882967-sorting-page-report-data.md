---
title: "Sorting Page Report Data"
id: 5741462882967
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741462882967-Sorting-Page-Report-Data
updated_at: 2022-10-31T17:18:17Z
---

# Sorting Page Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985371620375-Managing-Datasets-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483083159-Searching-for-Text-in-Page-Report)

# Sorting Page Report Data

You can sort the records, and the groups at a certain group level if you have defined one or more group levels, in a banded object or table. This topic describes how you can sort data using the Sort dialog box or shortcut menu.

* **Sorting records**: Changing the order of records in the whole banded object or table, or in each group if there exist one or more group levels. The sorting scope is the whole banded object or table.
* **Sorting groups at a group level**: Changing the order of groups at the specified group level, that is, the groups will be sorted by value of the first record in each group on the related field. The sorting scope is the group level.

You can achieve the above using the Sort dialog box or shortcut menu. However, you cannot sort the data by a global level formula.

**To sort a banded object/table using the Sort dialog box**:

1. Select **Menu** > **Report** > **Sort**, or the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905671926295/btn_pgrpt_sort.gif) on the toolbar.

   ![Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/9905672728983/sort.gif)
2. From the Sort in Scope drop-down list, select a banded object/table or a group field on which the sort condition will be based.
3. From the field drop-down list, select the field on which to sort the data, then set the sort order to Ascend or Descend.
4. If you select a banded object/table in step 2, you can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to add new rows of sorting conditions. When a group field is selected, only one sort condition can be composed.

   Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif) to move a row up or down so as to set the sorting priority, and ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905575282199/btn_pgrpt_no.gif) to delete the corresponding sorting condition if it is unwanted.

   ![Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/9905672755607/sort_more.gif)
5. To retrieve the opening status of this dialog box, select **Reset**.
6. Select **OK** to accept the settings and reload the report.

**To sort a banded object/table using shortcut menu**:

1. Right-click any value of a field, by which you want to sort the data in the banded object/table.
2. Choose the command **Sort** > **Ascend** or **Sort** > **Descend** from the shortcut menu.

   If you right-click a detail/summary field value in step 1, the sorting will affect the order of detail/summary records in the banded object or table. If it is a group field value, Server rearranges the order of groups in the group level represented by the group field.

   To remove the sort condition, select **Sort** > **No Sort**.

When you use the shortcut menu to sort the report data by a field and then by another field, the later sort condition always replaces the former one. And after applying a sort using the shortcut menu, if you open the Sort dialog box you can find the corresponding sort expression displays in the dialog box.

**Tips:**

* Administrators can [customize the buffer size for sorting of each report](https://devnet.logianalytics.com/hc/en-us/articles/5741415874327-Configuring-Cache#Sort) to improve performance.
* Using Logi Report Designer, you can set the Bind Column property for labels in banded objects and tables to enable the Sort shortcut menu on the labels, and show the sort button beside the labels for easy sorting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985371620375-Managing-Datasets-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483083159-Searching-for-Text-in-Page-Report)
