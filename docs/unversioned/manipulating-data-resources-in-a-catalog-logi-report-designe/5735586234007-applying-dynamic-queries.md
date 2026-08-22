---
title: "Applying Dynamic Queries"
id: 5735586234007
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735586234007-Applying-Dynamic-Queries
updated_at: 2022-11-02T08:17:44Z
---

# Applying Dynamic Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586255767-Using-Query-Modifiers)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735547021975-Working-with-Business-Views)

# Applying Dynamic Queries

You can build queries [using the Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog) or [from SQL statements](https://devnet.logianalytics.com/hc/en-us/articles/5735507746711-Using-Imported-SQLs). Either way, you should predefine the queries. However, sometimes you may want to specify the query at runtime. For example, in the catalog, you build the query as `"select customers_id from customers"`, but at runtime, you may want to fetch data from another table - customers1. You should then update the query according to the table index, such as `"select customers_id from customers1"`. To help you achieve this, Logi Report provides the Dynamic Query feature, which enables you to generate queries dynamically so as to fetch data from different tables at runtime. This topic introduces the dynamic query interface and how you apply dynamic queries in Designer. It also presents an example using the demo program included in Designer to explain the usage of dynamic queries.

This topic contains the following sections:

* [Dynamic Query Interface](#Interface)
* [Using Dynamic Queries](#Use)
* [Dynamic Query Sample](#Sample)

## Dynamic Query Interface

The dynamic query interface, SQLStmtCreator, is available in the JREngine.jar archive file in `<install_root>\lib`, and is contained in the toolkit.db.api package. You can apply it to any existing query in a catalog.

The following flowchart illustrates how the interface works when creating a dynamic query. The QueryInfo object is passed from Logi Report Engine to the interface as an input. Then, the completed SQL statement is returned from the interface. Finally, the completed SQL statement is sent to the database to get the result set for the report.

![Interface Flowchart for Dynamic Query](https://devnet.logianalytics.com/hc/article_attachments/9898458148119/qury_dynmc_intfc.gif)

This interface is very simple with only one method: *getSQLStmt(QueryInfo queryInfo)*. It receives information of a query and returns an SQL string. QueryInfo is a container that contains all information to build an SQL string. You can call the *getXXX()* methods to get all information step by step. For more information, refer to the toolkit.db.api.SQLStmtCreator interface in the Logi Report Java API Documentation.

The structure of QueryInfo is:

* **ConnectionInfo**  
  Driver, URL, User, Password, DateFormat, TimeFormat, TimestampFormat, TransactionIsolation level, ReadOnly, QualifiedNamePattern, ExtraNamePattern, EncodingPattern
* **Column array**  
  All the selected columns. Elements in this array are ColumnInfo object. ColumnInfo contains Mapping Name, Real Name, Table Info, and Expression (if this is a computed column).
* **Tables(array)**  
  Selected tables. Elements in this array are TableInfo objects. TableInfo contains Mapping Name, Real Name, Correlation Name, Schema, and Catalog.
* **Joins(array)**   
  Elements in this arrays are JoinInfo objects. JoinInfo includes Column from, Column to, Operator, and Join type.
* **QBEs(array)**   
  Part of the where condition. It is retrieved from the Query Editor. Elements in this array are QBEInfo objects. QBEInfo contains ColumnInfo with QBE condition bound to this column.
* **Ands(array)**   
  Part of the where condition. It is retrieved from the advanced search condition in the Query Editor. Elements in the array are AndInfo objects. AndInfo contains Left expression, Operator, Right expression, and Logic.
* **SubLinks(array)**  
  If the dynamic query is for a subreport, the SubLinks is used for the additional WHERE clause to filter data, and this is the way to link the dynamic query to the primary report. Elements in this array are composed of SubLinksInfo objects. SubLinkInfo contains Column, Operator, and Value.
* **Parameters (array)**  
  Parameters used for creating a query. You should encode parameters that the database can recognize. The elements in this array are ParameterInfo objects. ParameterInfo contains Name, Type, and Value.
* **OrderBys(array)**  
  Elements in the array are OrderByInfo objects. OrderByInfo contains Column and sort direction.
* **Other Information**   
  Query name, IsDistinct, and WherePortionString. The value of WherePortionString is set via *JRengine.setWherePortionString()*.

## Using Dynamic Queries

The following shows the basic procedure for using dynamic queries.

1. Compile the Java file you write and append the path of the compiled file with a valid path to the ADDCLASSPATH variable of **setenv.bat**/**setenv.sh** in `<install_root>\bin`.
2. Set the value of the JDBC connection property **SQL Statement Creator** to specify the dynamic query interface.

   In Designer, open the Catalog Manager, expand the data source node, select the JDBC connection, right-click it and select **Properties** from the shortcut menu. In the Properties sheet, specify the SQL Statement Creator property of the connection to set the real class name of the dynamic query object. For example:

   * You implement the interface by the class UserSQLStmtCreatorImpl, then specify the property value as **UserSQLStmtCreatorImpl;@param1;@param2**. "param1" and "param2" are type-in [parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) you used to specify criteria while creating the query.
   * School year which changes at runtime, requires to be inserted into the report template so that the input value for the runtime parameters can be passed to the dynamic query interface via the QueryInfo object, in order for a corresponding SQL statement to be returned.
3. Set the value of the query property **Enable SQL Statement Creator**.

   When you select a query in the Catalog Manager, you can find the property Enable SQL Statement Creator in the Properties sheet, which indicates whether the query uses the dynamic query interface to get the result set. If you set the property to "true", Logi Report Engine generates the query using the dynamic query interface at runtime.

## Dynamic Query Sample

Designer provides a demo program, SQLStmtCreatorImpl.java, in `<install_root>\help\samples\APIDynamicQuery`, which implements the dynamic query interface and changes the table name of the query that is sent to the database.

The following explains how you can compile the required files in the demo program and apply dynamic queries for a report.

1. Compile **SQLStmtCreatorImpl.java** (to compile the file, you need another file **MappingNameFinder.java** in the same folder).

   Assume that you have installed Designer in `C:\LogiReport\Designer`, and the class files of MappingNameFinder.java are in `C:\LogiReport\Designer\help\samples\APIDynamicQuery`. You can use the following command to compile SQLStmtCreatorImpl.java:

   `javac -classpath C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\help\samples\APIDynamicQuery SQLStmtCreatorImpl.java`
2. Modify **setenv.bat** in `<install_root>\bin` by appending the path of SQLStmtCreatorImpl.java into the batch file's ADDCLASSPATH variable.

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\LogiReport\Designer\help\samples\APIDynamicQuery;`
3. Start Designer.
4. Navigate to **File** > **Open**.
5. In the Open Report dialog box, select **Browse** to open the catalog file **SampleComponents.cat** in `<install_root>\Demo\Reports\SampleComponents`, then open the sample report **BandedObjectReport.cls**.
6. Open the Catalog Manager, expand the **Data Source 1** node, right-click the **Parameters** node, select **New Parameter** on the shortcut menu to [create a String type-in parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog)**pTableIndex** (leave the other settings to their default).

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/9898458159127/qury_dynmc_prm.gif)
7. Select the node of the JDBC connection in Data Source 1.
8. Select **Show Properties** on the Catalog Manager toolbar to display the Properties sheet, then set the **SQL Statement Creator** property to **SQLStmtCreatorImpl;@pTableIndex**. The parameter pTableIndex is used to specify which table is to be selected at runtime.

   ![SQL Statement Creator Property](https://devnet.logianalytics.com/hc/article_attachments/9898475238807/qury_dynmc_prpty.gif)
9. Select the query **QueryForBandedObject** in the Catalog Manager, and set its **Enable SQL Statement Creator** property to **true**.
10. Save the catalog.
11. Select the **View** tab to preview the report.
12. In the Enter Parameter Values dialog box, type **1** as the value of pTableIndex, the report then runs on the Customers1 table. When you specify nothing as the value of pTableIndex, the report runs on the Customers table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586255767-Using-Query-Modifiers)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735547021975-Working-with-Business-Views)
