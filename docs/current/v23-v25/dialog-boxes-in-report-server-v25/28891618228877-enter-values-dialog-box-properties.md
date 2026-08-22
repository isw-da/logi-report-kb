---
title: "Enter Values Dialog Box Properties"
id: 28891618228877
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891618228877-Enter-Values-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:59Z
source_host: docs-report.zendesk.com
---
# 
Enter Values Dialog Box Properties 

Use the Enter Values dialog box to specify multiple values for the parameter. This topic describes how to select or type multiple values.

Server displays the dialog box when you select the value combo box while specifying values for a parameter that enables multiple values.

All Values

Server displays this option when the parameter's Enable the "All Values" Option property is true. By default, Server selects this option and applies all the values of the parameter. In this case, when you insert the parameter as a field into a dashboard, the field will show the string All.

Clear this option if you want to customize the values. Then, Server enables the following properties.

Available Values

Server lists the predefined parameter values (500 at most) for selection. When the parameter is bound with a column, but the display column is different from the bound column, Server lists the values of the display column here.

Enter Value

Server displays this property when the parameter's Allow Type-in of Value property is true. You can add values for the parameter manually.

When the parameter is of the Date, DateTime, or Time type, you can select the calendar icon  to open the calendar to specify a date and time value.

Search

Server displays this property when the parameter's Allow Type-in of Value property is false. You can search for values among the available values. The search results are case insensitive and do not match whole word.

Selected Values

Server lists the values that you have selected. The selected values are case sensitive.

Add button

Select to add the selected values from the Available Values box to the Selected Values box, or add the value you typed in the Enter Value text box to the Selected Values box.

Remove button

Select to remove the selected values from the Selected Values box.

Add All button

Select to add all the listed values from the Available Values box to the Selected Values box.

Remove All button

Select to remove all the values from the Selected Values box.

OK

Select to apply the specified values for the parameter.

Cancel

Select to close the dialog box without changing the parameter values.

Help button

Select to view information about the Enter Values dialog box.

Close button

Select to close the dialog box without changing the parameter values.
