---
title: "EnterpriseDB Stored Procedure UDS"
id: 1500010064541
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064541-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2021-07-24T10:39:13Z
---

# EnterpriseDB Stored Procedure UDS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029542-Oracle-Stored-Procedure-UDS) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064201-Hierarchical-Data-Sources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a Logi JReport catalog. As a substitute, Logi JReport has developed the [user data source API](https://devnet.logianalytics.com/hc/en-us/articles/1500010064521-User-Data-Source-API) which can use stored procedures in EnterpriseDB. The usage of EnterpriseDB stored procedures is the same as that of [Oracle stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500010029542-Oracle-Stored-Procedure-UDS), except that the class name for EnterpriseDB stored procedures is EnterpriseDbProcedureUDS, in the package jet.datasource.enterprisedb. This class is already included in Logi JReport Designer and Logi JReport Server so you do not need to write any code or modify the classpath.

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

To add the stored procedure into a Logi JReport catalog, follow the steps below:

1. Start Logi JReport Designer and open the catalog to which you want to add the stored procedure.
2. In the Catalog Manager, right-click the data source the stored procedure is to be added, then select **New User Defined Data Source**. The New User Defined Data Source dialog appears.
3. In the Name text box, specify a name for the UDS, for example, UDS1.
4. In the Class Name text box, input the UDS class **jet.datasource.enterprisedb.EnterpriseDbProcedureUDS**.
5. In the Parameter box, enter any of the following:
   * `DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1`
   * `DRIVER=com.edb.Driver&URL="jdbc:edb://222.222.222.45:5444/edb"&USER=enterprisedb&PSWD=db1234&OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&INPARAMVALUE=@job1,varchar,1`
   * `OWNER=enterprisedb&PROCNAME=empquery&SQL={call empquery(?,?)}&REFCURSORINDEX=2&PARAMVALUE=@job1`

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901304855/cnctn_uds_entrprs.gif)
6. Select **OK**, and the UDS class will be added into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029542-Oracle-Stored-Procedure-UDS) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064201-Hierarchical-Data-Sources)
