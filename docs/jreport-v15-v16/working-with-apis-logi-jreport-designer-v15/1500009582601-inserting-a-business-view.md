---
title: "Inserting a Business View"
id: 1500009582601
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582601-Inserting-a-Business-View
updated_at: 2021-07-24T05:56:23Z
---

# Inserting a Business View

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582721-Inserting-a-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562222-Inserting-a-Formula-Summary-Parameter-or-a-WHERE-Portion)

# Inserting a Business View

To insert a business view, use the following method:

* insertBusinessView(String dataSourceName, String queriableName, String businessViewName, boolean isLogicView=false)

**Parameters**

* dataSourceName - The mapping name of the data source in the catalog to which you want to insert the object.
* queriableName - The queriable object's mapping name. The queriable object in Logi JReport catalog could be a query, UDS, stored procedure or imported SQL. When queriableName is a valid name of an existing queriable object, a business view will be created.
* businessViewName - The name of the business view.
* isLogicView - Indicates whether to insert a business view. When it is false, a business view will be created.

When you have a business view created successfully, you can then add elements into it. A business view can contain the following elements: categories, group objects, aggregation objects and detail objects。

The following methods are used to insert a view element into a business view and to return the handle of the newly inserted object if it is inserted successfully, otherwise null if there is a failure:

* insertBusinessViewCategory(String parentHandle, BusinessViewCategoryInfo info)
* insertBusinessViewGroup(String parentHandle, BVGroupInfo info)
* insertBusinessViewAggregation(String parentHandle, BVAggregationInfo info)
* insertBusinessViewDetail(String parentHandle, BVDetailInfo info)

**Parameters**

* parentHandle - The handle of the parent object. It can be a business view or a category.
* info - The definition class of the view element. It can contain its children's definition.

**See an example:** The sample TestCatalogBC.java in `<install_root>\help\samples\APICatalog` shows how to create a business view using the Catalog API.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582721-Inserting-a-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562222-Inserting-a-Formula-Summary-Parameter-or-a-WHERE-Portion)
