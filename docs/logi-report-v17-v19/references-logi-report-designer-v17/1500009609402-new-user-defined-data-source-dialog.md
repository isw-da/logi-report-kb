---
title: "New User Defined Data Source Dialog"
id: 1500009609402
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009609402-New-User-Defined-Data-Source-Dialog
updated_at: 2021-07-24T16:04:19Z
---

# New User Defined Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609362-New-Summary-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog)

# New User Defined Data Source Dialog

The New User Defined Data Source dialog helps you to [add a user data source object](https://devnet.logianalytics.com/hc/en-us/articles/1500009607002-Adding-User-Defined-Data-Sources-to-a-Catalog)  into a Logi Report catalog. It appears when you right-click a data source node and select New User Defined Data Source from its shortcut menu in the Catalog Manager.

![New User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916781207/nwuds.gif)

The following are details about options in the dialog:

**Name**

Specifies the name of the UDS. The name cannot be the same as any of the existing procedures, imported SQLs, HDSs, business views or queries. It also cannot be empty.

**Class Name**

Specifies the full name (including package name) of the class represented by the UDS. The jar file containing the class should be appended to the ADDCLASSPATH variable in the setenv.bat/setenv.sh file in the `<install_root>/bin` folder in both Logi Report Designer and Logi Report Server.

**The class implements**

After filling in the Class Name field, the classname of the interface that the class implements will be displayed here. If the class does not implement jet.datasource.JRUserDataSource you will receive an error message.

**Parameter**

Specifies the parameter for the UDS. The PARAMETER string must match the format defined in the [UDS class](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API#ParamString). You can reference parameters and constant level formulas predefined in the current catalog data source and the special field User Name in the string. By default the UDS will use the same database as the jdbc connection information used in the current data source. If your UDS includes the database information such as URL and Driver you can use the parameter to override the default data source.

**Edit Format**

Opens the Edit Format dialog to specify the value formats of the referenced parameters and formulas.

* **Name**  
   Displays names of the parameters and formulas.
* **Format**  
   Specifies the value formats of the parameters and formulas.
* **OK**  
   Accepts changes and closes the dialog.
* **Cancel**  
   Does not retain changes and closes the dialog.

**Specify Columns**

Specifies the column definitions. If you don't specify the column definitions, Logi Report will retrieve them from result set. When you select OK to add the UDS, Logi Report will run the UDS with the default parameters and use the returned data to determine the datatypes of the columns. If you are using formulas to provide the parameters you need to put temporary values into the formulas since Logi Report will not prompt you for the parameters when you add the UDS.

* **Name**  
   Specifies the valid name of the column. The name of the column should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
* **SQLType**  
   Specifies the data type of the column. The following types are supported:
  + **String**  
     The corresponding JDBC type is VARCHAR or LONGVARCHAR.
  + **java.math.BigDecimal**  
     The corresponding JDBC type is NUMERIC.
  + **boolean**  
     The corresponding JDBC type is BIT.
  + **byte**  
     The corresponding JDBC type is TINYINT.
  + **short**  
     The corresponding JDBC type is SMALLINT.
  + **int**  
     The corresponding JDBC type is INTEGER.
  + **long**  
     The corresponding JDBC type is BIGINT.
  + **float**  
     The corresponding JDBC type is REAL.
  + **double**  
     The corresponding JDBC type is DOUBLE.
  + **java.io.InputStream**  
     The corresponding JDBC type is VARBINARY or LONGVARBINARY.
  + **java.sql.Date**  
     The corresponding JDBC type is DATE.
  + **java.sql.Time**  
     The corresponding JDBC type is TIME.
  + **java.sql.Timestamp**  
     The corresponding JDBC type is TIMESTAMP.
* **Precision, Length, Scale, Radix**  
   Specifies the default value for each SQL type. You can select the cell to modify the value. The most common error is the scale may be 0 based on the returned data but you want it to be 2 for an amount.
* **Nullable**  
   Specifies whether the value of the column can be null. X stands for No Nulls, √ stands for Nullable and ? stands for Nullable Unknown.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a default row in the column definitions. If there is no row selected, an empty row will be added to the last line.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected row.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected column one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected column one step down.

**OK**

Adds the UDS and closes the dialog. If there is any error the UDS will not be added and it will return to this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609362-New-Summary-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632741-New-View-Element-Dialog)
