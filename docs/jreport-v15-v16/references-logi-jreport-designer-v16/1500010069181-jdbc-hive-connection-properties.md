---
title: "JDBC/Hive Connection Properties"
id: 1500010069181
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069181-JDBC-Hive-Connection-Properties
updated_at: 2021-07-24T10:38:06Z
---

# JDBC/Hive Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033742-Imported-SQL-Column-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033642-JSON-Elasticsearch-Connection-Properties)

# JDBC/Hive Connection Properties

This topic lists the properties of a JDBC/Hive Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| Custom Query Optimizer | Specifies the implementation class of the [QueryOptimizer](#QueryOptimizer) interface for optimizing the query SQL statement before being sent to the DB. The value can be "Package\_Name.Class\_Name". If the class file has no package name, set the value to "Class\_Name". Once Custom Query Optimizer is specified,   * Report data cache and in-memory cubes cannot be created or scheduled any more. * [The group level pushing down](#PushDown) will not be supported.   Data type: String |
| [Date Format](#Format) | Specifies the default Date format corresponding to the database. Data type: String |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first added connection in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the JDBC connection. Data type: String |
| Driver | Specifies the class name of the JDBC driver such as oracle.jdbc.driver.OracleDriver. While setting up the JDBC connection with the connection dialog, Logi JReport will use the driver that is specified to connect to the database. If no driver name is filled in, Logi JReport will use the default JDBC driver from the file jdbcdrivers.properties in `<install_root>\bin` file. You can add JDBC driver names into the text file, Logi JReport will load the drivers before building a connection. If your JDBC driver name is not correct, or you do not add JDBC driver names, the message "No suitable driver" will appear. Data type: String |
| Explicit Inner Join | Specifies whether to use Explicit Join notation or Implicit Join notation in the Where clause for inner joins. For Hive connection, it can only be true.  * **true** - Uses Explicit Join notation: SQL: select … from A inner join B on (A.c1 = B.c2) * **false** - Uses Implicit Join notation: SQL: select … from A,B where A.c1 = B.c2   Data type: Boolean |
| Included Schemas | Displays the schema names specified for the connection in the Get JDBC Connection Information dialog. The default is blank, which indicates that all schemas in the DBMS can be used in the catalog. This property is read only. To modify it, use the Get JDBC Connection Information dialog. |
| Name | Specifies the name of the connection which, by default, is the same as the connection URL, but can also be a user friendly name for the connection. If the name has already been used, a number starting from 1 will be appended to the name. For example, if aa exists, the new name will be aa1, and if both aa and aa1 exits, it will be aa2, and so on. If you change the name, the imported SQL and stored procedures that reference the connection will be automatically updated to use the new name.  Data type: String |
| Name Pattern | Specifies whether or not catalog or schema is used in data manipulation. Choose an option from the drop-down list.  * **unqualified name** - Neither catalog nor schema is included in data manipulation. Example: SELECT t.c FROM t * **2-part names**  - Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * **3-part names**  - Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t   Data type: Enumeration |
| Outer Join Marker | Specifies the behavior of the outer joins in the connection. Choose an option from the drop-down list.  * **SQL92** - Specifies to use the SQL92 standard. * **+** - Specifies to use Oracle's "+=+" standard.   Data type: Enumeration |
| Password | Specifies the password for connecting with the database, which is determined by the database DBA. Data type: String |
| [Push Down Group Query](#PushDown) | Specifies whether to push down group level summary computations in reports to the DBMS at runtime. Choose an option from the drop-down list. For Hive connection, it can only be true.  * **true** - Logi JReport will push down the group level summary computations to the DBMS if the DBMS can do the computations, otherwise, Logi JReport will do the computations itself. * **false** - Logi JReport will do the group level summary computations itself.   Data type: Boolean |
| Quote Qualifier | Specifies the characters, then a qualifier name which contains the characters that will not be quoted. Choose an option from the drop-down list.  * **Default (JDBC)** - If selected, the program will get the extra name characters from JDBC. * **User Defined** - If selected, you can modify the quote character according to the database system being used.   Data type: Enumeration |
| Read Only | Specifies the mode to open the connection to the JDBC data source. The initial setting is default which uses the mode specified by the DBMS Administrator which could be read only or read & write. Choose an option from the drop-down list.  * **default** - May be read & write or read only depending on the DBMS default setting. * **read only** - Allows the driver to optimize performance for reporting which does not need to write to the DBMS. * **read & write** - Opens the DBMS with updates enabled which requires more processing to ensure concurrency control.   Data type: Enumeration |
| Security Check | Specifies whether or not to check the JDBC connection security at runtime. Data type: Boolean |
| SQL Statement Creator | Specifies the parameters to implement the SQLStmtCreator interface (for details about the interface and its usage, refer to [Dynamic Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010034702-Dynamic-Queries)). Data type: String |
| Time Format | Specifies the default Time format corresponding to the database. Data type: String |
| [Timestamp Format](#Format) | Specifies the default Timestamp format corresponding to the database. Data type: String |
| Transaction Mode | Specifies the transaction mode for the connection. Choose an option from the drop-down list.  * **default** - Indicates the transaction information cannot be got from JDBC connection. * **none** - Indicates that transactions are not supported. * **read uncommitted** - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * **read committed** - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * **repeatable read** - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * **serializable** - Dirty reads, non-repeatable reads and phantom reads are prevented.   Data type: Enumeration |
| URL | Specifies the JDBC URL which establishes the connection to the database, for example jdbc:oracle:thin:@localhost:1521:ORCL. Data type: String |
| User | Specifies the user name for connecting to the database, which is determined by the database DBA. Data type: String |

## Timestamp Format and Date Format

| Symbol | Meaning | Presentation |
| --- | --- | --- |
| y | year | Number |
| M | month | Number |
| d | day in month | Number |
| H | hour in day (0~23) | Number |
| h | hour in am/pm (1~12) | Number |
| m | minute in hour | Number |
| s | second in minute | Number |
| S | millisecond | Number |

Example (using the US Locale):

"yyyyy.MMMMM.dd hh:mm aaa" ->> 1996.July.10 12:08 PM

**Note**: The Date and Timestamp format Logi JReport supports follows that of Java. Refer to the Java API Specification java.text package DateFormat interface.

## Push Down Group Query

This property is to specify whether to push down group level summary computations in reports to the DBMS at runtime. The group level summary computations can be pushed down to the DBMS when the aggregate function is Count, Sum, Maximum, Minimum**,** or Square Sum. The aggregate functions Average, PopulationStdDev, PopulationVariance, StdDev and Variance are not pushed down, but instead computed by Logi JReport using the results of the pushed down functions. By pushing down the group level summary computations, the DBMS' computation capability can be made use of, and thus the reports' running efficiency will be improved.

The property can be specified at three levels for page report: JDBC connection, query within the connection, and individual page report. The setting on page report has the highest priority. While, for web reports and library components, the property can be specified only on the JDBC connection or the query within the connection, and the setting on the query has higher priority. Since there is no affect on data returned when detail data is needed, it is recommended to set it on every JDBC connection.

After you activate Push Down Group Query, Logi JReport will generate aggregate functions and GROUP BY statements for any data components that only view aggregated results. This includes all charts, crosstabs, summary tables and banded objects which hide the detail panel. When Logi JReport retrieves the data for one of these types of data components, it dynamically modifies the SQL to only return the aggregated data. Thus you can use the same generic query to run many different data components without modifying the query. For example, a chart based on table Orders that shows sales by state will generate a query that just returns one row per state while a summary table by product name will return just one record for each product. This can result in orders of magnitude better performance.

## The QueryOptimizer interface

The QueryOptimizer interface is contained in the package toolkit.db.queryoptimization. See Logi JReport Javadoc in `<install_root>\help\api` for usage of the interface.

This interface contains only one method: *Optimizer optimizeQuery(QueryInfo queryInfo);*

One QueryInfo will be automatically passed into the interface, and one Optimizer object should be returned.

**To implement the interface and make it work:**

1. Define a Java class file that implements the QueryOptimizer interface.
2. Compile the Java file to generate the class file.
3. Append the class path to the ADDCLASSPATH variable of the file setenv.bat in `<install_root>\bin`.
4. Start Logi JReport Designer with the modified batch file.
5. Open the catalog that contains the connection you would like to optimize.
6. Set the Custom Query Optimizer property of the connection to "Package\_Name.Class\_Name".

**Note:** The List<ColumnInfo> parameter in the implementation class of the QueryOptimizer interface depends on the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500010069061-Business-View-Properties#Prefetch) property of the related business view. When Prefetch is true, List<ColumnInfo> will include all columns in the business view, otherwise, it will only include columns used by the related report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033742-Imported-SQL-Column-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033642-JSON-Elasticsearch-Connection-Properties)
