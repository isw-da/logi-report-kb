---
title: "EnterpriseDB Stored Procedure UDS"
id: 12491069171725
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491069171725-EnterpriseDB-Stored-Procedure-UDS
updated_at: 2025-05-30T02:58:18Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
EnterpriseDB Stored Procedure UDS

Due to the unique nature of EnterpriseDB stored procedures, you cannot add them directly into a catalog. In this sense, the usage of Designer is limited when you use an EnterpriseDB database. As a substitute, Report has developed the User Data Source API, which enables you to use stored procedures in EnterpriseDB.

In the following example, we add an EnterpriseDB stored procedure that is defined as follows  into a catalog. 

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

Previous Topic  Next Topic
