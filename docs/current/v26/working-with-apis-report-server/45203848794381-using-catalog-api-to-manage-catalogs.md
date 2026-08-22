---
title: "Using Catalog API to Manage Catalogs"
id: 45203848794381
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203848794381-Using-Catalog-API-to-Manage-Catalogs
updated_at: 2026-04-30T14:07:41Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Using Catalog API to Manage Catalogs 

You can use Report Catalog API to work with a catalog and manage the objects in it programmatically, instead of using the GUI in Report Designer. This topic describes the things that the Catalog APIs can do and the two Catalog API classes for different versions of catalogs.

You can perform the following operations with the Catalog API:
        

- Create a connection.

- Add and delete objects such as tables, queries, business views, formulas, parameters, and WHERE portions.

- Modify a query and update UDS.

- Get and modify object information.

You can choose from two different sets of Catalog APIs. The original jet.api.CatalogAPI class applies to catalogs created before v13.5, and the new jet.api.MultipliedCatalogAPI class applies to catalogs created since v13.5. Since v13.5, the Report catalog structure has changed greatly. The original Catalog API could not meet the new catalog structure, so Report provides a new set of Catalog API to extend and enhance the original one.

You can combine the Catalog API and the Design API to create any report to meet your requirements in a Java development environment.

For more information, see Using Catalog API to Manipulate Catalogs in the Report Designer Guide.
