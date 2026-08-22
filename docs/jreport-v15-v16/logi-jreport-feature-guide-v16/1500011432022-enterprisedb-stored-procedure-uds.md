---
title: "EnterpriseDB Stored Procedure UDS"
id: 1500011432022
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011432022-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2021-07-24T10:39:49Z
---

# EnterpriseDB Stored Procedure UDS

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011432042-MongoDB-Connection) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463901-Dynamic-Resources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a Logi JReport catalog. In this sense, the usage of Logi JReport Designer is limited when you use an EnterpriseDB database. As a substitute, Logi JReport has developed the User Data Source API which can use stored procedures in EnterpriseDB. The class name for EnterpriseDB stored procedures is EnterpriseDbProcedureUDS, in the package jet.datasource.enterprisedb.

In the following example, an EnterpriseDB stored procedure which is defined as follows will be added into a Logi JReport catalog.

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

![Add EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/article_attachments/4404909304343/cnctn_udsentrprs.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011432042-MongoDB-Connection) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463901-Dynamic-Resources)
