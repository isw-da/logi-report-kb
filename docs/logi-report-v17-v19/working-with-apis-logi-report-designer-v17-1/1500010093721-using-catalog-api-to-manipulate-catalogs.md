---
title: "Using Catalog API to Manipulate Catalogs"
id: 1500010093721
section: "Working with APIs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093721-Using-Catalog-API-to-Manipulate-Catalogs
updated_at: 2021-07-23T19:14:27Z
---

# Using Catalog API to Manipulate Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093941-Using-Server-API-to-Work-with-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093741-Installing-the-Catalog-API)

# Using Catalog API to Manipulate Catalogs

You can use the Catalog API to work with a catalog and manage the objects in it programmatically, instead of using the GUI in Designer. For example, you can create connections, add and delete objects such as tables, queries, and business views in a catalog using the Catalog API. By combining the Catalog API and the [Design API](https://devnet.logianalytics.com/hc/en-us/articles/1500010093801-Using-Design-API-to-Design-Reports), you can create any report to meet your requirements in a Java development environment. This topic introduces how you can install the Catalog API and use it to work with catalogs.

The following diagram illustrates the workflow of the Catalog API.

![Catalog API diagram](https://devnet.logianalytics.com/hc/article_attachments/4404848710807/wkapi_catapi.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Starting from v13.5, Logi Report changes the catalog structure greatly, thus the original Catalog API cannot meet the new catalog structure, therefore, Logi Report provides a new set of Catalog API to extend and enhance the original one. When you use the Catalog API, you can choose from two different sets: the original jet.api.CatalogAPI class which applies to catalogs created before v13.5, and the new jet.api.MultipliedCatalogAPI class that applies to catalogs created since v13.5.

Select the following links to view the topics:

* [Installing the Catalog API](https://devnet.logianalytics.com/hc/en-us/articles/1500010093741-Installing-the-Catalog-API)
* [Making Preparations Before Using the Catalog API](https://devnet.logianalytics.com/hc/en-us/articles/1500010056502-Making-Preparations-Before-Using-the-Catalog-API)
* [Manipulating Catalogs with the Catalog API](https://devnet.logianalytics.com/hc/en-us/articles/1500010093761-Manipulating-Catalogs-with-the-Catalog-API)
* [Running the Catalog API Samples](https://devnet.logianalytics.com/hc/en-us/articles/1500010093781-Running-the-Catalog-API-Samples)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093941-Using-Server-API-to-Work-with-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093741-Installing-the-Catalog-API)
