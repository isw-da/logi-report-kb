---
title: "Using Catalog API to Manage Catalogs"
id: 1500009628161
section: "Working with APIs - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628161-Using-Catalog-API-to-Manage-Catalogs
updated_at: 2022-10-14T07:40:58Z
---

# Using Catalog API to Manage Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605162-Using-Server-API-to-Work-with-Logi-Report-Server) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605122-Using-Design-API-to-Design-Reports)

# Using Catalog API to Manage Catalogs

You can use Logi Report Catalog API to work with a catalog and manage the objects in it programmatically, instead of using the GUI in Logi Report Designer, for example, you can create connections, add and delete objects such as tables, queries, and business views in a catalog, and so on. This topic describes how to install the Catalog API and use it to perform different tasks on a catalog.

The following diagram illustrates the workflow of the Catalog API. By combining the Catalog API and the [Design API](https://devnet.logianalytics.com/hc/en-us/articles/1500009605122-Using-Design-API-to-Design-Reports), you can create any report to meet your requirements in a Java development environment.

![Catalog API diagram](https://devnet.logianalytics.com/hc/article_attachments/4404904483607/wkapi_catapi.gif)

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can choose from two different sets of Catalog APIs. The original **jet.api.CatalogAPI** class applies to catalogs created before v13.5, and the new **jet.api.MultipliedCatalogAPI** class applies to catalogs created since v13.5. Since v13.5, the Logi Report catalog structure has changed greatly. The original Catalog API could not meet the new catalog structure, so Logi Report provides a new set of Catalog API to extend and enhance the original one.

You can jump to the following links to view the topics that interest you:

* [Installing the Catalog API](#Install)
* [Preparations Before Using the Catalog API](#Prep)
* [Using jet.api.CatalogAPI for Catalogs Before v13.5](#Use)
  + [Creating a Connection](#Connection)
  + [Inserting a Table/View/Synonym](#Table)
  + [Inserting a Stored Procedure](#SP)
  + [Importing an SQL File](#SQL)
  + [Inserting a UDS](#UDS)
  + [Creating and Modifying a Query](#Query)
  + [Inserting a Business View](#BV)
  + [Inserting a Formula, Summary, Parameter, or a WHERE Portion](#Formula)
  + [Inserting, Getting, and Deleting Objects in a Catalog](#Object)
  + [Refreshing the Reference Table of a Catalog](#RefTable)
  + [Saving a Catalog](#Save)
* [Catalog API Samples](#Sample)

## Installing the Catalog API

When you install Logi Report Designer, the Catalog API is also installed at the same time. After installation, you will have the following components in `<install_root>\lib`:

* report.jar
* JREngine.jar
* log4j-core-2.12.1.jar and log4j-api-2.12.1.jar (for the Logi Report logging system)
* sac-1.3.jar (for installing Catalog API with Design API product)
* ...

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

The Catalog API class is stored in the archive file report.jar. You will need to do the following steps before you can compile and run the program:

1. Set the class path environment variable. Append the following string to your class path that starts the Catalog API (make sure that the path of JREngine.jar is before that of report.jar):

   `<install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar;<install_root>\lib\log4j-core-2.12.1.jar;<install_root>\lib\log4j-api-2.12.1.jar`
2. In your Java program you must set the licensed user and Design API license key.

   `DesignerUserInfo userInfo=new DesignerUserInfo("UID","Design API Key");`
3. Set the reporthome parameter equal to the root path of Logi Report Designer. You can set this in your environment or with the *-Dreporthome* argument to your JVM.

Logi Report Server also includes the Catalog API. If you prefer to use the libraries from Logi Report Server, include the jar file *<server\_install\_root>\lib\JRESServlets.jar* in your class path instead of report.jar. You would then need to use the Server Design API license key rather than the Design API license key.

## Preparations Before Using the Catalog API

Before you can use the Catalog API to perform tasks, you will have to create a Designer object and then get a Catalog API instance.

**To create a Designer object**:

To create a Designer object, use the constructor Designer(String path, String name, DesignerUserInfo user) in the Design API. The constructor has three parameters: the catalog path, catalog name, and the user ID and license key provided by Logi Analytics. The path needs to be a valid path to an existing directory. The catalog name can be the name of an existing catalog when you want to open a catalog, or the name of a new catalog when you want to create a catalog. If you want to create a new catalog, the path directory should not already contain a catalog file.

To create the DesignerUserInfo instance, use the following constructor providing the user ID and the Server Designer License Key or Designer License Key you received when you purchased Logi Report.

`DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key);`

**To get a Catalog API instance**

To get a Catalog API instance, use the method *getCatalogAPI()* in the Design API. You need to first get an instance from Designer as follows:

`Designer desg = new Designer(catalogPath, catalogName, userInfo);  
CatalogAPI catalog = desg.getCatalogAPI();`

## Using jet.api.CatalogAPI for Catalogs Before v13.5

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can use the original Catalog API class jet.api.CatalogAPI to manipulate catalogs that were created in versions earlier than v13.5 in the following ways.

### Creating a Connection

You can use the following methods to insert a database connection and return the handle of the newly inserted connection. If not successful, a null value is returned:

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

### Inserting a Table/View/Synonym

You can use the following methods to insert a table, view or synonym into a catalog and return the handle of the newly inserted object:

* insert(String catalogName, String schemaPattern, String tableName, int type)
* insert(String catalogName, String schemaPattern, String tablePattern, int type, boolean setMappingName)

**Parameters**

* catalogName - The catalog name.
* schemaPattern - The schema pattern.
* tablePattern - The table name.
* type - The table type.

### Inserting a Stored Procedure

You can use the following methods to insert a stored procedure into a connection and return the handle of the newly inserted procedure.

* insert(String procName,String catalog,String schema,String name,String remarks,int iType)
* insert(String procName, String catalog, String schema, String name, String remarks, int iType)

**Parameters**

* procName - The procedure mapping name.
* catalog - The catalog name of the procedure.
* schema - The schema name of the procedure.
* name - The procedure name.
* remarks - The remarks on the procedure.
* iType - The result type of the procedure.

### Importing an SQL File

You can use the following methods to import an SQL file and return the handle of the newly inserted SQL file:

* insert(String SQLName, String filename)
* insertSql(String dataSourceName, String SQLName, String filename)

**Parameters**

* SQLName - The SQL name.
* filename - The imported file name.

### Inserting a UDS

You can use the following methods to insert a user defined data source and return the handle of the newly inserted UDS:

* insert(String strDSName, String strClassName, String strParameter, UDSColumnInfo udsColInfo)
* insert(String dataSourceName, String strDSName, String strClassName, String strParameter, UDSColumnInfo udsColInfo)

**Parameters**

* strDSName - The UDS name.
* strClassName - The name of the UDS class.
* strParameter - The parameter value.
* udsColInfo - The specified column information.

### Creating and Modifying a Query

You can perform the following tasks on a query using the Catalog API:

* [Inserting a Query into a Catalog](#QInsert)
* [Adding or Deleting Tables in a Query](#QTable)
* [Adding or Deleting Fields in a Query](#QField)
* [Adding or Deleting Joins in a Query](#QJoin)
* [Adding or Deleting QBE Conditions in a Query](#QBE)
* [Adding or Deleting Where Conditions in a Query](#QWhere)

#### Inserting a Query into a Catalog

You can use the following methods to insert a query into a catalog and return the handle of the newly inserted query:

* insert(String qryName, QueryFieldInfo queryFieldInfo,QueryJoinInfo queryJoinInfo, QueryQBEInfo queryQBEInfo, QueryAndInfo queryAndInfo)
* insert(String dataSourceName, String qryName, QueryFieldInfo queryFieldInfo, QueryJoinInfo queryJoinInfo, QueryQBEInfo queryQBEInfo, QueryAndInfo queryAndInfo)

**Parameters:**

* qryName - The query name.
* queryFieldInfo - The table and fields information.
* queryJoinInfo - The join information.
* queryQBEInfo - The QBE information.
* queryAndInfo - The where condition information.

#### Adding or Deleting Tables in a Query

* set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula) - Adds a new table to a query and returns a Boolean value: true if successful, otherwise false.
* deleteQueryTable(String dataSourceName, String qryName, String tablename) - Deletes the selected table in a query and returns a Boolean value: true if successful, otherwise false.

**Note:** The tables you want to add should exist in the specified catalog.

**Parameters**

* qryName - The query name.
* tablename - The name of the table that is to be inserted or deleted.
* SelectAllFields - Specifies whether or not to insert a table with all its fields.

#### Adding or Deleting Fields in a Query

* set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula) - Adds a new field to a query and returns a Boolean value: true if successful, otherwise false.
* deleteQueryField(String dataSourceName, String qryName, String tablename, String columnname) - Deletes the selected fields in a query and returns a Boolean value: true if successful, otherwise false.

**Parameters**

* qryName - The query name.
* tablename - The table name of the inserted or deleted field.
* isFormula - Indicates whether the inserted field is a formula.
* columnname - The column name of the deleted field.

#### Adding or Deleting Joins in a Query

* set(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo, boolean isSQL92, int outerJoin) - Adds a new join to a query and returns a Boolean value: true if successful, otherwise false.
* deleteQueryJoin(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo) - Deletes joins in a query and returns a Boolean value: true if successful, otherwise false.

**Parameters**

* qryName - The query name.
* tableFrom - The name of the table from which the join links.
* columFrom - The name of the column from which the join links.
* tableTo - The name of the table to which the join links.
* columnTo - The name of the column to which the join links.
* operator - Operator of the join to be inserted or deleted.

#### Adding or Deleting QBE Conditions in a Query

* setQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression) - Adds a new QBE condition to a query and returns a Boolean value: true if successful, otherwise false.
* deleteQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression) - Deletes the QBE condition in a query and returns a Boolean value: true if successful, otherwise false.

**Parameters**

* qryName - The query name.
* tablename - The name of the table where the QBE condition will be added or deleted.
* columnname - The name of the column where the QBE condition will be added or deleted.
* expression - The expression of the QBE condition.

#### Adding or Deleting Where Conditions in a Query

* setCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic) - Adds a new where condition to a query and returns a Boolean value: true if successful, otherwise false.
* deleteCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic) - Deletes the where conditions in a query and returns a Boolean value: true if successful, otherwise false.

**Parameters**

* qryName - The query handle.
* sLogic - The logic string of the where condition that is to be inserted or deleted.
* sExpression1 - The first expression of the where condition that is to be inserted or deleted.
* sOperator - The operator of the where condition that is to be inserted or deleted.
* sExpression2 - The second expression of the where condition that is to be inserted or deleted.

### Inserting a Business View

To insert a business view, use the following method:

* insertBusinessView(String dataSourceName, String queriableName, String businessViewName, boolean isLogicView=false)

**Parameters**

* dataSourceName - The mapping name of the data source in the catalog to which you want to insert the object.
* queriableName - The queriable object's mapping name. The queriable object in Logi Report catalog could be a query, UDS, stored procedure, or imported SQL. When queriableName is a valid name of an existing queriable object, a business view will be created.
* businessViewName - The name of the business view.
* isLogicView - Indicates whether to insert a business view. When it is false, a business view will be created.

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
* isRawExpression - Specifies whether to create a custom aggregation but not compile it. If it is false, the custom aggregation will be compiled and a javac thread will be started.

**Note:** When using *insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info)* or *setBusinessViewAggregationInfo(String aggHandle, BVAggregationInfo aggInfo)* to add or modify many custom aggregations at a time, Logi Report compiles the added custom aggregations one by one, therefore the performance could be very slow, however in this way you can easily figured out if any custom aggregation has error. If you want to enhance the performance, you can use *insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info, true//Boolean isRawExpression)* or *setBusinessViewAggregationInfo(String aggHandle, BVAggregationInfo aggInfo, true//Boolean isRawExpression)* instead and then call *compileBVFormulas(String bvHandle)* to compile all the custom aggregations once. The disadvantage of this way is that it is impossible to find out the custom aggregations that have errors.

### Inserting a Formula, Summary, Parameter or a WHERE Portion

You can use the following methods to insert a formula, summary, parameter, or a WHERE portion into a catalog and return the handle of the newly inserted object:

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

### Inserting, Getting, and Deleting Objects in a Catalog

* insert(String name, int type)/insert(String dataSourceName, String name, int type) - Inserts an object into a catalog and returns the handle of the newly inserted object.
* getTables(String dataSourceName) - Gets tables, views and synonyms in a connection and returns the mapping name array.
* getTables(boolean bIncludeSystemTable) - Gets tables, views and synonyms in a data source and returns the name array.

* getProcedureNames(String dataSourceName) - Gets all the stored procedures in a catalog and to return the mapping name array.

* getSQLs(String dataSourceName) - Gets all the SQL files in a catalog and to return the mapping name array.

* getUDSs(String dataSourceName) - Gets all the UDSs in a catalog and to return the mapping name array.

* getQueries(String dataSourceName) - Gets queries in a catalog and returns the mapping name array.
* getNewQueryName() - Gets a default name for a new query, which must be unique. The name for the first query in a catalog is query1. The following query is query2, then query3, and so on.

* getSQLString(String dataSourceName, String queryName) - Gets the sql statement text of a query or an imported SQL and returns the SQL statement string.
* getImportedSQLString(String dataSourceName, String importedSQLName) - Gets the original SQL statement of an imported SQL and returns the original SQL statement string.
* getColumns(String dataSourceName, String queryName, boolean allColumns) - Gets columns in a query and returns the table name and column real names.
* getColumnMappingnames(String dataSourceName, String queryName) - Gets column mapping names in a query and returns the table name and column mapping names.
* getColumnsCanBeGroupedBy(String dataSourceName, String queryName) - Gets the columns which can be grouped by in a query.
* getDBFields(String dataSourceName, String qryName) - Gets DBFields that can be used in a query and returns the mapping name array.
* getMappingnames(String dataSourceName, String DSName) - Gets the field mapping names in a data source and returns the table name and column mapping names.
* getFormulae(String dataSourceName) - Gets formulae that can be used in a catalog and returns the mapping name array.
* getFormulaeCanBeGroupedBy(String dataSourceName, String queryName, String groupBy) - Gets formulae that are valid to a query and returns the formula names.
* getSummaries(String dataSourceName) - Gets summaries that can be used in a catalog and returns the mapping name array.
* getSummaryCanBeSortedBy(String dataSourceName, String queryName, String groupBy) - Gets summaries that can be sorted by.
* getParameter(String dataSourceName) - Gets parameters in a catalog and returns the mapping name array.
* getParameterCanBeGroupedBy(String dataSourceName) - Gets parameters that can be grouped by.
* getJoins(String dataSourceName, String queryName) - Gets joins in a query and returns the join info array.

  **Note**: String[i][0] = Table "From" Name, String[i][1] = Column "From" Name, String[i][2] = Table "To" Name, String[i][3] = Column "To" Name
* getAndConditions(String dataSourceName, String queryName) - Gets AND conditions in a query and returns a condition info array.

  **Note**: String[i][0] = "Logic", String[i][1] = "Expression1" String[i][2] = "Operator", String[i][3] = "Expression2"
* getQBEInfo(String dataSourceName, String queryName) - Gets the QBE condition in a query and returns a QBE info array.

  **Note**: String[i][0] = column Name, String[i][j](j>=1) = condition expression of this column.
* getNewReportName() - Gets a default name for a new report, which must be unique. The name for the first report in a catalog is report1, after which the following reports will be named report2, report3, and so on.

* delete(Stringhandle) - Deletes an object from its parent node and to returns true if the specified object is removed.

**Parameters**

* name - The object name.
* type - The object type.
* dataSourceName - The mapping name of the data source in the catalog.
* queryName - The mapping name of the query.
* qryName - The query name.
* importedSQLName - The mapping name of the imported SQL.
* allColumns - Selects all columns in the specified tables.

* DSName - The data source object name, such as Query, SQL, UDS, and Procedure.
* groupBy - The groupBy field.

* handle - The handle of the object that is to be deleted.

### Refreshing the Reference Table of a Catalog

You can use the method *public boolean refreshReference()* to refresh the [reference table](https://devnet.logianalytics.com/hc/en-us/articles/1500009605342-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) of a catalog.

### Saving a Catalog

* save() - Saves an open catalog and returns a Boolean value: false if it fails, otherwise true.
* saveAs(String path, String name) - Saves an open catalog as a new catalog file. You can save the catalog as a binary catalog using the extension .cat, or an XML format catalog using the extension .cat.xml.

## Catalog API Samples

The sample programs TestCatalogAPI.java and TestCatalogBV.java in `<install_root>\help\samples\APICatalog` demonstrate how to use the Catalog API to create a catalog and to create business views in a catalog.

To compile and run the samples, you should add the required classes to the class path (make sure that the path of the file JREngine.jar is before that of the file report.jar).

For example, you can use the following command to compile and run the sample program TestCatalogAPI.java. After running the program, a new catalog file MyReports.cat will be created in `C:\LogiReport\Designer\Demo\MyReports`. Be sure to create this empty directory first.

`C:\LogiReport\Designer\help\samples\APICatalog>javac -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\log4j-core-2.12.1.jar;C:\LogiReport\Designer\lib\log4j-api-2.12.1.jar;C:\test\classes" TestCatalogAPI.java`

`C:\LogiReport\Designer\help\samples\APICatalog>java -classpath "C:\LogiReport\Designer\lib\jrengine.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\log4j-core-2.12.1.jar;C:\LogiReport\Designer\lib\log4j-api-2.12.1.jar;C:\LogiReport\Designer\help;C:\test\classes" -Dreporthome=C:\LogiReport\Designer TestCatalogAPI -path=C:\LogiReport\Designer\Demo\MyReports -catalog=MyReports.cat -log=C:\LogiReport\Designer\logs\designer.log`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605162-Using-Server-API-to-Work-with-Logi-Report-Server) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605122-Using-Design-API-to-Design-Reports)
