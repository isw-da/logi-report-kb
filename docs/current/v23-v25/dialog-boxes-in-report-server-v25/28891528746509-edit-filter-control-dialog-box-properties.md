---
title: "Edit Filter Control Dialog Box Properties"
id: 28891528746509
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891528746509-Edit-Filter-Control-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:58Z
source_host: docs-report.zendesk.com
---
# 
Edit Filter Control Dialog Box Properties 

You can use the Edit Filter Control dialog box to edit a filter control. This topic describes the properties in the dialog box.

Server displays the dialog box after you select the Options button  on the title bar of a filter control and then select Edit Setting from the drop-down menu. 

Title

Specify the title for the filter control. 

Control Type

Select the type of the filter control.

Select Fields

Select the fields you want to bind to the filter control. All the selected fields should be of the same data type. You cannot bind uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

Customize Initial Values

By default, Server applies all the values of the selected fields in the filter control. Select Customize Initial Values if you want to customize the value list.

The customization UI varies with control types:

- 
For Text List, Drop-down List, or Single Value Slider

- 
 Fetch Data
         Select to open the Fetch Data dialog box to select values from the database. Server adds the selected values to the value box. 

- 
Value box
You can type values directly here. Make sure the accuracy of their formats and values.
        The value box is an editable multi-row plain text box. It supports general text editing operations such as copy, paste, cut, backspace, and delete. Press Enter to start a new row. Each row is a value of the user defined value list.

When you have selected Customize Initial Values but do not provide any values in the value box, Server will add all the values of the selected fields in the filter control.

- 
Calendar icon
Select to open the calendar to specify a Date/Time value.

- 
For Range Slider

- 
From
Select the start value of the slider from the drop-down list.

- 
To
      Select the end value of the slider from the drop-down list. 

- 
Calendar icon
Select to open the calendar to specify a Date/Time value.

Link to Other Filters

Clear if you don't want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

Special Function

Select a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

Apply To

Select the components which you want the filter control to filter. <All> means all the data components involving the selected fields in the dashboard. 

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
