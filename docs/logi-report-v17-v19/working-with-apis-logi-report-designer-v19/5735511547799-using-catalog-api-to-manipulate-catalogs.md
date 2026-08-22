---
title: "Using Catalog API to Manipulate Catalogs"
id: 5735511547799
section: "Working with APIs - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735511547799-Using-Catalog-API-to-Manipulate-Catalogs
updated_at: 2022-11-02T08:17:03Z
---

# Using Catalog API to Manipulate Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735506505239-Using-Server-API-to-Work-with-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735526648855-Installing-the-Catalog-API)

# Using Catalog API to Manipulate Catalogs

You can use the Catalog API to work with a catalog and manage the objects in it programmatically, instead of using the GUI in Designer. For example, you can create connections, add and delete objects such as tables, queries, and business views in a catalog using the Catalog API. By combining the Catalog API and the [Design API](https://devnet.logianalytics.com/hc/en-us/articles/5735520110743-Using-Design-API-to-Design-Reports), you can create any report to meet your requirements in a Java development environment. This topic introduces how you can install the Catalog API and use it to work with catalogs.

The following diagram illustrates the workflow of the Catalog API.

![Catalog API diagram](https://devnet.logianalytics.com/hc/article_attachments/9898536425239/wkapi_catapi.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Starting from v13.5, Logi Report changes the catalog structure greatly, thus the original Catalog API cannot meet the new catalog structure, therefore, Logi Report provides a new set of Catalog API to extend and enhance the original one. When you use the Catalog API, you can choose from two different sets: the original jet.api.CatalogAPI class that applies to catalogs created before v13.5, and the new jet.api.MultipliedCatalogAPI class that applies to catalogs created since v13.5.

Select the following links to view the topics:

* [Installing the Catalog API](https://devnet.logianalytics.com/hc/en-us/articles/5735526648855-Installing-the-Catalog-API)
* [Making Preparations Before Using the Catalog API](https://devnet.logianalytics.com/hc/en-us/articles/5735526662551-Making-Preparations-Before-Using-the-Catalog-API)
* [Manipulating Catalogs with the Catalog API](https://devnet.logianalytics.com/hc/en-us/articles/5735506431639-Manipulating-Catalogs-with-the-Catalog-API)
* [Running the Catalog API Samples](https://devnet.logianalytics.com/hc/en-us/articles/5735520092695-Running-the-Catalog-API-Samples)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735506505239-Using-Server-API-to-Work-with-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735526648855-Installing-the-Catalog-API)
