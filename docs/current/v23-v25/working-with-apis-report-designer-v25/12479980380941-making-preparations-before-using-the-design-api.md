---
title: "Making Preparations Before Using the Design API"
id: 12479980380941
section: "Working with APIs - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479980380941-Making-Preparations-Before-Using-the-Design-API
updated_at: 2026-02-25T23:50:50Z
source_host: docs-report.zendesk.com
---
# 
Making Preparations Before Using the Design API

Before you can use the Design API to perform tasks, you need to first make some preparations. This topic describes what you need to do before working with reports via the Design API.

This topic contains the following sections:

- Setting the License Key

- Getting a Catalog API Instance

- Getting Handle Information

## 
Setting the License Key

You can set the license information using the setUserInfo(String uid, String key) method, where uid is the user ID, and key is the license key. You should call this method before you can call any other Design API methods. The UID is the license user ID you receive with the purchase of Server and Designer. The license key is either the Server Designer License Key or Designer License Key depending on the class path setting to <server_install_root>\lib or <designer_install_root>\lib respectively. 

 DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key);
  Designer desg = new Designer(catalogPath, catalogName, userInfo); // For creating page report 
  MultipliedDesigner md = new MultipliedDesigner(path, catName, Designer.CAT, userInfo); // For creating web report 

## 
Getting a Catalog API Instance
        

Before working with reports using the Design API, you need to specify the catalog in which you save them. You can use the public CatalogAPI getCatalogAPI() method to get a Catalog API instance.

## 
Getting Handle Information        

Report organizes all the objects in a report  and browses them from a tree structure. For each report, the Report Inspector consists of a report object tree  and the corresponding object properties. Selecting any object node on the tree also selects the same element in the report design area. The following diagrams cover all objects that you can use in a report with their relationships.

The Design API identifies every node and object in the trees by a HANDLE. Therefore, before you can create or edit a report with the Design API, you first need to get the handle information. Super class API provides the following methods to get handles of different nodes and different types:

- 
getHandles()
This method gets all the handles of a report and returns a handle array.

- 
getHandles(String handle)
This method gets handles of the subnode in the current node and returns a handle array. If it fails, it returns null.

- 
getHandles(String handle, int type)
This method gets subnode handles of the same types for the given node and returns a handle array. If it fails, it will return null.

- 
getHandles(String handle, int type, int depth)
This method gets subnode handles of the same types for the given node and returns a handle array. If it fails, it returns null.

- 
getParent(String handle)
This method gets the parent handle of an object and returns the parent handle. If it fails, it returns null.

Parameters in the methods: 

- 
handle
Parent node handle when getting subnode handles. Object handle when getting parent handle.

- 
type
Class type value defined in the API class.

- 
depth
This is related to the current level in the report tree. When the depth is -1, it returns all handles in the report; when the depth is 0, it returns the handles of the current level; when the depth is the number "n", it returns the handles of n levels and the current level.
