---
title: "Setting Up the JDBC Driver"
id: 1500009584801
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver
updated_at: 2021-07-24T05:55:50Z
---

# Setting Up the JDBC Driver

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection)

# Setting Up the JDBC Driver

Logi JReport supports all of the current mainstream databases as well as most databases which support JDBC drivers. For more information, refer to [Supported Report Databases](https://devnet.logianalytics.com/hc/en-us/articles/1500009568422-Supported-Report-Databases).

Below is a list of the sections covered in this topic:

> * [Limiting the Size of the Fetch Data Buffer](#Limit)
> * [Specifying Where to Implement the Maximum Query Runtime and Number of Records](#Property)

**To connect to a database via a JDBC driver:**

1. Install the JDBC driver according to the instructions provided by the JDBC driver supplier.
2. Edit setenv.bat for Windows or setenv.sh for Unix in `<designer_install_root>\bin`, by appending the class path for the JDBC driver.

**Note:** The step for appending the class path is very important. The same changes made to Logi JReport Designer’s class path must be made to the class path for Logi JReport Server too. A missing JDBC driver in the Logi JReport start-up batch file or command line will result in a "ClassNotFoundError message" when you try to run a report. Meanwhile, if you want to use the Preview as Page/Web Report Result feature in Logi JReport Designer, you also need to append the class path for the JDBC driver to setenv.bat/setenv.sh in `<designer_install_root>\server\bin.`

The following are two examples of setting up the JDBC driver.

**Example 1: Installing a MySQL JDBC driver**

1. Install MySQL JDBC driver mysql-connector-java-5.0.4-bin.jar.
2. Modify setenv.bat by appending the archive file path and file name of the driver to the set ADDCLASSPATH system variable:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;c:\classes\mysql-connector-java-5.0.4-bin.jar;`

**Example 2: Installing an Oracle JDBC driver**

1. Install Oracle JDBC driver ojdbc7.jar.
2. Modify setenv.bat by appending the archive file path and file name of the driver to the set ADDCLASSPATH system variable:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;c:\oracle\lib\ojdbc7.jar;`

## Limiting the Size of the Fetch Data Buffer

If you are using a database which supports the JDBC method Statement.setFetchSize(), you can request the database to retrieve a specified number of rows in each read instead of all rows which minimizes memory usage. This can improve performance. It can also avoid Java heap out of memory errors when doing large queries. Logi JReport provides a property setFetchSize in the JdbcDriversConfig.properties file for you to do this, which is located in the `<install_root>\bin` directory.

The following is an example of setting the setFetchSize property in the JdbcDriversConfig.properties file and detailed description of each property:

|  |
| --- |
| ``` DriverName_D1 = MySQL-AB JDBC Driver Vendor_D1 = MySql.com Version_D1 = 3.0.8-stable ($Date: 2003/05/19 00:57:19 $, $Revision: 1.27.2.18 $) setFetchSize_D1 = 5000 ``` |

* **DriverName\_[Name]**  
   Database driver name that should be used to establish a connection. You can use connection.getMetaData().getDriverName() to obtain the value.
* **Vendor\_[Name]**  
   The vendor of current JDBC driver. It is a string value.
* **Version\_[Name]**  
   The version of current JDBC driver. You can use connection.getMetaData().getDriverVersion() to obtain the value. The entire string must match exactly.
* **setFetchSize\_[Name]**  
   The number of rows retrieved in each buffer from the database. It is an Integer value that should be larger than 0 and less than or equal to getMaxRows(). The default value is different according to the driver in use. You can refer to your own database driver specification.
* **\_[Name]**  
   It is a user-defined name used to mark a group of driver settings different from the other groups.

## Specifying Where to Implement the Maximum Query Runtime and Number of Records

In the JdbcDriversConfig.properties file, you can also specify where the properties, Maximum Rows and Maximum Duration, will be implemented, on Logi JReport side or on the database side. For details about usage of these two properties, see [Limiting the query run time and number of records](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager#Limit).

The following is an example of setting the two properties:

|  |
| --- |
| ``` DriverName_D2 = Oracle JDBC driver Vendor_D2 = Oracle Version_D2 = 9.2.0.3.0  supportMaxRowPushDown_D2 = true supportMaxDurPushDown_D2 = true ``` |

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

**Notes:**

* If there are more than one group with the same group marking name, the last group will be adopted.
* If the sign # is seen before "DriverName" of a group, or if setFetchSize is given a negative value, the whole group will be disabled.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection)
