---
title: "EnterpriseDB Stored Procedure UDS"
id: 45190496973453
section: "Connecting to Your Data Sources - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190496973453-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2026-04-30T15:12:40Z
source_host: logi-report-v26.insightsoftware.com
---
# 
EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a catalog. As a substitute, Report has developed the User Data Source API which can use stored procedures in EnterpriseDB. This topic presents an example to show how you can add an EnterpriseDB stored procedure to a catalog.

 The usage of EnterpriseDB stored procedures is the same as that of Oracle stored procedures, except that the class name for EnterpriseDB stored procedures is EnterpriseDbProcedureUDS and in the jet.datasource.enterprisedb package. Both Designer and Server include the UDS class, so you do not need to write any Java code or modify the class path when you implement the API. 

## Example: Adding an EnterpriseDB Stored Procedure to a Catalog

Suppose you have an EnterpriseDB stored procedure as follows:

create or replace package shdemo

    as

    type curtype

    is

ref

cursor;

end shdemo;

    create or replace procedure empquery (param1 in varchar2,

    cur out shdemo.curtype) as lcur shdemo.curtype;

    begin

    open lcur for

    select

    *

    from

    emp

    where

    job = param1;

    cur:=lcur;

    end empquery;

To add the stored procedure into a catalog, take the following steps:

- 
Create a catalog or open a catalog to which you want to add the stored procedure.

- In the Catalog Manager, right-click the data source the stored procedure is to be added, then select New User Defined Data Source.

- In the New User Defined Data Source dialog box, specify a name for the UDS in the Name text box, for example, UDS1.

- In the Class Name text box, type the UDS class jet.datasource.enterprisedb.EnterpriseDbProcedureUDS.

- In the Parameter box, type one of the following:
- DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1

- DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&INPARAMVALUE=@job1,varchar,1

- OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1

- Select OK to add the UDS class  into the catalog.
