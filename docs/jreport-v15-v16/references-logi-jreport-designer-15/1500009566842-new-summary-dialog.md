---
title: "New Summary Dialog"
id: 1500009566842
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566842-New-Summary-Dialog
updated_at: 2021-07-24T05:55:00Z
---

# New Summary Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566862-New-User-Defined-Data-Source-Dialog)

# New Summary Dialog

The New Summary dialog appears when you right-click the Summaries node in the Catalog Manager and select New Summary from the shortcut menu. It helps you to [create a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009589741-Creating-a-Summary) in a catalog. [See the dialog](javascript:%20void(null)).

![New Summary dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893837079/nwsum.gif)

The following are details about options in the dialog:

**Resource**

Lists all the available resources that can be used to make a summary.

**Summaries**

By default, <Create...> is selected in the drop-down list. You can also select one of the existing summaries from the drop-down list for modifying it.

**Aggregate Function**

Lists the functions which are available to the selected field. For details about each function, see [Math Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions).

**Summary On**

Specifies the field on which the summary is to compute.

To specify the sum on field, highlight it in the Resource box and then select ![Add Sum On button](https://devnet.logianalytics.com/hc/article_attachments/4404889307799/btn_sumon.gif) next to Summary On to add it to the field box.

**Static Summary**

If selected, the summary will take effect on a specific group that you define in the Group By field and it can only be inserted into the group. This limits the usage of the summary to only a single group that you specify. It is much better to create a dynamic summary that can be used in any group.

* **Group By**  
   Specifies the field used to group the data.

  To specify the group by field, highlight it in the Resource box and then select ![Add Group By button](https://devnet.logianalytics.com/hc/article_attachments/4404889307799/btn_sumon.gif) next to Group By to add it to the field box.

**Dynamic Summary**

If selected, the summary will take effect on the group according to the number, which is specified in the Group By field and it can be inserted into any groups of a component.

* **Group By**  
   Specifies on which group the summary will take effect. In most cases, you want to leave it 0.

  To specify the group level, first select Up or Down from the drop-down list, then in the combo box, select a value or input an integer, which should be between 0 to 127, to specify the group on which the summary will take effect. For example, if you select Up or Down and input 0 in the combo box and insert this summary into any group, the summary will take effect on this group; if you select Up and input 1 and insert this summary to a group, the summary will take effect on the group higher than the group where the summary is inserted, and if you specify Down and 1, it will take effect on the lower group; and the rest may be deduced by analogy.

  **Notes:**

  + If the dynamic summary is to be used in a chart, when defining the summary, you must choose Down from the Group By drop-down list; if it is to be inserted to other data components, the summary must be defined on Up level.
  + When you insert a dynamic summary into a report and there is no corresponding group level to match settings of the dynamic summary, an error message will be generated.
  + If you want to insert a summary with a special function into a table or banded object, there must be a group with the same special function in the table or banded object.

**Special Function**

If the group by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field) for the field in the Special Function drop-down list to further specify to which level the data will be grouped by. If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog) dialog will be displayed, in which you can set the function by your own.

**OK**

Accepts all changes and closes the dialog.

**Apply**

Applies all changes to the existing summary or adds the new summary to the catalog.

**Cancel**

Does not retain any changes and closes this dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566862-New-User-Defined-Data-Source-Dialog)
