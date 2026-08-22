---
title: "New Summary Dialog"
id: 1500010031922
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031922-New-Summary-Dialog
updated_at: 2021-07-24T10:38:33Z
---

# New Summary Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067241-New-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067261-New-User-Defined-Data-Source-Dialog)

# New Summary Dialog

The New Summary dialog helps you to [create a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Predefine) in the current catalog. It appears when you do one of the following:

* Right-click the Summaries node in the Catalog Manager and select New Summary from the shortcut menu.
* Select the <New Summary...> item where a summary list is provided.
* In the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010066181-Formula-Editor-Dialog) or [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010032902-User-Defined-Function-Editor-Dialog), select Menu > File > New Summary.

![New Summary dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901160855/nwsum.gif)

The following are details about options in the dialog:

**Resource**

Lists all the available resources that can be used to make a summary.

**Summaries**

By default, <Create...> is selected in the drop-down list. You can also select one of the existing summaries from the drop-down list for modifying it.

**Aggregate Function**

Lists the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) which are available to the selected field. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.

**Summary On**

Specifies the field on which the summary is to compute. To specify the field, highlight it in the Resource box and then select ![Add Sum On button](https://devnet.logianalytics.com/hc/article_attachments/4404901161111/btn_sumon.gif) next to Summary On to add it to the field box.

**Static Summary**

If selected, the summary will take effect on a specific group that you define in the Group By field and it can only be inserted into the group. This limits the usage of the summary to only a single group that you specify. It is much better to create a dynamic summary that can be used in any group.

* **Group By**  
   Specifies the field used to group the data.

  To specify the group-by field, highlight it in the Resource box and then select ![Add Group By button](https://devnet.logianalytics.com/hc/article_attachments/4404901161111/btn_sumon.gif) next to Group By to add it to the field box.

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

If the group-by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Function) for the field in the Special Function drop-down list to further specify to which level the data will be grouped by. If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog) dialog will be displayed, in which you can set the function.

**OK**

Accepts all changes and closes the dialog.

**Apply**

Applies all changes to the existing summary or adds the new summary to the catalog.

**Cancel**

Does not retain any changes and closes this dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067241-New-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067261-New-User-Defined-Data-Source-Dialog)
