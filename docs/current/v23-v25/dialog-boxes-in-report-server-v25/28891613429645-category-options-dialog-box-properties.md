---
title: "Category Options Dialog Box Properties"
id: 28891613429645
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891613429645-Category-Options-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:42Z
source_host: docs-report.zendesk.com
---
# 
Category Options Dialog Box Properties

This topic describes how you can use the Category Options dialog box to set the sort order of the category values and define the number of the category values to show in a chart. 

Server displays the dialog box when you select the Top N button  above the category box in the Chart Wizard, Insert Chart dialog box, Convert to Chart dialog box, or To Chart dialog box, or in the Bind Data screen of chart in the Web Report Wizard.

Category Order

Specify the order in which you want to display data on the category axis of a chart.

- 
Ascend
    Select to display data in an ascending order.

- 
Descend
    Select to display data in a descending order.

- 
No Sort
       Select to keep the data in their original order as you see in the catalog.

Category Selection

Specify the number of the category values that you want to display in the chart. 

- 
Select
    Specify the Select N condition to define the number of the category values you want to display.
      
- 
All
 Select to display all category values.

- 
Top N
 Select Top N and then specify a number N in the field to the right if you want to display the first N category values. 

- 
Bottom N
        Select Bottom N and then specify a number N in the field to the right if you want to display the last N category values. 

- 
Based On
    Select and then you can select a field that you added to the value axis of the chart, to sort the category values based on this field, or select Custom Sort to customize the sort manner in the Custom Sort dialog box. 

- 
Remaining Categories In
    Select and then type a character string in the text box, to group all the category values beyond the top/bottom N range. Server enables this property when you select Top N or Bottom N from the Select drop-down list.

- 
Overall Series
    Select to calculate the top or bottom N category values based on the series values. Server enables this property when you select Top N or Bottom N from the Select drop-down list.

- 
Skip First
    If you type a number M in the Skip First text box, Server will skip the first M category values in the chart, and the Select N condition will take effect beginning with M+1. Server includes the skipped values in the Remaining Categories group together with all the category values beyond the top/bottom N range.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
