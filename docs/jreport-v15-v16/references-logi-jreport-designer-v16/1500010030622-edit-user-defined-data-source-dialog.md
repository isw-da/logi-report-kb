---
title: "Edit User Defined Data Source Dialog"
id: 1500010030622
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030622-Edit-User-Defined-Data-Source-Dialog
updated_at: 2021-07-24T10:38:56Z
---

# Edit User Defined Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030602-Edit-Summary-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065761-Edit-User-Dialog)

# Edit User Defined Data Source Dialog

The Edit User Defined Data Source dialog helps you to [edit a UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010064501-Adding-User-Defined-Data-Sources-to-a-Catalog) that you have added to a catalog. It appears when you right-click a user data source and select Edit User Defined Data Source from the shortcut menu in the Catalog Manager.

![Edit User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901266071/edtuds.gif)

The following are details about options in the dialog:

**Name**

Specifies the name of the UDS. The name cannot be the same as any of the existing procedures, SQL files, HDSs, business views or queries. It also cannot be empty.

**Class Name**

Specifies the full name (including package name) of the class represented by the UDS. The jar file containing the class should be appended to the ADDCLASSPATH variable in the setenv.bat/setenv.sh file in the `<install_root>/bin` folder in both Logi JReport Designer and Logi JReport Server.

**The class implements**

After filling in the Class Name field, the class name of the interface that the class implements will be displayed here.

**Parameter**

Specifies the parameter string for the UDS. The parameter string must match the format defined in the UDS class. You can use parameters predefined in a Logi JReport catalog in the parameter string, and the format used in the string is "@" + parameter name. For example, if the parameter string of a UDS is SQL=select \* from employee, and you want to use the parameter sql in a catalog to replace the part after "=" in the string, then the parameter string of the UDS will be SQL=@sql.

**Edit Format**

Opens the Edit Parameter Format dialog to edit the parameter format:

* **Name**  
   Displays names of parameters used in the user data source.
* **Format**  
   Specifies formats for parameters as required.
* **OK**  
   Accepts changes and closes the dialog.
* **Cancel**  
   Does not retain changes and closes the dialog.

**Specify Columns**

Specifies the column definitions. If you don't specify the column definitions, Logi JReport will retrieve them from result set.

* **Name**  
   Specifies the name of a column. The name of the column should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
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
   The default value for each SQL type will be displayed. Select the cell to modify the value if necessary.
* **Nullable**  
   Specifies whether the value of the column can be null. X stands for NoNulls, √ stands for Nullable and ? stands for Nullable Unknown.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a default row in the column definitions. If there is no row selected, an empty row will be added to the last line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected row. .

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected column one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected column one step down.

**OK**

Adds the UDS into a Logi JReport catalog.

**Cancel**

Does not retain any changes and closes this dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030602-Edit-Summary-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065761-Edit-User-Dialog)
