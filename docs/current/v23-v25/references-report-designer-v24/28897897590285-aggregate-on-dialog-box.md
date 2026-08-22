---
title: "Aggregate On Dialog Box"
id: 28897897590285
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897897590285-Aggregate-On-Dialog-Box
updated_at: 2024-09-30T09:08:23Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Aggregate On Dialog Box

You can use the Aggregate On dialog box  to calculate data using the field in the detail column. This topic describes the options in the dialog box.
    

Designer displays the Aggregate On dialog box when you right-click a detail column in a table and select Aggregate On from the shortcut menu.

Designer displays these options:

Aggregate On

This option shows the field bound with the detail column. The field is also the one on which the summary is based.

Aggregate Function

This drop-down list contains the aggregate functions that you can use to compute the field in the detail column. Select the function you need. 

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

Group By

If you select this option, you can select a group-by field from the drop-down list below, to which to apply the summary (if you do not select a field, the summary applies to the whole dataset); if you do not select this option, Designer creates a dynamic summary.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
