---
title: "Example 4: Functions Declared and Defined in a Package and Package Body"
id: 1500009564322
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564322-Example-4-Functions-Declared-and-Defined-in-a-Package-and-Package-Body
updated_at: 2021-07-24T05:55:42Z
---

# Example 4: Functions Declared and Defined in a Package and Package Body

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585341-Example-3-Functions-Defined-Outside-of-a-Package)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564282-EnterpriseDB-Stored-Procedure-UDS)

# Example 4: Functions Declared and Defined in a Package and Package Body

This topic provides an example of a function declared and defined in a package and package body.

Suppose that an Oracle stored procedure is defined as:

|  |
| --- |
| ``` CREATE OR REPLACE PACKAGE "SCOTT"."SHDEMO_PKG" AS type curtype is ref cursor; Procedure empquery_proc (p_job in varchar2, cur OUT SHDEMO_PKG.curtype); Function deptquery_func (p_dname in varchar2) return SHDEMO_PKG.curtype; end SHDEMO_PKG; CREATE OR REPLACE PACKAGE BODY "SCOTT"."SHDEMO_PKG" AS Procedure empquery_proc (p_job in varchar2, cur OUT SHDEMO_PKG.curtype) as lcur SHDEMO_PKG.curtype; begin   open lcur for   select * from EMP WHERE JOB = p_job;   cur:=lcur; end empquery_proc; Function deptquery_func (p_dname in varchar2) return SHDEMO_PKG.curtype as lcur SHDEMO_PKG.curtype; begin   open lcur for   select * from dept where dname = p_dname;   return lcur; end deptquery_func; end SHDEMO_PKG; ``` |

To add the stored procedure into a Logi JReport catalog, follow the steps below:

1. Start Logi JReport Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source to which the stored procedure is to be added, then select **New User Defined Data Source**. The New User Defined Data Source dialog appears.
3. In the Name field, specify a name for the UDS, for example, UDS1.
4. In the Class Name field, input the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, enter one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&PARAMVALUE="SALES"`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&INPARAMVALUE="SALES",varchar,2`
   * `OWNER=SCOTT&PROCNAME=deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&PARAMVALUE="SALES"`
   * `OWNER=SCOTT&PROCNAME=deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&INPARAMVALUE="SALES",varchar,2`

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893963927/cnctn_uds_orcl_eg4.gif)
6. Select the **OK** button. The UDS class will then be added into the catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585341-Example-3-Functions-Defined-Outside-of-a-Package)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564282-EnterpriseDB-Stored-Procedure-UDS)
