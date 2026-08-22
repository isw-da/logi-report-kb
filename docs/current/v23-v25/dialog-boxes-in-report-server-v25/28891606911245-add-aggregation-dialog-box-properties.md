---
title: "Add Aggregation Dialog Box Properties"
id: 28891606911245
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891606911245-Add-Aggregation-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:25Z
source_host: docs-report.zendesk.com
---
# 
Add Aggregation Dialog Box Properties

You can use the Add Aggregation dialog box to create a dynamic aggregation object in a report. This topic describes the properties in the dialog box.

Aggregation Name

Specify the display name of the aggregation object.

Mapping Name

Select the ellipsis button  to open the Select Resource dialog box. Then, select a field or a formula which the aggregation object is based on. Server displays the field with its parent node in the text box.

Aggregate Function

Select the aggregate function of the aggregation object. Server applies the function to the group where the aggregation is or to the entire report if the aggregation is in the report header or footer.

Distinct On

Server enables this property when you have selected DistinctSum as the aggregate function. Select the ellipsis button  to open the Select Fields dialog box.  Then, select the required fields according to whose unique values you want to calculate the DistinctSum function.

OK

Select to create the aggregation object and exit the dialog box.

Cancel

Select to close the dialog box without creating an aggregation object.

Help

Select to view information about the dialog box.
