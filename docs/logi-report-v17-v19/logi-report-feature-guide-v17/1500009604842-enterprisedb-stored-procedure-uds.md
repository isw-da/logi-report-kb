---
title: "EnterpriseDB Stored Procedure UDS"
id: 1500009604842
section: "Logi Report Feature Guide v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009604842-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2021-07-24T16:05:43Z
---

# EnterpriseDB Stored Procedure UDS

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009604822-JSON-Connection) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604982-Dynamic-Resources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a Logi Report catalog. In this sense, the usage of Logi Report Designer is limited when you use an EnterpriseDB database. As a substitute, Logi Report has developed the User Data Source API, which can use stored procedures in EnterpriseDB. The class name for EnterpriseDB stored procedures is EnterpriseDbProcedureUDS, in the package jet.datasource.enterprisedb.

In the following example, an EnterpriseDB stored procedure which is defined as follows will be added in to a Logi Report catalog.

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

![Add EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/article_attachments/4404904537751/cnctn_udsentrprs.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009604822-JSON-Connection) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604982-Dynamic-Resources)
