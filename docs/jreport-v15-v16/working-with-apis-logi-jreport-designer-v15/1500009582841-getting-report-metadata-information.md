---
title: "Getting Report Metadata Information"
id: 1500009582841
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582841-Getting-Report-Metadata-Information
updated_at: 2021-07-24T05:56:19Z
---

# Getting Report Metadata Information

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562502-Getting-Property-Information)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562482-Getting-Objects-and-Object-Information)

# Getting Report Metadata Information

Dataset information can be got by the method
getDataSet(), which returns the dataset object. Then, the following report metadata information can be retrieved from the dataset:

> * [Basic Information](#Basic)
> * [Query Information](#Query)
> * [Business View Information](#View)
> * [Data Buffer Information](#Buffer)

## Getting Basic Information

* **getName()**  
   Returns the dataset name.
* **getDataSourceName()**  
  Returns the name of the data source used to build the data component.
* **getResourceType()**  
  Returns the resource type. 1 means query, 2 means business view, and 3 means business/report cube.
* **getBlName()**  
   Returns the information of the query, imported SQL, stored procedure, user defined data source, business view, or business/report cube used to build the data component.
* **getMaxRecords()**  
  Returns the maximum number of records you want to display for all of the data components using this dataset.
* **setMaxRecords(int maxRecords)**  
   Sets the maximum number of records.
* **getDataDriver()**  
  Returns the path of the cached query result file that is used as the data resource.
* **setDataDriver(String dataDriver)**  
  Sets the path of the cached query result file.
* **getSecurityPolicyName()**  
  Returns the security policy name that is applied to the data component.
* **setSecurityPolicyName(String securityPolicyName)**  
  Sets the security policy name.

## Getting Query Information

The following methods are used to get information of the query, imported SQL or other data objects that are used to create the dataset.

* **getQueriableName()**  
   Returns the name of the query, imported SQL, stored procedure, or user defined data source.
* **getDataFieldNames()**  
  Returns a collection of data field mapping names that the dataset uses.

## Getting Business View Information

The following methods are used to get the business view information that is used to create the dataset.

* **getBVName()**  
  Returns the business view name.
* **getQueriableName()**  
  Returns the name of the query, imported SQL, stored procedure, or user defined data source that is used to create the business view.
* **getElementNames()**  
  Returns a collection of the qualified names of the business view elements that the dataset uses.
* **getDisplayName(String qualifiedName)**  
  Returns the display name of the business view element that has the qualified name.
* **getMappingName(String qualifiedName)**  
  Returns the mapping name of the queriable object data field used to create business view element that has the qualified name.

## Getting Data Buffer Information

* **getMaxPageNumber()**  
   Returns the maximum number of pages in the data buffer.
* **setMaxPageNumber(int maxPageNumber)**  
  Sets the maximum number of pages.
* **getRecordsPerPage()**  
  Returns the number of records in each page in the data buffer.
* **setRecordsPerPage(int recordsPerPage)**  
  Sets the number of records in each page.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562502-Getting-Property-Information)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562482-Getting-Objects-and-Object-Information)
