---
title: "Manipulating Catalogs with the Catalog API"
id: 4405661307927
section: "Working with APIs - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661307927-Manipulating-Catalogs-with-the-Catalog-API
updated_at: 2022-01-27T20:34:16Z
---

# Manipulating Catalogs with the Catalog API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661309079-Making-Preparations-Before-Using-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661310231-Running-the-Catalog-API-Samples)

# Manipulating Catalogs with the Catalog API

When you use the Catalog API to manipulate catalogs, you can choose from two different sets: the original jet.api.CatalogAPI class that applies to catalogs created before v13.5, and the new jet.api.MultipliedCatalogAPI class which applies to catalogs created since v13.5. This topic introduces how you can use the jet.api.CatalogAPI class to perform different tasks on catalogs that were created in versions earlier than v13.5.

This topic contains the following sections:

* [Creating a Connection](#Connection)
* [Inserting a Table/View/Synonym](#Table)
* [Inserting a Stored Procedure](#SP)
* [Importing an SQL File](#SQL)
* [Inserting a UDS](#UDS)
* [Inserting a Query](#Query)
* [Modifying a Query](#QModify)
  + [Adding or Deleting Tables in a Query](#QTable)
  + [Adding or Deleting Fields in a Query](#QField)
  + [Adding or Deleting Joins in a Query](#QJoin)
  + [Adding or Deleting QBE Conditions in a Query](#QBE)
  + [Adding or Deleting Where Conditions in a Query](#QWhere)
* [Inserting a Business View](#BV)
* [Inserting a Formula, Summary, Parameter, or a WHERE Portion](#Formula)
* [Inserting, Getting, and Deleting Objects in a Catalog](#Object)
* [Refreshing the Reference Table of a Catalog](#RefTable)
* [Saving a Catalog](#Save)

## Creating a Connection

You can use the following methods to insert a database connection in a catalog and return the handle of the newly inserted connection. If the operation is not successful, the methods return a null value.

* insert(boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver)
* insert(boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver, ConnectionInfo info)
* insert(String dataSourceName, boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver)
* insert(String dataSourceName, boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver, ConnectionInfo info)
* insertJSONConnection(String dataSourceName, String connectionName, String desc, JSONSchemaURIInfo jsonSchemaURIInfo, JSONInstanceURIInfo jsonInstURIInfo, boolean withAllTables)

## Inserting a Table/View/Synonym

You can use the following methods to insert a table, view, or synonym into a catalog and return the handle of the newly inserted object.

* insert(String catalogName, String schemaPattern, String tableName, int type)
* insert(String catalogName, String schemaPattern, String tablePattern, int type, boolean setMappingName)

## Inserting a Stored Procedure

You can use the following methods to insert a stored procedure into a catalog and return the handle of the newly inserted procedure.

* insert(String procName,String catalog,String schema,String name,String remarks,int iType)
* insert(String procName, String catalog, String schema, String name, String remarks, int iType)

## Importing an SQL File

You can use the following methods to import an SQL file into a catalog and return the handle of the newly imported SQL file.

* insert(String SQLName, String filename)
* insertSql(String dataSourceName, String SQLName, String filename)

## Inserting a UDS

You can use the following methods to insert a user-defined data source into a catalog and return the handle of the newly inserted UDS.

* insert(String strDSName, String strClassName, String strParameter, UDSColumnInfo udsColInfo)
* insert(String dataSourceName, String strDSName, String strClassName, String strParameter, UDSColumnInfo udsColInfo)

## Inserting a Query

You can use the following methods to insert a query into a catalog and return the handle of the newly inserted query.

* insert(String qryName, QueryFieldInfo queryFieldInfo, QueryJoinInfo queryJoinInfo, QueryQBEInfo queryQBEInfo, QueryAndInfo queryAndInfo)
* insert(String dataSourceName, String qryName, QueryFieldInfo queryFieldInfo, QueryJoinInfo queryJoinInfo, QueryQBEInfo queryQBEInfo, QueryAndInfo queryAndInfo)

## Modifying a Query

You can use the Catalog API to manage objects in the queries of a catalog, for example, add more tables to a query, or delete specific fields from a query.

### Adding or Deleting Tables in a Query

You can use the method *set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula)* to add a new table to a query and return a Boolean value (the tables you want to add should already exist in the specified catalog). The method returns "true" if the operation is successful; otherwise, it returns "false".

And use the method *deleteQueryTable(String dataSourceName, String qryName, String tablename)* to delete the selected table in a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

### Adding or Deleting Fields in a Query

You can use the method *set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula)* to add a new field to a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

And use the method *deleteQueryField(String dataSourceName, String qryName, String tablename, String columnname)* to delete the selected fields in a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

### Adding or Deleting Joins in a Query

You can use the method *set(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo, boolean isSQL92, int outerJoin)* to add a new join to a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

And use the method **deleteQueryJoin(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo)** to delete the joins in a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

### Adding or Deleting QBE Conditions in a Query

You can use the method to *setQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression)* to add a new QBE condition to a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

And use the method **deleteQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression)** to delete the QBE condition in a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

### Adding or Deleting Where Conditions in a Query

You can use the method *setCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic)* to add a new where condition to a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

And the method *deleteCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic)* to delete the where conditions in a query and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

## Inserting a Business View

You can use the method *insertBusinessView(String dataSourceName, String queriableName, String businessViewName, boolean isLogicView=false)* to insert a business view into a catalog.

After you create a business view successfully, you can add elements into it. A business view can contain the following elements: categories, group objects, aggregation objects, and detail objects.

You can use the following methods to insert a view element into a business view and return the handle of the newly inserted object if it is inserted successfully; otherwise, return null if there is a failure.

* insertBusinessViewCategory(String parentHandle, BusinessViewCategoryInfo info)
* insertBusinessViewGroup(String parentHandle, BVGroupInfo info)
* insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info)
* insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info, Boolean isRawExpression)
* insertBusinessViewDetail(String parentHandle, BVDetailInfo info)

When using *insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info)* or *setBusinessViewAggregationInfo(String aggHandle, BVAggregationInfo aggInfo)* to add or modify many custom aggregations at a time, the method compiles the added custom aggregations one by one, therefore, the performance could be very slow; however in this way, you can easily figured out if any custom aggregation has error. If you want to enhance the performance, you can use *insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info, true//Boolean isRawExpression)* or *setBusinessViewAggregationInfo(String aggHandle, BVAggregationInfo aggInfo, true//Boolean isRawExpression)* instead and then call *compileBVFormulas(String bvHandle)* to compile all the custom aggregations once. The disadvantage of this way is that it is impossible to find out the custom aggregations that have errors.

## Inserting a Formula, Summary, Parameter or a WHERE Portion

You can use the following methods to insert a formula, summary, parameter, or a WHERE portion into a catalog and return the handle of the newly inserted object.

* insert(String formulaName, String desc, String expression)
* insert(String summaryName, String desc, int functionType, String fieldName, String groupByFld)
* insert(String parameterName, String desc, String prompt, String type, String default Value)
* insert(String wherePortionName, String desc, WherePortionInfo whereportionInfo)

## Inserting, Getting, and Deleting Objects in a Catalog

You can use the following methods to manage the objects in a catalog.

* **insert(String name, int type)/insert(String dataSourceName, String name, int type)**  
  This method inserts an object into a catalog and returns the handle of the newly inserted object.
* **getTables(String dataSourceName)**  
  This method gets tables, views, and synonyms in a connection and returns the mapping name array.
* **getTables(boolean bIncludeSystemTable)**  
  This method gets tables, views, and synonyms in a data source and returns the name array.
* **getProcedureNames(String dataSourceName)**  
  This method gets all the stored procedures in a catalog and returns the mapping name array.
* **getSQLs(String dataSourceName)**  
  This method gets all the imported SQLs in a catalog and returns the mapping name array.
* **getUDSs(String dataSourceName)**  
  This method gets all the UDSs in a catalog and returns the mapping name array.
* **getQueries(String dataSourceName)**  
  This method gets queries in a catalog and returns the mapping name array.
* **getNewQueryName()**  
  This method gets the default name for a new query, which must be unique. The name for the first query in a catalog is query1. The succeeding query is query2, then query3, and so on.
* **getSQLString(String dataSourceName, String queryName)**  
  This method gets the SQL statement text of a query or an imported SQL and returns the SQL statement string.
* **getImportedSQLString(String dataSourceName, String importedSQLName)**  
  This method gets the original SQL statement of an imported SQL and returns the original SQL statement string.
* **getColumns(String dataSourceName, String queryName, boolean allColumns)**  
  This method gets columns in a query and returns the table name and column real names.
* **getColumnMappingnames(String dataSourceName, String queryName)**  
  This method gets column mapping names in a query and returns the table name and column mapping names.
* **getColumnsCanBeGroupedBy(String dataSourceName, String queryName)**  
  This method gets the columns which can be grouped by in a query.
* **getDBFields(String dataSourceName, String qryName)**  
  This method gets DBFields that can be used in a query and returns the mapping name array.
* **getMappingnames(String dataSourceName, String DSName)**  
  This method gets the field mapping names in a data source and returns the table name and column mapping names.
* **getFormulae(String dataSourceName)**  
  This method gets formulas that you can use in a catalog and returns the mapping name array.
* **getFormulaeCanBeGroupedBy(String dataSourceName, String queryName, String groupBy)**  
  This method gets formulas that are valid to a query and returns the formula names.
* **getSummaries(String dataSourceName)**  
  This method gets summaries that you can use in a catalog and returns the mapping name array.
* **getSummaryCanBeSortedBy(String dataSourceName, String queryName, String groupBy)**  
  This method gets summaries that can be sorted by.
* **getParameter(String dataSourceName)**  
  This method gets parameters in a catalog and returns the mapping name array.
* **getParameterCanBeGroupedBy(String dataSourceName)**  
  This method gets parameters that can be grouped by.
* **getJoins(String dataSourceName, String queryName)**  
  This method gets joins in a query and returns the join info array.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) String[i][0] = Table "From" Name, String[i][1] = Column "From" Name, String[i][2] = Table "To" Name, String[i][3] = Column "To" Name
* **getAndConditions(String dataSourceName, String queryName)**  
  This method gets AND conditions in a query and returns a condition info array.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) String[i][0] = "Logic", String[i][1] = "Expression1" String[i][2] = "Operator", String[i][3] = "Expression2"
* **getQBEInfo(String dataSourceName, String queryName)**  
  This method gets the QBE condition in a query and returns a QBE info array.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) String[i][0] = column Name, String[i][j](j>=1) = condition expression of this column.
* **getNewReportName()**  
  This method gets the default name for a new report, which must be unique. The name for the first report in a catalog is report1. The succeeding report is report2, then report3, and so on.
* **delete(Stringhandle)**  
  This method deletes an object from its parent node and returns "true" if the specified object is removed.

## Refreshing the Reference Table of a Catalog

You can use the method *public boolean refreshReference()* to refresh the [reference table](https://devnet.logianalytics.com/hc/en-us/articles/4405661336215-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) of a catalog.

## Saving a Catalog

You can use the method *save()* to save an open catalog and return a Boolean value. The method returns "true" if the operation is successful; otherwise, it returns "false".

Or use the method *saveAs(String path, String name)* to save an open catalog as a new catalog file. You can save the catalog as a binary catalog using the extension .cat, or an XML catalog using the extension .cat.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661309079-Making-Preparations-Before-Using-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661310231-Running-the-Catalog-API-Samples)
