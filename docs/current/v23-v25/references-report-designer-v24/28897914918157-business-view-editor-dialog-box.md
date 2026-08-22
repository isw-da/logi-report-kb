---
title: "Business View Editor Dialog Box"
id: 28897914918157
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897914918157-Business-View-Editor-Dialog-Box
updated_at: 2024-09-30T09:06:57Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Business View Editor Dialog Box

You can use the Business View Editor dialog box to create or edit a business view. This topic describes the options in the dialog box.
    

Designer displays the Business View Editor dialog box when you do one of the following:

-  In the Catalog Manager, right-click the Business Views node, select New Business View from the shortcut menu, type a name in the displayed dialog box and select OK. Then in the Add Tables/Views/Queries dialog box, select one resource and select OK.
    Or if you select more than one resource in the Add Tables/Views/Queries dialog box and select OK, then in the Query Editor dialog box, select the required table columns and join the tables and select OK.

- In the Catalog Manager, right-click a business view and select Edit from its shortcut menu.

-  In the Resources box of the Display screen in the map wizard, right-click a business view or an element in it and select Edit from the shortcut menu.

Designer displays these options:

Menu

- 
File
- 
Save
Select to save the business view with all the changes made in this editor.

- 
Save As
Select to save a copy of the business view with a different name.

- 
Close
Select to exit the dialog box.

- 
New
- 
Category
Select to open the Category Property dialog box to add a category into the business view.

- 
Group
Select to open the New View Element dialog box to add a group object into the business view.

- 
Aggregation
Select to open the New View Element dialog box to add an aggregation object into the business view.

- 
Detail
Select to open the New View Element dialog box to add a detail object into the business view.

- 
Hierarchy
Select it and Designer prompts you to provide a name for the new hierarchy you are going to create.

- 
Tools
- 
Security Configuration
Select to open the Edit Business View Security dialog box to configure security for all the business views in the current catalog data source.

- 
Query Editor
Select to open the Query Editor dialog box to edit the data resources used for the business view.

- 
Predefined Filter
Select to open the Predefined Filter dialog box to add predefined filters to the business view.

- 
Options
- 
Auto Add Prefix in Display Names
Similar to the data source property Use Mapping Name Prefix which controls whether to add "tablename_" as the prefix of the table names  in the default mapping names of their columns, this property determines whether to automatically append the same prefix in the default display names of the view elements in the business view when you add view elements based on the columns. The two properties work independently from each another, meaning, you can set Use Mapping Name Prefix to "true" to automatically prefix column names  with corresponding table names in a data source, but choose not to have the prefix for view elements by clearing Auto Add Prefix in Display Names.

By default, this option is cleared. In this case, when a column's mapping name contains the "tablename_" prefix which however is not automatically generated but user customized and you add a view element based on the column, Designer still removes the prefix  from the display name of the view element.

You can also set this option via the same-name property of the business view.

- 
Help
Select to view information about the dialog box.

Toolbar

- 
Save
Select to save the business view with all the changes made in this editor.

- 
Delete
Select to delete the specified categories, groups, aggregations, or details from the business view.

- 
New Category
Select to create a category in the business view.

- 
New Group 
Select to create a group object in the business view.

- 
New Aggregation
Select to create an aggregation object in the business view.

- 
New Detail
Select to create a detail object in the business view.

- 
New Hierarchy
Select it and Designer prompts you to provide a name for the new hierarchy you are going to create.

- 
Select Filter Resources
Select to open the Select Filter Resources dialog box to customize the view elements that are available when you filter reports which use the business view.

- 
Query Editor
Select to open the Query Editor dialog box to edit the data resources used for the business view.

- 
Predefined Filter
Select to add predefined filters to the business view.

- 
Help
Select to view information about the dialog box.

- 
Move Up button
Select to move the specified objects to a higher position.

- 
Move Down button
Select to move the specified objects to a lower position.

Resource Objects

This panel lists all the data resources that you can use for the business view.

- 
Sort icon
Select to display the Sort drop-down menu to specify how to sort the resources.
- 
Ascending
Select to sort the resources in the ascending order.

- 
Descending
Select to sort the resources in the descending order.

- 
No Sort
Select to keep the original order of the resources as in the database.

Designer determines the default sort order according to the Sort option in the Catalog category of the Options dialog box. If you do not select Sort in the Options dialog box, Designer selects No Sort  by default in the drop-down menu. In addition, the change of sort order is a one-off action which Designer does not remember after you exit  the dialog box, meaning, each time when you open the dialog box, Designer always applies the default sort order.

- 
Search icon
Select to open the search box to search for resources in the panel. To start searching, type the text you want to search for in the search box and Designer lists the resources containing the matched text.
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

- 
Close icon
Select to close the panel. To display the panel again, select the expand arrow on the left of the Business View panel.

Business View

You can add or edit the resources of a business view in this panel. Designer arranges the resources in a tree structure. Under the root category, you can add categories, view elements, and hierarchies. You can use categories as virtual folders to hold subcategories and view elements. You can add view elements and hierarchies  in any categories including the root category.

- 
Sort icon
Select to display the Sort drop-down menu to sort the resources excluding the elements in hierarchies in the ascending or descending order.

- 
Search icon
Select to open the search box to search for resources in the panel. To start searching, type the text you want to search in the search box for and Designer lists the resources containing the matched text.
                

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

Previous Topic  Next Topic
