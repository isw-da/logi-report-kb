---
title: "Insert Summary Dialog Box"
id: 45190536930317
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190536930317-Insert-Summary-Dialog-Box
updated_at: 2026-04-30T15:13:50Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Insert Summary Dialog Box

You can use the Insert Summary dialog box to insert a summary into a report. This topic describes the options in the dialog box.
    

Designer displays the Insert Summary dialog box when you navigate to Insert > Summary, or right-click a DBField and select Summary Function from the shortcut menu.

Designer displays these options:

Summaries

Select the summary to insert into the report. You can select an existing summary from the drop-down list, or select <Create...> to create a summary and use it in the report.

Aggregate Function

This drop-down list contains the aggregate functions that you can use to compute the selected field. Select the function you need. 

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

Summary On

This text box displays the field on which the summary is to compute.

Group By

Select the field using which to group the data. If you select a group-by field, Designer calculates a summary for each group.

Insert

Select to insert the specified or newly created summary into the report.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
