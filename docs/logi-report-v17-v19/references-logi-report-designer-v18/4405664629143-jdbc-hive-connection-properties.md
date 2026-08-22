---
title: "JDBC/Hive Connection Properties"
id: 4405664629143
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664629143-JDBC-Hive-Connection-Properties
updated_at: 2022-01-27T20:35:12Z
---

# JDBC/Hive Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661824663-Imported-SQL-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664630295-JSON-Elasticsearch-Connection-Properties)

# JDBC/Hive Connection Properties

This topic describes the properties of a [JDBC](https://devnet.logianalytics.com/hc/en-us/articles/4405664412311-Connecting-via-JDBC-Connections)/[Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405661421335-Connecting-via-Hive-Connections) Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| Custom Query Optimizer | Specifies the implementation class of the [QueryOptimizer](#QueryOptimizer) interface for optimizing the query SQL statement before being sent to the DB. The value can be "Package\_Name.Class\_Name". If the class file has no package name, set the value as "Class\_Name". Note icon Once you specify the property, the Server administrators are not able to create or schedule report data cache and in-memory cubes, and Logi Report Engine can no longer [push down group level summary computations](#PushDown) for the catalog containing the connection.  Data type: String |
| [Date Format](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#DateFormat) | Specifies the default format for Date type data. Data type: String |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first connection you create in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Driver | Specifies the class name of the JDBC driver such as oracle.jdbc.driver.OracleDriver for the connection. For more information, see [Setting Up the JDBC Driver](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog#Driver). Data type: String |
| Explicit Inner Join | Specifies whether to use Explicit Join notation or Implicit Join notation in the Where clause for inner joins of the connection.  * **true** - Select to use Explicit Join notation. SQL: select … from A inner join B on (A.c1 = B.c2) * **false** - Select to use Implicit Join notation. SQL: select … from A,B where A.c1 = B.c2   For Hive connections, the property value can only be "true".  Data type: Boolean |
| Included Schemas | Shows the schemas that you have selected for the connection in the [Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#Schema). This property is read only. |
| Name | Specifies the name of the connection. By default, the name is the same as the connection URL. If the name you provide has already been used, Designer appends a number starting from 1 to the name. For example, if "aa" exists, the new name is "aa1", and if both "aa" and "aa1" exit, it is "aa2", and so on. If you change the name, Designer automatically updates the imported SQLs and stored procedures that reference the connection to use the new name.  Data type: String |
| [Name Pattern](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#NamePattern) | Specifies whether to use catalog or schema in data manipulation. Choose an option from the drop-down list. Data type: Enumeration |
| Outer Join Marker | Specifies the behavior of the outer joins in the connection. Choose an option from the drop-down list.  * **SQL92** - Select to use the SQL92 standard. * **+** - Select to use Oracle's "+=+" standard.   Data type: Enumeration |
| Password | Specifies the password for connecting to the JDBC database. Data type: String |
| [Push Down Group Query](#PushDown) | Specifies whether to push down group level summary computations to the DBMS at runtime.  * **true** - Select to push down the group level summary computations to the DBMS if the DBMS can perform the computations; otherwise, Logi Report Engine do the computations itself. * **false** - Select to have Logi Report Engine perform the group level summary computations itself.   For Hive connections, the property value can only be "true".  Data type: Boolean |
| Quote Names | Specifies how you want Designer to quote the names of the resources obtained from the database. Choose an option from the drop-down list. When the names of the resources in the database to which the connection is connected contain uppercase or lowercase characters, such as the names of catalogs, schemas, tables, and columns, if you want to keep the uppercase and lowercase characters in the names exactly as what they are in the database when you use the resources in Designer, for example when you create queries based on the resources, you need to quote the names. You can use this property to specify in which way to let Designer quote the names automatically.   * **default** - If you select the option, Designer does not check whether the resource names contain uppercase or lowercase characters and therefore does not quote any names. * **when containing lowercase characters** - Select to let Designer quote the resource names that contain lowercase characters. * **when containing uppercase characters** - Select to let Designer quote the resource names that contain uppercase characters. |
| Quote Qualifier | Specifies the characters, then a qualifier name which contains the characters you do not want to quote. Choose an option from the drop-down list.  * **Default (JDBC)** - Select to get the extra name characters from JDBC. * **User Defined** - Select to modify the quote character according to the database system.   Data type: Enumeration |
| [Read Only](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#ReadOnly) | Specifies the mode to open the connection to the JDBC database. Choose an option from the drop-down list. Data type: Enumeration |
| Security Check | Specifies whether to check the connection security at runtime. Data type: Boolean |
| SQL Statement Creator | Specifies the parameters to implement the SQLStmtCreator interface. For more information about the interface and its usage, see [Dynamic Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405661919383-Applying-Dynamic-Queries). Data type: String |
| [Time Format](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#DateFormat) | Specifies the default format for Time type data. Data type: String |
| [Timestamp Format](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#DateFormat) | Specifies the default format for Timestamp type data. Data type: String |
| [Transaction Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#Transaction) | Specifies the transaction mode for the connection. Choose an option from the drop-down list. Data type: Enumeration |
| URL | Specifies the JDBC URL which establishes the connection to the database, for example `jdbc:oracle:thin:@localhost:1521:ORCL`. Data type: String |
| User | Specifies the user name for connecting to the JDBC database. Data type: String |

## Push Down Group Query

You can use this property to specify whether to push down group level summary computations in reports to the DBMS at runtime. The group level summary computations can be pushed down to the DBMS when the aggregate function is Count, Sum, Maximum, Minimum, or Square Sum. The aggregate functions Average, PopulationStdDev, PopulationVariance, StdDev, and Variance are not pushed down, but instead computed by Logi Report Engine using the results of the pushed down functions. By pushing down the group level summary computations, you can use the DBMS' computation capability, and thus improve the report running efficiency.

You can specify the property at three levels for page reports: JDBC connection, query within the connection, and individual page report. The setting on page report has the highest priority. While, for web reports and library components, you can only specify the property on the JDBC connection or the query within the connection, and the setting on the query has higher priority. Since there is no affect on the returned data when detail data is needed, you may want to set the property on every JDBC connection.

After you activate the Push Down Group Query feature, Logi Report Engine generates aggregate functions and GROUP BY statements for any data components that only view aggregated results. This includes all charts, crosstabs, summary tables, and banded objects which hide the detail panel. When Logi Report Engine retrieves the data for one of these types of data components, it dynamically modifies the SQL to only return the aggregated data. Thus, you can use the same generic query to run many different data components without modifying the query. For example, a chart using the table Orders which shows sales by state generates a query that just returns one row per state while a summary table by product name returns just one record for each product. This can result in orders of magnitude better performance.

## The QueryOptimizer Interface

The QueryOptimizer interface is in the package toolkit.db.queryoptimization. You can refer to the Logi Report Javadoc for usage of the interface.

This interface contains only one method: *Optimizer optimizeQuery(QueryInfo queryInfo);*

One QueryInfo is automatically passed into the interface, and one Optimizer object should be returned.

**To implement the interface and make it work**

1. Define a Java class file that implements the QueryOptimizer interface.
2. Compile the Java file to generate the class file.
3. Append the class path to the ADDCLASSPATH variable of the file **setenv.bat** in `<install_root>\bin`.
4. Start Designer.
5. Open the catalog that contains the connection you would like to optimize.
6. Set the **Custom Query Optimizer** property of the connection to **Package\_Name.Class\_Name**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) The List<ColumnInfo> parameter in the implementation class of the QueryOptimizer interface depends on the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/4405664618903-Business-View-Properties#Prefetch) property of the related business view. If you set Prefetch of the business view to "true", List<ColumnInfo> includes all columns in the business view; otherwise, it only includes columns used by the related report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661824663-Imported-SQL-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664630295-JSON-Elasticsearch-Connection-Properties)
