---
title: "Insert Banded Object Dialog Box Properties"
id: 28891597352589
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891597352589-Insert-Banded-Object-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:58Z
source_host: docs-report.zendesk.com
---
# 
Insert Banded Object Dialog Box Properties

This topic describes how you can use the Insert Banded Object dialog box to insert a banded object to a report. Server displays the dialog box when you drag Banded Object from the Components panel to the destination. 

This topic contains the following sections:

- Details Tab Properties

- Group Tab Properties

- Summary Tab Properties

You see these elements on all the tabs:

Banded Title

Specify a title for the banded object.

Font button

Specify the font properties for the title of the banded object. After you select this button, Server displays the following dialog box for you to edit the font properties:

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

Specify the business view or dataset in the current catalog on which you want to build the banded object.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter which you want to apply to the dataset of the banded object.

OK

Select to insert a banded object into the report and close the dialog box.

Cancel

Select to close the dialog box without inserting a banded object.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without inserting a banded object.

## 
Details Tab Properties

Specify the detail fields that you want to display in the banded object.

Resources

Select the group objects  and detail objects  in the selected business view or dataset to add them to the right box one by one.

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

Select to launch the search bar to search for fields that you want.

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

Select to add the selected object from the Resources box to the right box. 

Remove button

Select to remove the selected object from the right box.

Field

Server lists the group and detail objects that you have added (or want to add) to the banded object as the detail fields.

Label

Specify the text for the labels of the detail fields, which by default are the display names of the added objects. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Sort Fields By

Select to open the Custom Sort dialog box to specify how to sort data in the banded object.

## 
Group Tab Properties

Specify the fields for grouping the data in the banded object. 

Resources

Select the group objects  you want to use to group the data in the banded object and add them to the right box one by one.

Sort button

Select an order from the drop-down list to sort the group objects. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for group objects.

Add button

Select to add the selected group object as a group-by field.

Remove button

Select to remove the selected group object from the right box.

Field

Server lists all the group objects that you have added as the group-by fields.

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

## 
Summary Tab Properties

Specify the fields on which you want to create summaries.

Resources

Select the aggregation objects  you want to use to create summaries in the banded object, and add them to the right box one by one.

Sort button

Select an order from the drop-down list to sort the aggregation objects. The order applies to all the resource trees where you see the business view in Web Report Studio.

Search button

Select to launch the search bar to search for aggregation objects.

Add button

Select to add the selected aggregation object as the summary field. 

Remove button

Select to remove the selected aggregation object from the right box.

Field

Server lists the groups that you have added in the banded object and the aggregation objects that you have added to summarize data in each group.

Row

Specify to put the summary field in the header or footer row. If the summary is calculated on a group-by field, Server will place it in the group header or footer of the corresponding group; if the summary is calculated on the banded object, Server will place it in the banded header or footer.

Column

Not available to banded objects.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.
