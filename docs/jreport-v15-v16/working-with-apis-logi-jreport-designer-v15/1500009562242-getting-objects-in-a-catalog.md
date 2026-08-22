---
title: "Getting Objects in a Catalog"
id: 1500009562242
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562242-Getting-Objects-in-a-Catalog
updated_at: 2021-07-24T05:56:22Z
---

# Getting Objects in a Catalog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582621-Inserting-and-Deleting-an-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582661-Refreshing-the-Reference-Table-of-a-Catalog)

# Getting Objects in a Catalog

The following are methods to get objects into a catalog:

* **getTables(String dataSourceName)**  
   Gets tables, views and synonyms in a connection and returns the mapping name array.
* **getTables(boolean bIncludeSystemTable)**  
   Gets tables, views and synonyms in a data source and returns the name array.

* **getProcedureNames(String dataSourceName)**  
   Gets all the stored procedures in a catalog and to return the mapping name array.

* **getSQLs(String dataSourceName)**  
   Gets all the SQL files in a catalog and to return the mapping name array.

* **getUDSs(String dataSourceName)**  
   Gets all the UDSs in a catalog and to return the mapping name array.

* **getQueries(String dataSourceName)**  
   Gets queries in a catalog and returns the mapping name array.
* **getNewQueryName()**  
   Gets a default name for a new query, which must be unique. The name for the first query in a catalog is query1. The following query is query2, then query3 and so on.

* **getSQLString(String dataSourceName, String queryName)**  
   Gets the sql statement text of a query or an imported SQL and returns the SQL statement string.
* **getImportedSQLString(String dataSourceName, String importedSQLName)**  
   Gets the original SQL statement of an imported SQL and returns the original SQL statement string.
* **getColumns(String dataSourceName, String queryName, boolean allColumns)**  
   Gets columns in a query and returns the table name and column real names.
* **getColumnMappingnames(String dataSourceName, String queryName)**  
   Gets column mapping names in a query and returns the table name and column mapping names.
* **getColumnsCanBeGroupedBy(String dataSourceName, String queryName)**  
   Gets the columns which can be grouped by in a query.
* **getDBFields(String dataSourceName, String qryName)**  
   Gets DBFields that can be used in a query and returns the mapping name array.
* **getMappingnames(String dataSourceName, String DSName)**  
   Gets the field mapping names in a data source and returns the table name and column mapping names.
* **getFormulae(String dataSourceName)**  
   Gets formulae that can be used in a catalog and returns the mapping name array.
* **getFormulaeCanBeGroupedBy(String dataSourceName, String queryName, String groupBy)**  
   Gets formulae that are valid to a query and returns the formula names.
* **getSummaries(String dataSourceName)**  
   Gets summaries that can be used in a catalog and returns the mapping name array.
* **getSummaryCanBeSortedBy(String dataSourceName, String queryName, String groupBy)**  
   Gets summaries that can be sorted by.
* **getParameter(String dataSourceName)**  
   Gets parameters in a catalog and returns the mapping name array.
* **getParameterCanBeGroupedBy(String dataSourceName)**  
   Gets parameters that can be grouped by.
* **getJoins(String dataSourceName, String queryName)**  
   Gets joins in a query and returns the join info array.

  **Note**: String[i][0] = Table "From" Name, String[i][1] = Column "From" Name, String[i][2] = Table "To" Name, String[i][3] = Column "To" Name
* **getAndConditions(String dataSourceName, String queryName)**  
   Gets AND conditions in a query and returns a condition info array.

  **Note**: String[i][0] = "Logic", String[i][1] = "Expression1" String[i][2] = "Operator", String[i][3] = "Expression2"
* **getQBEInfo(String dataSourceName, String queryName)**  
   Gets the QBE condition in a query and returns a QBE info array.

  **Note**: String[i][0] = column Name, String[i][j](j>=1) = condition expression of this column.
* **getNewReportName()**  
  Gets a default name for a new report, which must be unique. The name for the first report in a catalog is report1, after which the following reports will be named report2, report3 and so on.

**Parameters**

* dataSourceName - The mapping name of the data source in the catalog.
* queryName - The mapping name of the query.
* qryName - The query name.
* importedSQLName - The mapping name of the imported SQL.
* allColumns - Selects all columns in the specified tables.

* DSName - The data source object name, such as Query, SQL, UDS, and Procedure.
* groupBy - The groupBy field.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582621-Inserting-and-Deleting-an-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582661-Refreshing-the-Reference-Table-of-a-Catalog)
