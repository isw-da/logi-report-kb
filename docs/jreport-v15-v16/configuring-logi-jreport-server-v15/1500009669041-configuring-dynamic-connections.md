---
title: "Configuring Dynamic Connections"
id: 1500009669041
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections
updated_at: 2021-07-24T20:55:22Z
---

# Configuring Dynamic Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644422-Configuring-Connections)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669061-Configuring-the-datasource-xml-File)

# Configuring Dynamic Connections

A dynamic connection is a group of connection properties that can be used to override the original data source connections in a catalog. The server administrator can modify some of the original catalog connection properties, and then save these modified properties as a dynamic connection property. For a dynamic connection, the administrator can define a database user mapping table which is a table containing the columns: SID, database user, and database password. Logi JReport Server manages the dynamic connections in the server system database.

When running a report or scheduling a report to run, if there are multiple dynamic connections available to the log-in user, the user needs to select one. Then the server will pass the changed connection properties of the selected dynamic connection into the report engine. The report engine will merge the changed properties with the other original catalog connection properties to setup the database connection.

Dynamic connections are categorized at the [organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations) level. If the system administrator creates a dynamic connection, the connection maps to no organization. If an organization administrator creates a dynamic connection, the connection maps to the organization. If a dynamic connection is defined in an organization, all users/groups/roles must be from the same organization. If a connection is defined in non-organization, all users/groups/roles must be from non-organizations. System administrator can define, view and edit all the dynamic connections.

Developer users can also [use API to apply dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009644022-Dynamic-Connection-API).

Below is a list of the sections covered in this topic:

* [Creating a Dynamic Connection](#Create)
* [Managing Dynamic Connections](#Manage)
* [Applying Dynamic Connections](#Apply)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Dynamic Connection

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Dynamic Connections** from the drop-down menu to open the Configuration - Dynamic Connections page.

   ![Configuration - Dynamic Connections page](https://devnet.logianalytics.com/hc/article_attachments/4404926783127/config_cnct_dyncnct1.gif)
2. Select the **New Dynamic Connection** link. The [New Dynamic Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009646602-New-Dynamic-Connection) dialog appears.

   ![New Dynamic Connection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404926740631/nwdyncnct.gif)
3. Select **Browse** to select a catalog in the Select Catalog dialog.
4. From the Data Source Name drop-down list, select a data source available in the selected catalog.
5. From the Connection Name drop-down list, select a connection to connect to the data source.
6. Select **Properties** to expand the properties table. To change a property's value, first select the checkbox beside it, and then enter a value in the text box or select a value from the drop-down list as required.
7. Select **Add Database User Mapping** to define the mapping relationship between SID and database user/password. A mapping row will be added in the mapping table. From the SID drop-down list, select a user, role, or group name. Double-select in the text box of Database User and Database Password and you can then type in database user name and password. Then select **Test Connection** to test whether the user name and password can connect to the database.

   ![Mapping Table](https://devnet.logianalytics.com/hc/article_attachments/4404920653335/config_cnct_dyncnct2.gif)

   Within a dynamic connection, make sure that an SID is mapped to only one pair of database user and name.
8. Select **OK** to create the dynamic connection. It is then added in the dynamic connection table which consists of the following columns.

   | Column Name | Description |
   | --- | --- |
   | Catalog | Displays the catalogs of the dynamic connections with the full resource path, for example, `/SampleReports/SampleReports.cat`. |
   | Data Source | Displays the data source names of the dynamic connections in the catalog. |
   | Connection Name | Displays the dynamic connection names. You can select a connection name to edit the dynamic connection. |
   | SID | Displays the security identifiers (SID). An SID can be a group, a role, or a user in the Logi JReport Server security system. |
   | Organization Name | Shows the organizations that the SIDs belong to. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations) feature is enabled. |
   | Database User | Displays the database user names of the dynamic connections. Null means using the default database user name. |
   | Database password | Displays the database passwords of the dynamic connections. The passwords are masked. |

   All columns in the table are sortable except for Database Password. To sort the table by certain column, select on the column name. By Default the table is sorted by Connection Name.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Dynamic Connections

You can perform the following tasks on the dynamic connections in the dynamic connection table:

**Searching for a dynamic connection**

First select a search category from the drop-down list, then type the text in the text box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) to start the search. The **x** button in the text box is used to clear the input text. After the results are filtered, to return to the state before search, select **x** in the text box.

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

In the dynamic connection table, select the connection name to open the [Edit Dynamic Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009646442-Edit-Dynamic-Connection) dialog, in which you can edit the properties of the dynamic connection as you want.

**Deleting dynamic connections**

In the dynamic connection table, select the checkboxes ahead of the dynamic connections and then select **Delete**. To delete all the dynamic connections at a time, select the checkbox on the column header and then select **Delete**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Applying Dynamic Connections

One user can have multiple dynamic connections for one catalog data source. When running a report, if there are multiple dynamic connections for the log-in user:

* For [advanced run](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports#Advanced), the user needs to select a dynamic connection from the available ones.
* For [schedule run](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports), if the selected dynamic connection cannot be found when running reports, then the first available dynamic connection will be applied.
* For direct run, link reports, API run, getting parameter values from the database, and getting filter values from the database, the first available dynamic connection is applied automatically.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644422-Configuring-Connections)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669061-Configuring-the-datasource-xml-File)
