---
title: "Convert to Chart Dialog Box Properties"
id: 28891622754573
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891622754573-Convert-to-Chart-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:38Z
source_host: docs-report.zendesk.com
---
# 
Convert to Chart Dialog Box Properties

This topic describes how you can use the Convert to Chart dialog box to convert a data component to the chart type. The dialog box varies with different chart types: 
common chart types, organization chart, and heat map.

 Server displays the dialog box when you focus on a table, crosstab, or chart, and then select a chart type on the visualization toolbar but the data fields in the current component are not enough for the target chart type. 

You see these elements for all the chart types:

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

 Font button

 Select the button, and Server displays the following dialog box for you to edit the font properties of the chart title:

- 
Font

Select the font face of the title.

- 
Font Style 

Select the font style of the title: regular, bold, italic, or bold italic.

- 
Size

Specify the font size of the title.

- 
Align

Specify the position of the title to be left, right, center, or justify. 

- 
Font Color

Specify the font color of the title. 

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

- 
Background Color

Specify the background color of the title. 

- 
OK

Select to apply any changes you made here and close the dialog box.

- 
Cancel

Select to close the dialog box without saving any changes.

Data Source

Select the business view or dataset in the current catalog on which you want to build the chart.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter you want to apply to the selected business view.

Resources

Server displays the resources that you can add to the chart.

Show All Fields/Show Used Fields 

Select to show all the business view elements or only the ones that the current data component uses, in the Resources box. This pair of properties are not available when you select another business view to convert to chart with.

 Sort button

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

The order can be one of the following:

- 
Predefined Order

Select if you want to sort the resources in the order as in the Business View Editor of Designer.

- 
Resource Types

Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects. 

- 
Alphabetical Order

Select if you want to sort the resources in alphabetical order. Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

 Search button

Select to launch the search bar to search for view elements.

See the following properties in the search bar:

- 
Text box

Type the text you want to search in the text box. Server lists the values that contain the matched text. 

- 
Close button

Select to close the search bar.

- 
More Options button

Select the button and Server displays more search options.
          

- 
Highlight All

Select if you want to highlight all matched text. 

- 
Match Case

Select if you want  to search for text that meets the case of the typed text. 

- Match Whole Word
Select if you want  to search for text that looks the same as the typed text.

- 
 Previous button

Select to go to the previous matched text when you have selected Highlight All.

- 
Next button

  Select to go to the next matched text when you have selected Highlight All.

OK

Select to convert to the specified chart type.

Cancel

Select to close the dialog box without conversion.

 Help button

Select to view information about the dialog box.

 Close button

Select to close the dialog box without conversion.

## 
For Common Chart Types

 Add button

Select to add the selected resource to display in the chart.

Value box

The actual name of the box varies with different chart types, for example, it is "Bar Length" for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects. 

- 
Primary Axis
    Select a chart type for the primary axis.

- 
Secondary Axis
    Select a chart type for the secondary axis. This tab is active only when you have selected Secondary Axis. It is not available to gauge chart.

- 
X-Axis
    The data field you want to show on the X axis of the bubble chart. 

- 
Y-Axis
    The data field you want to show on the Y axis of the bubble chart. 

- 
Size 
    The data field you want to show as the bubble size. 

 Add Combo Chart button

Select to add a combo chart to the Primary Axis or Secondary Axis. The button is not available to gauge chart.

Edit button

Select to open the Edit Additional Value dialog box to edit the selected additional value.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Add Axis button

Select to add a new pair of Y Axis and Radius for the bubble chart.

Secondary Axis

Select to show the secondary axis in the chart. This property is not available to gauge chart.

Category box

The actual name of the box varies with different chart types, for example, it is "X-Axis" for a clustered bar chart. The box lists the group object  that will display on the category axis of the chart.

For a real time chart, if you specify no object on the category axis, Server will automatically display "Use System Refresh Time" in the Category text box, namely, Server will use the time at which the chart refreshes itself as the category value.

Series box

The actual name of the box varies with different chart types, for example, it is "Clustering" for a clustered bar chart. The box lists the group object  that will display on the series axis of the chart. Not available to real time chart.

Top N button

Select to open the Category Options dialog box or Series Options dialog box to define the sort order of the category or series values and specify the number of the category or series values that will display in the chart.

Motion Bar for Playable Chart

Server lists the group object you want to use as the motion field. A motion field can only be of Integer, Date, or Time data type. Available to single bar, bench, and bubble chart types only. 

- 
Special Function
    Available only when the motion field is of Date data type. Select it to define the special function.
    
- 
Field
          Server displays the field to which the special function will apply. 

- 
Function
        Specify the special function to the field. 

- 
OK
         Select to accept the special function settings and close the dialog box. 

- 
Cancel
        Select to close the dialog box without saving any changes. 

Real Time

Select to run the chart in the real time mode, which means Server will automatically update it using real time data. Available to single bar, bench, line, and area chart types only.

- 
Use System Time for Category
    Select to use the time at which the chart refreshes itself as the category value.

- 
Refresh Interval
    Specify the time interval at which the chart will get data and refresh itself automatically.

- 
Show Most Recent N Points
    Specify the number of records that Server will keep for the real time data in the chart.

- 
Incremental Fetch
    Select to open the Unique Key dialog box to configure a unique key for the real time chart.

Remove button

Select to remove the selected resource.

## 
For Organization Chart

Value box

- 
Primary Axis
    Select Org from the chart type drop-down menu.

- 
Node
    Add a field from the Resources box which identifies the entity, by selecting both the field and Node and then selecting the Add button . 

- 
Parent
    Add a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting . 

- 
Remove button
    Select to remove the selected child node or parent field.

Properties box

 The properties box presents a node model of the org chart. You can insert data fields, labels, and images into the node as the information about the entity in the org chart, using . By default, Server places all added objects at the left top of the node. You need to adjust their positions and sizes in the node. You can also resize the node.

To remove an object from the node, select it, and then select the Remove button .

## 
For Heat Map

Add button

Select to add the selected field into the Area or Property box. 

Remove button

Select to remove the selected field from the Area or Property box. 

Chart type drop-down list

Select Heat Map as the chart type.

Area box

Server lists the fields you add to group the data to different areas. You should add at least one group. When you add multiple groups, their levels follow their positions here from top down. The group at the top is of the highest level and the bottom the lowest. 

- 
Color by
    Select to color by a group. 0-n groups can be used as the color-by fields.

- 
Label by
    Select to show the group name in the innermost rectangle.

- 
Move Up button
 Select to move the selected field higher in the list.

- 
Move Down button
    Select to move the selected field lower in the list.

- 
Top N button
    Select to open the Group Options dialog box to define the sort order of the group values and specify the number of the group values that will display in the chart.

- 
Remove button
    Select to remove the selected group field.

Property box

Server lists the summary fields you add as size-by/color-by or to display in the innermost rectangle.

- 
Size by
 Select to size by one summary or none.

- 
Color by
    Select to color by one summary or none.

- 
Label by
    Select to show a summary in the innermost rectangle.
