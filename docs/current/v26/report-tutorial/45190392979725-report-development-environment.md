---
title: "Report Development Environment"
id: 45190392979725
section: "Report Tutorial"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190392979725-Report-Development-Environment
updated_at: 2026-04-30T15:11:34Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Report Development Environment

This topic introduces the Report Designer development environment, which consists of the following parts:

- Ribbons

- Design/View Area

- Data Panel

- Components Panel

- Inspector Panel

## 
Ribbons

Designer contains seven ribbons that provide access to the following options.

| Tab | Description |
| --- | --- |
| Home | This ribbon contains the basic options for working in Designer, such as the commands for creating, opening, saving a report, undoing or redoing an operation, and editing the font properties like font face, size, color, and alignment. |
| File | This ribbon contains options for working with report files such as saving and closing report files, publishing the report files to Server. |
| View | This ribbon contains options for showing or hiding specific elements in the Designer window. |
| Insert | This ribbon contains options for inserting different report components into a report, such as Table, Chart, Crosstab, Map, KPI, Web Control, Image, and Label. You can also insert the components into a report by dragging them from the Components panel. |
| Format | This ribbon contains options for setting object position and editing font properties. |
| Report | This ribbon contains options for working with the current report, for example you can manage the datasets the report applies, adjust the display sequence of the parameters you have used in the report, and so on. |
| Window | This ribbon contains options for laying out the open reports and switching between the reports. |

## 
Design/View Area

The Design/View area is the window where you develop and test your reports.

The Designer/View area contains the following sections:

- Title bar
The title bar shows the report file name, and three buttons for you to minimize, maximize, and close the active report.

- Design tab
The Design tab is for laying out your report. You can use rulers, grids, and guidelines to position objects.

- View tab
The View tab is for previewing the report layout and result in Designer. The report may not display exactly as the user would see it on Server. Interactive objects such as parameter and filter objects are not active and report links are not active.

- Report tab bar
The report tab bar is for switching among report tabs in a page report. It also provides a shortcut menu that enables you to rename, duplicate, or remove a report tab.

## 
Data Panel

The Data panel is an integrated interface for managing the data resources that you can use in the current report. It contains a toolbar and a resource tree. The toolbar provides options for managing the data resources; the resource tree lists all available resources in the current catalog that are valid for the current report.

You can drag resources from the panel into the report. Queries, business views, formulas, summaries, and parameters in this panel respond to right-clicking events, and thus provide you with shortcuts for editing them in the same way as you would do in the catalog with the Catalog Manager.

## 
Components Panel

The Components panel lists all the components that you can insert into a report.

Designer classifies the components into the following categories. You can use different components in  different report types.

- 
Visual: Chart, Map, KPI, and Rank
            

- 
Grid: Table, Crosstab, and Tabular
            

- 
Basic: Label, Text Box, Image, Subreport, and Banded Object
            

- Web Controls

- 
Others: UDO, Barcode, QR Code, and Multimedia Object
            

The method to create a component using the Components panel is to drag an icon representing that component from the panel to the report design area.

## 
Inspector Panel

The Inspector panel (also referred to as the Report Inspector) lists all the objects contained in a report in a tree structure. You can edit the object properties in the panel to change the appearance of your report.

The Inspector panel contains a toolbar, a report structure tree, and the Properties sheet. 

Toolbar

You can use the buttons on the toolbar to switch the structure nodes for the current report and adjust the display sequence of the report objects in the report structure tree.

Report structure tree

Designer lists all the objects in the current report in a tree structure. By selecting an object in the tree, you also select it in the report design area. You can use the Ctrl and Shift keys to select multiple objects, then the Properties sheet shows only the properties that are common among the selected objects, and you can change the property values for all the selected objects at a time.

Properties sheet

This sheet lists all the properties of the selected object in the report structure tree. You can change how an object 
appears and behaves by changing its property values in this sheet. Depending on the object type, the properties that a certain object holds may greatly differ from those of another.
