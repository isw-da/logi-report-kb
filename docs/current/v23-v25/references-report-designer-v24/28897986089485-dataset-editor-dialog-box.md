---
title: "Dataset Editor Dialog Box"
id: 28897986089485
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897986089485-Dataset-Editor-Dialog-Box
updated_at: 2024-09-30T09:12:41Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Dataset Editor Dialog Box

You can use the Dataset Editor dialog box to edit a dataset in a page or web report. This topic describes the options in the dialog box.
    

Designer displays the Dataset Editor dialog box when you select an existing dataset and select Edit in one of the following dialog boxes: Bind Data dialog box, Choose Data dialog box, or the Data screen of the component wizard.

This dialog box contains the following tabs:

- Data Tab

- Filter Tab

Designer displays these buttons in all the tabs:

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Data Tab

Use this tab to add extra data fields to the dataset or remove existing data fields from the dataset.

Available Resources

This box lists the data fields you can use for the dataset.

- For a dataset based on a query resource, the available resources include all DBFields in the query resource, and the parameters and valid formulas of these DBFields in the same catalog data source as the query resource.
            

- For a dataset based on a business view, the available resources include all view elements of the business view and the dynamic resources you have created for the business view in the current report.            

Dataset Resources

This box lists the data fields you  add to the dataset.

Add button

Select to add the specified data field in the Available Resources box to include in the dataset.

Remove button

Select to remove the specified data field from the dataset. You can only remove the fields that are not used by any data component created on the dataset, either directly or indirectly. 

Remove All button

Select to remove all data fields from the dataset. When you select this button, Designer only removes the unused data fields actually. When you open the dialog box the next time, you can see that the data fields used by data components created on the dataset still display in the Dataset Resources box.

Move Up button

Select to move the specified data field higher in the display order.

Move Down button

Select to move the specified data field lower in the display order.

## 
Filter Tab

Use this tab to specify conditions to filter the dataset.

Designer displays different options in the Filter tab according to the type of the data resource  on which the dataset is based, query resource or business view. See Dataset Filter Dialog Box for more information about the options.

Previous Topic  Next Topic
