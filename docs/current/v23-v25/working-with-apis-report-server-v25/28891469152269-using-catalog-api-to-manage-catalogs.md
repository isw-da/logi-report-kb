---
title: "Using Catalog API to Manage Catalogs"
id: 28891469152269
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891469152269-Using-Catalog-API-to-Manage-Catalogs
updated_at: 2026-02-26T02:10:58Z
source_host: docs-report.zendesk.com
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
