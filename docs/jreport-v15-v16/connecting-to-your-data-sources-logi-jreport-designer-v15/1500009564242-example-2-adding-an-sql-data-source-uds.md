---
title: "Example 2: Adding an SQL Data Source UDS"
id: 1500009564242
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS
updated_at: 2021-07-24T05:55:44Z
---

# Example 2: Adding an SQL Data Source UDS

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585241-Example-1-Adding-a-Flat-File-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585261-Example-3-Adding-a-Java-Object-Data-Source-UDS)

# Example 2: Adding an SQL Data Source UDS

This topic demonstrates how to add an SQL Data Source UDS.

This is a fairly complex example, which executes an SQL statement and returns a result set through the JDBC API.

Below is the Java code for class definition:

|  |
| --- |
| ``` import jet.datasource.*; public class SQLDataSource implements JRUserDataSource { 	// Define data. 	public ResultSet getResultSet(String param) 			throws JRUserDataSourceException { 		// Method body. 	} 	/** 	 * Free the resources such as: Connection, Statement, ResultSet. 	 */ 	public void releaseResultSet() throws JRUserDataSourceException { 		// Method body. 	} } ``` |

The following explains the above code.

* The format of the String variable parameter is DRIVER=driver&URL=url&USER=user&PSWD=password&SQL=sql.

  For example, we used HSQL DB as the data source, and `C:\Logi JReport\Designer\Demo\db\JRDemo` as the hsql db path; "sa" as the user's name, "" as the password, and `select * from authors` as the SQL string. The parameter string may be similar to:

  `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\Logi JReport\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=select * from employee`

  If you want to use predefined parameters in the Logi JReport catalog, you can input the parameter string as:

  `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\Logi JReport\\Designer\\Demo\\db\\JRDemo"&USER=@un&PSWD=&SQL=@sql`

  Where, @sql is a parameter predefined in the catalog, and its default value is "select \* from employee".

  **Note:** Every time when running, java.sql.Resultset must return the same meta data (UDS fields), including the number and order of fields, and the field properties such as column name, SQL type, precision, scale, nullable, currency, and array.
* The getResultSet() method will parse the parameter string, build a connection to the URL, and then execute the SQL statement.
* The releaseResultSet() method will release the resource such as Connection, Statement, and ResultSet.

Below is a list of the sections covered in this topic:

> * [Compiling and Running SQLDataSource](#Compile)
> * [Adding the SQLDataSource UDS to a Catalog](#Add)

## Compiling and Running SQLDataSource

There is one class used in this example and its source code is SQLDataSource.java, which is available in `<install_root>\help\samples\APIUDS\sqlUDS`. In this example, SQLDataSource will return the result set from demo hsql db. You should set up the HSQL DB path in the URL string and point it to the demo database at `<install_root>\Demo\db\JRDemo`.

Copy SQLDataSource.java to `<install_root>\help`, and compile it to generate SQLDataSource.class. Append the path `<install_root>\help` to the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`, so that SQLDataSource can be found at runtime.

## Adding the SQLDataSource UDS to a Catalog

After compilation, you can now add the UDS to a Logi JReport catalog.

1. Start Logi JReport Designer with the batch file you just modified.
2. Open an existing catalog.
3. In the Catalog Manager resource tree, right-click the data source to which the UDS is to be added, then select **New****User Defined Data Source** from the shortcut menu.
4. In the New User Defined Data Source dialog, enter the required information.

   If you check the Specify Columns option, the column definitions list will be enabled and you can add column definitions. If you don't specify column definitions, Logi JReport will obtain them from the result set automatically. Here, we will not specify column definitions. Instead, we will use the default ones from the ResultSet and the ResultSetMetaData.

   Enter **employees** in the Name field and **SQLDataSource** in the Class Name field. In the Parameter box, enter:

   `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\Logi JReport\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=select * from employee`

   Make sure that the five bold parts in the above line are capitalized.
5. Select **OK** to add the UDS.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585241-Example-1-Adding-a-Flat-File-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585261-Example-3-Adding-a-Java-Object-Data-Source-UDS)
