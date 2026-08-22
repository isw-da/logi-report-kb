---
title: "Group Filter Dialog Box"
id: 28898143698573
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898143698573-Group-Filter-Dialog-Box
updated_at: 2024-09-30T09:14:24Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Group Filter Dialog Box

You can use the Group Filter dialog box to create and modify advanced filter conditions based on the selected group. This topic describes the options in the dialog box.
    

Designer displays the Group Filter dialog box when you select Group Filter in the Group screen of the component wizard.

Designer displays these options:

Logic

Select to evaluate the records that are not in the record aggregate.

Functions

Specify the function to aggregate on a certain field.

- 
Min
Select to evaluate the records that have the lowest values for the selected field.

- 
Max
Select to evaluate the records that have the largest values for the selected field.

- 
Exist
Select to check if there exists at least one qualified record.

Field Name (before Occur With)

Specify the field you want to aggregate on. 

Field Name (after Occur With)

Specify the criteria of the filter. Expression includes not only the DBField, but also formulas and parameters. You can type the strings supported by the database or select the the ellipsis  to select column names or fields values in the Expressions dialog box.

Operators

Specify the operator to compose the condition.

- 
=
Equal to

- 
>
Greater than

- 
<
Less than

- 
>=
Greater than or equal to

- 
<=
Less than or equal to

- 
<>
Not equal to

Value

Specify the value to use in the filter condition. You can also use a parameter for runtime input. You can type the value or parameter name, or for parameters, select the ellipsis  to select the parameter names in the Expressions dialog box.

Select to display some additional commands.

- 
END
Select to finish entering the condition.

- 
And
Select to insert the logic operator "AND" which applies to this line and the next line.

- 
OR
Select to insert the logic operator "OR" which applies to this line and the next line.

- 
Insert Row
Select to insert a single Expression line.

- 
Delete Row
Select to delete a single Expression line.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
