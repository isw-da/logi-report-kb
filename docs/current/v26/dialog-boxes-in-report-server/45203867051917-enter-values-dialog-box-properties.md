---
title: "Enter Values Dialog Box Properties"
id: 45203867051917
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203867051917-Enter-Values-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:18Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Enter Values Dialog Box Properties 

You can use the Enter Values dialog box to specify multiple values for a parameter. This topic describes how to select or type multiple values.

All Values

Server displays this property when the parameter's Enable the "All Values" Option property is true. By default, Server selects All Values and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string All.

Clear All Values if you want to customize the values. Then Server enables the following properties.

Available Values

Server lists the predefined parameter values (500 at most) for selection. When the parameter is bound with a column, but the display column is different from the bound column, Server lists the values of the display column here.

Enter Value

Server displays this property when the parameter's Allow Type-in of Value property is true. You can add values for the parameter manually.

- 
Calendar icon
Server displays this icon when the parameter is of the Date, DateTime, or Time type. Select the icon to open the calendar to specify a date and time value. 

Search

Server displays this property when the parameter's Allow Type-in of Value property is false. You can search for values among the available values. The search results are case insensitive and do not match the whole word.

Selected Values

Server lists the values that you have selected. The selected values are case sensitive.

Select to add the selected values from the Available Values box to the Selected Values box, or to add the value you typed in the Enter Value text box to the Selected Values box.

Select to remove the selected values from the Selected Values box.

Select to add all the listed values from the Available Values box to the Selected Values box.

Select to remove all the values from the Selected Values box.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
