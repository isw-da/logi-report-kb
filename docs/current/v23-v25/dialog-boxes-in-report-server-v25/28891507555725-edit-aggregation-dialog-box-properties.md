---
title: "Edit Aggregation Dialog Box Properties"
id: 28891507555725
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891507555725-Edit-Aggregation-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:32Z
source_host: docs-report.zendesk.com
---
# 
Edit Aggregation Dialog Box Properties

You can use the Edit Aggregation dialog box to edit an existing aggregation object. This topic describes the properties in the dialog box.

Aggregation Name

Specify the display name of the aggregation object.

Mapping Name

Specify the field on which the aggregation object is based. Select the ellipsis button  to select the field in the Select Resource dialog box.

Studio disables this property when you create an aggregation object on a dynamic formula.

Aggregate Function

Select the aggregate function of the aggregation object. Server applies the function according to the group where the aggregation is, or to the entire report if the aggregation is in the report header or footer.

Distinct On

The property is available and you should set it when you have selected DistinctSum as the aggregate function. Specify the fields according to whose unique values you want to calculate DistinctSum. Select the ellipsis button  to select the fields in the Select Fields dialog box. 

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
