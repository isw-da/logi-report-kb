---
title: "Sorting Report Data"
id: 1500009674001
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674001-Sorting-Report-Data
updated_at: 2021-07-24T20:53:54Z
---

# Sorting Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649362-Using-Dynamic-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674021-Searching-for-Text-in-a-Report)

# Sorting Report Data

You can sort the records in a banded object or table, and the groups in a certain group level of the banded object or table if you have defined one or more group levels.

* **Sorting records**: Changing the order of records in the whole banded object or table, or in each group if there exists one or more group levels. The sorting scope is the whole banded object or table.
* **Sorting groups at a group level**: Changing the order of groups at the specified group level, that is, the groups will be sorted by value of the first record in each group on the related field. The sorting scope is the group level.

You can achieve the above by using the Sort dialog or shortcut menu. However you cannot sort the data by a global level formula.

Below is a list of the sections covered in this topic:

* [Using the Sort Dialog](#Dialog)
* [Using the Shortcut Menu](#Menu)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using the Sort Dialog

1. Select **Menu** > **Report** > **Sort**, or the **Sort** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920435095/btn_pgrpt_sort.gif) on the toolbar.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920450839/sort.gif)
2. From the Sort in Scope drop-down list, select a banded object/table or a group field on which the sort condition will be based.
3. From the field drop-down list, select the field on which to sort the data, then set the sort order to Ascend or Descend.
4. If you select a banded object/table in step 2, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add new rows of sorting conditions if required. When a group field is selected, only one sort condition can be composed.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to move a row up or down so as to set the sorting priority, and ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398359/btn_pgrpt_no.gif) to delete the corresponding sorting condition if it is unwanted.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920451351/sort_more.gif)
5. To retrieve the opening status of this dialog, select the **Reset** button.
6. Select **OK** to accept the settings and to reload the result.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using the Shortcut Menu

1. Point to any value of a field by which to sort the data in the banded object/table, and then right-click.
2. Choose the command **Sort** > **Ascend** or **Sort** > **Descend** from the shortcut menu.

   If you right-click on a detail/summary field value in step 1, the sorting will affect the order of detail/summary records in the banded object or table; if it is a group field value, the order of groups in the group level represented by the group field will be rearranged.

   To remove the sort condition, select **Sort** > **No Sort**.

When you use the shortcut menu to sort the report data by a field and then by another field, the later sort condition always replaces the former one. And after applying a sort using the shortcut menu, if you open the Sort dialog you can find the corresponding sort expression displays in the dialog.

**Tips:**

* Administrators can [customize the buffer size for sorting of each report](https://devnet.logianalytics.com/hc/en-us/articles/1500009669021-Configuring-Cache#Sort) so as to improve performance.
* Using Logi JReport Designer, you can bind a field to a label to enable the Sort shortcut menu on the label, and show the sort button beside the label for easy sorting. For details, see "Enabling Sort and Filter on Labels" in the *Logi JReport Designer User's Guide*.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649362-Using-Dynamic-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674021-Searching-for-Text-in-a-Report)
