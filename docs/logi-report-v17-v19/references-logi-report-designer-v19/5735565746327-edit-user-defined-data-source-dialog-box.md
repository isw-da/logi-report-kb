---
title: "Edit User Defined Data Source Dialog Box"
id: 5735565746327
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735565746327-Edit-User-Defined-Data-Source-Dialog-Box
updated_at: 2022-11-02T04:35:22Z
---

# Edit User Defined Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529231895-Edit-Summary-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735500519447-Edit-User-Dialog-Box)

# Edit User Defined Data Source Dialog Box

You can use the Edit User Defined Data Source dialog box to [edit a UDS](https://devnet.logianalytics.com/hc/en-us/articles/5735499573911-Adding-User-Defined-Data-Sources-to-a-Catalog) that you have added to a catalog. This topic describes the options in the dialog box.

Designer displays the Edit User Defined Data Source dialog box when you right-click a user data source and select Edit User Defined Data Source from the shortcut menu in the Catalog Manager.

![Edit User Defined Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898481627799/edtuds.gif)

Designer displays these options:

**Name**

This option shows the name of the UDS.

**Class Name**

Specify the full name (including package name) of the class represented by the UDS. You should append the JAR file containing the class to the ADDCLASSPATH variable of setenv.bat/setenv.sh in the `<install_root>/bin` folder of both Designer and Server.

**The class implements**

After you fill in the Class Name text box, Designer displays the class name of the interface that the class implements here.

**Parameter**

Specify the parameter string for the UDS.

**Edit Format**

Select to open the Edit Parameter Format dialog box to edit the parameter format.

* **Name**  
  This column shows the names of the parameters used in the user data source.
* **Format**  
  This column shows the formats that you specify for the parameters used in the user data source.
* **OK**  
  Select to apply your settings and close the dialog box.
* **Cancel**  
  Select to close the dialog without saving any changes.

**Specify Columns**

Select to specify the column definitions. If you do not specify the column definitions, Designer retrieves them from the result set.

* **Name**  
  This column shows the names of the columns. The name of a column should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
* **SQLType**  
  This column shows the data types that you select for the columns. You can use the following types:
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
  This column shows the default values that you specify for each SQL type. You can select the cell to modify the value.
* **Nullable**  
  This column shows whether the values of the columns can be null. "X" stands for NoNulls, "√" stands for Nullable, and "?" stands for Nullable Unknown.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a default row in the column definitions. If you do not select any row, Designer adds an empty row to the last line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified row.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified row higher in the box.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified row lower in the box.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529231895-Edit-Summary-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735500519447-Edit-User-Dialog-Box)
