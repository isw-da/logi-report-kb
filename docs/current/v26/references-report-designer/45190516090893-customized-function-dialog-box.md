---
title: "Customized Function Dialog Box"
id: 45190516090893
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190516090893-Customized-Function-Dialog-Box
updated_at: 2026-04-30T15:13:02Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Customized Function Dialog Box

You can use the Customized Function dialog box to define customized special functions. This topic describes the options in the dialog box.
    

Designer displays the Customized Function dialog box when you select Customize from the Special Function drop-down list in the New Summary dialog box, Edit Summary dialog box, or in the Group screen of the component wizard, and provides you with different options in the dialog box according to the different data type of the selected group-by field: Numeric, String, or Date/Time.

When the group-by field is Numeric type, Designer displays the following options in the dialog box: 

By Intervals

Select to group data by intervals.

- 
Numerical Value
    Specify the intervals of the group.

Within Range

Select to group data within certain range.

- Within
Specify the range. You also need to select how to apply the range from the drop-down list: to increasing data or decreasing data.

Keep values outside of the range in special group

Select to put values that do not fall within the defined intervals or range in a new special group.

- 
Special Group Name
Specify the name of the special group. By default, the group name is Others. You can double-click in the text box to rename it.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

 

When the group-by field is String type, Designer displays the following options in the dialog box: 

First/Last N letters

Specify the intervals with which to group the report data. "N" should be an integer no larger than 255.

Case sensitive when grouping

Select  to distinguish between uppercase and lowercase characters for the groups.

Convert group name to

Designer enables this option when you do not select "Case sensitive when grouping". You can use it to specify how you want to convert the group name.

- 
Uppercase
Select to convert the group names to uppercase.

- 
Lowercase
Select to convert the group names to lowercase.

- 
No Conversion
Select if you do not want to convert any group names.

Keep values outside of the range in special group

Select  to put values that do not fall within the defined intervals in a new special group.

- 
Special Group Name
Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

 

When the group-by field is Date/Time type, Designer displays the following options in the dialog box: 

Time

Specify the time  intervals. The unit of the time intervals can be: second, minute, hour, day, week, month, quarter, half year, or year.

The Offset of Time Grouping

Specify the offset with which you want to group the data.

- 
1/1/1970 00:00:00
Select to use the default offset that Report defines.

- 
Customized Value
Select it and you can select  to define your required offset using the calendar widget.

The First Day of the Week

Specify which day is the first day of a week.

Keep values outside of the range in special group

Select to put values that do not fall within the defined intervals in a new special group.

- 
Special Group Name
Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
