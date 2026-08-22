---
title: "Example 2: Stored Procedures Declared and Defined in a Package and Package Body"
id: 1500009585321
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585321-Example-2-Stored-Procedures-Declared-and-Defined-in-a-Package-and-Package-Body
updated_at: 2021-07-24T05:55:42Z
---

# Example 2: Stored Procedures Declared and Defined in a Package and Package Body

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564302-Example-1-Stored-Procedures-Defined-Outside-of-a-Package)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585341-Example-3-Functions-Defined-Outside-of-a-Package)

# Example 2: Stored Procedures Declared and Defined in a Package and Package Body

This topic provides an example of a stored procedure declared and defined in a package and package body.

Suppose that an Oracle stored procedure is defined as:

|  |
| --- |
| ``` CREATE OR REPLACE PACKAGE DEMO_PKG AS type curtype is ref cursor; PROCEDURE empquery_proc(p_job in varchar2, cur OUT DEMO_PKG.curtype); end DEMO_PKG ; CREATE OR REPLACE PACKAGE BODY DEMO_PKG AS PROCEDURE empquery_proc(p_job in varchar2, cur OUT DEMO_PKG.curtype) AS lcur DEMO_PKG.curtype; begin   open lcur for   select * from EMP WHERE JOB = p_job;   cur:=lcur; end empquery_proc; end DEMO_PKG; ``` |

To add the stored procedure into a Logi JReport catalog, follow the steps below:

1. Start Logi JReport Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source to which the stored procedure is to be added, then select **New User Defined Data Source**. The New User Defined Data Source dialog appears.
3. In the Name field, specify a name for the UDS, for example, UDS1.
4. In the Class Name field, input the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, enter one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger  
      &OWNER=SCOTT&PROCNAME=empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&PARAMVALUE="SALESMAN"`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&INPARAMVALUE="SALESMAN",varchar,1`
   * `OWNER=SCOTT&PROCNAME=empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&PARAMVALUE="SALESMAN"`
   * `OWNER=SCOTT&PROCNAME=empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&INPARAMVALUE="SALESMAN",varchar,1`

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893964439/cnctn_uds_orcl_eg2.gif)
6. Select the **OK** button. The UDS class will then be added into the catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564302-Example-1-Stored-Procedures-Defined-Outside-of-a-Package)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585341-Example-3-Functions-Defined-Outside-of-a-Package)
