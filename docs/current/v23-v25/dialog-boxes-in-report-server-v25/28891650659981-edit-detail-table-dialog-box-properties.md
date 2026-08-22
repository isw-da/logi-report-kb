---
title: "Edit Detail Table Dialog Box Properties"
id: 28891650659981
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891650659981-Edit-Detail-Table-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:43Z
source_host: docs-report.zendesk.com
---
# 
Edit Detail Table Dialog Box Properties

This topic describes how you can use the Edit Detail Table dialog box to edit the fields to display in the table when performing the go-to-detail action on the summary. 

Server displays the dialog box when you right-click a summary value (for a chart it is any data marker) and select Edit Detail Table from the shortcut menu.

Resources

Server displays all the group and detail objects in the current business view or dataset.

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

Select to add the selected view element to display in the table. 

Remove button

Select to remove the selected view element.

 Field

Server lists the view elements that you have added to the detail table. 

Move Up button

Select to move the selected item higher in the list.

Move Down button

Select to move the selected item lower in the list.

Target

Specify the window or frame in which you want to load the detail table.

- 
New Window
  Select to load the detail table into a new window.

- 
Same Frame
 Select to load the detail table into the same frame or window where the main report is. 

- 
Other Frame
  Select to load the detail table into some other available frame. Type the frame name into the text box to find the frame. If it cannot find the frame, Server will load the detail table report into a new window.

- 
<Server Setting>
 Select to load the detail table according to the setting of Target of Detail Table Report and Links in the Web Report Studio profile. 

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
