---
title: "Insert Summary Dialog Box"
id: 5735551821719
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735551821719-Insert-Summary-Dialog-Box
updated_at: 2022-11-02T04:39:34Z
---

# Insert Summary Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735523667351-Insert-Parameter-Form-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523684631-Insert-Summary-Column-Dialog-Box)

# Insert Summary Dialog Box

You can use the Insert Summary dialog box to [insert a summary](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields#Insert) into a report. This topic describes the options in the dialog box.

Designer displays the Insert Summary dialog box when you navigate to Insert > Summary, or right-click a DBField and select Summary Function from the shortcut menu.

![Insert Summary dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898462075159/instsum.gif)

Designer displays these options:

**Summaries**

Select the summary to insert into the report. You can select an existing summary from the drop-down list, or select <Create...> to create a summary and use it in the report.

**Aggregate Function**

This drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you can use to compute the selected field. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735523667351-Insert-Parameter-Form-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523684631-Insert-Summary-Column-Dialog-Box)
