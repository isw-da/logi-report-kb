---
title: "EnterpriseDB Stored Procedure UDS"
id: 4405661281943
section: "Logi Report Feature Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661281943-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2022-01-27T20:34:10Z
---

# EnterpriseDB Stored Procedure UDS

![](https://devnet.logianalytics.com/hc/article_attachments/4420394628247/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661279639-JSON-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420402298007/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661294103-Dynamic-Resources)

# EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a Logi Report catalog. In this sense, the usage of Designer is limited when you use an EnterpriseDB database. As a substitute, Logi Report has developed the User Data Source API, which enables you to use stored procedures in EnterpriseDB.

In the following example, we will add an EnterpriseDB stored procedure which is defined as follows into a Logi Report catalog.

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

![Add EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/article_attachments/4420402678807/cnctn_udsentrprs.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4420394628247/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661279639-JSON-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420402298007/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661294103-Dynamic-Resources)
