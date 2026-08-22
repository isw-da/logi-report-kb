---
title: "Expressions Dialog Box"
id: 28898020968333
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898020968333-Expressions-Dialog-Box
updated_at: 2024-09-30T09:08:59Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Expressions Dialog Box

You can use the Expressions dialog box to compose filter conditions. This topic describes the options in the dialog box.
    

Designer displays the Expressions dialog box when you select the ellipsis  to compose a condition, and provides you with different options in the dialog box for defining filter condition or record level security condition.

When you use the Expressions dialog box to compose the filter conditions for a query or a dataset created from a query, Designer displays the following tabs in the dialog box (Designer displays the Subquery tab only when you use the dialog box  for filtering a query):

- Real Name Tab

- Subquery Tab

- Field Value Tab

## 
Real Name Tab

Use this tab to specify the field on which to create the filter.

- When you use the dialog box for defining a query filter, this tab lists the tables that you have added in the query with all their columns, and the parameters and valid formulas of these columns in the same catalog data source as the query.

- When you use the dialog box for defining a dataset filter, this tab lists the tables that you have added in the data resource on which the dataset is created with all their columns, and the parameters and valid formulas of these columns in the same catalog data source as the data resource.

Double-click the required field to create the filter on it.

You can use the following symbols at the bottom to modify the expression:

- 
+
Select the symbol to add numbers or fields together in the Expression menu.

- 
-
Select the symbol to subtract numbers or fields together in the Expression menu.

- 
*
Select the symbol to multiply numbers or fields together in the Expression menu.

- 
/
Select the symbol to divide numbers or fields together in the Expression menu.

- 
=
Select the symbol to equate fields together.

- 
"
Select the symbol to place quotations on long character strings or name that have blanks in them. For example, you should place quotes on values such as "New York" or "Washington DC").

- 
||
Select the symbol to place fields together in the same Expression menu, for example, "New York" || "Washington DC").

- 
( )
Select the symbol to place your fields in parentheses.

## 
Subquery Tab

Designer displays this tab when you use the dialog box for defining filter for a query. You can use it to create a subquery to use in the query filter by editing a query or creating a new query.

- 
Edit Subquery
Select to open the Query Editor dialog box to edit the query.

- 
New Subquery
Select to create a subquery here.

## 
Field Value Tab

Use this tab to specify the value using which to filter the specified field. 

Designer disables this tab when you open the Expressions dialog box to set the filter field. It lists all column names of the related table, in which the field to be filtered is. Select the column name of the field to be filtered, select OK. Designer then lists the values of the field. Choose the required value and select Set to use it to filter the field.

When you use the Expressions dialog box  to compose the conditions for a record level security policy, Designer displays the following tabs in the dialog box:

- Mapping Name Tab

- Value Tab

## 
Mapping Name Tab

Use this tab to specify the field to add in the condition.

This tab lists the tables/views/synonyms, queries, and hierarchical data sources in the current catalog data source with all their columns, and the parameters and valid formulas of these columns in the catalog data source, and the User Name special field. Double-click the required field to add it to the condition.

## 
Value Tab

Use this tab to specify the value using which to filter the specified field.

Designer disables this tab when you open the Expressions dialog box to set the field on which to build the condition. When you select a column for a condition, you can obtain the values of the column as follows:

- Select the column in the Mapping Name tab.

- Select the Value tab and Designer lists the values of the selected column.

- Double-click a value to set it as the value of the condition.

Previous Topic  Next Topic
