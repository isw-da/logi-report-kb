---
title: "New Dynamic Display Name Dialog Box Properties"
id: 28891578889357
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891578889357-New-Dynamic-Display-Name-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:22Z
source_host: docs-report.zendesk.com
---
# 
New Dynamic Display Name Dialog Box Properties

This topic describes how you can use the New Dynamic Display Name dialog box to add dynamic display names for business view elements in a catalog for a specified Security Identifier (SID). 

Server displays the dialog box when an administrator selects New Dynamic Display Name in the Administration > Other > Dynamic Display Names page on the Server Console.

Catalog

Specify the catalog that contains the business views for which you want to define dynamic display names.

Type the catalog with the full resource path in the text box, for example, /SampleReports/SampleReports.cat, or select Browse to select a catalog in the Select Catalog dialog box.

Organization

The property is available when the Organization feature is enabled. System admin can select the organization of the SID. For an organization admin, the organization of the admin is selected by default and cannot be changed.

SID

Select the SID for which you want to define dynamic display names. An SID can be a group, role, or user in the Report Server security system. When the value is blank, it means all the users (when the Organization feature is enabled, it means all the users in the specified organization).

Select Business View Elements 

 Select to open the Select Business View Elements dialog box to select business view elements in the specified catalog for which you want to define dynamic display names. 

Delete

 Select to delete the selected business view elements.

Business view elements table

After you select the business view elements, you can then delete them if you do not want them. Select the checkbox on the column header to select all the business view elements.

You can also select a column header name to sort the elements either by their qualified names or display names.

- 
Business View Element
Qualified names of the business view elements with the path in the catalog.

- 
Dynamic Display Name
Display names of the business view elements. Double-click a name box, and then edit the name.

OK

Select to apply the dynamic display names and exit the dialog box.

Cancel

Select to close the dialog box without adding dynamic display names.

Help

Select to view information about the dialog box.
