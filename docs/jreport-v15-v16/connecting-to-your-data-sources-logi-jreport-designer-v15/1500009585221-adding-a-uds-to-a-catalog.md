---
title: "Adding a UDS to a Catalog"
id: 1500009585221
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585221-Adding-a-UDS-to-a-Catalog
updated_at: 2021-07-24T05:55:45Z
---

# Adding a UDS to a Catalog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585281-User-Data-Source-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585241-Example-1-Adding-a-Flat-File-UDS)

# Adding a UDS to a Catalog

Logi JReport Designer can access data from an external user defined data source, such as a text file, or Excel file, which is not stored in a database, or when there is no JDBC driver available.

To add a UDS to a Logi JReport catalog, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog), then in the Catalog Manager, right-click the node of a data source and choose **New User Defined Data Source** from the shortcut menu.

   If you want to add the UDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **User Defined** connection type and select **OK**.

   The [New User Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009566862-New-User-Defined-Data-Source-Dialog) dialog appears.

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889327639/nwuds.gif)
2. In the Name field, specify a name for the UDS as required.
3. Provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you enter must exist and can be found by Logi JReport Designer, which means the class should be in the class path of the system environment or set in ADDCLASSPATH of setenv.bat/setenv.sh. After filling in this field, the class name of the interface that the class implements will be displayed automatically behind The class implements:.
4. Specify the parameter for the UDS in the Parameter box. The PARAMETER string must match the format defined in the [UDS class](https://devnet.logianalytics.com/hc/en-us/articles/1500009585281-User-Data-Source-API#ParamString). You can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) predefined in the current catalog data source and the special field User Name in the PARAMETER string in the format "@fieldname". For example, if the PARAMETER string of a UDS is `SQL=select * from employee`, and you want to use the predefined parameter *sql* to replace the part after "=", then the PARAMETER string will be `SQL=@sql`. If the special field User Name is used, to specify the user name, select **Options** on the Catalog Manager toolbar, in the General category of the Options dialog, set the User Name option.
5. When parameters and formulas are referenced in the PARAMETER string, you can select the **Edit Format** button to edit the format of their values.
6. Check the **Specify Columns** option to enable the column definitions list and add column definitions. If you don't specify the column definitions, Logi JReport will get them from the result set automatically.
   * **Name**  
     The name of a column. It should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
   * **SQLType**  
      The data type of the column.
   * **Precision**, **Length**, **Scale**, **Radix**  
     The default value for each SQL type. Select the cell and modify the value if necessary.
   * **Nullable**  
     Indicates whether the value of the column can be null. X stands for NoNulls, √ stands for Nullable and ? stands for Nullable Unknown.
7. Select **OK** to add the UDS.

The following examples show how to add some specific UDS to a catalog:

> * [Example 1: Adding a Flat File UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009585241-Example-1-Adding-a-Flat-File-UDS)
> * [Example 2: Adding an SQL Data Source UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS)
> * [Example 3: Adding a Java Object Data Source UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009585261-Example-3-Adding-a-Java-Object-Data-Source-UDS)
> * [Example 4: Adding a Dynamic UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009564262-Example-4-Adding-a-Dynamic-UDS)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585281-User-Data-Source-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585241-Example-1-Adding-a-Flat-File-UDS)
