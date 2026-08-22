---
title: "Configuring JdbcDriversConfig.properties"
id: 1500009644462
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties
updated_at: 2021-07-24T20:55:21Z
---

# Configuring JdbcDriversConfig.properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644502-Initializing-the-Database-System-as-a-Non-admin-Database-User)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service)

# Configuring JdbcDriversConfig.properties

You can configure the file JdbcDriversConfig.properties in the `<install_root>\bin` directory for better performance.

Below is a list of the sections covered in this topic:

* [Limiting the Size of the Fetch Data Buffer](#Limit)
* [Specifying Where to Implement the Maximum Query Run Time and Number of Records](#Query)
* [Canceling Running Query](#Cancel)

## Limiting the Size of the Fetch Data Buffer

If you are using a database which supports the JDBC method Statement.setFetchSize(), you can request the database retrieve a specified number of rows in each read instead of all rows which minimizes memory usage which can improve performance. It can also avoid Java heap out of memory errors when doing large queries. Logi JReport provides a property setFetchSize in the JdbcDriversConfig.properties file for you to do this.

The following is an example of setting the setFetchSize property in the JdbcDriversConfig.properties file and detailed description of each property:

|  |
| --- |
| ``` DriverName_D1 = MySQL-AB JDBC Driver Vendor_D1 = MySql.com Version_D1 = 3.0.8-stable ( $Date: 2003/05/19 00:57:19 $, $Revision: 1.27.2.18 $ ) setFetchSize_D1 = 5000 ``` |

* **DriverName\_[Name]**Database driver name that should be used to establish a connection. You can use connection.getMetaData().getDriverName() to obtain the value.
* **Vendor\_[Name]**The vendor of current JDBC driver. It is a string value.
* **Version\_[Name]**The version of current JDBC driver. You can use connection.getMetaData().getDriverVersion() to obtain the value. The entire string must match completely.
* **setFetchSize\_[Name]**The number of rows retrieved in each buffer from the database. It is an Integer value that should be larger than 0 and less than or equal to getMaxRows(). The default value is different according to the driver in use. You can refer to your own database driver specification.
* **\_[Name]**It is a user-defined name used to mark a group of driver settings different from the other groups.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Where to Implement the Maximum Query Run Time and Number of Records

In the JdbcDriversConfig.properties file, you can also specify where the properties, Maximum Rows and Maximum Duration will be implemented, on Logi JReport side or on the database side. For details about usage of these two properties, see "Limiting the Query Run Time and Number of Records" in the Queries section of the *Logi JReport Designer User's Guide*.

The following is an example of setting the two properties:

|  |
| --- |
| ``` DriverName_D2 = Oracle JDBC driver Vendor_D2 = Oracle Version_D2 = 9.2.0.3.0 supportMaxRowPushDown_D2 = true supportMaxDurPushDown_D2 = true ``` |

* **DriverName\_[Name]**  
   Database driver name that should be used to establish a connection. You can use connection.getMetaData().getDriverName() to obtain the value.
* **Vendor\_[Name]**  
   The vendor of current JDBC driver. It is a string value.
* **Version\_[Name]**  
   The version of current JDBC driver. You can use connection.getMetaData().getDriverVersion() to obtain the value.
* **SupportMaxRowPushDown\_[Name]**  
   Specifies where the property Maximum Rows will be implemented, on Logi JReport side or on the database side. By default, it is set to true, which means the property will take effect on the database side. If it is set to false, the property will take effect on Logi JReport side.
* **SupportMaxDurPushDown\_[Name]**  
   Specifies where the property Maximum Duration will be implemented, on Logi JReport side or on the database side. By default, it is set to true, which means the property will take effect on the database side. If it is set to false, the property will take effect on Logi JReport side.
* **\_[Name]**  
   It is a user-defined name used to mark a group of driver settings different from the other groups.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Canceling Running Query

If your JDBC driver support the Cancel Running Query feature and you want Logi JReport to cancel the running query used by a report in the database when you cancel the running task of the report, for example, when you select the Cancel button on the report processing page of Page Report Studio, or when you choose to stop a report running in background mode, configure the file JdbcDriversConfig.properties as follows:

1. Add the JDBC driver you use into JdbcDriversConfig.properties if it is not listed there.
2. In the file JdbcDriversConfig.properties there is a line:

   `#supportCancelQueryStatement_D5=true`

   Remove the sign # and use your driver number instead of D5 to activate the feature.
3. Restart your Logi JReport Server, then the next time, when you choose to cancel a running task, the query used by the report will also be cancelled in the database, provided that the DBMS supports this action.

**Notes:**

* After you modified the JdbcDriversConfig.properties file, you need start the server to load the changes.
* The Version information must match 100% with the version returned by the JDBC Driver, if not a full match the settings will be ignored without warning.
* If there is more than one group with the same group marking name, the last group will be adopted.
* If the sign # is seen before "DriverName" of a group, or if setFetchSize is given a negative value, the whole group will be disabled.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644502-Initializing-the-Database-System-as-a-Non-admin-Database-User)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service)
