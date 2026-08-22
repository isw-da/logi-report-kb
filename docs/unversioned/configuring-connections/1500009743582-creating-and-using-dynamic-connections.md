---
title: "Creating and Using Dynamic Connections"
id: 1500009743582
section: "Configuring Connections"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743582-Creating-and-Using-Dynamic-Connections
updated_at: 2021-07-24T00:49:28Z
---

# Creating and Using Dynamic Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743562-Configuring-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743602-Specifying-Connections-in-datasource-xml)

# Creating and Using Dynamic Connections

Administrators can modify the original catalog connection properties, and then save these modified properties as a dynamic connection. This topic describes how you can create, manage, and apply dynamic connections in Logi Report Server.

For a dynamic connection, you can define a database user mapping table to contain these columns: SID, database user, and database password. Then when a user runs a report, if there are dynamic connections available to his SID, the user can select a dynamic connection to apply. Logi Report Server manages dynamic connections in the server system database.

Dynamic connections are categorized at [organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) level. If the system administrator creates a dynamic connection, the connection is available to users that are not from any organizations. If an organization administrator creates a dynamic connection, the connection is available to users in the organization. If a dynamic connection is defined in an organization, all users/groups/roles must be from the same organization. If a connection is defined outside of all organizations, all users/groups/roles must be from outside of all organizations. System administrator can define, view, and edit all the dynamic connections.

Developers can also [call API methods for using dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009771041-Dynamic-Connection-API).

This topic contains the following sections:

* [Creating Dynamic Connections](#Create)
* [Managing Dynamic Connections](#Manage)
* [Applying Dynamic Connections](#Apply)

## Creating Dynamic Connections

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Connection** > **Dynamic Connections** from the drop-down menu. Server displays the Dynamic Connections page.

   ![Dynamic Connections page](https://devnet.logianalytics.com/hc/article_attachments/4404880568215/config_cnct_dyncnct.gif)
2. Select **New Dynamic Connection**. Server displays the [New Dynamic Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009746142-New-Dynamic-Connection-Dialog-Box-Properties) dialog box.

   ![New Dynamic Connection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885511063/nwdyncnct.gif)
3. Select **Browse**.
4. Server displays the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009774661-Select-Catalog-Dialog-Box-Properties) dialog box. Select a catalog and select **OK**.
5. From the **Data Source Name** drop-down list, select a data source available in the selected catalog.
6. From the **Connection Name** drop-down list, select a connection to connect to the data source.
7. Select **Properties**. Server displays the properties of the selected connection. To change a property's value, first select the property, then type a value in the **Value** text box or select a value from the drop-down list. Initially all the properties are unselected and uneditable. Whenever a property is unselected, it always shows the original value regardless of whether you have changed the value.

   See the connection properties in the following table:

   | Property Name | Description |
   | --- | --- |
   | Date Format | Specifies the default Date format corresponding to the database. The Date format Logi Report supports follows that of Java. |
   | Description | Specifies the description of the connection. |
   | Driver | Specifies the class name of the JDBC driver such as oracle.jdbc.driver.OracleDriver. |
   | Is JNDI Data Source | Specifies whether it is a JNDI data source. |
   | JNDI Data Source Name | Specifies the JNDI data source name when the Is JNDI Data Source property is true. |
   | Name | Specifies the name of the connection which, by default, is the connection URL, but can also be a user-friendly name for the connection. |
   | Name Pattern | Specifies whether catalog or schema is used in data manipulation. Choose an option from the drop-down list. * Unqualified - Neither catalog nor schema is included in data manipulation. Example: SELECT t.c FROM t * Qualified\_2part - Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * Qualified\_3part- Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t |
   | Read Only | Specifies the mode to open the connection to the JDBC data source. The initial setting is Default which uses the mode specified by the DBMS Administrator which could be read only or read & write. Choose an option from the drop-down list. * Default - May be read & write or read only depending on the DBMS default setting. * Read only - Allows the driver to optimize performance for reporting which does not need to write to the DBMS. * Read & write - Opens the DBMS with updates enabled which requires more processing to ensure concurrency control. |
   | Time Format | Specifies the default time format corresponding to the database. |
   | Timestamp Format | Specifies the default timestamp format corresponding to the database. The Timestamp formats Logi Report supports follows that of Java. |
   | Transaction Mode | Specifies the transaction mode for the connection. Choose an option from the drop-down list. * Default - Indicates the transaction information cannot be got from JDBC connection. * None - Indicates that transactions are not supported. * Read\_uncommitted - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog. * Read\_committed - Dirty reads are prevented; non-repeatable reads and phantom reads can occur. * Repeatable\_read - Dirty reads and non-repeatable reads are prevented; phantom reads can occur. * Serializable - Dirty reads, non-repeatable reads and phantom reads are prevented. |
   | URL | Specifies the JDBC URL which establishes the connection to the database, for example, jdbc:oracle:thin:@localhost:1521:ORCL. |
   | User Defined Extra Characters | Specifies extra characters of user defined quote qualifier. |
   | User Defined Quote Characters | Specifies the quote character of user defined quote qualifier. |
   | Default Database User | Specifies the user name for connecting to the database, which is determined by the database DBA. Null means using the default database user name. |
   | Default Database Password | Specifies the password for connecting with the database, which is determined by the database DBA. Null means using the default database password. |
8. Select **Add Database User Mapping**. Report Server adds a row in the table below. You can define the mapping relationship between SID and database user/password in the row as follows:
   1. Double-click in the **Organization Name** text box and then select an item from the drop-down list. The item **System** means that you can select users outside of any organizations as SID.
   2. The **SID** drop-down list displays the users, roles, and groups in the selected organization. Select one as the security identifiers (SID).
   3. Double-click in the text box of **Database User** and type a user name.
   4. Double-click in the text box of Database Password and type the password.
   5. Select **Test Connection** to test whether the user name and password can connect to the database.

   Within a dynamic connection, make sure that one SID is mapped to only one pair of database user and name.
9. Select **OK** to create the dynamic connection.

Report Server then adds the dynamic connection in the dynamic connection table, which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Catalog | Displays the catalogs of the dynamic connections with the full resource path, for example, `/SampleReports/SampleReports.cat`. |
| Data Source | Displays the data source names of the dynamic connections in the catalog. |
| Connection Name | Displays the dynamic connection names. You can select a connection name to edit the dynamic connection. |
| SID | Displays the security identifiers (SID). SID can be a group, a role, or a user in the Logi Report Server security system. |
| Organization Name | Shows the organizations that the SIDs belong to. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) feature is enabled. |
| Database User | Displays the database user names of the dynamic connections. Null means using the default database user name. |
| Database password | Displays the database passwords of the dynamic connections. The passwords are masked. |

## Managing Dynamic Connections

Administrators can perform the following tasks for the dynamic connections in the dynamic connection table:

**Sorting the dynamic connections**

Dynamic connections can be sorted by columns except for Database Password in the dynamic connection table. To sort the dynamic connections by a column, select on the column name.

**Searching for a dynamic connection**

First select a search category from the drop-down list, then type the text in the text box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif) to start the search. The **x** button in the text box is used to clear the input text. After the results are filtered, to return to the state before search, select **x** in the text box.

There are the following search categories:

* **Catalog**  
   Searches for catalogs.
* **Connection Name**  
   Searches for connection names.
* **SID**  
   Searches for SIDs.
* **Database User**  
   Searches for database users.

For example, in order to find the dynamic connections which use the catalog **SampleReprts.cat**, you can select **Catalog** from the search category drop-down list and type *sam* as the keyword. Logi Report will search for *sam* in the **Catalog** column and the dynamic connections whose catalogs contain the text will be kept in the dynamic connection table.

**Editing a dynamic connection**

Select the connection name to open the [Edit Dynamic Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009745922-Edit-Dynamic-Connection-Dialog-Box-Properties) dialog box, in which you can edit the properties of the dynamic connection as you want.

**Deleting dynamic connections**

Select the dynamic connections and then select **Delete** above the dynamic connection table. To delete all the dynamic connections at a time, select the check box on the column header and select **Delete**.

## Applying Dynamic Connections

When [running a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports) or [scheduling a task to run a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009749542-Scheduling-Reports), if there are dynamic connections available to the log-in user, the user needs to select one. Logi Report Server then passes the changed connection properties of the selected dynamic connection into the Report Engine. The Report Engine will merge the changed properties with the other original catalog connection properties to setup the database connection.

One user can have multiple dynamic connections for one catalog data source, so when there are multiple dynamic connections for a log-in user:

* For direct run, link reports, API run, getting parameter values from the database, and getting filter values from the database, the first available dynamic connection is applied automatically.
* For advanced run, the user needs to select a dynamic connection from the available ones.
* For schedule run, if the selected dynamic connection cannot be found when running reports, then the first available dynamic connection will be applied.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743562-Configuring-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743602-Specifying-Connections-in-datasource-xml)
