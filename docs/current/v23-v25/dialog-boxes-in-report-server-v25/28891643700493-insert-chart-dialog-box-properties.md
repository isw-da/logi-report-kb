---
title: "Insert Chart Dialog Box Properties"
id: 28891643700493
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891643700493-Insert-Chart-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:59Z
source_host: docs-report.zendesk.com
---
# 
Insert Chart Dialog Box Properties

This topic describes how you can use the Insert Chart dialog box to define a chart and insert it into a web report. The dialog box varies with different chart types: common chart types, organization chart, heat map, and KPI chart. 

Server displays the dialog box when you do either of the following:

- Drag Chart from the Components panel to the report.

- Right-click the icon  of a KPI or the blank area in a KPI that contains no KPI chart, then select Insert KPI Chart from the shortcut menu.

OK

Select to insert a chart into the report and close the dialog box.

Cancel

Select to close the dialog box without inserting a chart.

Help button

Select to view information about the  dialog box.

Close button

Select to close the dialog box without inserting a chart.

## 
For Common Chart Types

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Font button

 Specify the font properties of the chart title.

After you select the button, Server displays the following dialog box for you to edit the font properties:

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

Specify the business view or dataset in the current catalog on which you want to build the chart.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter that you want to apply to the dataset of the chart.

Resources

Server displays the resources that you can add to the chart.

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

Add button

Select to add the selected resource to display in the chart.

Value box 

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to display in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects. 

- 
Primary Axis
    Select a chart type to the primary axis.

- 
Secondary Axis
    Select a chart type for the secondary axis. Active only when you select Secondary Axis. Not available to gauge charts.

- 
X-Axis
 Server lists the value that you want to show on the X axis of the bubble chart. 

- 
Y-Axis
 Server lists the value that you want to show on the Y axis of the bubble chart. 

- 
Size 
  Server lists the value that you want to show as the bubble size.

Add Combo Chart button

Select to add a combo chart to the Primary Axis or Secondary Axis. Not available to gauge charts.

Edit button

Select to open the Edit Additional Value dialog box to edit the selected additional value.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Add Axis button

Select to add a new pair of Y Axis and Radius for the bubble chart.

Secondary Axis

Select if you want to show the secondary axis in the chart. Not available to gauge charts.

Category box

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object   that will display on the category axis of the chart.

For a real time chart, if you specify no object on the category axis, Server automatically displays Use System Refresh Time in the Category text box, namely, it will use the time at which the chart refreshes itself as the category value.

Series box

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object   that will display on the series axis of the chart. Not available to real time charts.

Top N button

Select to open the Category Options dialog box or Series Options dialog box to define the sort order of the category or series values and specify the number of the category or series values that will display in the chart.

Motion Bar for Playable Chart

Select and then add a group object you want to use as the motion field. A motion field can only be of Integer, Date, or Time data type. Available to single bar, bench, and bubble chart types only. 

- 
Special Function
    Available only when the motion field is of Date data type. Select it to define the special function.
    
- 
Field
 Server displays the field to which you will apply the special function. 

- 
Function
        Specify the special function to apply to the field. 

- 
OK
        Select to apply any changes you made here and close the dialog box.

- 
Cancel
               Select to close the dialog box without saving any changes.

Real Time

              Select to run the chart in real time mode, which means it will update automatically using real time data. Available to single bar, bench, line, and area chart types only.

- 
Use System Time for Category
               Select to use the time when the chart refreshes itself as the category value.

- 
Refresh Interval
    Specify the time interval at which the chart will get data and refresh itself automatically.

- 
Show Most Recent N Points
    Specify the number of records you want to keep for the real time data in the chart.

- 
Incremental Fetch
 Select to open the Unique Key dialog box to configure a unique key for the real time chart.

Remove button

Select to remove the selected resource.

## 
For Organization Chart

The chart type is Org.

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Font button

  Specify the font properties of the chart title. 

Data Source

Specify the business view or dataset in the current catalog on which you want to build the chart.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter you want to apply to the selected business view.

Resources

Server displays the resources that you can add to the chart.

Sort button

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for view elements.

Primary Axis

- 
Chart Type
    Select Org from the chart type drop-down list.

- 
Node
    Add a field from the Resources box which identifies the entity by selecting both the field and Node and then selecting the Add button . 

- 
Parent
    Add a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting . 

- 
Remove button
    Select to remove the selected child node or parent field.

Properties

 The Properties box presents a node model of the org chart. You can insert data fields, labels, and images into the node as the information about the entity in the org chart, using . By default, Server places all added objects at the left top of the node, and you need to adjust their positions and sizes in the node. You can also resize the node.

To remove an object from the node, select it, and then select the Remove button .

## 
For Heat Map

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Font button

Specify the font properties of the chart title.

Data Source

Specify the business view or dataset in the current catalog on which you want to build the chart.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter you want to apply to the selected business view.

Resources

Server displays the resources that you can add to the chart.

Sort button

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for view elements.

Add button

Select to add the selected field into the Area or Property box. 

Remove button

Select to remove the selected field from the Area or Property box. 

Chart type drop-down list

Select Heat Map as the chart type.

Area

Server lists the fields you add to group the data to different areas. There should be at least one group. When there are multiple groups, Server defines their levels  by their positions from top down. The group at the top is of the highest level and the bottom the lowest. 

- 
Color by
    Select to color by a group. You can use 0 or more groups as the color-by fields.

- 
Label by
    Select to show the group name in the innermost rectangle.

- 
Move Up button
    Select to move the selected group field higher in the list.

- 
Move Down button
    Select to move the selected group field lower in the list.

- 
Top N button
    Select to open the Group Options dialog box to define the sort order of the group values and specify the number of the group values you want to display in the chart.

Property

Server lists the summary fields you add as size-by/color-by or you want to display in the innermost rectangle.

- 
Size by
  Select to size by one summary or none.

- 
Color by
  Select to color by one summary or none.

- 
Label by
  Select to show a summary in the innermost rectangle.

## 
For KPI Chart

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Specify the font properties of the chart title.

Data Source

Specify the business view or dataset in the current catalog on which you want to build the chart.

Resources

Server displays the resources that you can add to the chart.

Sort button

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for view elements.

Add button

Select to add the selected resource to display in the chart.

Value box

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects. 

- 
Primary Axis
    Select a chart type for the primary axis.

- 
Secondary Axis
 Select a chart type for the secondary axis. Active only when you select Secondary Axis.

Add Combo Chart button

Select to add a combo chart to the Primary Axis or Secondary Axis.

Edit button

Select to open the Edit Additional Value dialog box to edit the selected additional value.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Secondary Axis

Select to show the secondary axis in the chart.

Category box 

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object  you add to display on the category axis of the chart.

For a real time chart, if you specify no object on the category axis, Server automatically displays Use System Refresh Time in the Category text box, namely, it will use the time when the chart refreshes itself as the category value.

Series box

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object  you add to display on the series axis of the chart. Not available to real time charts.

Top N button

Select to open the Category Options dialog box or Series Options dialog box to define the sort order of the category or series values and specify the number of the category or series values you want to display in the chart.

Motion Bar for Playable Chart

Select and then add a group object  you want to use as the motion field. A motion field can only be of Integer, Date, or Time data type. Available to single bar and bench chart types only. 

- 
Special Function
    Available only when the motion field is of Date data type. Select it to define the special function.
    
- 
Field
          Server displays the field to which you want to apply the special function. 

- 
Function
        Select the special function you want to apply to the field. 

- 
OK
        Select to apply any changes you made here and close the dialog box.

- 
Cancel
        Select to close the dialog box without saving any changes.

Real Time

       Select to run the chart in real time mode, which means it will update automatically using real time data. Available to single bar, bench, line, and area chart types only.

- 
Use System Time for Category
           Select to use the time when the chart refreshes itself as the category value.

- 
Refresh Interval
    Specify the time interval at which the chart will get data and refresh itself automatically.

- 
Show Most Recent N Points
    Specify the number of records you want to keep for the real time data in the chart.

- 
Incremental Fetch
           Select to open the Unique Key dialog box to configure a unique key for the real time chart.

Remove button

       Select remove the selected resource.
