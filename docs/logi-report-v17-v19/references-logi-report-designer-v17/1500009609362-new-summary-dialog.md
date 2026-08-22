---
title: "New Summary Dialog"
id: 1500009609362
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009609362-New-Summary-Dialog
updated_at: 2021-07-24T16:04:20Z
---

# New Summary Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009632681-New-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609402-New-User-Defined-Data-Source-Dialog)

# New Summary Dialog

The New Summary dialog helps you to [create a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Predefine) in the current catalog. It appears when you do one of the following:

* Right-click the Summaries node in the Catalog Manager and select New Summary from the shortcut menu.
* Select the <New Summary...> item where a summary list is provided.
* In the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009631241-Formula-Editor-Dialog) or [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009633941-User-Defined-Function-Editor-Dialog), select Menu > File > New Summary.

![New Summary dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904222615/nwsum.gif)

The following are details about options in the dialog:

**Resource**

Lists all the available resources that can be used to make a summary.

**Summaries**

By default, <Create...> is selected in the drop-down list. You can also select one of the existing summaries from the drop-down list for modifying it.

**Aggregate Function**

Lists the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) which are available to the selected field. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Summary On**

Specifies the field on which the summary is to compute. To specify the field, highlight it in the Resource box and then select ![Add Sum On button](https://devnet.logianalytics.com/hc/article_attachments/4404904222871/btn_sumon.gif) next to Summary On to add it to the field box.

**Static Summary**

If selected, the summary will take effect on a specific group that you define in the Group By field and it can only be inserted into the group. This limits the usage of the summary to only a single group that you specify. It is much better to create a dynamic summary that can be used in any group.

* **Group By**  
  Specifies the field used to group the data.

  To specify the group-by field, highlight it in the Resource box and then select ![Add Group By button](https://devnet.logianalytics.com/hc/article_attachments/4404904222871/btn_sumon.gif) next to Group By to add it to the field box.

**Dynamic Summary**

If selected, the summary will take effect on the group according to the number, which is specified in the Group By field and it can be inserted into any groups of a component.

* **Group By**  
  Specifies on which group the summary will take effect.

  To specify the group level, first select Up or Down from the drop-down list, then in the combo box, select a value or type in an integer between 0 to 127.

**Special Function**

If the group-by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Function) for the field in the Special Function drop-down list to further specify to which level the data will be grouped by. If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog) dialog will be displayed, in which you can set the function.

**OK**

Accepts all changes and closes the dialog.

**Apply**

Applies all changes to the existing summary or adds the new summary to the catalog.

**Cancel**

Does not retain any changes and closes this dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009632681-New-Parameter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609402-New-User-Defined-Data-Source-Dialog)
