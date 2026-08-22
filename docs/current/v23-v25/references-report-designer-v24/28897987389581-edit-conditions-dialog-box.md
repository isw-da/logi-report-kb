---
title: "Edit Conditions Dialog Box"
id: 28897987389581
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897987389581-Edit-Conditions-Dialog-Box
updated_at: 2024-09-30T09:07:09Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Edit Conditions Dialog Box

You can use the Edit Conditions dialog box to edit conditions for the selected object. This topic describes the options in the dialog box, which vary according to different sources where you open it.

When you open the dialog box from the Conditional Formatting dialog box, Insert Link dialog box, Edit Link dialog box, Shape Map Area Conditional Formatting dialog box, or the Display screen of the Chart Wizard dialog box or Create Chart dialog box for the Back-to-back Bench chart type in a query-based page report, you can use it to add a new or edit an existing condition for the selected object.

Designer displays these options:

Add Condition

Select to add a new condition.

Delete

Select to delete the specified condition.

Group

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

Ungroup

Select to ungroup the specified conditions.

Up

Select to move the specified condition or group up to a higher level.

Down 

Select to move the specified condition or group down to a lower level.

Logical operator drop-down menu

Specify the logical operator to apply for the specified conditions. It can be 
"And", "Or", "And Not", or "Or Not".    

Field text box

Specify the field on which to define the condition. 

Operator drop-down list

Specify the operator to compose the condition.

- 
=
Equal to

- 
>
Greater than

- 
>=
Greater than or equal to

- 
<
Less than

- 
<=
Less than or equal to

- 
!=
Not equal to

Value text box

Specify the value of how to build the condition.

- If you are editing conditional link or conditional formatting on a field, select the value from the drop-down list, which contains the top 50 values of the selected field. When you are editing conditional formatting on a field in a crosstab, Designer displays the button . Select the button and you can choose an object from the drop-down list to use its value in the condition.

- If you are editing conditional formatting on shape map areas, select the ellipsis   to specify the value.

Condition Expression

This box displays the SQL statement of the conditions.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

When you open the dialog box from the Fill tab of the Format Line dialog box, you can use it to add advanced single color conditional fill to values of the line chart.

Designer displays these options:

Select Query for Value Field

Designer displays the drop-down list when you select Imported Conditions. It contains the queries which you can use for editing the conditions. Select the query that contains the fields you want to use as the values to build the conditions. 

Add Condition

Select to add a new condition.

Delete

Select to delete the specified condition.

Group

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

Ungroup

Select to ungroup the specified conditions.

Up

Select to move the specified condition or group up to a higher level.

Down 

Select to move the specified condition or group down to a lower level.

Logical operator drop-down menu

Specify the logical operator to apply for the specified conditions. It can be 
"And", "Or", "And Not", or "Or Not".    

Field text box

Specify the field on which to define the condition.

Operator drop-down list

Specify the operator to compose the condition. It can be "=", ">", ">=", "<", "<=", "!=".

Value text box

Specify the value of how to build the condition. When you select Imported Conditions, you can select a field in the specified query as the value to build the condition.

Condition Expression

This box displays the SQL statement of the conditions.

Fill

You can specify the fill pattern of the chart values which meet the condition in this box. Designer disables this box if you select Apply Color to Line in the Node tab of the Format Line dialog box.

- 
Color
Specify the color.
- When you do not select Imported Conditions, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value (for example, 0xff0000) of a color in the text box.

- When you select Imported Conditions, you can select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and type the value in the text box.

- 
Transparency
Specify the transparency of the color. When you select Imported Conditions, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box. 

Area

You can specify properties for the areas that meet the condition in this box (the areas are formed by the chart axes and the chart line). Designer applies these properties to 2-D lines only. 

- 
Color
Specify the color.
- When you do not select Imported Conditions, select the color indicator and select a color from the color palette, or type the hexadecimal RGB value (for example, 0xff0000) of a color in the text box.

- When you select Imported Conditions, you can select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and type the value in the text box.

- 
Transparency
Specify the transparency of the color. When you select Imported Conditions, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.

Line

You can specify the line properties of the chart values that meet the condition in this box.

- 
Line Style
Specify the style of the chart line.

- 
Thickness
Specify the line thickness, in pixels.

Sample

This box displays a preview sample of your settings.

Imported Conditions 

Select  to use field values to build the conditions and control the color and transparency settings.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

When you open the dialog box from the Fill tab of the Format Rectangle dialog box, you can use it to add advanced single color conditional fill to values of the heat map.

Designer displays these options:

Select Query for Value Field

This drop-down list contains the queries which you can use for editing the conditions. Select the query which contains the fields you want to use as the values to build the conditions. 

Add Condition

Select to add a new condition.

Delete

Select to delete the specified condition.

Group

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

Ungroup

Select to ungroup the specified conditions.

Up

Select to move the specified condition or group up to a higher level.

Down 

Select to move the specified condition or group down to a lower level.

Logical operator drop-down menu

Specify the logical operator to apply for the specified conditions. It can be 
"And", "Or", "And Not", or "Or Not".    

Field text box

Specify the field on which to define the condition.

Operator drop-down list

Specify the operator to compose the condition. It can be "=", ">", ">=", "<", "<=", or "!=". 

Value text box

Specify the field in the selected query as the value to build the condition. You can also select <Input...> and type the value in the text box.

Condition Expression

This box displays the SQL statement of the conditions.

Color

Specify the color to apply to the chart values which meet the condition. Select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and type the value in the text box. 

Transparency

Specify the transparency of the color. Select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.

Value

Select to display the data in the condition expression as value. Designer applies this option only when the field which the condition is based on is a value field of the chart, or a field containing numeric values.

Percent

Designer does not support this option when you edit conditions for a heat map.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

When you open the dialog box from the Edit Values dialog box, you can use it to compose an expression for retrieving values when configuring business view security.

Designer displays these options:

Add Condition

Select to add a new condition.

Delete

Select to delete the specified condition.

Group

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

Ungroup

Select to ungroup the specified conditions.

Up

Select to move the specified condition or group up to a higher level.

Down 

Select to move the specified condition or group down to a lower level.

Logical operator drop-down menu

Specify the logical operator to apply for the specified conditions. It can be 
"And", "Or", "And Not", or "Or Not".    

Field text box

This text box displays the group object on which to define the condition. It is read only.

Operator drop-down list

Specify the operator to compose the condition.

- 
=
Equal to

- 
>=
Greater than or equal to

- 
>
Greater than

- 
<
Less than

- 
<=
Less than or equal to

- 
!=/<>
Not equal to

- 
[not] in
The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the operator "in" or "not in", you can use multiple values separated by comma (,).

- 
[not] like
The like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, you can only use "_" and "%".

- 
[not] between
The operator allows the system to evaluate whether  data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", Designer displays two value text boxes for inputting the same type of values.

- 
is [not] null
The operator is used in the WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", Designer does not display the value text box.

Value text box

Specify the value of how to build the condition. Select the value from the drop-down list, which contains the top 50 values of the selected field. When the field is based on a formula which references a parameter, the value list is null. You cannot use parameter as the value.

SQL Statement

This box displays the SQL statement of the conditions.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
