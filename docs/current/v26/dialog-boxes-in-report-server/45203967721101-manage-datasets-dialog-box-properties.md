---
title: "Manage Datasets Dialog Box Properties"
id: 45203967721101
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203967721101-Manage-Datasets-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:57Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Manage Datasets Dialog Box Properties

This topic describes how you can use the Manage Datasets dialog box to manage datasets in a web report.

Server displays the Manage Datasets dialog box when you navigate to Menu > Edit > Manage Datasets in the Edit Mode of Web Report Studio.

Dataset List

Server lists all the datasets you have created for the report.

- 
Name
Name of a dataset. You can select a name to edit it. 

- 
Data Source
Catalog data source in which you have created a dataset.

- 
Business View
Data resource based on which you have created a dataset.

New

Select to add a new dataset in the report. Server displays the New Dataset dialog box. See the properties in the dialog box:

- 
Choose Data from
Select a business view that contains the resources you want to use for the new dataset.

- 
New Dataset Name
Type a name for the new dataset.

- 
OK
Select to create the dataset and close the dialog box.
            

- 
Cancel
Select to close the dialog box without creating a dataset.
            

Remove

Select to remove the selected dataset from the report. You cannot remove a dataset when any data component is using it.

Optimize Dataset

Select to optimize the specified dataset. Server displays the Optimize Dataset dialog box. Choose a retrieved data scope for the dataset:

- 
Only Resources Used in Report
Select it if you only want to retrieve data resources used in the current report at runtime. This way ensures the best performance since the least data is retrieved.

- 
All Resources  in Dataset
Select it if you want to retrieve all data resources defined in the dataset at runtime. Unless you manually added data fields to the dataset, this is the same as Only Resources Used in Report.
            

- 
All Resources  in Business View
Select it if you want to retrieve all data resources in the business view on which the dataset is based at runtime. This usually leads to lower performance and is not of any benefit unless you expect to often need to add more fields to the report.
            

Data tab

You can specify the data fields to include in the selected dataset.

- 
Resources
This box lists the resources you can use for the dataset.  The available resources include all view elements of the business view and the dynamic resources you have created for the business view in the report.

- 
Dataset Resources
This box lists the data fields you  add to the dataset.

- 
Add button
Select to add the specified data field in the Resources box to include in the dataset.

- 
Remove button
Select to remove the specified data field from the dataset. You can only remove the fields that are not used by any data component that uses the dataset, either directly or indirectly. 

- 
Move Up button
Select to move the specified data field higher in the display order.

- 
Move Down button
Select to move the specified data field lower in the display order.

Filter tab

You can specify conditions to filter the selected dataset. See Edit Dataset Filter Dialog Box Properties for more information about the properties.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
