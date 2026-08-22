---
title: "Series Options Dialog Box"
id: 45190568092941
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190568092941-Series-Options-Dialog-Box
updated_at: 2026-04-30T15:14:16Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Series Options Dialog Box

You can use the Series Options dialog box to specify order of the data series and define the number of the data series to display in a chart. This topic describes the options in the dialog box.
    

Designer displays the Series Options dialog box when you select Order/Select N below the Series box in the Display screen of the chart wizard.

Designer displays these options:

Series Order

You can specify how to sort the data series in this box.

- 
Ascend
Select to sort values in an ascending order (A, B, C).

- 
Descend
Select to sort values in a descending order (C, B, A).

- 
No Sort
Select to keep the values in their original order in the database.

Series Selection

You can specify the number of data series to display in the chart in this box.

- 
Select
- 
All
Select to display all data series in the chart.

- 
Top N
Select and specify a number in the text box to display the first N data series in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Top N condition at runtime.

- 
Bottom N
Select and specify a number in the text box to display the last N data series in the chart. You can also select a parameter which returns an integer from the drop-down list so as to dynamically define the Bottom N condition at runtime.

- 
Based On
Select it and select a field that you have added to the value axis of the chart from the drop-down list to sort the data series based on this field. You can also select Custom Sort from the drop-down list to customize the sort manner in the Custom Sort dialog box.    
- 
Ascend
Select to sort the data series based on the specified field in an ascending order.

- 
Descend
Select  to sort the data series based on the specified field in a descending order.

- 
Remaining Series In
Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a character string in the text box to group all the data series beyond the top/bottom N range.

- 
Overall Series
Designer does not enable this option for setting data series.

- 
Skip First
Designer enables this option when you select Top N or Bottom N from the Select drop-down list. Select it and type a number M in the text box to the right, Designer then skips the first M data series in the chart and the Select N condition takes effect beginning with M+1. Designer includes the skipped data series in the remaining series group together with all the data series beyond the top/bottom N range.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
