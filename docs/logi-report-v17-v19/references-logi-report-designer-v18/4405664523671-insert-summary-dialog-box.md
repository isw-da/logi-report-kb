---
title: "Insert Summary Dialog Box"
id: 4405664523671
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664523671-Insert-Summary-Dialog-Box
updated_at: 2022-01-27T20:36:16Z
---

# Insert Summary Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661631511-Insert-Parameter-Form-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661632663-Insert-Summary-Column-Dialog-Box)

# Insert Summary Dialog Box

You can use the Insert Summary dialog box to [insert a summary](https://devnet.logianalytics.com/hc/en-us/articles/4405661398551-Working-with-Summary-Fields#Insert) into a report. This topic describes the options in the dialog box.

Designer displays the Insert Summary dialog box when you navigate to Insert > Summary, or right-click a DBField and select Summary Function from the shortcut menu.

![Insert Summary dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550886295/instsum.gif)

You see the following options in the dialog box:

**Summaries**

Select the summary to insert into the report. You can select an existing summary from the drop-down list, or select <Create...> to create a summary and use it in the report.

**Aggregate Function**

This drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) that you can use to compute the selected field. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box).

**Summary On**

This text box displays the field on which the summary is to compute.

**Group By**

Select the field using which to group the data. If you select a group-by field, Designer calculates a summary for each group.

**Insert**

Select to insert the specified or newly created summary into the report.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661631511-Insert-Parameter-Form-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661632663-Insert-Summary-Column-Dialog-Box)
