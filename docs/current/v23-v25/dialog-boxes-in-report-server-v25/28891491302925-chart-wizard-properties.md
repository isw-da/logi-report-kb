---
title: "Chart Wizard Properties"
id: 28891491302925
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891491302925-Chart-Wizard-Properties
updated_at: 2026-02-26T02:12:38Z
source_host: docs-report.zendesk.com
---
# 
Chart Wizard Properties

This topic describes how you can use Chart Wizard to edit a chart. Chart Wizard varies with different chart types: common chart types, organization chart, heat map, and KPI chart.

Server displays the wizard when you do one of the following:

- Select a chart, then select Menu > Edit > Wizard.

- Select a chart, then select the Chart Wizard button  on the visualization toolbar.

- Right-click the icon  of a chart, then select Chart Wizard from the shortcut menu.

- Right-click any part of a chart other than the legend and label, or right-click the blank area in a KPI chart, then select Chart Wizard from the shortcut menu.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
Chart Wizard Properties for Common Chart Types

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

Server shows the dataset that the chart uses.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter which you want to apply to the dataset.

Resources

Server displays the resources that you can add to the chart. Select an item, an then select an Add button  to add the item to the corresponding box on the right.

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

Value box 

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects.

- 
Primary Axis
 Select a chart type for the primary axis.

- 
Secondary Axis
 When you select Secondary Axis, you can then select a chart type for the secondary axis, which is not available to gauge charts.

- 
X-Axis
  Server lists the value you want to show on the X axis of the bubble chart. 

- 
Y-Axis
  Server lists the value you want to show on the Y axis of the bubble chart. 

- 
Size
  Server lists the value you want to show as the bubble size.  

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

Select to show the secondary axis in the chart. Not available to gauge charts.

Category box

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object   that will display on the category axis of the chart.

Series box

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object   that will display on the series axis of the chart. Not available to real time charts.

Top N button

Select to open the Category Options dialog box or Series Options dialog box. Then, define the sort order of the category or series values and specify the number of the category or series values you want to display in the chart.

Motion Bar for Playable Chart

Available to single bar, bench, and bubble chart types only. Select if you want to create a motion chart, then add a group object  of Integer, Date, or Time data type as the motion field. 

- 
Special Function
  Available only when the motion field is of Date data type. Select to define the special function. 
    
- 
Field
        Server displays the field to which you want to apply the special function. 

- 
Function
        Select the special function for the field. 

- 
OK
        Select to apply the special function and close the dialog box. 

- 
Cancel
        Select to close the dialog box without saving any changes. 

Real Time

Select to run the chart in the real time mode, which means it will update automatically using the real time data. Available to single bar, bench, line, and area chart types only.

- 
Use System Time for Category
    Select to use the time at which the chart refreshes itself as the category value. Then, Server automatically displays Use System Time for Category in the Category box.

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

   Select to remove a resource from its box.

## 
Chart Wizard Properties for Organization Chart 

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Font button

 Specify the font properties of the chart title. 

Data Source

Server displays the dataset that the chart uses.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter you want to apply to the dataset.

Resources

Server displays the resources that you can add to the chart.

Sort button

Select an order for sorting the view elements. Once you change the order, it will apply to all the resource trees where you see the business view elements.

Search button

Select to launch the search bar to search for view elements.

Value box

- 
Primary Axis
    Select Org from the chart type drop-down menu.

- 
Node
  Add a field from the Resources box which identifies the entity, by selecting both the field and Child and then selecting the Add button . 

- 
Parent
    Add a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting . 

- 
Remove button
  Select to remove the selected child node or parent field.

Properties

The Properties box presents a node model of the org chart. You can add data fields, labels, and images into the node as the information about the entity in the org chart, using . By default, Server places all added objects at the upper left of the node. You can adjust their positions and sizes in the node. You can also resize the node.

To remove an object from the node, select it, and then select the Remove button .

## 
Chart Wizard Properties for Heat Map

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Specify the font properties of the chart title.

Data Source

Server displays the dataset that the chart uses.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter you want to apply to the dataset.

Resources

Server displays the resources that you can add to the chart.

Sort button

Select an order for sorting the view elements. Once you change the order, it will apply to all the resource trees where you see the business view elements.

Search button

Select to launch the search bar to search for view elements.

Add button

Select to add the selected field into the Area or Property box. 

Remove button

Select to remove the selected field from the Area or Property box. 

Chart type drop-down list

Select Heat Map as the chart type.

Area

Server lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their positions here define their levels. The group at the top is of the highest level and the bottom the lowest. 

- 
Color By
    Select 0-n groups as the color-by fields.

- 
Label By
  Select the groups you want to display in the innermost rectangle.

- 
Move Up button
  Select to move the selected group field higher in the list.

- 
Move Down button
  Select to move the selected group field lower in the list.

- 
 Top N button
Select to open the Group Options dialog box. Then, define the sort order of the group values and specify the number of the group values you want to display in the chart.

- 
Remove button
  Select to remove the selected group field.

Property

Server lists the summary fields you want to use as size-by/color-by fields or display in the innermost rectangle.

- 
Size By
  Select one summary or none you want to size by.

- 
Color By
  Select one summary or none you want to color by.

- 
Label By
  Select the summaries you want to display in the innermost rectangle.

## 
Chart Wizard Properties for KPI Chart

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Font button

Specify the font properties of the chart title. 

Data Source

Server displays the dataset that the chart uses.

Resources

Server displays the resources you can add to the chart. Select a resource and select the Add button  to add the resource to the corresponding box on the right.

Sort button

Select an order for sorting the view elements. Once you change the order, it will apply to all the resource trees where you see the business view elements.

Search button

Select to launch the search bar to search for view elements.

Value box 

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. 

For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects. 

- 
Primary Axis
 Select a chart type for the primary axis.

- 
Secondary Axis
    Select a chart type for the secondary axis. Active only when you have selected Secondary Axis.

Add Combo Chart button

Select to add a combo chart to the Primary Axis or Secondary Axis.

Edit button

Select open the Edit Additional Value dialog box to edit the selected additional value.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Secondary Axis

Select if you want to show the secondary axis in the chart.

Category box 

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object  that will display on the category axis of the chart.

Series box

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object  that will display on the series axis of the chart. Not available to real time charts.

Top N button

Select to open the Category Options dialog box or Series Options dialog box. Then, define the sort order of the category or series values and specify the number of the category or series values you want to display in the chart.

Motion Bar for Playable Chart

Available to single bar and bench chart types only. Select if you want to create a motion chart. Then, select a group object  of Integer, Date, or Time data type as the motion field. 

- 
Special Function
    Available only when the motion field is of Date data type. Select to define the special function in a dialog box, which contains the following properties:
        
- 
Field
 Server displays the field to which the special function will apply. 

- 
Function
        Select the special function for the field. 

- 
OK
        Select to apply the special function and close the dialog box. 

- 
Cancel
        Select to close the dialog box without saving any changes. 

Real Time

Select if you want to run the chart in the real time mode, which means it will update automatically using the real time data. Available to single bar, bench, line, and area chart types only.

- 
Use System Time for Category
 Select if you want to use the time at which the chart refreshes itself as the category value. Server will 
automatically display Use System Time for Category in the Category text box.

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

Select to remove a resource.
