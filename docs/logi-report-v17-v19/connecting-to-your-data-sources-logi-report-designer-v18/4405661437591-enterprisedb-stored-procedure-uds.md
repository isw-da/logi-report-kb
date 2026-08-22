---
title: "EnterpriseDB Stored Procedure UDS"
id: 4405661437591
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661437591-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2022-01-27T20:34:42Z
---

# EnterpriseDB Stored Procedure UDS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661438615-Oracle-Stored-Procedure-UDS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664410263-Using-Hierarchical-Data-Sources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a catalog. As a substitute, Logi Report has developed the [User Data Source API](https://devnet.logianalytics.com/hc/en-us/articles/4405664421655-User-Data-Source-API) which can use stored procedures in EnterpriseDB. This topic presents an example to show how you can add an EnterpriseDB stored procedure to a catalog.

The usage of EnterpriseDB stored procedures is the same as that of [Oracle stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/4405661438615-Oracle-Stored-Procedure-UDS), except that the class name for EnterpriseDB stored procedures is EnterpriseDbProcedureUDS and in the package jet.datasource.enterprisedb. Both Designer and Server include the UDS class, so you do not need to write any Java code or modify the classpath when you implement the API.

## Example of Adding an EnterpriseDB Stored Procedure to a Catalog

Suppose that an EnterpriseDB stored procedure is defined as follows:

```
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
```

To add the stored procedure into a catalog, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405661330711-Creating-Opening-and-Saving-Catalogs#Open) to which you want to add the stored procedure.
2. In the Catalog Manager, right-click the data source the stored procedure is to be added, then select **New User Defined Data Source**.
3. In the New User Defined Data Source dialog box, specify a name for the UDS in the **Name** text box, for example, **UDS1**.
4. In the **Class Name** text box, type the UDS class **jet.datasource.enterprisedb.EnterpriseDbProcedureUDS**.
5. In the **Parameter** box, type any of the following:
   * `DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1`
   * `DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&INPARAMVALUE=@job1,varchar,1`
   * `OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1`

   ![Add User Defined Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420394869271/cnctn_uds_entrprs.gif)
6. Select **OK** to add the UDS class into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661438615-Oracle-Stored-Procedure-UDS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664410263-Using-Hierarchical-Data-Sources)
