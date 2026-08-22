---
title: "Enter Values Dialog Box"
id: 28898034022797
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898034022797-Enter-Values-Dialog-Box
updated_at: 2024-09-30T09:08:00Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Enter Values Dialog Box

You can use the Enter Values dialog box to specify multiple values for a parameter. This topic describes the options in the dialog box.
    

Designer displays the Enter Values dialog box when you select  in the Enter Parameter Values dialog box if the parameter allows for multiple values.

Designer displays these options:

All Values

Designer displays this option when the  Enable the "All Values" Option property of the parameter is "true". Select it if you want to apply all values to the parameter, which can be all values of the parameter determined by Report Engine, all values in the database, or all the available values according to the Scope of All Values setting of the parameter.

Only when you clear this option, Designer enables the following options for adding values.

Available Values

This box lists all the available values of the parameter for selection. When the parameter is bound with a column, but the display column is different from the bound column, Designer lists values of the display column in the box.

Enter Values

Designer displays this option when the parameter's Allow Type-in of Value property is "true". You can use it to add values for the parameter manually.

- 
Calendar button
Designer displays this button only when the parameter is  Date, Time, or DateTime type. Select it to open the calendar widget to specify a date and time value. 

Selected Values

This box lists the values that you select to apply to the parameter. The selected values are case sensitive.

Sort icon

Select to display the Sort drop-down menu to select the order to sort the values.

- 
Ascending
Select to sort the values in ascending order.

- 
Descending
Select to sort the values in descending order.

- 
No Sort
Select to list the values  as how you add them if the parameter is a type-in parameter, or based on their original order in the database if the parameter is bound with a column. It is the default order.

 The change of sort order is a one-off action which Designer does not remember after you exit  the dialog box, meaning, each time when you open the dialog box, Designer always applies No Sort to the values.

Search icon

Select to open the search box to search for values. To start searching, type the text you want to search for in the search box and Designer lists the values containing the matched text.
                

You can use the following options in the search box:

- 
Drop-down icon
Select to list more search options.
						
- 
Highlight All
Select to highlight all the matched text. 

- 
Match Case
Select to search for text that meets the case of the text you type. 

- 
Match Whole Word
Select to search for text that looks the same as the text you type.

- 
Delete icon
Select to close the search  box and cancel the search.

Add button

Select to add the specified values from the Available Values box to the Selected Values box, or add the value you type in the Enter Values text box to the Selected Values box.

Remove button

Select to remove the specified values from the Selected Values box.

Add All button

Select to add all the listed values from the Available Values box to the Selected Values box.

Remove All button

Select to remove all the values from the Selected Values box.

OK

Select to apply the specified values for the parameter and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
