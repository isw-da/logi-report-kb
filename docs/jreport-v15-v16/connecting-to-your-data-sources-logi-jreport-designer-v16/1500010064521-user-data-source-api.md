---
title: "User Data Source API"
id: 1500010064521
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064521-User-Data-Source-API
updated_at: 2021-07-24T10:39:12Z
---

# User Data Source API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064481-User-Defined-Data-Sources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064501-Adding-User-Defined-Data-Sources-to-a-Catalog)

# User Data Source API

User Data Source API enables Logi JReport Designer to access data from an external data source, which is not stored in a databas, or when there is no JDBC driver available.

Below is a list of the sections covered in this topic:

* [Introduction to the UDS API](#Intro)
* [UDS API Interface](#Interface)
* [JDBC API Used by UDS](#JDBC)
* [Examples of Using the UDS API](#Example)

## Introduction to the UDS API

The User Data Source API is a part of the Logi JReport data Access Model as shown in the following diagram. It is:

* Is a Java interface that provides a dataset to Logi JReport
* Has a PARAMETER string, which can be changed when the UDS object is added into Logi JReport Designer. The result set may differ according to the PARAMETER string. It is very flexible and convenient.

![Logi JReport Data Access Model diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901305367/cnctn_uds_api.gif)

Through the UDS API, Logi JReport Designer can access data from an external data source, such as a text file, or Excel file, which is not stored in a database, or when there is no JDBC driver available.

**Notes:**

* The PARAMETER here is the parameter string given to the UDS interface. That is, the UDS API provides the method *getResultSet (String strParam)*, and PARAMETER is the string strParam in this method. As a reminder, PARAMETER here is different from the parameter object in the Logi JReport catalog. To distinguish between them, an upper case PARAMETER is used to refer to the parameter string in the UDS, and a lower case parameter for the parameter object in a catalog.
* To design a report, Logi JReport requires a metadata (see java.sql.ResultSetMetaData) which corresponds to the ResultSet that the data source has returned. To view or run a report, Logi JReport requires a ResultSet object. The user data source must provide both of these two parts for Logi JReport

## UDS API Interface

To use the UDS API, the interface jet.datasource.JRUserDataSource must be implemented, and the class definition may be as follows. For detailed information, see the jet.datasource.JRUserDataSource class in the Logi JReport Javadoc located in `<install_root>\help\api`.

```
import jet.datasource.*;  
public class UserUDS   
    implements JRUserDataSource  
{  
    // Class body.  
}
```

The following are methods of the interface:

**Public java.sql.ResultSet getResultSet(String strParam) throws JRUserDataSourceException**

This method gets the result set for user data source.

* **PARAMETER**: strParam - A String value used to request and get different result sets. The format of the PARAMETER string is defined and parsed by your Java class. You can enter the PARAMETER string when you add the UDS to a catalog. If you want to use [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) predefined in the catalog, you can reference them as *@ParameterName* in the PARAMETER string.

  Below are the parsing rules for the PARAMETER string you should get known of:

  + The characters used for parameter name can be any character defined on the keyboard, except for quotation marks.
  + Parameter name is introduced with @, and sometimes colon : is also recognized as an introducer.
  + When the PARAMETER string contains characters such as: At sign(@), ':', double quotation mark('"'), or other strings that do not need to be parsed by Logi JReport, you can use a pair of double quotation marks to quote them. For example, your PARAMETER string may be:

    `jdbc:oracle:thin:@204.177.148.30:1521:orcl`

    Here, @ is a character used by the URL. If you add this PARAMETER string for a UDS in a catalog, Logi JReport will regard 204 as the name of a parameter in the catalog. The correct form is:

    `"jdbc:oracle:thin:@204.177.148.30:1521:orcl"`
* **Returns**: java.sql.ResultSet - A row and column dataset that can be used in Logi JReport.
* **Throws**: JRUserDataSourceException - If a database access error occurs.

  When you provide a java.sql.ResultSet instance, to reduce your work, you do not need to implement all methods of java.sql.ResultSet. You can just extend abstract class jet.datasource.JRResultSet. If you specify the column properties, for example, SQL data type, and precision, you will not need to provide a ResultSetMetaData instance, and Logi JReport will not invoke the *getMetaData()* function of ResultSet. However, if you do not specify the properties, you will have to implement the *getMetaData()* function and provide a ResultSetMetaData instance.

**Public void releaseResultSet() throws JRUserDataSourceException**

This method frees the ResultSet object.

* **Throws**: JRUserDataSourceException - If there are some errors when freeing the resource.

## JDBC API Used by UDS

In order to get data from user defined data source, Logi JReport needs to invoke the following JDBC API (for details about the API, refer to <http://java.sun.com/javase/6/docs/api/>).

**java.sql.ResultSet**

* boolean next() throws SQLException
* void close() throws SQLException
* boolean wasNull() throws SQLException
* String getString(int columnIndex) throws SQLException
* boolean getBoolean(int columnIndex) throws SQLException
* byte getByte(int columnIndex) throws SQLException
* short getShort(int columnIndex) throws SQLException
* int getInt(int columnIndex) throws SQLException
* long getLong(int columnIndex) throws SQLException
* float getFloat(int columnIndex) throws SQLException
* double getDouble(int columnIndex) throws SQLException
* byte[] getBytes(int columnIndex) throws SQLException
* java.sql.Date getDate(int columnIndex) throws SQLException
* java.sql.Time getTime(int columnIndex) throws SQLException
* java.sql.Timestamp getTimestamp(int columnIndex) throws SQLException
* java.io.InputStream getAsciiStream(int columnIndex) throws SQLException
* java.io.InputStream getBinaryStream(int columnIndex) throws SQLException
* ResultSetMetaData getMetaData() throws SQLException
* Object getObject(int columnIndex) throws SQLException
* int findColumn(String columnLabel) throws SQLException
* BigDecimal getBigDecimal(int columnIndex) throws SQLException
* Blob getBlob(int columnIndex) throws SQLException
* Clob getClob(int columnIndex) throws SQLException

**java.sql.ResultSetMetaData**

* int getColumnCount() throws SQLException
* boolean isCurrency(int column) throws SQLException
* int isNullable(int column) throws SQLException
* int getColumnDisplaySize(int column) throws SQLException
* String getColumnLabel(int column) throws SQLException
* String getColumnName(int column) throws SQLException
* String getSchemaName(int column) throws SQLException
* int getPrecision(int column) throws SQLException
* int getScale(int column) throws SQLException
* String getTableName(int column) throws SQLException
* int getColumnType(int column) throws SQLException

**Note:** The method *ResultSetMetaData getMetaData()* throws SQLException is only invoked when the [Specify Columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010067261-New-User-Defined-Data-Source-Dialog#Column) option is not checked in the New User Defined Data Source dialog.

## Examples of Using the UDS API

The UDS API is flexible and convenient to use. Before you implement it, you should first make an overall consideration of the architecture. Logi JReport provides you with several scenarios which use the Logi JReport UDS API. You can refer to them for assistance.

* When there is no JDBC driver available for an external data source (for example, a comma-delimited text file), you can create a ResultSet object to return the data to the requesting report. See [Example 1: Adding a Flat File UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010064501-Adding-User-Defined-Data-Sources-to-a-Catalog#Example1).
* You can return a ResultSet through the JDBC API. See [Example 2: Adding an SQL Data Source UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010064501-Adding-User-Defined-Data-Sources-to-a-Catalog#Example2).
* [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010029542-Oracle-Stored-Procedure-UDS).
* [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010064541-EnterpriseDB-Stored-Procedure-UDS).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064481-User-Defined-Data-Sources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064501-Adding-User-Defined-Data-Sources-to-a-Catalog)
