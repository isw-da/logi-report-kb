---
title: "Insert Filter Control Dialog Box Properties"
id: 45203904962701
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203904962701-Insert-Filter-Control-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:49Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Insert Filter Control Dialog Box Properties 

You can use the Insert Filter Control dialog box to insert a filter control into the dashboard body to filter component data. This topic describes the properties in the dialog box.

Server displays the dialog box when you drag Filter Control from Toolbox in the Resources panel to the dashboard body.

Title

Specify the title of the filter control. 

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

- Calendar icon
Select to open the calendar to specify a Date/Time value. 

Link to Other Filters

Clear if you don't want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

Special Function

Select a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

Apply To

Select the components which you want the filter control to filter. <All> means all the data components involving the selected fields in the dashboard.  

OK

Select to insert the filter control in the dashboard body.

Cancel

Select to close the dialog box without the insertion.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without the insertion.
