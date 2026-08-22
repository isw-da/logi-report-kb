---
title: "Edit Summary Dialog"
id: 1500009630881
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630881-Edit-Summary-Dialog
updated_at: 2021-07-24T16:04:44Z
---

# Edit Summary Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630861-Edit-Style-Group-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630901-Edit-User-Defined-Data-Source-Dialog)

# Edit Summary Dialog

The Edit Summary dialog helps you to [edit a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Predefine). It appears when you right-click a summary and select Edit Summary from the shortcut menu in the Catalog Manager or the Data panel.

![Edit Summary dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904345751/edtsum.gif)

The following are details about options in the dialog:

**Resource**

Lists the resources that can be used to make a summary.

**Summaries**

Displays the name of the summary that is to be edited. You can also choose to create a new summary or edit another one by selecting <Create...> or the name of the summary from the drop-down list.

**Aggregate Function**

Lists the [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) which are available to the selected field. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Summary On**

Specifies the field on which the summary is to compute.

To specify the sum on field, highlight it in the Resource box and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904222871/btn_sumon.gif) next to Summary On to add it to the field box.

**Static Summary**

If selected, the summary will take effect on a specific group that you define in the Group By field and it can only be inserted into the group.

* **Group By**  
   Specifies the field used to group the data.

  To specify the group-by field, highlight it in the Resource box and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904222871/btn_sumon.gif) next to Group By to add it to the field box.

**Dynamic Summary**

If selected, the summary will take effect on the group according to the number, which is specified in the Group By field and it can be inserted into any banded panels of a component.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630861-Edit-Style-Group-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630901-Edit-User-Defined-Data-Source-Dialog)
