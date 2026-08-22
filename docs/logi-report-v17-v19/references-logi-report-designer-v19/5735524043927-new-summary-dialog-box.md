---
title: "New Summary Dialog Box"
id: 5735524043927
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735524043927-New-Summary-Dialog-Box
updated_at: 2022-11-02T07:53:12Z
---

# New Summary Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735543814807-New-User-Defined-Data-Source-Dialog-Box)

# New Summary Dialog Box

You can use the New Summary dialog box to [create a summary](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Predefine) in the current catalog. This topic describes the options in the dialog box.

Designer displays the New Summary dialog box when you do one of the following:

* In the Catalog Manager, right-click the Summaries node and select New Summary from the shortcut menu.
* Select <New Summary...> where a summary list is available.
* In the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box) or [User Defined Function Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735553198231-User-Defined-Function-Editor-Dialog-Box), select New Summary on the toolbar or navigate to Menu > File > New Summary.

![New Summary dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898459644055/nwsum.gif)

Designer displays these options:

**Resource**

This box lists all the available resources that you can use to create the summary.

**Summaries**

By default, Designer selects <Create...> in the drop-down list. You can also select one of the existing summaries to edit it.

**Aggregate Function**

This drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you can use to compute the selected field. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

**Summary On**

Specify the field on which the summary is to compute. To specify the field, select it in the Resource box and then select ![Add Sum On button](https://devnet.logianalytics.com/hc/article_attachments/9898476718615/btn_sumon.gif) beside Summary On to add it to the text box.

**Static Summary**

Select it if you want the summary to take effect on a specific group that you define in the Group By text box.

* **Group By**  
  Specify the field by which to group the data. To specify the group-by field, select it in the Resource box and then select ![Add Group By button](https://devnet.logianalytics.com/hc/article_attachments/9898476718615/btn_sumon.gif) beside Group By to add it to the text box.

**Dynamic Summary**

Select it if you want the summary to take effect on the group according to the number that you specify in the Group By text box.

* **Group By**  
  Specify on which group you want the summary to take effect. To specify the group level, first select Up or Down from the drop-down list, then in the combo box, select a value or type an integer between 0 to 127.

**Special Function**

When the group-by field is Numeric, String, Date, or Time data type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#Function) for the field from the drop-down list to further specify to which level to group the data. If you select Customize, Designer displays the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522295831-Customized-Function-Dialog-Box) for you to set the function.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735543814807-New-User-Defined-Data-Source-Dialog-Box)
