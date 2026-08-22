---
title: "Making High-Efficiency Reports"
id: 5735547328663
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735547328663-Making-High-Efficiency-Reports
updated_at: 2022-11-02T08:23:49Z
---

# Making High-Efficiency Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534254999-Managing-Page-Reports)

# Making High-Efficiency Reports

This topic introduces the settings you can specify in Designer in order to make your reports more efficient, reliable, and fast at runtime.

You can use the following methods to improve the efficiency, reliability, and running speed of your reports.

* Suppress all unused panels in a banded object, such as Group Header and Footer panels which are not adding values to a report.

  To do this, select the panel, then in the Report Inspector, set its **Suppress** property to **true**. When you right-click in the panel and select **Hide** on the shortcut menu, Designer also sets Suppress to "true" automatically.
* Set the precision (length) of DBFields or record level formulas to the size of the maximum value you need to display in a report. Making them larger than necessary wastes resources.

  To do this, in the Catalog Manager, select **Show Properties** on the toolbar to expand the Properties sheet, then select the DBField or record level formula and set its **Precision** property to an appropriate value.
* Set the data buffer size to a larger value.

  By default, the size of one data buffer is 2MB. When data exceeds the default size, Logi Report Engine writes it to disk, which slows down data processing. You can set the data buffer size by specifying two properties of a dataset or subreport in the Report Inspector: **Max Page Number** and **Records per Page**. For more information, see [Data Buffer](https://devnet.logianalytics.com/hc/en-us/articles/5735517112983-Dataset-Properties#DataBuffer).
* Adjust the result buffer size.

  The result buffer is used to store report in pages. Its default size is 4, which indicates Logi Report Engine allocates four pages of a report to the result buffer, and stores other pages on disk. If you have enough memory, to get better performance, you can increase the result buffer size to store more pages of a report.

  To adjust the result buffer size, in the Report Inspector, highlight the node which represents the page report tab or web report, and then change the value of the **Result Buffer Size** property to the number of pages you want to hold in memory.
* Adjust the Excel buffer size for exporting to Excel.

  The Excel buffer is used to store report in the Excel buffer sheets when you export page report tabs to Excel. Its default size is 1, meaning, Logi Report Engine allocates one sheet of a report to the result buffer, and stores other sheets on disk. If you have enough memory, you can increase the Excel buffer size to store more sheets of the Excel output in memory by setting the **Excel Buffer Size** property of page report tabs in the Report Inspector.
* Arrange the object coordinates for exporting to a columned file.

  Normally, when you export a report to a columned file, such as Excel and CSV, Logi Report Engine calculates the coordinates of the report objects, which can require a great deal of processing time. You can predefine the coordinates of the report objects to save the extra position calculating time (you should set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Columned) property to "true" for the report tab or web report in order for the customized coordinates to take effect).
* When running a page report tab to the delimited format such as CSV on Server, the property Fast Pass can help you speed up the generation process. Setting Fast Pass to "true" enables you to specify the position of the object you want to display in the output, thus Logi Report Engine does not need to calculate the position for every object during the generation process.
  For more information, see [Improving the Performance of Running a Page Report to Delimited Format on Server](https://devnet.logianalytics.com/hc/en-us/articles/5735525405719-Exporting-a-Report-to-Text#Performance).
* Set the Cache Section property.

  You can set the **Cache Section** property for the detail panel in a banded object to "true" in the Report Inspector to cache the objects in the panel instead of creating them repeatedly, which is helpful in improving the performance.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/7933685587863/noteicon.jpg) The Cache Section property doesn't work if there is crosstab, text object, chart, and so on in the detail panel of the banded object, because these objects may contain child DBFields.
* Set the Cache Value property (only for DBFields).

  To get better performance, you can set the **Cache Value** property for DBFields to "true" in the Report Inspector, which caches the layout attributes (font size, font face, width, and so on) when you export the report to any format.
* Set the [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/5735516614679-JDBC-Hive-Connection-Properties#PushDown) property.

  The Push Down Group Query property controls whether to push down group level summary computations in reports to the database at runtime. By pushing down the computations, you can benefit from the database's computation capabilities, and thus improve the running efficiency of your reports.
* Limit the size of the fetch data buffer.

  If you create your reports on queries that use data from a relational database which supports the JDBC method *Statement.setFetchSize()*, you can request the database to retrieve a specified number of rows in each read instead of all rows by setting the **setFetchSize** property in the file **JdbcDriversConfig.properties** that is saved in the `<designer_install_root>\bin` directory. This can minimize memory usage and improve performance, and also avoid Java heap out of memory errors when executing large queries.

  The following is an example of setting the setFetchSize property in JdbcDriversConfig.properties and detailed description of each property in the file.

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
    It is a user-defined name used to mark a group of driver settings different from the other groups.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534254999-Managing-Page-Reports)
