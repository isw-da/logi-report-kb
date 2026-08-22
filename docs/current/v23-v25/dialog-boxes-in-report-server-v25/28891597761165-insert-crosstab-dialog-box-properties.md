---
title: "Insert Crosstab Dialog Box Properties"
id: 28891597761165
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891597761165-Insert-Crosstab-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:59Z
source_host: docs-report.zendesk.com
---
# 
Insert Crosstab Dialog Box Properties

This topic describes how you can use the Insert Crosstab dialog box to insert a crosstab into a web report. Server displays the dialog box when you drag Crosstab from the Components panel to the destination.

This topic contains the following sections:

- Data Tab Properties

- Layout Tab Properties

You see these elements on both tabs:

Crosstab Title

Specify a title for the crosstab.

Font button

Specify the font properties of the crosstab title. After you select the button, Server displays the following dialog box for you to edit the font properties:

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

Specify the business view or dataset in the current catalog on which you want to build the crosstab.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter that you want to apply to the dataset of the crosstab.

OK

Select to insert a crosstab into the report and close the dialog box.

Cancel

Select to close the dialog box without inserting a crosstab.

Help button

Select to view information about the  dialog box.

Close button

Select to close the dialog box without inserting a crosstab.

## 
Data Tab Properties

Specify the column, row, and aggregate fields that you want to display in the crosstab.

Resources

Server displays the elements in the selected business view or dataset.

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

Add Column button

Select to add the selected group object  from the Resources box to display in the columns of the crosstab.

Add Row button

Select to add the selected group object  from the Resources box to display in the rows of the crosstab.

Add Summary button

Select to add the selected aggregation object  or detail object  from the Resources box to be the summary field of the crosstab.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Remove button

Select to remove the selected resource.

## 
Layout Tab Properties

Specify the layout of the crosstab. 

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

Suppress Row Grand Totals

Select to hide the grand total row in the crosstab.

Suppress Column Grand Totals

Select to hide the grand total column in the crosstab.

Suppress Row Subtotals

Server enables this property when the crosstab contains more than one row field.

Select to hide the subtotals of the row fields in the crosstab. You can select the ellipsis button  to customize which subtotals of the row fields you want to suppress and which to show in the Suppress Row Subtotal dialog box.

Suppress Column Subtotals

Server enables this property when the crosstab contains more than one column field.

Select to hide the subtotals of the column fields in the crosstab. You can select the ellipsis button  to customize which subtotals of the column fields you want to suppress and which to show in the Suppress Column Subtotal dialog box.

Column Totals On

Specify the position of subtotal and grand total columns on the left or right of the detail aggregations.

Row Totals On

Specify the position of subtotal and grand total rows on the top or bottom of the detail aggregations.
