---
title: "Making Preparations Before Using the Catalog API"
id: 45190394380813
section: "Working with APIs - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190394380813-Making-Preparations-Before-Using-the-Catalog-API
updated_at: 2026-04-30T15:11:52Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Making Preparations Before Using the Catalog API

Before you can use the Catalog API to perform tasks, you need to create a Designer object and then get a Catalog API instance. This topic describes how you can make the preparations for using the Catalog API.

This topic contains the following sections:

- Creating a Designer Object

- Getting a Catalog API Instance

## 
Creating a Designer Object

To create a Designer object, use the constructor Designer(String path, String name, DesignerUserInfo user) in the Design API. The constructor has three parameters: the catalog path, catalog name, and the user ID and license key provided by Logi Analytics. The path should be a valid path of an existing directory. The catalog name can be the name of an existing catalog when you want to open a catalog, or the name of a new catalog when you want to create a catalog. If you want to create a new catalog, the path should not already contain a catalog file.

To create the DesignerUserInfo instance, use the following constructor with the user ID and the Designer License Key or Server Designer License Key  you receive when you purchase Report.

DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key); 

 

## 
Getting a Catalog API Instance

To get a Catalog API instance, use the getCatalogAPI() method in the Design API. You need to first get an instance from Designer as follows:

Designer desg = new Designer(catalogPath, catalogName, userInfo);
CatalogAPI catalog = desg.getCatalogAPI();
