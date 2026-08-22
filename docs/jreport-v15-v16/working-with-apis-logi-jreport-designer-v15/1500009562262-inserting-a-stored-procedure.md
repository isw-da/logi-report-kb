---
title: "Inserting a Stored Procedure"
id: 1500009562262
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562262-Inserting-a-Stored-Procedure
updated_at: 2021-07-24T05:56:21Z
---

# Inserting a Stored Procedure

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582701-Inserting-a-Table-View-Synonym)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562302-Importing-an-SQL-File)

# Inserting a Stored Procedure

The following methods are used to insert a stored procedure into a connection and to return the handle of the newly inserted procedure:

* insert(String procName,String catalog,String schema,String name,String remarks,int iType)
* insert(String procName, String catalog, String schema, String name, String remarks, int iType)

**Parameters**

* procName - The procedure mapping name.
* catalog - The catalog name of the procedure.
* schema - The schema name of the procedure.
* name - The procedure name.
* remarks - The remarks on the procedure.
* iType - The result type of the procedure.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582701-Inserting-a-Table-View-Synonym)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562302-Importing-an-SQL-File)
