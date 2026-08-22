---
title: "Convert to Crosstab Dialog Box Properties"
id: 45203954798733
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203954798733-Convert-to-Crosstab-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:31Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Convert to Crosstab Dialog Box Properties

This topic describes how you can use the Convert to Crosstab dialog box to convert a table or chart to a crosstab. 

Server displays the dialog box when you focus on a table or a chart and then select the crosstab icon  on the visualization toolbar but the data fields in the table or chart are not enough for a crosstab.

Crosstab Title

Specify a title for the crosstab.

Font button

Select the button, and Server displays the following dialog box for you to edit the font properties of the crosstab title:

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

Select a business view or dataset on which you want to build the crosstab.

Filter

Select to open the Edit Dataset Filter dialog box to specify the filter you want to apply to the selected business view.

Resources

Server displays the elements in the selected business view or dataset.

Show All Fields/Show Used Fields

Select to show all the business view elements or only the ones that the current data component uses, in the Resources box. This pair of properties are not available when you select another business view to convert to crosstab with.

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

Add Column button

Select to add the selected group object  to display in the columns of the crosstab.

Add Row button

Select to add the selected group object  to display in the rows of the crosstab.

Add Summary button

Select to add the selected aggregation object  or detail object  to be the summary field of the crosstab.

Columns/Rows

- 
Field
    Server lists the group objects that will display in the columns/rows of the crosstab.

- 
Label
  Specify the text of the labels for the column/row headers. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

- 
Sort
    Specify the sort order of the group objects.

Summaries

- 
Field
    Server lists the objects that you select to create summaries.

- 
Label
  Specify the text of the labels for the summaries. You can select a text box to edit the label, or select the Auto Map Field Name checkbox beside the text box to automatically map the label to the dynamic display name of the object.

- 
 Aggregate
    Specify the functions for summarizing data of the selected detail objects.

- 
Distinct On

       Server enables this property when you select DistinctSum as the aggregate function, and you should set it. Select the ellipsis button , and then in the Select Fields dialog box select the fields according to whose unique values you want to calculate the DistinctSum function.    

- 
Comparison Function
    Select to open the Comparison Function dialog box to add a comparison function as an aggregate for the crosstab.

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Remove button

Select to remove the selected resource.

OK

Select to convert to the specified crosstab and close the dialog box.

Cancel

Select to close the dialog box without conversion.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without conversion.
