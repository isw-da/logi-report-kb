---
title: "Edit Parameter Dialog Box"
id: 45190503666189
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190503666189-Edit-Parameter-Dialog-Box
updated_at: 2026-04-30T15:13:15Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Edit Parameter Dialog Box

You can use the Edit Parameter dialog box to edit the specified parameter. This topic describes the options in the dialog box.
    

Designer displays the Edit Parameter dialog box when you right-click a parameter and select Edit Parameter from the shortcut menu in the Catalog Manager or in the Data panel.

Designer displays these options:

Name

This option shows the name of the parameter.

Value Setting

Select the parameter type.

- 
Type-in Parameter
Select this type if you want to predefine parameter values by typing manually.

- 
Bind with Single Column
Select this type if you want to bind DBField with the parameter so as to retrieve the values of the DBField as the parameter values.

- 
Bind with Cascading Columns
Select this type if you want to create a group of cascading parameters so as to achieve the function of filtering parameters with parameters in a simple way. Designer does not display this type when the parameter is in a catalog data source that contains only XML connections.

Value Type

Select the data type of the parameter.

Value section

Designer displays different options in the section after Value Type according to the type you select from the Value Setting drop-down list.

- 
For Type-in Parameter- 
Value List
This box lists the values that you predefine for the parameter.
- 
Prompt Values [format hint] 
Specify the prompt values for the parameter. The [format hint] shows what the predefined values should look like.
        You can add more than one prompt value. All the prompt values must be of the same type as specified by Value Type.
        

- 
Add button
Select to add a new prompt value to the list. Double-click in the value line to edit the value. When the parameter is  Date, Time, or DateTime data type, you can also select  to set a date and time value from the calendar widget.

- 
Remove button
Select to delete the specified prompt value.

- 
Move Up button
Select to move the specified value higher in the display sequence.

- 
Move Down button
Select to move the specified value lower in the display sequence.

- 
For Bind with Single Column

- 
Data Source
Select the data source from which to retrieve the DBFields  that you can  bind with the parameter.

- 
Bind Column
Select the DBFields to bind with the parameter. 

- 
Sort icon
Select to display the Sort drop-down menu to specify how to sort the DBFields in the drop-down list. 
- 
Ascending
Select to sort the DBFields  in the ascending order.

- 
Descending
Select to sort the DBFields in the descending order.

- 
No Sort
Select to keep the original order of the DBFields  as in the database. It is the default order

- 
Search icon
Select to open the search box to search for the required DBField. To start searching, type the text you want to search for in the search box and Designer lists the DBFields containing the matched text.
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

- 
Close icon
Select to close the drop-down list.

- 
Display Column
Select the DBField the values of which you want to display for specifying the parameter value at runtime.

- 
Sort icon
Select to display the Sort drop-down menu to specify how to sort the DBFields in the drop-down list: Ascending, Descending, or No Sort.

- 
Search icon
Select to open the search box to search for the required DBField.  

- 
Close icon
Select to close the drop-down list.

The change of sort order for the DBFields in both the Bind Column and Display Column drop-down lists is a one-off action which Designer does not remember after you exit  the dialog box, meaning, each time when you open the dialog box, Designer always applies No Sort to the DBFields in the drop-down lists.

- 
For Bind with Cascading Columns
- 
Data Source
Select the data source from which to retrieve the DBFields that you can  bind with the parameters.

- 
Cache Data
Specify how you want to cache data of the cascading parameters. Designer applies the setting only when you have set the Cache data of cascading parameters option to either False or True in the Options dialog box.
- 
Default
Select to apply the default cache setting specified for parameter level in the Options dialog box. 

- 
True
Select to cache data of the cascading parameters.

- 
False
Select this option if you do not want to cache data of the cascading parameters.

- 
Value List
Specify a group of cascading parameters.
        
- 
Add button
Select to add a new parameter.

- 
Remove button
Select to delete the specified parameter.

- 
Move Up button
Select to move the specified parameter to a higher level. The higher position a parameter has, the higher level it gets. Values of the lower-level parameters are controlled by values of the higher-level parameters.

- 
Move Down button
Select to move the specified parameter to a lower level.

- 
Bind Column
Select the DBField to bind with the parameter.

- 
Display Column
Select the DBField the values of which you want to display for specifying the parameter value at runtime.

- 
Parameter
Specify whether to set a group of Bind Column and Display Column as a parameter which becomes a member of the cascading parameter group. 

Options

You can specify options for the parameter in this box.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
