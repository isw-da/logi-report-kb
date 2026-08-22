---
title: "Insert Table Dialog Box Properties"
id: 28891654809869
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891654809869-Insert-Table-Dialog-Box-Properties
updated_at: 2026-02-26T02:13:01Z
source_host: docs-report.zendesk.com
---
# 
Insert Table Dialog Box Properties

This topic describes how you can use the Insert Table dialog box to insert a table into a web report. Server displays the dialog box when you drag Table from the Components panel to the destination.

Table Title

Specify a title for the table.

Font button

Specify the font properties of the table title. After you select the button, Server displays the following dialog box for you to edit the font properties:

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

Specify the business view or dataset in the current catalog on which you want to build the table.

- 
Inherit from the Parent

Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter that you want to apply to the dataset of the table.

Table type drop-down menu

Specify the type of the table. The tabs available in the dialog box differ according to the selected table type. For a group table type, you can define the table in the Details, Group, and Summary tabs respectively; for the summary table type, only the Columns tab is available.

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

OK

Select to insert a table into the report and close the dialog box.

Cancel

Select to close the dialog box without inserting a table.

Help button

Select to view information about the  dialog box.

Close button

Select to close the dialog box without inserting a table.

The tabs in the dialog box are different according to the following table types:

- 
                    For Group Left, Group Above, or Group Left Above
                

- 
                    For Summary Table
                

## 
For Group Left, Group Above, or Group Left Above

The dialog box consists of the following tabs: Details, Group, and Summary.

### 
Details

Specify the detail fields that you want to display in the table.

Resources

Server displays all the group objects  and detail objects  in the selected business view or dataset.

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

Add button

Select to add the selected object from the Resources box to display in the table. 

Remove button

Select to remove the selected object from the table.

Field

Group and detail objects that you have added to the table as the detail fields. 

Label

Specify the text for the labels of the detail columns, which by default are the display names of the added objects. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Sort Fields By

Select to open the Custom Sort dialog box to specify how to sort data in the table.

### 
Group

Specify the fields to group the data in the table.

Resources

Server displays all the available group objects  you can use to group the data in the table.

Sort button

Select an order for sorting the group objects in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for group objects.

Add button

Select to add the selected group object from the Resources box as a group field.

Remove button

Select to remove the selected group object from the table.

Field

Group objects that you have added as the group fields.

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

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

### 
Summary

Specify the fields on which you want to create summaries.

Resources

Server displays all the available aggregation objects  you can use to create summaries in the table.

Sort button

Select an order for sorting the aggregation objects in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for aggregation objects.

Add button

Select to add the selected aggregation object as a summary field. 

Remove button

Select to remove the selected aggregation object from the table.

Field

Groups that you have added in the table and aggregation objects that you have added to summarize data in each group.

Row

Available only when the table is Group Left type.

Specify to place a summary field in the header or footer row. If you add the summary to a group-by field, Server will place it in the group header or footer of the corresponding group. If you add the summary in the table (not in any group), Server will place it in the table header or footer.

Column

Available only when the table is Group Left type.

Select a detail column where you want to place the summary field, or select no column to display the summary field in a separate summary column. 

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

## 
For Summary Table

The dialog box consists of the following tabs: Columns and Summary.

### 
Columns

Specify the fields that you want to display as the columns of the table.

Resources

Server displays all the group and aggregation objects in the selected business view or dataset.

Sort button

Select an order for sorting the view elements in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for objects.

Add button

Select to add the selected object from the Resources box to display in the table.

Remove button

Select to remove the selected object that you added.

Column

Objects that you have added to the table.

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

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

### 
Summary

Specify to insert aggregations to the header/footer rows of the table and groups.

Resources

Server displays the aggregations you have selected in the Columns tab.

Summarized Fields

Group fields you have selected in the Columns tab under the Table node. 

Header

Represent the table header or the group header of a specific group. After you select an aggregation in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows. 

Footer

Represent the table footer or the group footer of a specific group. After you select an aggregation in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.
