---
title: "Table Wizard Properties"
id: 45204002983437
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204002983437-Table-Wizard-Properties
updated_at: 2026-04-30T14:10:10Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Table Wizard Properties

This topic describes how you can use the Table Wizard to change data of a table.

Server displays the wizard when you do one of the following:

- Select a table, and then navigate to Menu > Edit > Wizard. 

- Select a table, and then select the Table Wizard button  on the visualization toolbar.

- Right-click the icon  of a table and select Table Wizard from the shortcut menu.

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

Server displays the dataset that the table uses.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter which you want to apply to the dataset.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

The tabs in the dialog box are different according to the following table types:

- 
                    For Group Left, Group Above, and Group Left Above
                

- 
                    For Summary Table
                

## 
For Group Left, Group Above, and Group Left Above

When the table is one of the group types, the wizard contains these tabs: Details, Group, and Summary.

### 
Details

Specify the detail fields that you want to display in the table.

Resources

Server displays all the group and detail objects in the selected business view or dataset.

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

Select to add the selected object to display in the table. 

Remove button

Select to remove the added object.

Field

Server lists the group and detail objects that you have added to the table as the detail fields.

Label

Specify the text of the labels of the detail columns, which by default are the display names of the added objects. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Sort Fields By

Select to open the Custom Sort dialog box to define how to sort data in the table.

### 
Group

Specify the fields for group data of the table. 

Resources

Server displays all the available group objects  you can use to group the data in the table. 

Sort button

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for group objects.

Add button

Select to add the selected group object as a group field.

Remove button

Select to remove the selected group object.

Field

Server lists all the group objects that you have added as the group fields.

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

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for aggregation objects.

Add button

Select to add the selected aggregation object as the summary field. 

Remove button

Select to remove the selected aggregation object.

Field

Server lists the groups that you have added in the table and the aggregation objects added to summarize data in each group.

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

The wizard contains two tabs: Columns and Summary.

### 
Columns

Specify the group and aggregation objects you want to display as the columns of the table. 

Resources

Server displays all the group and aggregation objects in the selected business view or dataset.

Sort button

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

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
