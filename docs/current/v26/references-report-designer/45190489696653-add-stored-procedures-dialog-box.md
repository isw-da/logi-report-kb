---
title: "Add Stored Procedures Dialog Box"
id: 45190489696653
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190489696653-Add-Stored-Procedures-Dialog-Box
updated_at: 2026-04-30T15:12:44Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Add Stored Procedures Dialog Box

You can use the Add Stored Procedures dialog box to add stored procedures from the database to a catalog. This topic describes the options in the dialog box.
    

Designer displays the Add Stored Procedure dialog box when you right-click a JDBC connection node and then select Add Stored Procedure from the shortcut menu in the Catalog Manager, or in the dialog box where a stored procedure list is available, expand the Stored Procedures node in a catalog data source that contains only one JDBC connection and select <Add Stored Procedure...>. 

Designer displays these options:

Database Catalog

This drop-down list displays all the catalogs in the database. Select the catalog that contains the stored procedures you need. 

Stored Procedures

This box lists the stored procedures in the selected database catalog in a three-level tree. The top level is SQL-catalog, second is SQL-schema, and the third are stored procedures. Select one or more stored procedures to add to the catalog.

Sort icon

Select to display the Sort drop-down menu to specify how to sort the stored procedures.

- 
Ascending
Select to sort the stored procedures in the ascending order.

- 
Descending
Select to sort the stored procedures in the descending order.

- 
No Sort
Select to keep the original order of the stored procedures as in the database.

Designer determines the default sort order  according to the Sort option in the Catalog category of the Options dialog box. If you do not select Sort in the Options dialog box, Designer selects No Sort by default in the drop-down menu. In addition, the change of sort order is a one-off action which Designer does not remember after you exit  the dialog box, meaning, each time when you open the dialog box, Designer always applies the default sort order.

Search icon

Select to open the search box to search for stored procedures. To start searching, type the text you want to search for in the search box and Designer lists the stored procedures containing the matched text.

You can use the following options in the search box:

- 
Drop-down icon

Select to list more search options.
						

- 
Highlight All

Select to highlight all the matched text. 

- 
Match Case

Select to search for text that meets the case of the text you type. 

- 
Match Whole Word

Select to search for text that looks the same as the text you type.

- 
Delete icon

Select to close the search  box and cancel the search.

Add

Select to add the specified stored procedures to the catalog.

Done

Select to apply all changes and close the dialog box.

Help

Select to view information about the dialog box.
