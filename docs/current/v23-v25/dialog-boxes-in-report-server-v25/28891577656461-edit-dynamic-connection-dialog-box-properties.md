---
title: "Edit Dynamic Connection Dialog Box Properties"
id: 28891577656461
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891577656461-Edit-Dynamic-Connection-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:16Z
source_host: docs-report.zendesk.com
---
# 
Edit Dynamic Connection Dialog Box Properties

This topic describes how you can use the Edit Dynamic Condition dialog box to edit a dynamic connection. 

Server displays the dialog box when an administrator selects a connection name in the Connection Name column of the Administration > Connection > Dynamic Connections page on the Server Console.

Catalog

Catalog of the dynamic connection. It is read only. 

Data Source Name

Data source of the dynamic connection. It is read only. 

Connection Name

Connection to connect to the data source. It is read only.

Properties

Properties of the database connection. You can select it to expand or collapse the property table.

Add Database User Mapping

Select to add a new database user mapping.

Delete

Select to delete the selected database user mappings.

Database user mapping table

            After you select the database user mappings, you can then delete them if you do not want them. You can select the checkbox on the column header to select all database user mappings. 

- 
SID
  Select the security identifier (SID). A SID can be a group, role, or user in the Report Server security system. You can define at most one database user mapping for an SID within a dynamic connection.

- 
Organization Name
  Double-click the text box, and then select an organization. You can first specify the organization and then the SID. The column is available to system admin when the Organization feature is enabled.

- 
Database User
   Double-click the text box, and then type the database username. Null means using the default database username.  

- 
Database Password
  Double-click the text box, and then type the database password. Server masks the password.

- 
Control
Select Test Connection to test whether the connection configuration works using the database username and password.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
