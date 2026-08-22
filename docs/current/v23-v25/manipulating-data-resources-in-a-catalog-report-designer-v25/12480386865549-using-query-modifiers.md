---
title: "Using Query Modifiers"
id: 12480386865549
section: "Manipulating Data Resources in a Catalog - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480386865549-Using-Query-Modifiers
updated_at: 2026-02-25T23:47:39Z
source_host: docs-report.zendesk.com
---
# 
Using Query Modifiers

Query modifiers, also called WHERE portions in Report, are the WHERE clauses in SQL select statements, which are saved independently from queries in a catalog (not related to queries). When you run a report using a Java application that uses the Engine Bean, you can specify a query modifier to the Report system via the Engine Bean, the Report API then constructs the SQL statement based on the query  the report uses and may substitute the WHERE clause in the SQL statement if there is a given query modifier, so that you can generate the report on different data. This topic describes how you can create query modifiers in a catalog.

To add a query modifier in a catalog

- 
Open the catalog to which you want to add the query modifier.

- In the Catalog Manager, expand the node of a data source, and then the Queries node.

- Right-click the Query Modifiers node and select New Query Modifier from the shortcut menu. Designer displays the Query Modifier Editor dialog box.
    

- Type a name for the query modifier in the Name text box.

-  From the Type drop-down list, select the type of the query modifier: Structure or String. You can save a query modifier in a catalog in two formats: structure and string. In the structure format, the groups of conditions are stored. The query modifier consists of many condition groups and the groups are connected by a logical operator. Each condition consists of many conditions and the conditions are also connected by a logical operator. Each condition contains a left expression, the relationship operator, and a right expression. In the string format, the text of the query modifier is stored.

- Select a query from the Query drop-down list to build the query modifier. You can select Show Query to view the query.

- In the editing panel, edit the query modifier. If you select the String type, a text editor is available where you can type the WHERE clause; if you select the Structure type, a condition editor is available and you can construct the query modifier by selecting buttons (for more information about how to set the condition, see Filtering with the Filter Format).
    

- Select Check to check the validity of the query modifier according to the query. Designer defines the validity of a query modifier as, all the fields and formulas referenced by the query modifier are available to the chosen query. This validation check also ensures that the query modifier can work with the specified query.
    

- Select Show SQL to view the string of the query modifier.

- Select OK to create the query modifier.
