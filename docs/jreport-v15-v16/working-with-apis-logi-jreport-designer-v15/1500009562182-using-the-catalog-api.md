---
title: "Using the Catalog API"
id: 1500009562182
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562182-Using-the-Catalog-API
updated_at: 2021-07-24T05:56:23Z
---

# Using the Catalog API

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582581-Installing-the-Catalog-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562202-Creating-a-Connection)

# Using the Catalog API

The Catalog API provides methods which enable you to create a connection, add and delete objects such as tables, queries, business views in a catalog, and so on. Before you can use the Catalog API to perform certain tasks, you will have to create a Designer object and then get a Catalog API instance.

**To create a Designer object**:

To create a Designer object, use the constructor Designer(String path, String name, DesignerUserInfo user) in the Design API. The constructor has three parameters: the catalog path, catalog name, and the user ID and license key provided by Jinfonet.

The path needs to be a valid path to an existiing directory. The catalog name can be the name of an existing catalog when you want to open a catalog, or the name of a new catalog when you want to create a catalog. If you want to create a new catalog, the path directory should not already contain a catalog file.

To create the DesignerUserInfo instance, use the following constructor providing the user ID and the Server Designer License Key or Designer License Key you received when you purchased Logi JReport.

`DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key);`

**To get a Catalog API instance**

To get a Catalog API instance, use the method getCatalogAPI() in the Design API. You need to first get an instance from Designer as follows.

 `Designer desg = new Designer(catalogPath, catalogName, userInfo);  
CatalogAPI catalog = desg.getCatalogAPI();` 

Then with the methods in Logi JReport Catalog API, you can do the following:

> * [Creating a Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009562202-Creating-a-Connection)
> * [Inserting a Table/View/Synonym](https://devnet.logianalytics.com/hc/en-us/articles/1500009582701-Inserting-a-Table-View-Synonym)
> * [Inserting a Stored Procedure](https://devnet.logianalytics.com/hc/en-us/articles/1500009562262-Inserting-a-Stored-Procedure)
> * [Importing an SQL File](https://devnet.logianalytics.com/hc/en-us/articles/1500009562302-Importing-an-SQL-File)
> * [Inserting a UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009582721-Inserting-a-UDS)
> * [Inserting a Business View](https://devnet.logianalytics.com/hc/en-us/articles/1500009582601-Inserting-a-Business-View)
> * [Inserting a Formula, Summary, Parameter or a WHERE Portion](https://devnet.logianalytics.com/hc/en-us/articles/1500009562222-Inserting-a-Formula-Summary-Parameter-or-a-WHERE-Portion)
> * [Creating and Modifying a Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009582641-Creating-and-Modifying-a-Query)
> * [Inserting and Deleting an Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009582621-Inserting-and-Deleting-an-Object)
> * [Getting Objects in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562242-Getting-Objects-in-a-Catalog)
> * [Refreshing the Reference Table of a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009582661-Refreshing-the-Reference-Table-of-a-Catalog)
> * [Saving a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562282-Saving-a-Catalog)
> * [Catalog API Sample](https://devnet.logianalytics.com/hc/en-us/articles/1500009582681-Catalog-API-Sample)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582581-Installing-the-Catalog-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562202-Creating-a-Connection)
