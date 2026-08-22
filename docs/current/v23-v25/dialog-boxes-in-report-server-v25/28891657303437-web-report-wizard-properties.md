---
title: "Web Report Wizard Properties"
id: 28891657303437
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891657303437-Web-Report-Wizard-Properties
updated_at: 2026-02-26T02:13:14Z
source_host: docs-report.zendesk.com
---
# 
Web Report Wizard Properties

This topic describes how you can use the Web Report Wizard to create a web report. Server displays the wizard when you select New > Web Report on the task bar of the Resources page on the Server Console, or select Menu > File > New Report or the New Report button  on the toolbar in Web Report Studio.

This topic contains the following sections:

- Page Properties

- Layout Properties

- Bind Data Properties

- Style Properties

You see these elements on all the  screens:

Help button

Select to view information about the Web Report Wizard.

Cancel

The button is available when you have cleared the Create and Export Reports in New Window property in the Customize Server Preferences dialog box. Select Cancel to go back to the previous server page.

Back

Select to go back to the previous screen.

Next

Select to go to the next screen.

Save

Select to save the report to the server resource tree.

Run

Select to open the report in Web Report Studio in the Edit Mode.

## 
Page Properties

Specify the page settings of the report. 

Templates

Specify the template to apply to the report.

- 
Blank
  Select to use the blank template.
  

- 
Template1
  Select to use Template1, in which you can specify the report title and company logo.

- 
Template2
  Select to use Template2, in which you can specify the company logo, company title, report title, and subtitle. 

Page Setup

Select to open the Page Setup dialog box to specify the page properties.

Label/Report Title

Specify the title of the report.

Company Logo

Specify the company logo image file. Select the ellipsis button  to select the image in the Insert Image dialog box. 

Company Title 1

Specify the first company title.

Company Title 2 

Specify the second company title.

Sub Title

Specify the subtitle.

Font button

Specify the font properties for report title, subtitle, or company title.

After you select the font button, Server displays the following dialog box for you to edit the font properties:

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

## 
Layout Properties

Specify the layout of the report.

Layouts

Server lists the built-in layouts for arranging components in the report. Choose the layout you want to use for the report.

Buttons

Server enables the buttons when you select a cell in the editing layout box. 

- 
Horizontal Split
    Select to split the selected cell into two cells horizontally.

- 
Vertical Split
    Select to split the selected cell into two cells vertically.

- 
Merge
    Select to merge the selected adjacent cells that form a rectangular into one cell.

- 
Align
    Specify how to align the component  in the cell. It is available when you select Use Tabular.  
      
- 
left
          Select to align the component to the left of the cell.

- 
center
                   Select to align the component to the center of the cell.

- 
right
                   Select to align the component to the right of the cell.

Use Tabular

Select if you want to use a tabular to lay out the components in the report.

Editing layout box

Specify the component that you want to insert into the selected cell.

- 
New Components
  Select the component type you want to place in the cell: Table, 
 Crosstab, Chart, Banded Object, or Blank.

- 
Existing Components
  Select a component from the ones existing in the open report.

## 
Bind Data Properties

Specify the data source and the fields you want to display in each component that you selected in the Layout screen. This Bind Data screen differs according to the following component types: Table, Crosstab, Chart and Banded Object. When the component type is Blank, you cannot use the screen.

### 
For Table Component

Table Title

Specify the title of the table. The title is a special label bound with the table. You can position the table title freely in a report. Once you remove the table from the report, Server removes the table title too.

Font button

Specify the font properties of the table title.

Data Source

Specify the business view or dataset in the current catalog on which you want to build the table.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter that you want to apply to the dataset of the table.

Table type drop-down menu

Specify the type of the table. The tabs available in the screen differ according to the selected table type. For a group table type, you can define the table in the Details, Group, and Summary tabs respectively; for the summary table type, only the Columns and Summary tabs are available.

- 
Group Left
Select to create a table with group information left to the detail row.

- 
Group Above
Select to create a table with group information above the detail row.

- 
Group Left Above
Select to create a table with group information left above the detail row.

- 
Summary Table
Select to create a table with only group and summary information.

The tabs for defining a table are different according to the following table types:

- 
                    For Group Left, Group Above and Group Left Above
                

- 
                    For Summary Table
                

#### 
For Group Left, Group Above and Group Left Above

Details Tab

Specify the detail fields that you want to display in the table.
  

- 
Resources
Server displays the group objects  and detail objects  in the selected business view or dataset. You can also create dynamic formulas to use in the table.

- 
Edit button
  Select to edit the selected dynamic resource.

- 
Remove button
 Select to remove the selected dynamic resource.

- 
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

- 
Search button
 Select to launch the search bar to search for objects.
                

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

- 
Add button
  Select to add the selected object from the Resources box to display in the table.

- 
Remove button
  Select to remove the selected object from the right box.

- 
Field
 Group and detail objects that you have added to the table as the detail fields. 

- 
Label
 Specify the text for the labels of the detail columns, which by default are the display names of the added objects. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

- 
Move Up button
  Select to move the selected object higher in the list.

- 
Move Down button
  Select to move the selected object lower in the list.

- 
Sort Fields By
  Select to open the Custom Sort dialog box to specify how to sort data in the table.

Group tab

Specify the fields to group the data in the table.

- 
Resources
    Server displays all the available group objects  you can use to group data in the table. You can also create dynamic formulas to use in the table.

- 
Edit button
 Select to edit the selected dynamic resource.

- 
Remove button
 Select to remove the selected dynamic resource.

- 
Sort button
  Select an order for sorting the group objects in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
 Select to launch the search bar to search for objects.

- 
Add button
  Select to add the selected group object from the Resources box as a group field.

- 
Remove button
 Select to remove the selected group object from the table.

- 
Field
  Group objects that you have added as the group fields.

- 
Sort
  Specify the sort order for groups at the specific group level.
  
- 
No Sort
    Select to sort a group  in the same order as in the catalog.

- 
Ascend
    Select to sort a group in an ascending order.

- 
Descend
    Select to sort a group in a descending order.

- 
Custom Sort
Select to open the Custom Sort dialog box to sort a group by sorting the values of other fields.

- 
Move Up button
  Select to move the selected group higher in the list.

- 
Move Down button
  Select to move the selected group lower in the list.

Summary tab

Specify the fields on which you want to create summaries.

- 
Resources
 Server displays all the available aggregation objects  you can use to create summaries in the table. You can also create dynamic formulas and aggregations to use in the table.

- 
Edit button
 Select to edit the selected dynamic resource.

- 
Remove button
  Select to remove the selected dynamic resource.

- 
Sort button
 Select an order for sorting the aggregation objects in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
 Select to launch the search bar to search for objects.

- 
Add button
 Select to add the selected aggregation object as a summary field. 

- 
Remove button
  Select to remove the selected aggregation object from the table.

- 
Field
  Groups that you have added in the table and aggregation objects that you have added to summarize data in each group.

- 
Row
  Available only when the table is Group Left type. Specify to place a summary field in the header or footer row. If you add the summary to a group-by field, Server will place it in the group header or footer of the corresponding group. If you add the summary in the table (not in any group), Server will place it in the table header or footer.

- 
Column
  Available only when the table is Group Left type. Select a detail column where you want to place the summary field, or select no column to display the summary field in a separate summary column. 

- 
Move Up button
  Select to move the selected item higher in the list.

- 
Move Down button
  Select to move the selected item lower in the list.

#### 
For Summary Table

Columns tab

Specify the fields that you want to display as the columns of the table.

- 
Resources 
    Server displays all the group objects  and aggregation objects  in the selected business view or dataset. You can also create dynamic formulas and aggregations to use in the table.

- 
Edit button
    Select to edit the selected dynamic resource.

- 
Remove button
Select to remove the selected dynamic resource.

- 
Sort button
    Select an order for sorting the view elements in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
   Select to launch the search bar to search for objects.

- 
Add button
    Select to add the selected object from the Resources box to display in the table.

- 
Remove button
Select to remove the selected object that you added.

- 
Column
 Objects that you have added to the table.

- 
Sort
    Specify the sort order for groups at the specific group level.
- 
No Sort
    Select to sort a group  in the same order as in the catalog.

- 
Ascend
    Select to sort a group in an ascending order.

- 
Descend
    Select to sort a group in a descending order.

- 
Custom Sort
Select to open the Custom Sort dialog box to sort a group by sorting the values of other fields.

- 
Move Up button
    Select to move the selected item higher in the list.

- 
Move Down button
    Select to move the selected item lower in the list.

Summary tab

Specify to insert aggregations to the header/footer rows of the table and groups.

- 
Resources
 Server displays the aggregations you have selected in the Columns tab.

- 
Summarized Fields
  Server displays the group fields you have selected in the Columns tab under the Table node. 

- 
Header
 Represent the table header or the group header of a specific group. After you select an aggregation in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows. 

- 
Footer
 Represent the table footer or the group footer of a specific group. After you select an aggregation in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

### 
For Crosstab Component

Crosstab Title

Specify the title of the crosstab. The title is a special label bound with the crosstab. You can position the crosstab title freely in a report. Once you remove the crosstab from the report, Server removes the crosstab title too.

Font button

Specify the font properties of the crosstab title. 

Data Source

Specify the business view or dataset in the current catalog on which you want to build the crosstab.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter that you want to apply to the dataset of the crosstab.

Data tab

Specify the column, row, and aggregate fields that you want to display in the crosstab.

- 
Resources
    Server displays the group, detail, and aggregation objects in the selected business view or dataset. You can also create dynamic formulas and aggregations to use in the crosstab.
    
- 
Edit button
        Select to edit the selected dynamic resource.

- 
Remove button
        Select to remove the selected dynamic resource.

- 
Sort button
        Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
       Select to launch the search bar to search for objects.

- 
Columns/Rows
    Specify the group objects that you want to display on the columns/rows of the crosstab.      
- 
Field
          Group objects that you select to display on the columns/rows of the crosstab.

- 
Label
          Specify the text of the labels for the column/row headers. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

- 
Sort
          Specify the sort order of the group objects.

- 
Summaries
    Specify the aggregate fields that you want to display in the crosstab.    
- 
Field
        The aggregation/detail objects that you select to create summaries.

- 
Label
        Specify the text of the labels for the summaries. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

- 
 Aggregate
        Specify the functions that you want to use to summarize data of the selected detail objects.

- 
Distinct On

       Server enables this property when you select DistinctSum as the aggregate function, and you should set it. Select the ellipsis button , and then in the Select Fields dialog box select the fields according to whose unique values you want to calculate the DistinctSum function.    

- 
Comparison Function
        Select to open the Comparison Function dialog box to add a comparison function as an aggregate for the crosstab.

- 
Add Column button
    Select to add the selected group object  from the Resources box to display in the columns of the crosstab.

- 
Add Row button
    Select to add the selected group object  from the Resources box to display in the rows of the crosstab.

- 
Add Summary button
    Select to add the selected aggregation object  or detail object  from the Resources box to be the summary field of the crosstab.

- 
Move Up button
    Select to move the selected item higher in the list.

- 
Move Down button
    Select to move the selected item lower in the list.

- 
Remove button
    Select to remove the selected object.

Layout tab

Specify the layout of the crosstab.

- 
Aggregate

 Specify the layout of the aggregate fields. 

- 
Vertical Layout

Select to arrange the aggregate fields vertically.
    

- 
Number of Rows

        Specify the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a row so that the aggregate fields are in one column vertically. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.

- 
Horizontal Layout

 Select to arrange the aggregate fields horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
    

- 
Number of Columns

        Specify the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a column so that the aggregate fields are in one row horizontally. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

- 
Suppress Row Grand Totals
  Select to hide the grand total row in the crosstab.

- 
Suppress Column Grand Totals
 Select to hide the grand total column in the crosstab.

- 
Suppress Row Subtotals
 Server enables this property when the crosstab contains more than one row field.
                Select to hide the subtotals of the row fields in the crosstab. You can select the ellipsis button  to customize which subtotals of the row fields you want to suppress and which to show in the Suppress Row Subtotal dialog box.

- 
Suppress Column Subtotals
  Server enables this property when the crosstab contains more than one column field.Select to hide the subtotals of the column fields in the crosstab. You can select the ellipsis button  to customize which subtotals of the column fields you want to suppress and which to show in the Suppress Column Subtotal dialog box.

- 
Column Totals On
Specify the position of subtotal and grand total columns on the left or right of the detail aggregations.

- 
Row Totals On
  Specify the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

### 
For Chart Component

Chart Title

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

Specify the font properties of the chart title. 

Data Source

Specify the business view or dataset in the current catalog on which you want to build the chart.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter that you want to apply to the dataset of the chart.

Resources

Server displays the group, detail, and aggregation objects in the selected business view or dataset. You can also create dynamic formulas and aggregations to use in the chart.

- 
Edit button
    Select to edit the selected dynamic resource.

- 
Remove button
    Select to remove the selected dynamic resource.

- 
Sort button
    Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
Select to launch the search bar to search for objects.

Add button

Select to add the selected resource to display in the chart.

The other options for defining the chart component varies according to different chart types: common chart types, organization chart, and heat map. 

#### 
For Common Chart Types

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

Remove button

Select to remove the selected resource.

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

#### 
For Organization Chart

Specify the data to display in the chart.

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

#### 
For Heat Map

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

### 
For Banded Object Component

Banded Title

Specify the title of the banded object. The title is a special label bound with the banded object. You can position the banded object title freely in a report. Once you remove the banded object from the report, Server removes the banded object title too.

Font button

Specify the font properties of the banded object title.

Data Source

Specify the business view or dataset in the current catalog on which you want to build the banded object.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter which you want to apply to the dataset of the banded object.

Details tab

Specify the detail fields that you want to display in the banded object.

- 
Resources
      Server displays the group objects  and detail objects  in the selected business view or dataset. You can also create dynamic formulas to use in the banded object.

- 
Edit button
    Select to edit the selected dynamic resource.

- 
Remove button
 Select to remove the selected dynamic resource.

- 
Sort button
  Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
   Select to launch the search bar to search for objects.

- 
Add button
    Select to add the selected object from the Resources box to the right box. 

- 
Remove button
 Select to remove the selected object from the right box.

- 
Field
  Server lists the group and detail objects that you have added (or want to add) to the banded object as the detail fields.

- 
Label
    Specify the text for the labels of the detail fields, which by default are the display names of the added objects. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

- 
Move Up button
    Select to move the selected item higher in the list.

- 
Move Down button
    Select to move the selected item lower in the list.

- 
Sort Fields By
    Select to open the Custom Sort dialog box to specify how to sort data in the banded object.

Group tab

Specify the fields for grouping the data in the banded object. 

- 
Resources
      Server displays all the available group objects  you can use to group data in the banded object. You can also create dynamic formulas to use in the banded object.

- 
Edit button
      Select to edit the selected dynamic resource.

- 
Remove button
      Select to remove the selected dynamic resource.

- 
Sort button
      Select an order from the drop-down list to sort the group objects. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
     Select to launch the search bar to search for objects.

- 
Add button
      Select to add the selected group object as a group-by field.

- 
Remove button
      Select to remove the selected group object from the right box.

- 
Field
 Server lists all the group objects that you have added as the group-by fields.

- 
Sort
      Specify the sort order for groups at the specific group level.
      
- 
No Sort
    Select to sort a group  in the same order as in the catalog.

- 
Ascend
    Select to sort a group in an ascending order.

- 
Descend
    Select to sort a group in a descending order.

- 
Custom Sort
Select to open the Custom Sort dialog box to sort a group by sorting the values of other fields.

- 
Move Up button
      Select to move the selected group higher in the list.

- 
Move Down button
      Select to move the selected group lower in the list.

Summary tab

Specify the fields on which you want to create summaries.

- 
Resources
      Server displays all the available aggregation objects  you can use to create summaries in the banded object. You can also create dynamic formulas and aggregations to use in the banded object.

- 
Edit button
      Select to edit the selected dynamic resource.

- 
Remove button
      Select to remove the selected dynamic resource.

- 
Sort button
      Select an order from the drop-down list to sort the aggregation objects. The order applies to all the resource trees where you see the business view in Web Report Studio.

- 
Search button
     Select to launch the search bar to search for aggregation objects.

- 
Add button
      Select to add the selected aggregation object as the summary field. 

- 
Remove button
      Select to remove the selected aggregation object from the right box.

- 
Field
      Server lists the groups that you have added in the banded object and the aggregation objects that you have added to summarize data in each group.

- 
Row
      Specify to put the summary field in the header or footer row. If the summary is calculated on a group-by field, Server will place it in the group header or footer of the corresponding group; if the summary is calculated on the banded object, Server will place it in the banded header or footer.

- 
Column
    Not available to banded objects.

- 
Move Up button
      Select to move the selected item higher in the list.

- 
Move Down button
      Select to move the selected item lower in the list.

## 
Style Properties

Specify the style of the report.

Styles

Server lists all the available styles for you to select from. No style will apply when you select <No Style>.
