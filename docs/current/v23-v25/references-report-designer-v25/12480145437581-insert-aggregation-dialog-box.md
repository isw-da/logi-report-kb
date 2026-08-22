---
title: "Insert Aggregation Dialog Box"
id: 12480145437581
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480145437581-Insert-Aggregation-Dialog-Box
updated_at: 2026-02-25T23:49:13Z
source_host: docs-report.zendesk.com
---
# 
Insert Aggregation Dialog Box

You can use the Insert Aggregation dialog box to add an aggregation in a crosstab based on the selected field. This topic describes the options in the dialog box.
    

Designer displays the Insert Aggregation dialog box when you drag a field that can be used as aggregate field from the Data panel to the aggregation area in a crosstab.

Designer displays these options:

Aggregate Function

This drop-down list contains the aggregate functions that you can use for the aggregation. Select the function you need. 

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

When the field you select in the crosstab has predefined aggregate function, this option is Aggregation. Designer displays the name of the field  in the text box and you cannot edit the name.

Label

Specify the label of the new aggregation in the crosstab. You can leave it blank.

Auto Map Field Name

Designer displays this option when you use the dialog box to insert an aggregation into a crosstab that uses a business view. Select it to apply the display name of the field as the aggregation label  and map the label to the dynamic display name of the field at runtime if the Server administrator defines it.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
