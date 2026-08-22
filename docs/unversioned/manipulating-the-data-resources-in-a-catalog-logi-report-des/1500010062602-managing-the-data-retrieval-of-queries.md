---
title: "Managing the Data Retrieval of Queries"
id: 1500010062602
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries
updated_at: 2021-07-23T19:16:46Z
---

# Managing the Data Retrieval of Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062622-Applying-the-Filter-of-a-Query-to-Multiple-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results)

# Managing the Data Retrieval of Queries

The Data Manager in Designer enables you to control the data retrieval of your queries (and also [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures), and [user-defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources) that function similarly as queries), including the number of rows to display and the duration allowed for retrieval. It can also keep access information from previous runs of a query. This topic describes how you can use the Data Manager to limit the run time and number of records of queries, as well as view the running histories of queries.

This topic contains the following sections:

* [Limiting the Query Run Time and Number of Records](#Limit)
* [Viewing a Query's Running History](#View)
  + [Viewing the Designer-Side Run History Information of a Query](#Designer)
  + [Viewing the Server-Side Run History Information of a Query](#Server)

## Limiting the Query Run Time and Number of Records

There may be many records in a table on which you are to build a report. After you have generated the query and designed the rough report, you may only want to preview several lines of records for testing, in which case, you can take advantage of the two properties - Maximum Rows and Maximum Duration, which enable you to limit the run time and number of records, saving time and resources.

The following example explains the usage of the two properties based on the page report Payroll Report.cls:

1. Select **File** > **Open** to open the page report **Payroll Report.cls** in the catalog **SampleReports.cat** saved in `<designer_install_root>\Demo\Reports\SampleReports`.
2. Adjust the **Maximum Rows** and **Maximum Duration** properties of the query **Payroll** the report uses to suitable levels. You can adjust the values in either of the following ways:
   * In the Catalog Manager, right-click the query and select **Properties** from the shortcut menu. In the Properties sheet, change the property values as required, then press **Enter** on your keyboard to apply the change.
   * In the Data panel, right-click the query and select **Properties** on the shortcut menu. In the Properties dialog box, edit the property values as required and then press **Enter** to confirm.

   Here, modify the value of Maximum Rows to **10** and change the value of Maximum Duration to **1** second. This specifies the maximum elapsed time to be one second, and that within this duration no more than ten records are fetched.
3. Select the **View** tab to preview the report. Designer fetches only ten rows within one second for the report.

If your queries use data from a relational database, you can further customize where to implement the two properties: on Logi Report side or on the database side by configuring the file **JdbcDriversConfig.properties**, which is available in both Designer and Server in its `<install_root>\bin` directory.

The following is an example of setting the two properties:

`DriverName_D2 = Oracle JDBC driver  
Vendor_D2 = Oracle  
Version_D2 = 9.2.0.3.0  
supportMaxRowPushDown_D2 = true  
supportMaxDurPushDown_D2 = true`

* **DriverName\_[Name]**  
  The name of the database driver used to establish a connection. You can use *connection.getMetaData().getDriverName()* to obtain the value.
* **Vendor\_[Name]**  
  The vendor of current JDBC driver. It is a string value.
* **Version\_[Name]**  
  The version of the current JDBC driver. You can use *connection.getMetaData().getDriverVersion()* to obtain the value.
* **SupportMaxRowPushDown\_[Name]**  
  You can use this property to specify where to implement the property Maximum Rows: on Logi Report side or on the database side. By default, it is " true", which means the property takes effect on the database side. If you set it to "false", the property takes effect on Logi Report side.
* **SupportMaxDurPushDown\_[Name]**  
  You can use this property to specify where to implement the property Maximum Duration: on Logi Report side or on the database side. By default, it is "true", which means the property takes effect on the database side. If you set it to "false", the property takes effect on Logi Report side.
* **\_[Name]**  
  It is a user-defined name used to mark a group of driver settings different from the other groups.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* If the value of the Maximum Rows/Maximum Duration property is 0 or a negative number, it means the number is unlimited.
* If the number you specify for Maximum Rows/Maximum Duration is equal to or more than that required for running all the records in your report, Logi Report Engine retrieves all of the records.
* It is not recommended to specify both of the properties at the same time. Sometimes the time information for large-data reports may not be very accurate. For example, if you specify 5 seconds, you may find that it takes 7 seconds, since this time also includes the time for writing the history information to a file.
* Select the Refetch Data button ![Refetch Data button](https://devnet.logianalytics.com/hc/article_attachments/4404848385303/btn_refetchdt.gif) on the toolbar of the View tab to run the report again if you find that the specified properties do not take effect.
* These two properties apply to the specified query, not the report. For a report with a subreport, specifying the properties for a query used by the primary report does not have any effect on the subreport's query, and vice versa. For example, Report A.cls uses query Q1, and Report B.cls uses query Q2. B.cls is the subreport of A.cls. Maximum Rows for Q1 is to 3. The primary report only fetches three records, whereas Q2 for subreport B.cls is not affected. To limit the subreport records, you have to restrict Q2.
* In JdbcDriversConfig.properties:
  + If there are more than one group with the same group marking name, Logi Report Engine applies the last group.
  + If Logi Report Engine encounters the "#" symbol before "DriverName" of a group, or if you specify a negative value for setFetchSize, Logi Report Engine disables the whole group.

## Viewing a Query's Running History

An important function of the Data Manager is to keep track of the run information of queries. By default, Designer does not record the information and show it in the Data Manager in order to improve performance. If you want to show the history information, you need to first add the command line `alwaysShowDMRecord=true` in the file report.ini in `<designer_install_root>\bin`, and then specify the Maximum Duration and Maximum Rows properties of the queries in Designer. Then, Designer records the history information in a file in `<install_root>\dm`. In this folder, Designer generates a sub folder for each catalog. For example, if you run the Logi Report sample report, Designer creates a folder "SampleReports" in `<install_root>\dm`. In addition, Designer creates a file with a .dmt extension corresponding to the query in the sub folder to store the run history information.

To change the Data Manager information output location (the default is `<install_root>\dm`), edit report.ini in `<install_root>\bin`. Change the location in the argument `dmPath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\dm` to the location where you would like the information to go to. For instance, `dmPath=C\:\\temp\\dm`. Make sure that the folder you specify in the report.ini argument already exists.

### Viewing the Designer-Side Run History Information of a Query

1. Open the file **report.ini** in `<designer_install_root>\bin` and add the command line **`alwaysShowDMRecord=true`** as follows. Here, it is assumed that you have installed Designer to `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer`. The escape character backslash following "=" and before each special character such as ":" and "\" are required.

   ```
   #paths  
   #Wed Jan 04 15:55:43 CST 2017  
   dmPath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\dm  
   helpPath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\help  
   templatePath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\template  
   tempPath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\temp  
   stylePath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\style  
   gisinfoPath=C\:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\gisinfo  
   alwaysShowDMRecord=true
   ```
2. Start Designer and open a report.
3. [Adjust the Maximum Rows and Maximum Duration properties of the query](#Property) the report uses to suitable values.
4. Select the **View** tab to preview the report.
5. In the Catalog Manager or the Data panel, right-click the query the report uses and select **Data Manager** from the shortcut menu. Designer displays the [Data Manager dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096101-Data-Manager-Dialog-Box).

   ![Data Manager dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848429719/dtmngr.gif)

   The dialog box shows the running information of the query, including when the report is run - date and time, the running duration, the number of rows displayed, and the report that uses the query. You can sort the items by Date, Time, Number of Rows, Duration, or Report, by selecting the column title.

The following example demonstrates how to use the Data Manager with the sample report Payroll Report.cls. Here it is assumed that you have added the command line `alwaysShowDMRecord=true` to the file report.ini in `<designer_install_root>\bin`.

1. Open the page report **Payroll Report.cls** in the catalog **SampleReports.cat**. Do not preview the report.
2. Select **Home** >  **Catalog Manager**.
3. In the Catalog Manager, expand the **Data Source 1** > **Queries** node, locate the query **Payroll** then right-click it and select **Data Manager**. Designer displays the Data Manager dialog box without any history information, because you have not yet run the report.
4. Close the Data Manager dialog box, then specify Maximum Duration as **3** and Maximum Rows as **5** in the Properties sheet of the Catalog Manager for the Payroll query.
5. Select the **View** tab to preview the report.
6. Open the Data Manager dialog box again. You can now see the history of this first run of the query.
7. Use the query Payroll to [create another page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) report1.cls.
8. Preview report1.cls. Designer appends the run information as a record in the Data Manager dialog box.

### Viewing the Server-Side Run History Information of a Query

1. Open the **report.ini** file in `<server_install_root>\bin` and add the command line **`alwaysShowDMRecord=true`** to it.
2. [Publish a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely) that has its query properties Maximum Rows and/or Maximum Duration set together with its catalog to Server.
3. Run the report on Server. The Server Engine saves the query run information, but does not have a GUI to display it. In order to view the information, you need to use the Data Manager in Designer.
4. Start Designer. Make sure that you have pointed the *dmPath* argument in the file report.ini in `<designer_install_root>\bin` to the output location (containing the "dm" folder) of Server. In most cases, you need to use FTP or remote copy to copy the "dm" folder from the Server machine to the Designer machine.
5. In Designer, use the Data Manager to view the query's Server-side run history information.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062622-Applying-the-Filter-of-a-Query-to-Multiple-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results)
