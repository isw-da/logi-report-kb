---
title: "Series Options Dialog Box Properties"
id: 45203968363405
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203968363405-Series-Options-Dialog-Box-Properties
updated_at: 2026-04-30T14:10:02Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Series Options Dialog Box Properties

This topic describes how you can use the Series Options dialog box to set the sort order of the series values and define the number of the series values to show in a chart. 

Server displays the dialog box when you select the Top N button  above the series box in the Chart Wizard, Insert Chart dialog box, Convert to Chart dialog box, or To Chart dialog box, or the Bind Data screen of chart in the Web Report Wizard. 

Series Order

Specify the order in which you want to display data on the series axis.

- 
Ascend
    Select to display data in an ascending order.

- 
Descend
    Select to display data in a descending order.

- 
No Sort
       Select to keep the data in their original order as you see in the catalog.

Series Selection

Specify the number of the series values you want to display in the chart. 

- 
Select
    Specify the Select N condition to define the number of series values you want to display.
    
- 
All
        Select to display all series values.

- 
Top N
 Select and then specify a number N in the field to the right if you want to display the first N series values. 

- 
Bottom N
        Select and then specify a number N in the field to the right if you want to display the last N series values. 

- 
Based On
 Select and then you can select a field that you added to the value axis of the chart to sort the series values based on this field, or select Custom Sort to customize the sort manner in the Custom Sort dialog box.

- 
Remaining Series In
    Select and then type a character string in the text box to group all the series values beyond the top/bottom N range. Server enables this property when you select Top N or Bottom N from the Select drop-down list.

- 
Overall Series
    Not supported on series values.

- 
Skip First
    If you type a number M in the Skip First text box, Server will skip the first M series values in the chart, and the Select N condition will take effect beginning with M+1. Server includes the skipped values in the Remaining Series group together with all the series values beyond the top/bottom N range.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
