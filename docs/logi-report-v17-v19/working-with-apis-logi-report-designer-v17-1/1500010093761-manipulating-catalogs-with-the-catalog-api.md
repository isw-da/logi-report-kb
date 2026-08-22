---
title: "Manipulating Catalogs with the Catalog API"
id: 1500010093761
section: "Working with APIs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093761-Manipulating-Catalogs-with-the-Catalog-API
updated_at: 2021-07-23T19:14:28Z
---

# Manipulating Catalogs with the Catalog API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056502-Making-Preparations-Before-Using-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093781-Running-the-Catalog-API-Samples)

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

**Parameters**

* UseJDBCODBCBridge - Indicates to connect to the database with a JDBC-ODBC Bridge.
* name - The name of the connection.
* desc - The description for the connection.
* url - The URL used to connect to the database.
* driver - The database driver.
* info - The connection information.

## Inserting a Table/View/Synonym

You can use the following methods to insert a table, view, or synonym into a catalog and return the handle of the newly inserted object.

* insert(String catalogName, String schemaPattern, String tableName, int type)
* insert(String catalogName, String schemaPattern, String tablePattern, int type, boolean setMappingName)

**Parameters**

* catalogName - The catalog name.
* schemaPattern - The schema pattern.
* tablePattern - The table name.
* type - The table type.

## Inserting a Stored Procedure

You can use the following methods to insert a stored procedure into a catalog and return the handle of the newly inserted procedure.

* insert(String procName,String catalog,String schema,String name,String remarks,int iType)
* insert(String procName, String catalog, String schema, String name, String remarks, int iType)

**Parameters**

* procName - The procedure mapping name.
* catalog - The catalog name of the procedure.
* schema - The schema name of the procedure.
* name - The procedure name.
* remarks - The remarks on the procedure.
* iType - The result type of the procedure.

## Importing an SQL File

You can use the following methods to import an SQL file into a catalog and return the handle of the newly imported SQL file.

* insert(String SQLName, String filename)
* insertSql(String dataSourceName, String SQLName, String filename)

**Parameters**

* SQLName - The SQL name.
* filename - The imported file name.

## Inserting a UDS

You can use the following methods to insert a user-defined data source into a catalog and return the handle of the newly inserted UDS.

* insert(String strDSName, String strClassName, String strParameter, UDSColumnInfo udsColInfo)
* insert(String dataSourceName, String strDSName, String strClassName, String strParameter,
  UDSColumnInfo udsColInfo)

**Parameters**

* strDSName - The UDS name.
* strClassName - The name of the UDS class.
* strParameter - The parameter value.
* udsColInfo - The specified column information.

## Inserting a Query

You can use the following methods to insert a query into a catalog and return the handle of the newly inserted query.

* insert(String qryName, QueryFieldInfo queryFieldInfo,QueryJoinInfo queryJoinInfo, QueryQBEInfo queryQBEInfo, QueryAndInfo queryAndInfo)
* insert(String dataSourceName, String qryName, QueryFieldInfo queryFieldInfo, QueryJoinInfo queryJoinInfo, QueryQBEInfo queryQBEInfo, QueryAndInfo queryAndInfo)

**Parameters:**

* qryName - The query name.
* queryFieldInfo - The table and fields information.
* queryJoinInfo - The join information.
* queryQBEInfo - The QBE information.
* queryAndInfo - The where condition information.

## Modifying a Query

You can modify a query using the Catalog API in the following ways.

### Adding or Deleting Tables in a Query

* set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula) - Adds a new table to a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.
* deleteQueryTable(String dataSourceName, String qryName, String tablename) - Deletes the selected table in a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The tables you want to add should already exist in the specified catalog.

**Parameters**

* qryName - The query name.
* tablename - The name of the table that is to be inserted or deleted.
* SelectAllFields - Specifies whether or not to insert a table with all its fields.

### Adding or Deleting Fields in a Query

* set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula) - Adds a new field to a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.
* deleteQueryField(String dataSourceName, String qryName, String tablename, String columnname) - Deletes the selected fields in a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.

**Parameters**

* qryName - The query name.
* tablename - The table name of the inserted or deleted field.
* isFormula - Indicates whether the inserted field is a formula.
* columnname - The column name of the deleted field.

### Adding or Deleting Joins in a Query

* set(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo, boolean isSQL92, int outerJoin) - Adds a new join to a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.
* deleteQueryJoin(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo) - Deletes joins in a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.

**Parameters**

* qryName - The query name.
* tableFrom - The name of the table from which the join links.
* columFrom - The name of the column from which the join links.
* tableTo - The name of the table to which the join links.
* columnTo - The name of the column to which the join links.
* operator - Operator of the join to be inserted or deleted.

### Adding or Deleting QBE Conditions in a Query

* setQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression) - Adds a new QBE condition to a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.
* deleteQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression) - Deletes the QBE condition in a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.

**Parameters**

* qryName - The query name.
* tablename - The name of the table where the QBE condition is added or deleted.
* columnname - The name of the column where the QBE condition is added or deleted.
* expression - The expression of the QBE condition.

### Adding or Deleting Where Conditions in a Query

* setCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic) - Adds a new where condition to a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.
* deleteCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic) - Deletes the where conditions in a query and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.

**Parameters**

* qryName - The query handle.
* sLogic - The logic string of the where condition that is to be inserted or deleted.
* sExpression1 - The first expression of the where condition that is to be inserted or deleted.
* sOperator - The operator of the where condition that is to be inserted or deleted.
* sExpression2 - The second expression of the where condition that is to be inserted or deleted.

## Inserting a Business View

To insert a business view into a catalog, use the following method:

* insertBusinessView(String dataSourceName, String queriableName, String businessViewName, boolean isLogicView=false)

**Parameters**

* dataSourceName - The mapping name of the data source in the catalog to which you want to insert the object.
* queriableName - The queriable object's mapping name. The queriable object in a catalog could be a query, UDS, stored procedure, or imported SQL. When queriableName is a valid name of an existing queriable object, a business view is created.
* businessViewName - The name of the business view.
* isLogicView - Indicates whether to insert a business view. When it is false, a business view is created.

When you have a business view created successfully, you can then add elements into it. A business view can contain the following elements: categories, group objects, aggregation objects, and detail objects.

You can use the following methods to insert a view element into a business view and return the handle of the newly inserted object if it is inserted successfully, otherwise null if there is a failure:

* insertBusinessViewCategory(String parentHandle, BusinessViewCategoryInfo info)
* insertBusinessViewGroup(String parentHandle, BVGroupInfo info)
* insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info)
* insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info, Boolean isRawExpression)
* insertBusinessViewDetail(String parentHandle, BVDetailInfo info)

**Parameters**

* parentHandle - The handle of the parent object. It can be a business view or a category.
* info - The definition class of the view element. It can contain its children's definition.
* isRawExpression - Specifies whether to create a custom aggregation but not compile it. If it is false, the method complies the custom aggregation and starts a javac thread.

When using *insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info)* or *setBusinessViewAggregationInfo(String aggHandle, BVAggregationInfo aggInfo)* to add or modify many custom aggregations at a time, the method compiles the added custom aggregations one by one, therefore the performance could be very slow; however in this way, you can easily figured out if any custom aggregation has error. If you want to enhance the performance, you can use *insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info, true//Boolean isRawExpression)* or *setBusinessViewAggregationInfo(String aggHandle, BVAggregationInfo aggInfo, true//Boolean isRawExpression)* instead and then call *compileBVFormulas(String bvHandle)* to compile all the custom aggregations once. The disadvantage of this way is that it is impossible to find out the custom aggregations that have errors.

## Inserting a Formula, Summary, Parameter or a WHERE Portion

You can use the following methods to insert a formula, summary, parameter, or a WHERE portion into a catalog and return the handle of the newly inserted object.

* insert(String formulaName, String desc, String expression)
* insert(String summaryName, String desc, int functionType, String fieldName, String groupByFld)
* insert(String parameterName, String desc, String prompt, String type, String default Value)
* insert(String wherePortionName, String desc, WherePortionInfo whereportionInfo)

**Parameters**

* formulaName - The name of the formula.
* desc - The description of the object.
* expression - The expression.
* summaryName - The name of the summary.
* functionType - The type of the function.
* fieldName - The field name calculated on.
* groupByFld - The field name grouped by.
* parameterName - The parameter Name.
* prompt - The specified text prompt.
* type - The parameter data type.
* defaultValue - The defaultValue of the parameter.
* wherePortionName - The WHERE portion name.
* whereportionInfo - The WHERE portion information.

## Inserting, Getting, and Deleting Objects in a Catalog

* insert(String name, int type)/insert(String dataSourceName, String name, int type) - Inserts an object into a catalog and returns the handle of the newly inserted object.
* getTables(String dataSourceName) - Gets tables, views, and synonyms in a connection and returns the mapping name array.
* getTables(boolean bIncludeSystemTable) - Gets tables, views, and synonyms in a data source and returns the name array.

* getProcedureNames(String dataSourceName) - Gets all the stored procedures in a catalog and to return the mapping name array.

* getSQLs(String dataSourceName) - Gets all the imported SQLs in a catalog and returns the mapping name array.

* getUDSs(String dataSourceName) - Gets all the UDSs in a catalog and returns the mapping name array.

* getQueries(String dataSourceName) - Gets queries in a catalog and returns the mapping name array.
* getNewQueryName() - Gets a default name for a new query, which must be unique. The name for the first query in a catalog is query1. The following query is query2, then query3, and so on.

* getSQLString(String dataSourceName, String queryName) - Gets the SQL statement text of a query or an imported SQL and returns the SQL statement string.
* getImportedSQLString(String dataSourceName, String importedSQLName) - Gets the original SQL statement of an imported SQL and returns the original SQL statement string.
* getColumns(String dataSourceName, String queryName, boolean allColumns) - Gets columns in a query and returns the table name and column real names.
* getColumnMappingnames(String dataSourceName, String queryName) - Gets column mapping names in a query and returns the table name and column mapping names.
* getColumnsCanBeGroupedBy(String dataSourceName, String queryName) - Gets the columns which can be grouped by in a query.
* getDBFields(String dataSourceName, String qryName) - Gets DBFields that can be used in a query and returns the mapping name array.
* getMappingnames(String dataSourceName, String DSName) - Gets the field mapping names in a data source and returns the table name and column mapping names.
* getFormulae(String dataSourceName) - Gets formulas that can be used in a catalog and returns the mapping name array.
* getFormulaeCanBeGroupedBy(String dataSourceName, String queryName, String groupBy) - Gets formulas that are valid to a query and returns the formula names.
* getSummaries(String dataSourceName) - Gets summaries that can be used in a catalog and returns the mapping name array.
* getSummaryCanBeSortedBy(String dataSourceName, String queryName, String groupBy) - Gets summaries that can be sorted by.
* getParameter(String dataSourceName) - Gets parameters in a catalog and returns the mapping name array.
* getParameterCanBeGroupedBy(String dataSourceName) - Gets parameters that can be grouped by.
* getJoins(String dataSourceName, String queryName) - Gets joins in a query and returns the join info array.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) String[i][0] = Table "From" Name, String[i][1] = Column "From" Name, String[i][2] = Table "To" Name, String[i][3] = Column "To" Name
* getAndConditions(String dataSourceName, String queryName) - Gets AND conditions in a query and returns a condition info array.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) String[i][0] = "Logic", String[i][1] = "Expression1" String[i][2] = "Operator", String[i][3] = "Expression2"
* getQBEInfo(String dataSourceName, String queryName) - Gets the QBE condition in a query and returns a QBE info array.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) String[i][0] = column Name, String[i][j](j>=1) = condition expression of this column.
* getNewReportName() - Gets a default name for a new report, which must be unique. The name for the first report in a catalog is report1. The following report is report2, then report3, and so on.

* delete(Stringhandle) - Deletes an object from its parent node and returns true if the specified object is removed.

**Parameters**

* name - The object name.
* type - The object type.
* dataSourceName - The mapping name of the data source in the catalog.
* queryName - The mapping name of the query.
* qryName - The query name.
* importedSQLName - The mapping name of the imported SQL.
* allColumns - Selects all columns in the specified tables.

* DSName - The data source object name, such as Query, SQL, UDS, and Procedure.
* groupBy - The group-by field.

* handle - The handle of the object that is to be deleted.

## Refreshing the Reference Table of a Catalog

You can use the method *public boolean refreshReference()* to refresh the [reference table](https://devnet.logianalytics.com/hc/en-us/articles/1500010056662-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) of a catalog.

## Saving a Catalog

* save() - Saves an open catalog and returns a Boolean value. If the operation is successful, the method returns true; otherwise, it returns false.
* saveAs(String path, String name) - Saves an open catalog as a new catalog file. You can save the catalog as a binary catalog using the extension .cat, or an XML catalog using the extension .cat.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056502-Making-Preparations-Before-Using-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093781-Running-the-Catalog-API-Samples)
