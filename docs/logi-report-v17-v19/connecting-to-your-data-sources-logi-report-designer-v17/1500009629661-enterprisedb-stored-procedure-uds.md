---
title: "EnterpriseDB Stored Procedure UDS"
id: 1500009629661
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629661-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2021-07-24T16:05:05Z
---

# EnterpriseDB Stored Procedure UDS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606722-Hierarchical-Data-Sources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a Logi Report catalog. As a substitute, Logi Report has developed the [user data source API](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API) which can use stored procedures in EnterpriseDB. The usage of EnterpriseDB stored procedures is the same as that of [Oracle stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS), except that the class name for EnterpriseDB stored procedures is EnterpriseDbProcedureUDS, in the package jet.datasource.enterprisedb. This class is already included in Logi Report Designer and Logi Report Server so you do not need to write any code or modify the classpath.

The following takes an example to show how to add an EnterpriseDB stored procedure to a catalog.

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

To add the stored procedure into a Logi Report catalog, follow the steps below:

1. Start Logi Report Designer and open the catalog to which you want to add the stored procedure.
2. In the Catalog Manager, right-click the data source the stored procedure is to be added, then select **New User Defined Data Source**. The New User Defined Data Source dialog appears.
3. In the Name text box, specify a name for the UDS, for example, UDS1.
4. In the Class Name text box, type the UDS class **jet.datasource.enterprisedb.EnterpriseDbProcedureUDS**.
5. In the Parameter box, type any of the following:
   * `DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1`
   * `DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&INPARAMVALUE=@job1,varchar,1`
   * `OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1`

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904405783/cnctn_uds_entrprs.gif)
6. Select **OK**, and the UDS class will be added into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606722-Hierarchical-Data-Sources)
