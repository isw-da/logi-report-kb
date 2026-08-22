---
title: "Creating and Using Dynamic Connections"
id: 1500009712421
section: "Configuring Connections"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712421-Creating-and-Using-Dynamic-Connections
updated_at: 2021-11-03T06:58:27Z
---

# Creating and Using Dynamic Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712401-Configuring-Connections)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712441-Specifying-Connections-in-datasource-xml)

# Creating and Using Dynamic Connections

A dynamic connection is a group of connection properties that can be used to override the original data source connections in a catalog. Administrators can modify some of the original catalog connection properties, and then save these modified properties as a dynamic connection. For a dynamic connection, administrators can define a database user mapping table which is a table containing the columns: SID, database user, and database password. Then when an end user running a report, if there are dynamic connections available to his SID, the user can select a dynamic connection to apply. Logi JReport Server manages dynamic connections in the server system database.

Dynamic connections are categorized at [organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations) level. If the system administrator creates a dynamic connection, the connection is available to users that are not from any organizations. If an organization administrator creates a dynamic connection, the connection is available to users of the organization. If a dynamic connection is defined in an organization, all users/groups/roles must be from the same organization. If a connection is defined outside of all organizations, all users/groups/roles must be from outside of all organizations. System administrator can define, view and edit all the dynamic connections.

Developer users can also [call API methods for using dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009686302-Dynamic-Connection-API).

Below is a list of the sections covered in this topic:

* [Creating Dynamic Connections](#Create)
* [Managing Dynamic Connections](#Manage)
* [Applying Dynamic Connections](#Apply)

## Creating Dynamic Connections

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Connection** > **Dynamic Connections** from the drop-down menu to open the Dynamic Connections page.

   ![Dynamic Connections page](https://devnet.logianalytics.com/hc/article_attachments/4412112635287/config_cnct_dyncnct.gif)
2. Select the **New Dynamic Connection** link. The [New Dynamic Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009688782-New-Dynamic-Connection) dialog appears.

   ![New Dynamic Connection dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131467671/nwdyncnct.gif)
3. Select **Browse** to select a catalog in the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009715121-Select-Catalog) dialog.
4. From the Data Source Name drop-down list, select a data source available in the selected catalog.
5. From the Connection Name drop-down list, select a connection to connect to the data source.
6. Select **Properties** to edit properties of the selected connection. To change a property's value, first select the checkbox beside it, then enter a value in the Value text box or select a value from the drop-down list. Initially all the properties are unchecked and uneditable. Whenever a property is unchecked, it always shows the original value regardless of whether you have changed the value or not.

   There are the following properties:

   | Property Name | Description |
   | --- | --- |
   | Date Format | Specifies the default Date format corresponding to the database. The Date format Logi JReport supports follows that of Java. |
   | Description | Specifies the description of the connection. |
   | Driver | Specifies the class name of the JDBC driver such as oracle.jdbc.driver.OracleDriver. |
   | Is JNDI Data Source | Specifies whether it is a JNDI data source. |
   | JNDI Data Source Name | Specifies the JNDI data source name when the Is JNDI Data Source property is true. |
   | Name | Specifies the name of the connection which, by default, is the connection URL, but can also be a user friendly name for the connection. |
   | Name Pattern | Specifies whether or not catalog or schema is used in data manipulation. Choose an option from the drop-down list. * Unqualified - Neither catalog nor schema is included in data manipulation. Example: SELECT t.c FROM t * Qualified\_2part - Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * Qualified\_3part- Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t |
   | Read Only | Specifies the mode to open the connection to the JDBC data source. The initial setting is Default which uses the mode specified by the DBMS Administrator which could be read only or read & write. Choose an option from the drop-down list. * Default - May be read & write or read only depending on the DBMS default setting. * Read only - Allows the driver to optimize performance for reporting which does not need to write to the DBMS. * Read & write - Opens the DBMS with updates enabled which requires more processing to ensure concurrency control. |
   | Time Format | Specifies the default time format corresponding to the database. |
   | Timestamp Format | Specifies the default timestamp format corresponding to the database. The Timestamp formats Logi JReport supports follows that of Java. |
   | Transaction Mode | Specifies the transaction mode for the connection. Choose an option from the drop-down list. * Default - Indicates the transaction information cannot be got from JDBC connection. * None - Indicates that transactions are not supported. * Read\_uncommitted - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * Read\_committed - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * Repeatable\_read - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * Serializable - Dirty reads, non-repeatable reads and phantom reads are prevented. |
   | URL | Specifies the JDBC URL which establishes the connection to the database, for example, jdbc:oracle:thin:@localhost:1521:ORCL. |
   | User-Defined Extra Characters | Specifies extra characters of user-defined quote qualifier. |
   | User-Defined Quote Characters | Specifies the quote character of user-defined quote qualifier. |
   | Default Database User | Specifies the user name for connecting to the database, which is determined by the database DBA. Null means using the default database user name. |
   | Default Database Password | Specifies the password for connecting with the database, which is determined by the database DBA. Null means using the default database password. |
7. Select **Add Database User Mapping** to define the mapping relationship between SID and database user/password as follows: from the SID drop-down list, select a user, role or group name, double-click in the text box of Database User and Database Password and type in database user name and password, then select **Test Connection** to test whether the user name and password can connect to the database.

   Within a dynamic connection, make sure that an SID is mapped to only one pair of database user and name.
8. Select **OK** to create the dynamic connection.

The dynamic connection is then added in the dynamic connection table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Catalog | Displays the catalogs of the dynamic connections with the full resource path, for example, `/SampleReports/SampleReports.cat`. |
| Data Source | Displays the data source names of the dynamic connections in the catalog. |
| Connection Name | Displays the dynamic connection names. You can select a connection name to edit the dynamic connection. |
| SID | Displays the security identifiers (SID). An SID can be a group, a role, or a user in the Logi JReport Server security system. |
| Organization Name | Shows the organizations that the SIDs belong to. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations) feature is enabled. |
| Database User | Displays the database user names of the dynamic connections. Null means using the default database user name. |
| Database password | Displays the database passwords of the dynamic connections. The passwords are masked. |

## Managing Dynamic Connections

Administrators can perform the following tasks for the dynamic connections in the dynamic connection table:

**Sorting the dynamic connections**

Dynamic connections can be sorted by columns except for Database Password in the dynamic connection table. To sort the dynamic connections by a column, select on the column name.

**Searching for a dynamic connection**

First select a search category from the drop-down list, then type the text in the text box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif) to start the search. The **x** button in the text box is used to clear the input text. After the results are filtered, to return to the state before search, select **x** in the text box.

There are the following search categories:

* **Catalog**  
   Searches for catalogs.
* **Connection Name**  
   Searches for connection names.
* **SID**  
   Searches for SIDs.
* **Database User**  
   Searches for database users.

For example, in order to find the dynamic connections which use the catalog SampleReprts.cat, you can select Catalog from the search category drop-down list and input *sam* as the keyword. Logi JReport will search for *sam* in the Catalog column and the dynamic connections whose catalogs contain the text will be kept in the dynamic connection table.

**Editing a dynamic connection**

Select the connection name to open the [Edit Dynamic Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009688642-Edit-Dynamic-Connection) dialog, in which you can edit the properties of the dynamic connection as you want.

**Deleting dynamic connections**

Select the checkboxes ahead of the dynamic connections and select **Delete** above the dynamic connection table. To delete all the dynamic connections at a time, select the checkbox on the column header and select **Delete**.

## Applying Dynamic Connections

When [running a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports) or [scheduling a task to run a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009692482-Scheduling-Reports), if there are dynamic connections available to the log-in user, the user needs to select one. Logi JReport Server then passes the changed connection properties of the selected dynamic connection into the Report Engine. The Report Engine will merge the changed properties with the other original catalog connection properties to setup the database connection.

One user can have multiple dynamic connections for one catalog data source, so when there are multiple dynamic connections for a log-in user:

* For direct run, link reports, API run, getting parameter values from the database, and getting filter values from the database, the first available dynamic connection is applied automatically.
* For advanced run, the user needs to select a dynamic connection from the available ones.
* For schedule run, if the selected dynamic connection cannot be found when running reports, then the first available dynamic connection will be applied.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712401-Configuring-Connections)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712441-Specifying-Connections-in-datasource-xml)
