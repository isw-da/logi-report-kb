---
title: "Edit View Element Dialog Box"
id: 12480071303053
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480071303053-Edit-View-Element-Dialog-Box
updated_at: 2026-02-25T23:49:38Z
source_host: docs-report.zendesk.com
---
# 
Edit View Element Dialog Box

You can use the Edit View Element dialog box to edit the specified view element. This topic describes the options in the dialog box.
    

Designer displays the Edit View Element dialog box when you right-click any view element of a business view and select Edit from the shortcut menu in the Catalog Manager.

This dialog box contains the following tabs:

- General Tab

- Security Tab

Designer displays these buttons in all the tabs:

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab

Use this tab to specify the general properties of the view element. 

Display Name

Specify the display name of the view element. An intuitive display name can help users easily understand the element.

Mapping Name

Specify the mapping  field to which you want to map the view element. Select the ellipsis  to select the field.

Type

Select the type of the view element: Group, Aggregation, or Detail.

By Expression 

Designer displays this option when you select Group as the type of the view element. Select it if you want to use an expression to retrieve values for the group object. After you select this option, Designer disables the Mapping Name text box.

- 
Settings
    Select to open the Formula Editor dialog box to compose the expression.

Aggregate Function

Designer displays the drop-down list when you select Aggregation as the type of the view element. It contains the aggregate functions that you can use for the aggregation object. Select the function you need.

- 
Distinct On
Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis  to select the fields according to whose unique values to calculate DistinctSum in the Select Fields dialog box.

Customized

Designer displays this option when you select Aggregation as the type of the view element. Select it if you want to create a custom aggregation by writing a formula. 

- 
Settings
Select to open the Formula Editor dialog box to compose a formula using resources in the current business view, which can return an aggregation.

Tip

Specify the tool tip that displays when users hover over the view element in the business view resource tree at runtime.

Description

Specify the description of the view element.

## 
Security

Use this tab to specify user accessibility to elements of the business views in the current catalog data source. 
For more information about options in the tab, see the Edit Business View Security dialog box.
