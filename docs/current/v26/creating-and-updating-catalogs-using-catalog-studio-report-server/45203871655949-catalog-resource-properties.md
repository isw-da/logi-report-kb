---
title: "Catalog Resource Properties"
id: 45203871655949
section: "Creating and Updating Catalogs Using Catalog Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203871655949-Catalog-Resource-Properties
updated_at: 2026-04-30T14:07:53Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Catalog Resource Properties

Server lists the properties of resources in a catalog in the Properties panel when you create or update the catalog resources in Catalog Studio. You can edit the properties there to customize the catalog resources. This topic introduces   the properties of the resources that a catalog may contain, in alphabetical order, including their child objects if any.

This topic contains the following sections:

- Business View Resource Properties

- JDBC Connection Properties

- JSON Schema Properties

- 
Parameter Properties- User-Defined Format for Parameters

- Query/Stored Procedure/Imported SQL Properties

- Table Column Properties

- Table/View/Synonym Properties

- The properties described here might not be a full list. For properties that you don't find here, see  Setting Report Object Properties Using the Inspector Panel.

- You should use the default values of the properties except for the two properties - Name and Description. Make changes only after you are sure of the meaning of each property.

- Make sure that the precision you specify in the catalog is same as that in the database. This is to avoid inconsistency between the database data values and reports.

## 
Business View Resource Properties

This section describes the properties of a business view or a/an category/group object/detail object/aggregation object/hierarchy in a business view.

| Property Name | Description |
| --- | --- |
| Aggregate Function | Specify the aggregation function of the aggregation object. Data type: String |
| Auto Add Prefix in Display Names | Similar to the data source property "Use Mapping Name Prefix" which controls whether to add "tablename_" as the prefix of the table names in the default mapping names of their columns, this property determines whether to automatically append the same prefix in the default display names of the view elements in the business view when you add view elements based on the columns. The two properties work independently from each another, meaning, you can set Use Mapping Name Prefix to "true" to automatically prefix column names with corresponding table names in a data source, but choose not to have the prefix for view elements by setting Auto Add Prefix in Display Names to "false". By default, the property is "false". In this case, when a column's mapping name contains the "tablename_" prefix which however is not automatically generated but user customized and you add a view element based on the column, Server still removes the prefix from the display name of the view element. Data type: Boolean |
| Description | Specify the description of the object. Data type: String |
| Display Name | Specify the display name of the object. Data type: String |
| Enable Filter | Specify whether you can filter on the object. Data type: Boolean |
| Mapping Name | Specify the name of the column to which the object is mapped. Data type: String |
| Prefetch | When this property is "true", Report Engine fetches all the columns from the raw database which the business view references into cache and reuses them afterwards when users run web reports and dashboards that apply the business view at runtime. This reduces the querying and connecting times to the database and can help improve the runtime performance. However, "Prefetch=true" does not work when users schedule to run web reports, therefore they may get different results when running the same web report in different ways. When this property is "false", Report Engine queries data on demand at runtime. When several business view elements are based on the same columns, they reuse the columns. This property also affects the following: When it is "true", the List parameter in the implementation class of the QueryOptimizer interface includes all columns in the business view; otherwise, it only includes columns that the report or dashboard uses. When it is "true", Server displays all the parameters that the business view applies in the UI for specifying the parameter values at runtime; otherwise, it only displays the parameters the data objects in the report or dashboard reference. Data type: Boolean |
| Tip | Specify the tool tip that displays when users hover over the object in the business view resource tree at runtime. Data type: String |
| Type | Select the type of the object: Group, Detail, or Aggregation. Data type: Enumeration |

## 
JDBC Connection Properties

This section describes the properties for setting up a JDBC connection.

| Property Name | Description |  |  |
| --- | --- | --- | --- |
| Qualifier |  |  |  |
| Name Pattern | Specify whether to use catalog or schema in data manipulation in this box. Unqualified Name Select to include neither catalog nor schema in data manipulation. If you add a table or view from a different schema, you can create queries on it and use the queries to build reports, but when you run the reports, the table or view applies the default schema and you get an error that the table or view does not exist. Example: SELECT t.c FROM t 2-Part Names Select to use schema in data manipulation. If you want to use tables and views from more than one schema, you must use 2 part or 3 part names.Example: SELECT schema.t.c FROM schema.t 3-Part Names Select to use both catalog and schema in data manipulation.Example: SELECT catalog.schema.t.c from catalog.schema.t This is very useful when you want to build reports that get data from more than one catalog and/or schema. If you only use one unqualified name, the SQL statement that Server generates does not contain the catalog and schema name, and therefore Server may not be able to find the table or view in the default schema and/or catalog. Data type: Enumeration |  |  |
| Quote Qualifier | You can specify the characters, and then the qualifier name which contains the characters that you do not want to quote in this box. In Server, you need to quote the characters defined by the database. The default character is double quotation marks (" "). Default (JDBC) Select to get the extra name characters from JDBC. User Defined Select to modify the quote character according to the database system. Extra Characters Specify the extra characters for identifier names. Quote Character Specify the quote character. Data type: Enumeration |  |  |
| Qualifier | This drop-down list contains all the available qualifiers. You can change the current qualifier by selecting one from the drop-down list. The default value is the first one in the list. If the database does not support qualifier, Server does not display the drop-down list, and you cannot type the qualifier name. |  |  |
| Apply To | Specify to which data resources you want to apply the modified qualifier. Tables Select to apply the modified qualifier to all tables in the connection. Views Select to apply the modified qualifier to all views in the connection. Imported SQLs Select to apply the modified qualifier to all imported SQLs in the connection. Stored Procedures Select to apply the modified qualifier to all stored procedures in the connection. |  |  |
| Date Format |  |  |  |
| Boolean Format | Select the default format for Boolean type data in the connection. Data type: Enumeration |  |  |
| Date Format | Specify the default format for Date type data in the connection. Different database systems use different Date and Time formats for Date and Time values. You can specify the format here, so that when Server sends the SQL statement with Date or Time parameters, they can be correctly translated into the format of your database system. For example, in an Oracle database, the default Date format is "dd-MMM-yy"; while in a MySQL database system, it is "yyyy-MM-dd". Thus, you need to modify the Date format for the connection accordingly, so that the Server generated SQL statements can function correctly with the database. Symbol | Meaning | Presentation |
| y | year | Number |  |
| M | month | Number |  |
| d | day in month | Number |  |
| H | hour in day (0~23) | Number |  |
| h | hour in am/pm (1~12) | Number |  |
| m | minute in hour | Number |  |
| s | second in minute | Number |  |
| S | millisecond | Number |  |

 The Date and Time formats Report supports follows that of Java. For more information, refer to the java.text package DateFormat interface in the Java API Specification.

Data type: String

Time Format
Specify the default format for Time type data in the connection.
					Data type: String

Timestamp Format
Specify the default format for Timestamp type data in the connection.
                        Data type: String

Transaction

Read Only
Select the mode to open the connection to the JDBC database.
                        
- 
Default
Select to apply the default setting of the database, which can be "Read & Write" or "Read Only".

- 
Read Only
Select to allow users  to access the database in read-only mode. This allows the driver to optimize performance for reporting which does not need to write to the database.

- 
Read & Write
Select to allow users to access the database in read-write mode. This opens the database with updates enabled which requires more processing to ensure concurrency control. 

Data type: Enumeration

Transaction Mode
Select the transaction mode for the connection.
                        
- 
Default
Select to apply the setting from the database.

- 
None
Select to not use transactions in the connection.

- 
Read Uncommitted
Select to allow dirty reads, non-repeatable reads, and phantom reads to occur in the connection. This mode can speed up the transaction of the connection. If you select this mode, transactions are not isolated from each other. If the database supports other transaction isolation levels, it ignores whatever mechanism it uses to implement those levels, so that they do not adversely affect other transactions. Transactions running at the Read Uncommitted level are usually read-only.

 When you set the Read Only option and select the Transaction Isolation option of "Read Uncommitted", it provides faster access to the data. However, if a database transaction is rolled back, the read retrieves an invalid row and results in an inaccurate report.

- 
Read Committed
Select to prevent dirty reads, and allow non-repeatable reads and phantom reads to occur in the connection. If you select this mode, when one transaction is reading, updating, or deleting a row, other transactions cannot update or delete it until this transaction has been committed or rolled back.

- 
Repeatable Read
Select to prevent dirty reads and non-repeatable reads, and allow phantom reads to occur in the connection.If you select this mode, when one transaction is updating, deleting several rows, or inserting new rows into them, other transactions cannot also update or delete these rows, until this transaction has been committed or rolled back.

- 
Serializable
Select to prevent dirty reads, non-repeatable reads, and phantom reads in the connection.If you select this mode, when one transaction is updating, deleting several rows, or inserting new rows into them, other transactions cannot update, delete these rows, or insert any new rows into these rows, until this transaction has been committed or rolled back.

Data type: Enumeration

Schema

Schema List box
This box lists the schemas for you to choose.

Included Schemas box
This box shows the schemas that you have selected.

 Add button
Select to add the specified schemas to the Included Schemas box.

 Remove button
Select to remove the specified schemas from the Included Schemas box.

Schema List
This drop-down list contains all the available schemas. You can change the current schema by selecting one from the drop-down list.

Apply To
Specify to which data resources you want to apply the modified schema.                        
- 
Tables
Select to apply the specified schema to all tables in the connection.

- 
Views
Select to apply the specified schema to all views in the connection.

- 
Stored Procedures
Select to apply the specified schema to all stored procedures in the connection.

Other

Description

Specify the description of the connection. 

Data type: String 

SQL Statement Creator
Specify the parameters to implement the SQLStmtCreator interface. For more information about the interface and its usage, see Applying Dynamic Queries in the Report Designer Guide.
					Data type: String

Security Check
Specify whether to check the connection security at runtime.
					Data type: Boolean

Push Down Group Query
Specify whether to push down group level summary computations to the database at runtime. 
- Select to push down the group level summary computations to the database if it can perform the computations; otherwise, Report Engine do the computations itself.

- Clear to have Report Engine perform the group level summary computations itself. 

Data type: Boolean 

 For Hive connections, this property can only be "true".

Outer Join Marker 
Specify the behavior of the outer joins in the connection. Choose an option from the drop-down list.
					
- 
SQL92
Select to use the SQL92 standard.

- 
+
Select to use Oracle's "+=+" standard. 

Data type: Enumeration

Explicit Inner Join
Specify whether to use Explicit Join notation in the Where clause for inner joins of the connection. "false" means using Implicit Join notation. SQL of Explicit Join notation: select … from A inner join B on (A.c1 = B.c2)

SQL of Implicit Join notation: select … from A,B where A.c1 = B.c2

Data type: Boolean

 For Hive connections, this property can only be "true".
					

Custom Query Optimizer
Specify the implementation class of the QueryOptimizer interface for optimizing the query SQL statement before being sent to the DB. The value can be "Package_Name.Class_Name". If the class file has no package name, set the value as "Class_Name".
					 Once you specify the property, the Server administrators are not able to create or schedule report data cache and in-memory cubes, and Report Engine can no longer push down group level summary computations for the catalog containing the connection.

Data type: String

Characters to Be Replaced

When you use parameters to build queries, there may be special characters in the parameter values like a back slash (\), and you would like Server to interpret them literally, rather than as a special character. In this case, you can replace the special characters with another string according to your database, for example, for an MySQL database, use "\\" to represent "\".

Specify the characters that you want to replace in parameter values when Server passes the parameter values to queries.

Data type: String

Replaced By
Specify the characters you use to replace the specified special characters.Data type: String

### 
Push Down Group Query

You can use this property to specify whether to push down group level summary computations in reports to the database at runtime. The group level summary computations can be pushed down to the database when the aggregate function is Count, Sum, Maximum, Minimum, or Square Sum. The aggregate functions Average, PopulationStdDev, PopulationVariance, StdDev, and Variance are not pushed down, but instead computed by Report Engine using the results of the pushed down functions. By pushing down group level summary computations, you can take benefit from the database's computation capability, and thus improve the report running efficiency.

You can specify the property at three levels for page reports: JDBC connection, query within the connection, and individual page report. The setting on page report has the highest priority. While, for web reports and library components, you can only specify the property on the JDBC connection or the query within the connection, and the setting on the query has higher priority. Since there is no effect on the returned data when detail data is needed, you may want to set the property on every JDBC connection.

After you activate the Push Down Group Query feature, Report Engine generates aggregate functions and GROUP BY statements for any data components that only view aggregated results. This includes all charts, crosstabs, summary tables, and banded objects which hide the detail panel. When Report Engine retrieves data for one of these types of data components, it dynamically modifies the SQL to only return the aggregated data. Thus, you can use the same generic query to run many different data components without modifying the query. For example, a chart using the Orders table that shows sales by state generates a query that just returns one row per state while a summary table by product name returns just one record for each product. This can result in orders of magnitude better performance.

### 
The QueryOptimizer Interface

The QueryOptimizer interface is in the toolkit.db.queryoptimization package. You can refer to the Report Java API Documentation for usage of the interface.

This interface contains only one method: Optimizer optimizeQuery(QueryInfo queryInfo);.

 One QueryInfo is automatically passed into the interface, and one Optimizer object should be returned.

To implement the interface and make it work

- Define a Java class file that implements the QueryOptimizer interface.

- Compile the Java file to generate the class file.

- Append the class path to the ADDCLASSPATH variable of setenv.bat in <install_root>\bin.

- Start Server.

- Open the catalog that contains the connection you would like to optimize.

- Set the Custom Query Optimizer property of the connection to Package_Name.Class_Name. 

 The List<ColumnInfo> parameter in the implementation class of the QueryOptimizer interface depends on the Prefetch property of the related business view. If you set Prefetch of the business view to "true", List<ColumnInfo> includes all columns in the business view; otherwise, it only includes columns used by the related report.

## 
JSON Schema Properties           

This section describes the properties of a Schema object in a JSON connection.

| Property Name | Description |
| --- | --- |
| Data Type | Show the JSON data type of the element whose element type is attribute or simple data array. Read only. |
| Element Type | Show the type of the element. Read only. |
| Format for Parsing Date/Time | Server displays this property when you set Mapped SQL Type to DATE, TIME, or TIMESTAMP. You can use it to specify the format to parse the Date/Time data. Select a format from the drop-down list or type an acceptable format pattern of the java.text.SimpleDateFormat class in the value cell. If the property value is blank, Server applies the rules as described in How Designer Gets Data from JSON Data Sources in the Report Designer Guide. ISO 8601 format Select to parse the Date/Time data using ISO 8601 format. JDBC timestamp escape format Select to parse the Date/Time data using the JDBC Timestamp format. Data type: String |
| Mapped SQL Type | Specify the SQL type mapped from JSON data type. You can set this property for attribute and simple data array elements only. Data type: String |
| Name | Show the name of the element. Read only. |

## 
Parameter Properties
            

This section describes the general properties of a Parameter object in a catalog. For the other parameter properties, see  Setting Report Object Properties Using the Inspector Panel.

| Property Name | Description |
| --- | --- |
| General |  |
| Allow Showing Unencrypted Value | Specify whether to display the "Hide Parameter Value" option in the UI for specifying the parameter values to allow users to view the unencrypted values of the parameter after the values are encrypted. Data type: Boolean |
| Binding | Specify the parameter to bind with the current parameter to sort the column controlled by the current parameter. Data type: String |
| Column | Show the column name of the field in the raw database. |
| Default Value Number | Specify the default parameter value you want to prompt to users. Set the property value to 0 when you want to prompt the first parameter value that you specify for the parameter; set the property value to -1 to prompt the last parameter value. Data type: Integer |
| Description | Specify the description of the object. Data type: String |
| Display Column | Specify the display column of the parameter. Data type: String |
| Display Width | Specify the display width of the object, which takes effect when you insert the object into reports. Type a numeric value to change the width. If you do not set the display width, Server applies a default width to it automatically. Data type: Float After you set the Display Width property of an object and use the object while creating a data component with wizard, Server may adjust its width according to the paper size. |
| Distinct | Specify whether to display identical values only once in the UI for specifying the parameter value. Data type: Boolean |
| Encrypt Parameter Value | Specify whether to encrypt values of the parameter in the UI where the parameter is used or required (excluding parameter control and parameter form control) and in log files. However, when you bind the parameter with a column or set its Allow Multiple Values property to "true", Report Engine only encrypts its values in log files. When writing the value of a formula or string that references an encrypted parameter to log, Report Engine may not encrypt the parameter value. Data type: Boolean |
| Get Value from API Only | Specify whether the parameter values can only be specified using API. When this property is "true", users should obtain parameter values only from API and there is no parameter dialog box available in any Designer or Server UI for inputting values. Users need to provide values of the parameter by API such as URLs, coding, and sessions; otherwise, Report Engine applies the default value of the parameter. When this property is "false", the parameter values can be obtained from both GUI and API. When a member of a cascading parameter group can get values from API only, it means that all the higher-level members shall get values from API only. This also applies to parameters on which other parameters depend. When several parameters share values in JDashboard, if any of them can get values from API only, they will share the values from API. Data type: Boolean |
| GUI Field | This property is read only. |
| Hide Parameter When Single Value Returned | Specify whether to hide the parameter when only a single value is returned to it. When you bind a parameter with a column, you can specify to hide the parameter if only a single value is returned to it at runtime. Report Engine then applies the returned single value as the default value of the parameter. This can be very useful for security. For example, you can use a parameter bound with a DBField such as UserID and if there is one to one mapping of UserID to the Server users, then a query for a parameter such as Select UserID FROM Employees WHERE UserID = @username would just return a single value and thus you can use it as a filter for any other queries you create. Data type: Boolean |
| Import SQL | Specify the SQL statement for retrieving values of the bound column and display column for the parameter. You can use the special field "User Name" in the SQL statement as @username. Data type: String Once you edit the SQL statement, the later changes to the Bind Column and Display Column properties cannot take effect unless you remove the SQL lines or bind column to the parameter all over again using dialog box. |
| Maximum Value | Specify the maximum value allowed for the parameter, or the maximum length for a String type parameter. Data type: String |
| Minimum Value | Specify the minimum value allowed for the parameter, or the minimum length for a String type parameter. Data type: String |
| Name | Specify the mapped name of the object in the catalog. Data type: String |
| Object Name | Specify the name of the OOJDBC class related to the parameter. Data type: String |
| Object Parameter Name | Specify the parameter name for the OOJDBC class. Data type: String |
| Operation | Specify whether to check the minimum and maximum values users provide to the parameter. If you want to perform the check, set the property value to -1; otherwise, set it to 1. Data type: Integer |
| Prompt Text | Specify the text for prompting users to provide values for the parameter. To help users avoid typing a value out of range, you can add the value range to the end of the prompt text, for example, "Type a customer ID (1~100):"; to help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text, for example, "Type an order date (MMM-dd-yy):". |
| Record Level Security | Specify the record level security to apply to the parameter. If you bind a parameter with a column, you can specify a RLS policy defined on the bound column to the parameter, then at runtime, the specified security identifier only sees the records it is allowed to view in the parameter value drop-down list. See Applying RLS to a Parameter in the Report Designer Guide for an example. Data type: String |
| Required | Specify whether the parameter is a required parameter. A required parameter must be fulfilled, meaning, users must supply a value to the parameter before they can run the report. If you clear the option, the parameter is an optional parameter. The value of an optional parameter can be blank, which means users can either type a value, or leave it as it is. In the dialog box for specifying the parameter values, Report marks the prompt text of a required parameter with the "*" symbol. Data type: Boolean If a parameter is optional and you do not expect it to take effect in the report, when specifying the parameter value, you should clear the content in the value text box. Any value left in the text box functions in the report. |
| String Format | Specify the user-defined format for values of the parameter when the parameter is String data type. Data type: String |
| Treat Blank as Null | Specify whether to treat blank value as null for the parameter when the parameter is String data type. Data type: Boolean |
| Use Current Date-Time | Specify whether to use the current system's date time as the value of the parameter when the parameter is Date, Time, or DateTime data type. Data type: Boolean |
| Use Current Date-Time When Blank | Specify whether to use the current system's date time as the value of the parameter when the parameter is Date, Time, or DateTime data type, and the parameter value is blank. Data type: Boolean |
| User Defined Format | Specify the user-defined format for values of the parameter. For certain types of parameters, the value format Report provides may not satisfy your requirement. In this case, you can define your own preferred format. Once you define the value format, any value supplied to the parameter should be in accordance with this format; otherwise, there is an error message. Data type: String |
| Value | Shows values of the parameter. Read only. |
| Value Type | Specify the data type of the parameter. Choose an option from the drop-down list. Data type: Enumeration |

### 
User-Defined Format for Parameters

You should pay attention to the following when using user-defined formats for parameter values. 

- The date and time formats should follow the JDK standard.

- The user-defined format shows different appearance under different locale, and you need to specify values according to the displayed format. For example, under the Spanish or French locale, "####.##" displays as "#0,##" and you should follow "#0,##" to type values.

- The user-defined format only limits the format of the input value, which does not mean that the display value is in the same format. To change the display format of a parameter, you need to specify the Format property of this parameter in the Properties panel.

The following tables show the format syntax for decimal numbers and strings.

Decimal Number Format Syntax

| Symbol | Meaning | Notes |
| --- | --- | --- |
| 0 | A digit. |  |
| * | A digit, zero shows as a star. | Cannot mix 0, "*", and "_" in the same format. |
| _ | A digit, zero shows as a space. | Cannot mix 0, "*", and "_" in the same format. |
| # | A digit, zero shows as blank. | The actual number may be much larger than the provided format. |
| . | Placeholder for decimal separator, it may be a comma in some locales. |  |
| , | Placeholder for grouping delimiter. It may be a period in some locales. | Shows the interval to be used. |
| ; | Separates formats. | Positive and negative. |
| - | If there is no explicit negative sign, "-" is prefixed. | "#,##0.00" -> "#,##0.00;(#,##0.00)" |
| % | Divides by 100 and shows as a percentage. |  |
| X | Any other characters can be used in the prefix or suffix. |  |

String Format Syntax

| Symbol | Meaning | Example |
| --- | --- | --- |
| % | Any string of zero or more characters. | WHERE title LIKE "%computer%" finds all book titles with the word "computer" anywhere in the book title. |
| _ (underscore) | Any single character. | WHERE au_fname LIKE "_ean" finds all four-letter first names that end with "ean" (Dean, Sean, and so on). |
| [ ] | Any single character within the specified range ([a-f]) or set ([abcdef]). | WHERE au_lname LIKE "[C-P]arsen" finds author last names ending with "arsen" and beginning with any single character between "C" and "P", for example Carsen, Larsen, and Karsen. |
| [^] | Any single character not within the specified range ([^a-f]) or set ([^abcdef]). | WHERE au_lname LIKE "de[^l]%" finds all author last names beginning with "de" and where the following letter is not "l". |

## 
Query/Stored Procedure/Imported SQL Properties

This section describes the properties of a query/stored procedure or an imported SQL statement in a catalog.

| Property Name | Description |
| --- | --- |
| General |  |
| Connection Name | Specify the connection to execute the object. Data type: String |
| Data Source Filter | Specify whether to allow using the object to filter multiple queries. For more information, see Using a Query to Filter Multiple Queries in the Report Designer Guide.Data type: Boolean |
| Description | Specify the description of the object. Data type: String |
| Enable SQL Statement Creator | Specify whether the query uses the dynamic query interface to get the result set. When you set this property to "true", Report Engine can regenerate the query at runtime using the dynamic query interface. For more information, see Dynamic Queries in the Report Designer Guide. Data type: Boolean |
| Maximum Duration | Specify the maximum elapsed time allowed to fetch data from the data source when the object runs, measured in seconds. By default, the property value is 0, meaning the time is unlimited. For more information, see Limiting the Query Run Time and Number of Records in the Report Designer Guide. Data type: Integer |
| Maximum Rows | Specify the maximum number of rows to be fetched from the data source when the object runs. By default, the property value is 0, meaning the number is unlimited. For more information, see Limiting the Query Run Time and Number of Records in the Report Designer Guide. Data type: Integer |
| Name | Specify the mapped name of the object in the catalog. Data type: String |
| Path Name | Specify the pre-join path the object applies. For more information, see Creating Queries Using Pre-join in the Report Designer Guide. Data type: String |
| Procedure Name | Specify the stored procedure name in the raw database. Data type: String |
| Push Down Query/Push Down Group Query | Specify whether to push down group level summary computations in the reports that use the object to the database at runtime. true Select to push down the group level summary computations to the database if it can perform the computations; otherwise, Report Engine do the computations itself. false Select to have Report Engine perform the group level summary computations itself. Data type: Enumeration |
| Qualifier | Specify the name of the database catalog which contains the object. Data type: String Server does not provide this property when the object is in a MongoDB/JSON/Elasticsearch connection. |
| Read Only | Specify whether the object is read only. Choose an option from the drop-down list. default Select to apply the setting from the database. read & write Select to allow users to access the database in read-write mode. read only Select to allow users to access the database in read-only mode. This option can speed up the transaction of the catalog. Data type: Enumeration |
| Schema | Specify the stored procedure schema. Data type: String |
| Share | Specify whether to share the object. For more information, see Locking Queries in the Report Designer Guide. Data type: Boolean |
| Transaction Mode | Specify the transaction mode for the object. Choose an option from the drop-down list. default Select to apply the setting from the database. none Select to not use transactions for the object. read uncommitted Select to allow dirty reads, non-repeatable reads, and phantom reads to occur for the object. This mode can speed up the transaction of the catalog. read committed Select to prevent dirty reads, and allow non-repeatable reads and phantom reads to occur for the object. repeatable read Select to prevent dirty reads and non-repeatable reads, and allow phantom reads to occur for the object. serializable Select to prevent dirty reads, non-repeatable reads, and phantom reads for object. Data type: Enumeration |
| General (for Query) |  |
| Ignore Predicate If Parameter Value Is Null | If you select this option, when the query uses a parameter and the parameter value is null at runtime, Server removes this condition from the query's or business view's criterion. If a query applies a String-typed parameter and users leave the value of the parameter blank at runtime: If you select "Ignore Predicate If Parameter Value Is Null" for the query, Server regards the value of the parameter as "NULL" and does not display the predicate in the WHERE clause. If you do not select "Ignore Predicate If Parameter Value Is Null" for the query, Server treats the value of the parameter as an empty string (¡®¡¯). |
| Join on Foreign Keys | Select to automatically join tables in a query through a reference from Table A to a primary key in Table B. For example, an order form in Table A shows information on purchases that are made by a customer with a primary key of CustomerID. The customer ID # refers to a record in Table B which lists a specific address, phone number, name, and so on for the customer. CustomerID in Table A is a foreign key because it links the customer's ordering information in Table A to the customer's information in Table B using the CustomerID field. |
| Join on Primary Key with Same Names | Select to automatically join tables in a query through a field or a combination of fields that uniquely and specifically identifies a record. For example, OrderID may be the primary key in a table for Orders and also for Payments. |
| Join on Same Names | Select to automatically join tables in a query through a link between two columns of the same name in two different tables. This often creates many invalid joins such as Amount that appears in both tables. |
| Show Mapping Names | Select to display the full names of the columns in the criteria panel. This option does not affect the content in the definition. Server enables this option when the query contains only tables/views/synonyms from one JDBC connection. When it is disabled, Server treats it as selected. |
| Show Table Names | Select to display the full names of the columns in the tables in the criteria panel. |
| Select Distinct | Select to use the SELECT DISTINCT command instead of SELECT in the SQL statement of the query. Server enables this option when the query contains only tables/views/synonyms from one JDBC connection, or tables from the same collection of a database in a MongoDB connection. |
| Warn When Cartesian Exists | Select to let Server display a warning message when a Cartesian product exists. A Cartesian product is used when you add tables to the query with no join specifications. For example, Table A has three values: A, B, and C. Table B has three values: 1, 2, and 3. Value A matches value 1, value B matches value 2, and so on. This is a specific match. However, a Cartesian product could have value A matching with 1, 2, and 3, and value B matching with 1, 2, and 3, and so on. Depending on the data values, Cartesian products can produce a large dataset as unnecessary information is duplicated. For every record in Table A, a record is created for every record in Table B, thus if Table A has 10 records and Table B has 10 records, the result is a dataset containing 100 rows. However, not all Cartesian products are bad so you could use Cartesian product if the result is what you need. |

## 
Table Column Properties

This section describes the general properties of a column in query tables, tables/views/synonyms, stored procedures, or  imported SQLs. For the other column properties, see  Setting Report Object Properties Using the Inspector Panel.

| Property Name | Description |
| --- | --- |
| General |  |
| Array | Specify whether the column is an array type. Data type: Boolean |
| Column Index | Specify the column index in the result set. Data type: Integer |
| Column Name | Specify the name of the column in the raw data source. Data type: String |
| Currency | Specify whether to control the SQL type of the formulas and summaries which reference the column if the column is of the BigDecimal type. true Select to apply the BigDecimal type to the formulas and summaries and set their SQL Type to 3. false Select to apply the normal data type to the formulas and summaries. Data type: Boolean |
| Description | Specify the description of the object. Data type: String |
| Display Width | Specify the display width of the object, which takes effect when you insert the object into reports. Type a numeric value to change the width. If you do not set the display width, Server applies a default width to it automatically. Data type: Float After you set the Display Width property of an object and use the object while creating a data component with wizard, Server may adjust its width according to the paper size. |
| GUI Field | This property is read only.Data type: String |
| Length | Specify the length for the values of the column, in bytes. Data type: Integer |
| Name | Specify the mapped name of the object in the catalog. Data type: String |
| Nullable | Specify the nullability for the values of the object. true Select to indicate the object supports null values. false Select to indicate the values of the object cannot be null. unknown Select to indicate whether the values of the object can be null or not is unknown. Data type: Enumeration |
| Number Base | Specify the number base of the column. Data type: Integer |
| Precision | Specify the precision for the values of the object. The default precision comes from data source metadata and defines the object's largest number of digits. The larger the precision is, the more memory it might take; however, the more accurate values you can get. Data type: Integer |
| Scale | Specify the number of digits to the right of the decimal point for the values of the object. Data type: Integer |
| SQL Type | Specify the SQL type of the object defined in Java. Data type: Integer |

### 
SQL Type

| Option | Type | Option | Type |
| --- | --- | --- | --- |
| -7 | BIT | -6 | TINYINT |
| -5 | BIGINT | -4 | LONGVARBINARY |
| -3 | VARBINARY | -2 | BINARY |
| -1 | LONGVARCHAR | 1 | CHAR |
| 2 | NUMERIC | 3 | DECIMAL |
| 4 | INTEGER | 5 | SMALLINT |
| 6 | FLOAT | 7 | REAL |
| 8 | DOUBLE | 12 | VARCHAR |
| 16 | BOOLEAN | 91 | DATE |
| 92 | TIME | 93 | TIMESTAMP |
| 2003 | ARRAY | 2004 | BLOB |
| 2005 | CLOB |  |  |

## 
Table/View/Synonym Properties

This section describes the properties of a Table/View/Synonym object in a catalog when you edit connection resources.

| Property Name | Description |
| --- | --- |
| Collection Name | Server displays this property when the table is in a MongoDB connection. You can use it to specify the name of the collection in the MongoDB database. Data type: String |
| Database Name | Server displays this property when the table is in a MongoDB connection. You can use it to specify the name of the database in the MongoDB database. If the database you specify exists in the MongoDB database, Server connects to the database; otherwise, Server gets no data. Data type: String |
| Description | Specify the description of the object. Data type: String |
| Element Path | When the table is in a MongoDB connection, you can use this property to specify the element name path from the top-level document if the table is mapped to a document array element. The path is the element names separated by ".". The property value is blank if the table is mapped to the top-level element. Server uses "\" as an escaped char. If the element name contains "." and "\", Server records them as "\." and "\\". When the table is in a JSON/Elasticsearch connection, this property shows the element path from the root element to current element, and is read only. Data type: String |
| Linked Parameter | Specify the parameter you want to bind to the parameter in OOJDBC. Data type: String Server does not provide this property when the table is in a JSON/Elasticsearch connection. |
| Name | Specify the mapped name of the object in the catalog. Data type: String |
| Qualifier | Specify the name of the database catalog which contains the object. Data type: String Server does not provide this property when the table is in a MongoDB/JSON/Elasticsearch connection. |
| Schema | Specify the name of the schema which contains the object. Data type: String Server does not provide this property when the table is in a MongoDB/JSON/Elasticsearch connection. |
| Table Name | Specify the name of the object in the raw database. Data type: String Server does not provide this property when the table is in a MongoDB/JSON/Elasticsearch connection. |
| Type | Specify the type of the object. Choose an option from the drop-down list. After you edit the type, Server moves the object to the corresponding resource node automatically. Data type: Enumeration Server does not provide this property when the table is in a JSON/Elasticsearch connection. |
