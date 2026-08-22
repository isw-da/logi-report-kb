---
title: "Choose Data Dialog Box"
id: 45190483723917
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190483723917-Choose-Data-Dialog-Box
updated_at: 2026-04-30T15:12:51Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Choose Data Dialog Box

You can use the Choose Data dialog box to specify the dataset you want to use for a blank page report tab or for a KPI. This topic describes the options in the dialog box.
    

Designer displays the Choose Data dialog box  when you do one of the following:

- In the Select Component for Page Report dialog box, select the Blank component and select OK. 

- When creating a new page report tab, in the Select Component for Page Report Tab dialog box, select the Blank component and select OK. 

- Drag the KPI icon  from the Components panel to the destination in a web report or library component.

Designer displays these options:

Data resource box

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the report tab or KPI.

- 
<New XXX...>/<Add XXX...>
Select to create or add a data resource of the same type in the catalog. Designer does not display this option when you use the dialog box for choosing KPI data in a library component.
            

More Options/Less Options

Select to show or hide the options for specifying the dataset you want to use. Designer does not display this pair of buttons when you use the dialog box for choosing KPI data in a library component. 

- 
New Dataset
Select to create a dataset based on a data resource in the current catalog.

- 
Existing Dataset
Select to use a dataset from the ones that you have created in the page report.- 
<New Dataset...>
Select to create a dataset  using the New Dataset dialog box.

- 
Current Dataset
Designer disables this option because a page report tab cannot use inherited dataset.

Edit

Select to  edit the specified query  in the Query Editor dialog box, business view in the Business View Editor dialog box, or dataset in the Dataset Editor dialog box. Designer does not display this button when you use the dialog box for choosing KPI data  in a library component. 

OK

Select to apply the specified dataset to the report tab or KPI and close the dialog box.

Cancel

Select to quit choosing a dataset for the report tab  or KPI and close the dialog box.

Help

Select to view information about the dialog box.
