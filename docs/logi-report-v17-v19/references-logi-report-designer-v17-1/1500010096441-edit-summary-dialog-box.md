---
title: "Edit Summary Dialog Box"
id: 1500010096441
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096441-Edit-Summary-Dialog-Box
updated_at: 2021-07-23T19:15:19Z
---

# Edit Summary Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058842-Edit-Style-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058862-Edit-User-Defined-Data-Source-Dialog-Box)

# Edit Summary Dialog Box

You can use the Edit Summary dialog box to [edit a summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Predefine). This topic describes the options in the dialog box.

Designer displays the Edit Summary dialog box when you right-click a summary and select Edit Summary from the shortcut menu in the Catalog Manager or in the Data panel.

![Edit Summary dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848581783/edtsum.gif)

You see the following options in the dialog box:

**Resource**

The box lists all the available resources that you can use for the summary.

**Summaries**

The option shows the name of the summary. You can also choose to create a new summary or edit another one by selecting <Create...> or the name of the summary from the drop-down list.

**Aggregate Function**

The drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you can use to compute the selected field. Select the function you need.

* **Distinct On**  
  Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

**Summary On**

Specify the field on which the summary is to compute. To specify the field, select it in the Resource box and then select the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848470423/btn_sumon.gif) beside Summary On to add it to the text box.

**Static Summary**

Select it if you want the summary to take effect on a specific group that you define in the Group By text box.

* **Group By**  
  Specify the field by which to group the data.
  To specify the group-by field, select it in the Resource box and then select ![Add Group By button](https://devnet.logianalytics.com/hc/article_attachments/4404848470423/btn_sumon.gif) beside Group By to add it to the text box.

**Dynamic Summary**

Select it if you want the summary to take effect on the group according to the number that you specify in the Group By text box.

* **Group By**  
  Specify on which group you want the summary to take effect.
  To specify the group level, first select Up or Down from the drop-down list, then in the combo box, select a value or type an integer between 0 to 127.

**Special Function**

If the group-by field is of the Numeric, String, Date, or Time data type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) for the field from the drop-down list to further specify to which level to group the data. If you select Customize, Designer displays the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box) for you to set the function.

**OK**

Select to apply all changes and close the dialog box.

**Apply**

Select to apply all changes to the summary and leave the dialog box open.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058842-Edit-Style-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058862-Edit-User-Defined-Data-Source-Dialog-Box)
