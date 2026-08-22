---
title: "EnterpriseDB Stored Procedure UDS"
id: 5735497866903
section: "Logi Report Feature Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735497866903-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2022-11-02T04:11:50Z
---

# EnterpriseDB Stored Procedure UDS

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511265815-JSON-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563367191-Dynamic-Resources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a catalog. In this sense, the usage of Designer is limited when you use an EnterpriseDB database. As a substitute, Logi Report has developed the User Data Source API, which enables you to use stored procedures in EnterpriseDB.

In the following example, we add an EnterpriseDB stored procedure that is defined as follows into a catalog.

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

![Add EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/article_attachments/9898521758103/cnctn_udsentrprs.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511265815-JSON-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563367191-Dynamic-Resources)
