---
title: "Unique Key Dialog Box Properties"
id: 28891562975885
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891562975885-Unique-Key-Dialog-Box-Properties
updated_at: 2026-02-26T02:13:13Z
source_host: docs-report.zendesk.com
---
# 
Unique Key Dialog Box Properties

This topic describes how you can use the Unique Key dialog box to select a unique key for a real time chart. 

Server displays the dialog box when you select Incremental Fetch in the Bind Data screen of a chart in the Web Report Wizard, or select Incremental Fetch in the Insert Chart dialog box, Chart Wizard, or Convert to Chart dialog box.

Resources

Server lists all the elements in the business view used by the real time chart.

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

Select to add the selected fields to the Unique Key box.

Remove button

Select to remove the selected fields from the Unique Key box.

Unique Key

Server lists the fields you have added as the unique key, which is used to guarantee there are no two records with the same unique key value in the real time chart.

When you have specified a real time chart with a unique key, each time when the chart automatically updates itself, Server will filter the data that has the same unique key value as the previous loaded data records and only add data with different unique key value to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when Server has already loaded a record with the product ID 1 in USA into the chart, it will add no more records of this product ID in USA into the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the chart will update each time you add new records to the database with more recent times. 

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
