---
title: "Sorting Report Data"
id: 1500009691702
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691702-Sorting-Report-Data
updated_at: 2021-11-03T06:56:47Z
---

# Sorting Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691582-Using-Dynamic-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691722-Searching-for-Text-in-a-Report)

# Sorting Report Data

You can sort the records in a banded object or table, and the groups in a certain group level of the banded object or table if you have defined one or more group levels.

* **Sorting records**: Changing the order of records in the whole banded object or table, or in each group if there exists one or more group levels. The sorting scope is the whole banded object or table.
* **Sorting groups at a group level**: Changing the order of groups at the specified group level, that is, the groups will be sorted by value of the first record in each group on the related field. The sorting scope is the group level.

You can achieve the above using the Sort dialog or shortcut menu. However you cannot sort the data by a global level formula.

**To sort a banded object/table using the Sort dialog**:

1. Select **Menu** > **Report** > **Sort**, or the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112533271/btn_pgrpt_sort.gif) on the toolbar.

   ![Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112540695/sort.gif)
2. From the Sort in Scope drop-down list, select a banded object/table or a group field on which the sort condition will be based.
3. From the field drop-down list, select the field on which to sort the data, then set the sort order to Ascend or Descend.
4. If you select a banded object/table in step 2, you can select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif) to add new rows of sorting conditions if required. When a group field is selected, only one sort condition can be composed.

   Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif) to move a row up or down so as to set the sorting priority, and ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112514327/btn_pgrpt_no.gif) to delete the corresponding sorting condition if it is unwanted.

   ![Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112540951/sort_more.gif)
5. To retrieve the opening status of this dialog, select the **Reset** button.
6. Select **OK** to accept the settings and to reload the result.

**To sort a banded object/table using shortcut menu**:

1. Point to any value of a field by which to sort the data in the banded object/table, and then right-click.
2. Choose the command **Sort** > **Ascend** or **Sort** > **Descend** from the shortcut menu.

   If you right-click on a detail/summary field value in step 1, the sorting will affect the order of detail/summary records in the banded object or table; if it is a group field value, the order of groups in the group level represented by the group field will be rearranged.

   To remove the sort condition, select **Sort** > **No Sort**.

When you use the shortcut menu to sort the report data by a field and then by another field, the later sort condition always replaces the former one. And after applying a sort using the shortcut menu, if you open the Sort dialog you can find the corresponding sort expression displays in the dialog.

**Tips:**

* Administrators can [customize the buffer size for sorting of each report](https://devnet.logianalytics.com/hc/en-us/articles/1500009712381-Configuring-Cache#Sort) so as to improve performance.
* Using Logi JReport Designer, you can set the Bind Column property for labels in banded objects and tables to enable the Sort shortcut menu on the labels, and show the sort button beside the labels for easy sorting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691582-Using-Dynamic-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691722-Searching-for-Text-in-a-Report)
