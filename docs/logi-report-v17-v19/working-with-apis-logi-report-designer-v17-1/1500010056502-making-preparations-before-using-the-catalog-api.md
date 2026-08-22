---
title: "Making Preparations Before Using the Catalog API"
id: 1500010056502
section: "Working with APIs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056502-Making-Preparations-Before-Using-the-Catalog-API
updated_at: 2021-07-23T19:14:28Z
---

# Making Preparations Before Using the Catalog API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093741-Installing-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093761-Manipulating-Catalogs-with-the-Catalog-API)

# Making Preparations Before Using the Catalog API

Before you can use the Catalog API to perform tasks, you need to create a Designer object and then get a Catalog API instance. This topic describes how you can make the preparations for using the Catalog API.

This topic contains the following sections:

* [Creating a Designer Object](#Object)
* [Getting a Catalog API Instance](#Instance)

## Creating a Designer Object

To create a Designer object, use the constructor *Designer(String path, String name, DesignerUserInfo user)* in the Design API. The constructor has three parameters: the catalog path, catalog name, and the user ID and license key provided by Logi Analytics. The path needs to be a valid path to an existing directory. The catalog name can be the name of an existing catalog when you want to open a catalog, or the name of a new catalog when you want to create a catalog. If you want to create a new catalog, the path directory should not already contain a catalog file.

To create the DesignerUserInfo instance, use the following constructor with the user ID and the Designer License Key or Server Designer License Key you receive when you purchase Logi Report.

`DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key);`

## Getting a Catalog API Instance

To get a Catalog API instance, use the method *getCatalogAPI()* in the Design API. You need to first get an instance from Designer as follows:

`Designer desg = new Designer(catalogPath, catalogName, userInfo);  
CatalogAPI catalog = desg.getCatalogAPI();`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093741-Installing-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093761-Manipulating-Catalogs-with-the-Catalog-API)

# Making Preparations Before Using the Catalog API
