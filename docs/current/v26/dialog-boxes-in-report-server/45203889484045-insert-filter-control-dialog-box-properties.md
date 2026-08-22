---
title: "Insert Filter Control Dialog Box Properties"
id: 45203889484045
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203889484045-Insert-Filter-Control-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:30Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Insert Filter Control Dialog Box Properties

You can use the Insert Filter Control dialog box to insert a filter control into a report for filtering data components in the report (excluding its subreport). This topic describes the properties in the dialog box.

Control Type

You can only select Text List as the type of the filter control. 

Select Fields

Select the fields you want to bind to the filter control from the list. All the selected fields should be of the same data type. You cannot bind the uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

The common usage is to select one field, and then based on the field to filter the data of the components that use the same data source as the selected field. 

To filter components using different data sources, choose a common field all the data sources contain and select the field in all the data sources one by one.

Customize Initial Values

By default, Server applies all the values of the selected fields in the filter control. Select Customize Initial Values if you want to customize the value list.

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

Link to Other Filters

Clear if you don't want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

In the case of one filter using a business view and another using a query, if the business view contains the query definition, Server also interlinks the two filter controls. 

Apply To 

Select the components which you want the filter control to filter. <All> means all the data components involving the selected fields in the dashboard. 

OK

Select to insert the filter control into the report.

Cancel

Select to close the dialog box without the insertion.

Help

Select to view information about the dialog box.
