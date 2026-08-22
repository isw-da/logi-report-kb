---
title: "Oracle Stored Procedure UDS"
id: 1500009629681
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS
updated_at: 2021-07-24T16:05:05Z
---

# Oracle Stored Procedure UDS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607002-Adding-User-Defined-Data-Sources-to-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629661-EnterpriseDB-Stored-Procedure-UDS)

# Oracle Stored Procedure UDS

Due to the unique nature of Oracle stored procedures, you cannot add them directly into a Logi Report catalog. As a substitute, Logi Report has developed the [user data source API](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API) which can use stored procedures in Oracle. The class is named OracleProcedureUDS, in the package jet.datasource.oracle. The UDS class is already included in Logi Report Designer and Logi Report Server; therefore, you do not need to write any Java code or modify the classpath.

This topic includes the following sections:

* [Adding Oracle Stored Procedures into a Catalog](#Add)
* [Example 1: Stored Procedures Defined Outside of a Package](#Example1)
* [Example 2: Stored Procedures Declared and Defined in a Package and Package Body](#Example2)
* [Example 3: Functions Defined Outside of a Package](#Example3)
* [Example 4: Functions Declared and Defined in a Package and Package body](#Example4)

## Adding Oracle Stored Procedures into a Catalog

The general steps to add an Oracle stored procedure to a Logi Report catalog are as follows:

1. In Logi Report Designer open the catalog to which you want to add it.
2. In the Catalog Manager, right-click the catalog data source the stored procedure is to be added, then select **New User Defined Data Source**. The [New User Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609402-New-User-Defined-Data-Source-Dialog) dialog appears.

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916781207/nwuds.gif)
3. In the Name text box, specify a name for the UDS.
4. In the Class Name text box, type the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, specify the parameter as required.
6. Select **OK**, and the UDS class will be added into the catalog.

**Formats of the parameter string**

In the New User Defined Data Source dialog, the format of the parameter string is one of the following types. You can choose one according to your requirements. When the stored procedures used in Oracle have different names, either of the following two formats can be used. However, when the stored procedures used in Oracle have the same names, you can only use the second parameter string. In addition, when you use the second parameter string, the parameter value only contains value. You need to add the data type and index of the parameter value in the user defined data source class.

* `DRIVER=drivername&URL=url&USER=user&PSWD=password&OWNER=owner&PROCNAME=procname&SQL=sql&REFCURSORINDEX=index&PARAMVALUE=value1,value2,value3&OUTPARAMINDEX=index1,index2`
* `DRIVER=drivername&URL=url&USER=user&PSWD=password&OWNER=owner&PROCNAME=procname&SQL=sql&REFCURSORINDEX=index&INPARAMVALUE=value1,datatype1,index1;value2,datatye2,index2;…Valuen,datatypen,indexn&OUTPARAM=datatype1,index1;… datatypen,indexn`

If you do not want to specify the connection information in the parameter string, you can also write the parameter as follows:

* `OWNER=owner&PROCNAME=procname&SQL=sql&REFCURSORINDEX=index&PARAMVALUE=value1,value2,value3&OUTPARAMINDEX=index1,index2`
* `OWNER=owner&PROCNAME=procname&SQL=sql&REFCURSORINDEX=index&INPARAMVALUE=value1,datatype1,index1;value2,datatye2,index2;…Valuen,datatypen,indexn&OUTPARAM=datatype1,index1;… datatypen,indexn`

In this case, the default connection defined on the data source, to which the stored procedure UDS is added will be used. Only when the information of the default connection and that of the stored procedure UDS match, can the stored procedure UDS be added successfully. You can change the connection at runtime via datasource.xml, Engine API or Server API in Logi Report Server.

The following explains the lower-case words in the parameter strings in detail. Substitute them according to your requirements.

* **drivername** - The name of JDBC driver, for instance: oracle.jdbc.driver.OracleDriver.
* **url** - A database URL of the form jdbc:subprotocol:subname, for instance: jdbc:oracle:thin:@dbserver:1521:orcl.
* **user** - The database user on whose behalf the Connection is being made, for instance: scott.
* **password** - The user's password, for instance: tiger.
* **owner** - The owner of the procedure, for instance: scott. It can also be left empty.
* **procname** - The name of the Stored Procedure, for instance: getAuthor.
* **sql** - The SQL statement used to call the procedure or function. For instance, with regards to procedure: {call getAuthor(?, ?)} and for function: {? = getAuthor(?, ?)}. When a stored procedure is defined in Package/Package Body, the package name should be contained in the stored procedure name.
* **index** - The index of the output parameter with data type equal to Ref Cursor. The start index is 1.
* **valueX** - The value of the parameters separated by ',' and the data types must correspond to the ones defined in the DBMS. If valueX should contain a set of constant string values, for example, 10, 20, and 30 together serve as valueX, you will need to use '\\' to escape the comma.

  For example, if the PARAMVALUE part of the parameter string is as follows:

  `...&PARAMVALUE=10\\,20\\,30,30\\,10\\,23,,a,`

  Then the parameter values will be parsed as follows:

  ParaValue1 =10,20,30  
  ParaValue2 =30,10,23  
  ParaValue3 =null  
  ParaValue4 =a  
  ParaValue5 =null

  Or, instead of typing the parameter values one by one in the above parameter string, you can also use the [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) in the current catalog data source to substitute the parameter values, then '\\' will automatically be added to escape the comma. It is recommended to use the parameters and constant level formulas to control one input parameter value of the oracle stored procedure. For example:

  `...&PARAMVALUE=@PARAM1,30\\,10\\,23,,a,`

  In this case, in the Create/Edit Parameter dialog, the prompt value of parameter PARAM1 must be typed as follows:

  10,20,30
* **datatypeX** - The name of the data type mapping to JDBC. The name is the same as the static variable name in java.sql.types.
* **IndexX** - The index of the input parameter. It is natural number and integer.

See an example of the parameter string below:

`DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@dbserver:1521:orcl"&USER=scott&PSWD=tiger&OWNER=SCOTT&PROCNAME=getAuthor&SQL={call getAuthor(?, ?, ?}&REFCURSORINDEX=2&PARAMVALUE=0.5,1999-7-10`

If you want to change the connection dynamically, you can define the parameters in this way:

* `DRIVER=@driver&URL=@url&USER=@user&PSWD=tiger&OWNER=SCOTT&PROCNAME=getAuthor&SQL={call getAuthor(?, ?,?}&REFCURSORINDEX=1&PARAMVALUE=0.5,1999-7-10`
* `DRIVER=@driver&URL=@url&USER=@user&PSWD=tiger&OWNER=SCOTT&PROCNAME=getAuthor&SQL={call getAuthor(?, ?,?}&REFCURSORINDEX=1&INPARAMVALUE=0.5,number,2;1999-7-10,date,3`

You can change the parameter dynamically to suit your requirements.

**Troubleshooting**

If you get an "ArrayOutOfBound" error or a "Not all variables are bound" error while importing a stored procedure, you can check the following points:

* Make sure the OWNER is correct.
* If your stored procedure is defined in Package/Package Body and the PROCNAME argument does not contain package name, but the call argument contains.
* Make sure that your REFCURSORINDEX has been set correctly.

  For example, if you have defined that the Out cursor is the third argument in your stored procedure, then REFCURSORINDEX should be 3.

When you get a NegativeArraySizeException error while running a report designed with a stored procedure, you can check whether some UDS columns return a negative scale (right-click the UDS column, select Properties, and then select Scale). If yes, it means that your original table column called by the stored procedure is likely to be of a Float data type. This returns the wrong Scale for the UDS column. Follow the steps below to modify the UDS column's scale:

1. Open the Catalog Manager.
2. Highlight the UDS column name that you are having the problem with and select **Show Properties**  on the toolbar to show the Properties sheet. You can change the property values, such as SQL type, precision, and scale to the correct values. For instance, you can change the negative scale of the problematic column to the correct value.

**Notes:**

* Your oracle.jdbc.driver should use at least ojdbc6.jar.
* The UDS class is in a package named jet.datasource.oracle. When it is being added into the Catalog Manager, it requires classes in package oracle.jdbc.driver. So before adding it, make sure the class path contains the package oracle.jdbc.driver.
* When your parameter string contains characters such as: At sign(@), ':', double quotation mark('"'), or other strings that do not need to be parsed by Logi Report, you can use a pair of double quotation marks to quote them. For example, your parameter string may be:

  `jdbc:oracle:thin:@204.177.148.30:1521:orcl`

  Here, @ is a character used by the URL. If you add this parameter string into a catalog, Logi Report will regard 204 as the name of a parameter in the catalog. The correct form is:

  `"jdbc:oracle:thin:@204.177.148.30:1521:orcl"`
* The procedure must contain one and only one OUT parameter of the REF CURSOR type. If the procedure doesn't have such a parameter, it cannot be added into the Logi Report catalog since Logi Report cannot create a report without a ResultSet. If it contains additional OUT parameters they will be ignored.

## Example 1: Stored Procedures Defined Outside of a Package

Suppose that an Oracle stored procedure is defined as:

```
CREATE OR REPLACE PACKAGE SHDEMO as  
type curtype is ref cursor;  
END SHDEMO;  
CREATE OR REPLACE PROCEDURE empquery (p_job in varchar2, cur OUT SHDEMO.curtype) as  
lcur SHDEMO.curtype;  
begin  
    open lcur for  
    select * from EMP WHERE JOB = p_job;  
    cur:=lcur;  
END empquery;
```

To add the stored procedure into a Logi Report catalog, follow the steps below:

1. Start Logi Report Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source node to which the stored procedure is to be added, then select **New User Defined Data Source**.
3. In the New User Defined Data Source dialog, specify a name for the UDS in the Name text box, for example, **UDSDemo1**.
4. In the Class Name text box, type the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameters box, type one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE="SALESMAN"`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&INPARAMVALUE="SALESMAN",varchar,1`
   * `OWNER=SCOTT&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE="SALESMAN"`
   * `OWNER=SCOTT&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&INPARAMVALUE="SALESMAN",varchar,1`

   ![New UDS Example](https://devnet.logianalytics.com/hc/article_attachments/4404904404759/cnctn_uds_orcl_eg1.gif)
6. Select the **OK** button, and the UDS class will then be added into the catalog.

## Example 2: Stored Procedures Declared and Defined in a Package and Package Body

Suppose that an Oracle stored procedure is defined as:

```
CREATE OR REPLACE PACKAGE DEMO_PKG AS  
type curtype is ref cursor;  
PROCEDURE empquery_proc(p_job in varchar2, cur OUT DEMO_PKG.curtype);  
end DEMO_PKG ;  
CREATE OR REPLACE PACKAGE BODY DEMO_PKG AS  
PROCEDURE empquery_proc(p_job in varchar2, cur OUT DEMO_PKG.curtype) AS  
lcur DEMO_PKG.curtype;  
begin  
    open lcur for  
    select * from EMP WHERE JOB = p_job;  
    cur:=lcur;  
end empquery_proc;  
end DEMO_PKG;
```

To add the stored procedure into a Logi Report catalog, follow the steps below:

1. Start Logi Report Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source to which the stored procedure is to be added, then select **New User Defined Data Source**.
3. In the New User Defined Data Source dialog, specify a name for the UDS in the Name text box, for example, **UDSDemo2**.
4. In the Class Name text box, type the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, type one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger  
      &OWNER=SCOTT&PROCNAME=demo_pkg.empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&PARAMVALUE="SALESMAN"`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=demo_pkg.empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&INPARAMVALUE="SALESMAN",varchar,1`
   * `OWNER=SCOTT&PROCNAME=demo_pkg.empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&PARAMVALUE="SALESMAN"`
   * `OWNER=SCOTT&PROCNAME=demo_pkg.empquery_proc&SQL={call demo_pkg.empquery_proc(?,?)}&REFCURSORINDEX=2&INPARAMVALUE="SALESMAN",varchar,1`

   ![New UDS Example](https://devnet.logianalytics.com/hc/article_attachments/4404904405015/cnctn_uds_orcl_eg2.gif)
6. Select the **OK** button. The UDS class will then be added into the catalog.

## Example 3: Functions Defined Outside of a Package

Suppose that an Oracle stored procedure is defined as:

```
CREATE OR REPLACE PACKAGE SHDEMO AS  
type curtype is ref cursor;  
end SHDEMO;  
CREATE OR REPLACE FUNCTION "SCOTT"."DEPTQUERY"(p_dname in varchar2)  
return SHDEMO.curtype  
is  
lcur SHDEMO.curtype;  
begin  
    open lcur for  
    select * from dept where dname = p_dname;  
    return lcur;  
end DEPTQUERY;
```

To add the stored procedure into a Logi Report catalog, follow the steps below:

1. Start Logi Report Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source to which the stored procedure is to be added, then select **New User Defined Data Source**.
3. In the New User Defined Data Source dialog, specify a name for the UDS in the Name text box, for example, **UDSDemo3**.
4. In the Class Name text box, type the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, type one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&PARAMVALUE=@p_dname`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&INPARAMVALUE=@p_dname,varchar,1`
   * `OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&PARAMVALUE=@p_dname`
   * `OWNER=SCOTT&PROCNAME=deptquery&SQL={? = call deptquery(?)}&REFCURSORINDEX=1&INPARAMVALUE=@p_dname,varchar,1`

   ![New UDS Example](https://devnet.logianalytics.com/hc/article_attachments/4404904405271/cnctn_uds_orcl_eg3.gif)
6. Select the **OK** button. The UDS class will then be added into the catalog.

## Example 4: Functions Declared and Defined in a Package and Package Body

Suppose that an Oracle stored procedure is defined as:

```
CREATE OR REPLACE PACKAGE "SCOTT"."SHDEMO_PKG" AS  
type curtype is ref cursor;  
Procedure empquery_proc (p_job in varchar2, cur OUT SHDEMO_PKG.curtype);  
Function deptquery_func (p_dname in varchar2) return SHDEMO_PKG.curtype;  
end SHDEMO_PKG;  
CREATE OR REPLACE PACKAGE BODY "SCOTT"."SHDEMO_PKG" AS  
Procedure empquery_proc (p_job in varchar2, cur OUT SHDEMO_PKG.curtype)  
as  
lcur SHDEMO_PKG.curtype;  
begin  
    open lcur for  
    select * from EMP WHERE JOB = p_job;  
    cur:=lcur;  
end empquery_proc;  
Function deptquery_func (p_dname in varchar2) return SHDEMO_PKG.curtype  
as  
lcur SHDEMO_PKG.curtype;  
begin  
    open lcur for  
    select * from dept where dname = p_dname;  
    return lcur;  
end deptquery_func;  
end SHDEMO_PKG;
```

To add the stored procedure into a Logi Report catalog, follow the steps below:

1. Start Logi Report Designer and open an existing catalog.
2. In the Catalog Manager, right-click the data source to which the stored procedure is to be added, then select **New User Defined Data Source**.
3. In the New User Defined Data Source dialog, specify a name for the UDS in the Name text box, for example, **UDSDemo4**.
4. In the Class Name text box, type the UDS class **jet.datasource.oracle.OracleProcedureUDS**.
5. In the Parameter box, type one of the following:
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=shdemo_pkg.deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&PARAMVALUE="SALES"`
   * `DRIVER=oracle.jdbc.driver.OracleDriver&URL="jdbc:oracle:thin:@<hostname>:1521:oracle8"&USER=scott&PSWD=tiger&  
      OWNER=SCOTT&PROCNAME=shdemo_pkg.deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&INPARAMVALUE="SALES",varchar,2`
   * `OWNER=SCOTT&PROCNAME=shdemo_pkg.deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&PARAMVALUE="SALES"`
   * `OWNER=SCOTT&PROCNAME=shdemo_pkg.deptquery_func&SQL={? = call shdemo_pkg.deptquery_func(?)}&REFCURSORINDEX=1&INPARAMVALUE="SALES",varchar,2`

   ![New UDS Example](https://devnet.logianalytics.com/hc/article_attachments/4404904405527/cnctn_uds_orcl_eg4.gif)
6. Select the **OK** button. The UDS class will then be added into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607002-Adding-User-Defined-Data-Sources-to-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629661-EnterpriseDB-Stored-Procedure-UDS)
