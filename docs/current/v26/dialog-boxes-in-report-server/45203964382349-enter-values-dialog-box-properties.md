---
title: "Enter Values Dialog Box Properties"
id: 45203964382349
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203964382349-Enter-Values-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:38Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Enter Values Dialog Box Properties

You can use the Enter Values dialog box to specify multiple values for a parameter. This topic describes how to select or type multiple values.

Report displays the dialog box when you select in the value combo box while specifying values for a parameter that enables multiple values.

All Values

Report displays this option when the parameter's Enable the "All Values" Option property is true. By default, Report selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a report, the field will show the string All.

Clear this option if you want to customize the values. Then Report enables the following options.

Available Values

Report lists the predefined parameter values for selection. When the parameter is bound with a column, but the display column is different from the bound column, it lists the values of the display column here.

When the parameter has more than 500 values, after you scroll down to the bottom of the value list, more values will be automatically loaded into the list.

- 
Search button
Select to open the search box to search for values among the available values. To start the search, type the text you want to search for and Report lists the values that contain the matched text. The search results are case insensitive and do not match whole word.

- 
Sort button
Select to open the Sort drop-down menu to sort the values in the ascending or descending order or following the original order as in the database.

Enter Values

Report displays this option when the parameter's Allow Type-in of Value property is true. You can add values for the parameter manually.

- 
Calendar icon
Select this icon to open the calendar to specify a date and time value. Report displays this icon only when the parameter is of the Date, DateTime, or Time type.

Selected Values

Report lists the values that you have selected. The selected values are case sensitive.

Add button

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Values text box to the Selected Values box.

Remove button

Select to remove the selected values from the Selected Values box.

Add All button

Select to add all the listed values from the Available Values box to the Selected Values box.

Remove All button

Select to remove all the values from the Selected Values box.

OK

Select to select the values you specified for the parameter.

Cancel

Select to close the dialog box without changing the parameter values.

Help button

Select to view information about the Enter Values dialog box.

Close button

Select to close the dialog box without changing the parameter values.
