---
title: "Bind Data Dialog Box"
id: 45190482908429
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190482908429-Bind-Data-Dialog-Box
updated_at: 2026-04-30T15:12:48Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Bind Data Dialog Box

You can use the Bind Data dialog box to bind a dataset to the report body. This topic describes the options in the dialog box.
    

Designer displays the Bind Data dialog box when you do one of the following:

- Navigate to Report > Bind Data.
            

- Right-click any blank area in the report body and select Bind Data from the shortcut menu.
            

- Select  to specify a formula to return value to some page  properties for a page report tab in the General tab of the Page Setup dialog box or via the  Page Panel object in the Report Inspector, or to some Excel properties of a page report tab or web report, but you have not bound a dataset to the report body, then select OK in the message box.

Designer provides you with different options in the dialog box for binding data to a page/web report or a library component.

## 
For Binding Data to a Page/Web Report

Designer displays these options:

New Dataset

Select to create a dataset based on a data resource in the current catalog. The data resource box on the right lists the predefined data resources in the catalog. Select the data resource you want to bind to the report body. Designer then automatically creates a dataset based on the specified data resource in the report. 

- 
<New XXX...>/<Add XXX...>
Select to create or add a data resource of the same type in the catalog.

Existing Dataset

Select to use a dataset from the ones that you have created in the report.

- 
<New Dataset...>
Select to create a dataset using the New Dataset dialog box.
            

Current Dataset

Designer disables this option because  the report body cannot use inherited dataset.

Less Options/More Options

Select to hide or show the dataset selection panel to choose a dataset to bind to the report body.

Edit

Select to modify the specified query  in the Query Editor dialog box, business view in the Business View Editor dialog box, or dataset in the Dataset Editor dialog box.

OK

Select to bind the specified dataset to the report body and close the dialog box.

Cancel

Select to quit binding   data to the report body and close the dialog box.

Help

Select to view information about the dialog box.

 

## 
For Binding Data to a Library Component

Designer displays these options:

Available data resources

This box lists the predefined business views in the current catalog. Select the business view you want to bind to the report body. Designer then automatically creates a dataset based on the specified business view in the library component.

OK

Select to bind the specified dataset to the report body and close the dialog box.

Cancel

Select to quit binding data to the report body and close the dialog box.

Help

Select to view information about the dialog box.
