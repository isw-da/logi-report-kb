---
title: "Example 3: Functions Defined Outside of a Package"
id: 1500009585341
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585341-Example-3-Functions-Defined-Outside-of-a-Package
updated_at: 2021-07-24T05:55:43Z
---

# Example 3: Functions Defined Outside of a Package

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585321-Example-2-Stored-Procedures-Declared-and-Defined-in-a-Package-and-Package-Body)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564322-Example-4-Functions-Declared-and-Defined-in-a-Package-and-Package-Body)

# Example 3: Functions Defined Outside of a Package

This topic provides an example of a function defined outside of a package.

Suppose that an Oracle stored procedure is defined as:

|  |
| --- |
| ``` CREATE OR REPLACE PACKAGE SHDEMO AS type curtype is ref cursor; end SHDEMO; CREATE OR REPLACE FUNCTION "SCOTT"."DEPTQUERY"(p_dname in varchar2) return SHDEMO.curtype is lcur SHDEMO.curtype; begin   open lcur for   select * from dept where dname = p_dname;   return lcur; end DEPTQUERY; ``` |

To add the stored procedure into a Logi JReport catalog, follow the steps below:

1. Start Logi JReport Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source to which the stored procedure is to be added, then select **New User Defined Data Source**. The New User Defined Data Source dialog appears.
3. In the Name field, specify a name for the UDS, for example, UDS1.
4. In the Class Name field, input the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, enter one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&PARAMVALUE=@p_dname`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&INPARAMVALUE=@p_dname,varchar,1`
   * `OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&PARAMVALUE=@p_dname`
   * `OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&INPARAMVALUE=@p_dname,varchar,1`

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893964183/cnctn_uds_orcl_eg3.gif)
6. Select the **OK** button. The UDS class will then be added into the catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585321-Example-2-Stored-Procedures-Declared-and-Defined-in-a-Package-and-Package-Body)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564322-Example-4-Functions-Declared-and-Defined-in-a-Package-and-Package-Body)
