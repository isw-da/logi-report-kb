---
title: "Getting Objects and Object Information"
id: 1500009562482
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562482-Getting-Objects-and-Object-Information
updated_at: 2021-07-24T05:56:18Z
---

# Getting Objects and Object Information

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582841-Getting-Report-Metadata-Information)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582801-Getting-Editing-Information)

# Getting Objects and Object Information

The following methods are used to get objects and object information:

* **getDBFields(String handle)**  
   Gets DBFields that can be used in the report and returns a mapping name array.
* **getControlFields(String handle, String name)**  
   Gets fields that control property values at runtime.
* **getFormulae(String handle)**  
   Gets formulas that can be used in the report and returns a mapping name array.
* **getSummaries(String handle)**  
   Gets summaries that can be used in the report and returns a mapping name array.
* **getParameter()**  
   Gets parameters in the catalog and returns a mapping name array.
* **getQueries()**  
   Gets queries in the catalog and returns a mapping name array.
* **getQueryName(String handle)**  
   Gets the query name of a report.
* **getProcedures()**  
   Gets stored procedures in the catalog and returns a mapping name array.
* **getSections(String handle, boolean visible), getSections(String handle)**  
   Gets handles of sections in a report.
* **getGroups(String handle)**  
   Gets handles of groups in a report.
* **public GroupInfo[] getGroupInfo(String handle)**  
   Gets the group information in a report.
* **public ReportSortInfo****getReportSortInfo(String handle)**  
   Gets the sort information of a report.
* **public SortInfo[] getSortInfo(java.lang.String handle)**  
   Gets the sort information of a group.
* **getSQLs()**  
   Gets the SQLs in the catalog.
* **getUDS()**  
   Gets the UDSs in the catalog.
* **getViews()**  
   Gets the viewss in the catalog.
* **getObjectType(String handle)**  
   Gets the type information of an object.
* **getObjectInfo(String handle)**  
   Gets the handle of an object in a report.
* **getInstanceName(String handle)**  
   Gets the instance name of an object, and returns the instance name. If it fails, it will return null.
* **getClassType(String handle)**  
   Gets the class type of an object and returns one of the class type values that are defined in the Designer class. If an error or a warning occurs, it will return UNKNOWN.

**Parameters**

* handle - Object handle.
* name - The property name.
* visible - A Boolean type parameter which specifies that the section is visible.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582841-Getting-Report-Metadata-Information)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582801-Getting-Editing-Information)
