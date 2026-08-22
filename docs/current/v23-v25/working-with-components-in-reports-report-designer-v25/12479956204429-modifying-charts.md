---
title: "Modifying Charts"
id: 12479956204429
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479956204429-Modifying-Charts
updated_at: 2026-02-25T23:50:32Z
source_host: docs-report.zendesk.com
---
# 
Modifying Charts

For any chart in a report, you can further modify it at any time. For example, you can define special groups on the category/series axis of the chart and apply Order/Select N conditions to the chart. This topic introduces how you can modify the charts in a report.

This topic contains the following sections:

- Editing a Chart with Wizard

- Defining Special Groups for a Chart

- Grouping Chart Data by Intervals

- 
Setting Order/Select N Conditions for a Chart- Example: Applying an Order/Select N Condition to a Chart

## 
Editing a Chart with Wizard

You can further modify a chart by accessing its shortcut menu wizard which contains a set of screens that are similar to the wizard screens that you use to create the chart. For example, you can change the data  the chart applies, modify the chart type, and reset the layout and style of the chart.

- Right-click the chart and select Chart Wizard from the shortcut menu to display the Chart Wizard dialog box.

- In the Data screen, you can specify a new data source for the chart.

- In the Type screen, specify the type of the chart. If you want to change the chart type, you may need to first remove all the chart data. Specially, if you change a combo type to a single type or vice versa, Designer prompts you to make sure because it will remove all chart data automatically.
    

- In the Display screen, specify the fields to display in the chart. 
 Use Replace to replace a current field. For more information about how to define a chart, see Inserting Charts in a Report.

- In the Layout screen, specify settings for the chart elements.

- In the Style screen, select a style for the chart.

- Select Finish to accept the changes.

 When you change a type of 2-D chart to another type of 2-D chart, or a type of 3-D chart to another type of 3-D chart, Designer keeps all the previous properties. Nevertheless, when you change a 2-D chart to a 3-D chart, Designer sets the properties of the Z axis, the Y-Z wall, and the floor of the 3-D chart to the default values (since a 2-D chart does not have the Z axis, the Y-Z wall, or the floor), and removes all the other properties  from the 2-D chart; when you change a 3-D chart to a 2-D chart, Designer sets the properties of the Y2 axis of the 2-D chart  to the default values (since a 3-D chart does not have the Y2 axis).

## 
Defining Special Groups for a Chart

You can customize how to group values on the category/series axis of a chart (for a heat map, on its groups).

- When creating or editing a chart with wizard, select Special Group in the Display screen. Designer displays the User Defined Group dialog box.
    

- Select Add to add a grouping line and specify the Group Name, Operator, and Operand options respectively.

- Repeat the preceding step to add more group criteria.
    

- Select Keep values outside of the range in special group if you want to put values that do not fall within any of the specified criteria in a new special group, and then type a name for the special group in the Special Group Name text box.

- Select OK to accept the settings.

- Select Finish in the chart wizard to apply the changes.

## 
Grouping Chart Data by Intervals

For a chart that uses a query resource in a page report, if the data type of the field on the category/series axis of the chart (for a heat map, a group-by field) is  Numeric, String, Date, Time, or DateTime type, you can specify a special function to the field  to group data by intervals.

- When creating or editing a chart with wizard, select Special Function in the Display screen. Designer displays the Special Function dialog box.
    

- Select the special function for the category/series/group field from the Function drop-down list.

- Select OK.

- Select Finish in the chart wizard to apply the specified special function to the field.

- The special function for field on the category axis should be the same as that of the summary on the value axis. If you add a summary with a special function to the value axis, Designer applies the special function automatically to the field on the category axis and you cannot change the function. If you want to apply a special function to the summary on the value axis, you should make sure the category field has the same special function. When the summary applies no special function, you can add any special function to the category field as you want.

- If you have defined a special function to the group-by field of a table or banded object, and insert a chart in the table or banded object which inherits dataset from the parent and has the same grouping structure with the parent, Designer applies the special function defined for the field to the chart too. You can specify another special function to the field on the chart axis if you want.

- When you define both special functions and Select N conditions in a chart, the former takes higher priority, meaning, grouping data by intervals takes effect before Top/Bottom N.

## 
Setting Order/Select N Conditions for a Chart

One of the most difficult problems with charts is when there are too many category or series values, the chart becomes unreadable and also can become very slow to run, so you may want to show only specified category/series values on a chart and sort the values according to a specified order. To achieve this, you can use the Order/Select N feature. By applying  an Order/Select N condition to a chart, you can decide how many category/series values you want to display on the chart and how to sort the values. You can also use an Integer parameter to control the value of Select N. The Order/Select N feature also works on the groups of heat maps. 

To apply an Order/Select N condition to a chart

- When creating or editing a chart with wizard, select Order/Select N in the Display screen. Designer displays the Category Options dialog box, Series Options dialog box, or Group Options dialog box.
    

- 
In the Category Order/Series Order/Group Order box of the dialog box, specify the sort order of the category/series/group values. Select No Sort if you want to display the values in their original order from the database.
    

- Specify the Select condition to All, Top N, or Bottom N.
    
- 
All
Select to display all category/series/group values.

- 
Top/Bottom N 
If you select this option, Designer enables the combo box to the right and you can specify an integer number in the text box, or select a parameter which returns an integer from the drop-down list to dynamically define the Top/Bottom N condition. The chart then only displays the first or last N (N is the number you specify by the integer or parameter) category/series/group values.
           If you use an Integer parameter to define the Top/Bottom N condition dynamically at runtime, you should make sure the parameter has at least one default value that is larger than 0; otherwise, users get exceptions when they run the report on Server.

- Select Based On and specify  the options.
    
- When Based On is cleared, Designer sorts all the category/series/group values or its first/last N values  in the order you specify in the Category/Series/Group Order box of the dialog box.

- When you select Based On, you can sort the values based on a field that you have added to the value axis of the chart and select a radio button next to the Based On drop-down list to specify the sort order as you want. If you select Custom Sort from the Based On drop-down list, you can customize the fields based on which to sort the values and set the sort order for each sort-by field using the Custom Sort dialog box.

- When you select Top N or Bottom N from the Select drop-down list, you can select Remaining Categories In and type a string in the text box, Designer then merges the category/series/group values beyond the first or last N range  into the group with the name as that string.

- If you are specifying the Order/Select N condition for the category field, you can also select Overall Series to  calculate the top or bottom N category values based on the series values.

- You can select Skip First and type a number M in the text box, Designer then skips the first M category/series/group values, and the Select N condition begins with "M+1". Designer merges the skipped values into the Remaining Categories group.

- Select OK to accept the settings.

- Select Finish in the chart wizard to apply the changes.

### 
Example: Applying an Order/Select N Condition to a Chart

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- Navigate to File > New > Web Report. Designer creates a blank web report.

- 
Insert a chart in the web report as follows: 

- Use WorldWideSalesBV in Data Source 1 of the catalog.

- Display in the Clustered Bar 2-D chart type.

- Show Product ID on the category axis and Total Sales on the value axis.

- Apply the Classic style.

- Save the report and select the View tab to preview the chart.

- Right-click the chart and select Chart Wizard from the shortcut menu. Designer displays the Chart Wizard dialog box.

- In the Display screen, select Order/Select N below the Category box.

- In the Category Options dialog box, set the Select condition to Top 6, based on Total Sales descending, then select Remaining Categories In and type Other in the text box  to put the categories that do not meet the condition into the Other group. Select OK to accept the settings and close the dialog box.
    

- Select Finish in the Chart Wizard dialog box to finish editing the chart. 

- Preview the chart again.

- Select the Design tab to go back to design mode and repeat step 5 to 7.

- In the Category Options dialog box, select Skip First and type 2 in the text box, then select OK.

- Select Finish in the Chart Wizard dialog box.

- Preview the chart and the result is now as follows:
