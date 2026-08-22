---
title: "Using Catalog API to Manage Catalogs"
id: 5741381190423
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741381190423-Using-Catalog-API-to-Manage-Catalogs
updated_at: 2022-10-31T17:15:42Z
---

# Using Catalog API to Manage Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741363379863-RMI-Demos)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386010903-Using-Design-API-to-Design-Reports)

# Using Catalog API to Manage Catalogs

You can use Logi Report Catalog API to work with a catalog and manage the objects in it programmatically, instead of using the GUI in Logi Report Designer. This topic describes the things that the Catalog APIs can do and the two Catalog API classes for different versions of catalogs.

You can perform the following operations with the Catalog API:

* Create a connection.
* Add and delete objects such as tables, queries, business views, formulas, parameters, and WHERE portions.
* Modify a query and update UDS.
* Get and modify object information.

You can choose from two different sets of Catalog APIs. The original jet.api.CatalogAPI class applies to catalogs created before v13.5, and the new jet.api.MultipliedCatalogAPI class applies to catalogs created since v13.5. Since v13.5, the Logi Report catalog structure has changed greatly. The original Catalog API could not meet the new catalog structure, so Logi Report provides a new set of Catalog API to extend and enhance the original one.

You can combine the Catalog API and the Design API to create any report to meet your requirements in a Java development environment.

For more information, see Using Catalog API to Manipulate Catalogs in the *Logi Report Designer Guide*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741363379863-RMI-Demos)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386010903-Using-Design-API-to-Design-Reports)
