---
title: "Making High-Efficiency Reports"
id: 1500009636141
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009636141-Making-High-Efficiency-Reports
updated_at: 2021-07-24T16:03:22Z
---

# Making High-Efficiency Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613342-Managing-Page-Reports)

# Making High-Efficiency Reports

This topic introduces how to make reports efficient, reliable, and fast at runtime.

The following ways are provided for you to make reports efficient, reliable, and fast at runtime.

* Suppress all unused panels in a banded object, such as Group Header and Footer panels which are not adding values to a report.

  To do this, select the panel, go to the Report Inspector, and then change the property Suppress to true. When you right-click in the panel and select Hide it also sets Suppress to true.
* Set the precision (length) of DBFields or record level formulas to the size of the maximum value you need to display in a report. Making them larger than necessary wastes resources.

  **To do this:**

  1. Go to the Catalog Manager, select **Show Properties**  on the toolbar to expand the Properties sheet.
  2. Select the DBField or record level formula, then change the Precision property to an appropriate value.
* Set the data buffer size to a larger value.

  By default, the size of data buffer is 2MB. When data exceeds the default size, data will be written to disk, which will slow down the report processing. Logi Report Designer enables you to set data buffer size by specifying two properties of a dataset or subreport in the Report Inspector: Records per Page and Max Page Number. For details, see [Data Buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009612242-Dataset-Properties#DataBuffer).
* Adjust result buffer size.

  The result buffer is used to store the report result in pages. Its default size is 4 which indicates 4 pages of the report result are allocated to the result buffer, other pages will be stored on disk. If you have enough memory, to get better performance, you can increase the result buffer size to store more pages of report result.

  To adjust the result buffer size, in the Report Inspector, highlight the node which represents the page report tab or web report, and then change the value of Result Buffer Size to the number of pages you want to hold in memory.
* Adjust Excel buffer size for exporting to Excel.

  The Excel buffer is used to store the report result in excel buffer sheets when exporting page report tabs to Excel format. Its default size is 1, which indicates 1 sheet of the report result are allocated to the result buffer; other sheets will be stored on disk. If you have enough memory, you can increase the Excel buffer size to store more sheets of Excel format report result in memory by setting the Excel Buffer Size property of page report tabs in the Report Inspector.
* Arrange object coordinates for exporting to Excel.

  Normally, when a report is being exported to an Excel file, the coordinates of the report objects are calculated by Logi Report Engine, and can require a great deal of processing time. However you can predefine the coordinates of the report objects by setting the Column Index and Row Index properties for each object so that the extra position calculating time can be saved.
* When running a page report tab to the Delimited Format (such as the CSV format) on Logi Report Server, the property Fast Pass can help you speed up the generation process. Setting Fast Pass to true will enable you to specify the position of the object you want to display in the result file, thus Logi Report will not calculate the position for every object during the generation process.

  **To use this method:**

  1. In the Report Inspector, select the node that represents the page report tab and set the properties Fast Pass and Columned to **true**.
  2. For each DBField or label in the page report tab, set the exact coordinate using the properties Column Index and Row Index.

     For example, set the properties Column Index=0 and Row Index=2 for a DBField, Logi Report Designer will put this DBField into the first column and the third row in the generated Text file.
  3. Set the property **engine.single\_thread=false** in the file server.propertise in `<server_install_root>\bin`. This enables the property Fast Pass to take effect when running the report to the Delimited Format.
* Cache Section.

  The Cache Section property is used to cache the objects in the detail panel of a banded object instead of creating them repeatedly. You can set Cache Section in the Report Inspector to true to improve the performance.

  **Note:** Cache Section doesn't work if there is crosstab, text object, chart, and so on in the detail panel of the banded object, because these objects contain child-DBFields.
* Cache Value (only for DBFields).

  The Cache Value property is used to cache the layout attributes (font size, font face, width, and so on) of DBFields when exporting the report to any format. To get better performance, set it to true in the Report Inspector.
* [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009634701-JDBC-Hive-Connection-Properties#PushDown).

  The Push Down Group Query property controls whether to push down group level summary computations in reports to the DBMS at runtime. By pushing down the computations, the DBMS' computation capability can be made use of, and thus the reports' running efficiency will be improved.
* Limit the size of the fetch data buffer.

  If your reports are created on queries that use data from a relational database which supports the JDBC method *Statement.setFetchSize(*), you can request the database to retrieve a specified number of rows in each read instead of all rows by setting the property setFetchSize in the JdbcDriversConfig.properties file saved in the `<install_root>\bin` directory. This can minimize memory usage and improve performance, and also avoid Java heap out of memory errors when doing large queries.

  The following is an example of setting the setFetchSize property in the JdbcDriversConfig.properties file and detailed description of each property:

  `DriverName_D1 = MySQL-AB JDBC Driver  
  Vendor_D1 = MySql.com  
  Version_D1 = 3.0.8-stable ($Date: 2003/05/19 00:57:19 $, $Revision: 1.27.2.18 $)  
  setFetchSize_D1 = 5000`

  + **DriverName\_[Name]**  
     Database driver name that should be used to establish a connection. You can use *connection.getMetaData().getDriverName()* to obtain the value.
  + **Vendor\_[Name]**  
     The vendor of current JDBC driver. It is a string value.
  + **Version\_[Name]**  
     The version of current JDBC driver. You can use *connection.getMetaData().getDriverVersion()* to obtain the value. The entire string must match exactly.
  + **setFetchSize\_[Name]**  
     The number of rows retrieved in each buffer from the database. It is an Integer value that should be larger than 0 and less than or equal to *getMaxRows()*. The default value is different according to the driver in use. You can refer to your own database driver specification.
  + **\_[Name]**  
     It is a user defined name used to mark a group of driver settings different from the other groups.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613342-Managing-Page-Reports)
