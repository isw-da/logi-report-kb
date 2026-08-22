---
title: "New Dynamic Connection Dialog Box Properties"
id: 28891618883469
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891618883469-New-Dynamic-Connection-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:21Z
source_host: docs-report.zendesk.com
---
# 
New Dynamic Connection Dialog Box Properties

This topic describes how you can use the New Dynamic Connection dialog box to create a dynamic connection. 

Server displays the dialog box when an administrator selects New Dynamic Connection in the Administration > Connection > Dynamic Connections page on the Server Console.

Catalog

Specify the catalog in which you would like to create a dynamic connection. Select Browse to select a catalog in the Select Catalog dialog box, or type the catalog path in the text box, for example, /SampleReports/SampleReports.cat.

Data Source Name

Select the data source in which you would like to create a dynamic connection in the catalog.

Connection Name

Select a connection to connect to the data source.

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

Select to create the dynamic connection and exit the dialog box.

Cancel

Select to close the dialog box without creating a dynamic connection.

Help

Select to view information about the dialog box.
