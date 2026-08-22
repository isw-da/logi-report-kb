---
title: "Using Catalog API to Manipulate Catalogs"
id: 28897710747789
section: "Working with APIs - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897710747789-Using-Catalog-API-to-Manipulate-Catalogs
updated_at: 2024-09-30T09:11:44Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Using Catalog API to Manipulate Catalogs

You can use the Catalog API to work with a catalog and manage the objects in it programmatically, instead of using the GUI in Designer. For example, you can create connections, add and delete objects such as tables, queries, and business views in a catalog using the Catalog API. By combining the Catalog API and the Design API, you can create any report to meet your requirements in a Java development environment. This topic introduces how you can install the Catalog API and use it to work with catalogs.

The following diagram illustrates the workflow of the Catalog API. 

 Starting from v13.5, Report changes the catalog structure greatly, thus the original Catalog API cannot meet the new catalog structure, therefore, Report provides a new set of Catalog API to extend and enhance the original one. When you use the Catalog API, you can choose from two different sets: the original jet.api.CatalogAPI class that applies to catalogs created before v13.5, and the new jet.api.MultipliedCatalogAPI class that applies to catalogs created since v13.5. 

Select the following links to view the topics:

- Installing the Catalog API

- Making Preparations Before Using the Catalog API 

- Manipulating Catalogs with the Catalog API

- Running the Catalog API Samples

Previous Topic  Next Topic
