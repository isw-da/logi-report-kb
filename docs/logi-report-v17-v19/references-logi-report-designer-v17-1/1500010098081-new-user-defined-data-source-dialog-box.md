---
title: "New User Defined Data Source Dialog Box"
id: 1500010098081
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098081-New-User-Defined-Data-Source-Dialog-Box
updated_at: 2021-07-23T19:15:47Z
---

# New User Defined Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box)

# New User Defined Data Source Dialog Box

You can use the New User Defined Data Source dialog box to [add a user data source object](https://devnet.logianalytics.com/hc/en-us/articles/1500010095321-Adding-User-Defined-Data-Sources-to-a-Catalog) in the current catalog. This topic describes the options in the dialog box.

Designer displays the New User Defined Data Source dialog box when you right-click a data source node and select New User Defined Data Source from the shortcut menu in the Catalog Manager.

![New User Defined Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856906647/nwuds.gif)

You see the following options in the dialog box:

**Name**

Specify the name of the UDS. The name cannot be the same as any of the existing stored procedures, imported SQLs, HDSs, business views, or queries. It cannot be empty either.

**Class Name**

Specify the full name (including package name) of the class represented by the UDS. You should append the jar file containing the class to the ADDCLASSPATH variable in the setenv.bat/setenv.sh file in the `<install_root>/bin` folder of both Designer and Server.

**The class implements**

After you fill in the Class Name text box, Designer displays the class name of the interface that the class implements here.

**Parameter**

Specify the parameter string for the UDS.

**Edit Format**

Select to open the Edit Parameter Format dialog box to edit the parameter format.

* **Name**  
  The column shows the names of the parameters used in the user data source.
* **Format**  
  The column shows the formats that you specify for the parameters used in the user data source.
* **OK**  
  Select to accept the changes and close the dialog box.
* **Cancel**  
  Select to close the dialog without saving any changes.

**Specify Columns**

Select to specify the column definitions. If you don't specify the column definitions, Logi Report Engine retrieves them from the result set.

* **Name**  
  The column shows the names of the columns. The name of a column should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
* **SQLType**  
  The column shows the data types that you select for the columns. You can use the following types:
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
* **Precision**/**Length**/**Scale**/**Radix**  
  The column shows the default values that you specify for each SQL type. You can select the cell to modify the value.
* **Nullable**  
  The column shows whether the values of the columns can be null. "X" stands for NoNulls, "√" stands for Nullable, and "?" stands for Nullable Unknown.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a default row in the column definitions. If you do not select any row, Designer adds an empty row to the last line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified row.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified row higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified row lower in the list.

**OK**

Select to add the UDS to the catalog and close the dialog box. You cannot add the UDS if there is any error.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box)
