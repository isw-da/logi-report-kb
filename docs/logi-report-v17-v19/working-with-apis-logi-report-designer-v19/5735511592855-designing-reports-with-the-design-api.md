---
title: "Designing Reports with the Design API"
id: 5735511592855
section: "Working with APIs - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735511592855-Designing-Reports-with-the-Design-API
updated_at: 2022-11-02T08:17:09Z
---

# Designing Reports with the Design API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526762007-Getting-Started-Using-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735498221463-Running-the-Design-API-Samples)

# Designing Reports with the Design API

This topic introduces how you can use the Design API to perform different tasks on reports.

The class API is the root of the class hierarchy of the Design API (Design API and Catalog API). It is an abstract class and provides a series of editing methods for users. The Design API class has an API as a super class.

Designer is the principal class that manipulates reports. The application creates a Designer instance and calls the Designer methods to create or modify a report. For more information about the summary of FIELD, CONSTRUCTOR, and METHOD, see the jet.api package in the Logi Report Java API Documentation.

This topic contains the following sections:

* [Creating, Opening, Closing, and Deleting a Report](#Report)
* [Inserting, Creating, Moving, and Deleting an Object in a Report](#Object)
* [Getting and Setting Object Property Information](#Property)
* [Getting Report Metadata Information](#Metadata)
* [Getting Objects and Object Information](#ObjectInfo)
* [Setting, Getting, and Clearing Filters in a Report](#Filter)
* [Getting Editing Information](#EditInfo)
* [Working with Library Components](#LC)
* [Exiting from the Editing Status](#Exit)

## Creating, Opening, Closing, and Deleting a Report

You can use the following methods to manage reports in a catalog.

* **createReportSet(String name)**  
  This method creates a new page report with the specified name.
* **addReport(String reportsetHandle, String name)**  
  This method creates a new report tab with the specified name in the specified page report.
* **createWebReportSet(String reportsetName, String reportTabName)**  
  This method creates a new web report with the specified name. Creating a web report creates a report tab in the web report automatically.
* **open(String name)**  
  This method opens an existing report and returns the handle of the report.
* **close(String handle)**  
  This method saves any changes and closes the open report tab in the current page report.
* **closeReportSet()**  
  This method saves any changes and closes the current report.
* **quit(String handle)**  
  This method closes an open report without saving any changes.
* **deleteReport(java.lang.String name)**  
  This method deletes an existing report with the specified name, and returns "true" if the report is successfully removed.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you create reports, you should create the reports based on an existing catalog file; otherwise, you get an error.

## Inserting, Creating, Moving, and Deleting an Object in a Report

You can use the following methods to perform operations on the objects in a report.

* **insert(String parent, int type, String name)**  
  This method inserts an object into the parent node.
* **insert(String parent, int type, String name, String mapping)**  
  This method inserts a DBField, parameter, formula, or summary into the parent node.
* **insertTable(String parent, TableTemplateInfo info, boolean increasePanel)**  
  This method inserts a table into the parent node.
* **insert(String parent, String name, CTRowColFieldInfo colInfo[], CTRowColFieldInfo rowInfo[], CTAggFieldInfo aggInfo[])**  
  This method inserts a crosstab object and its children into the parent node.
* **insert(String parent, CTRowColFieldInfo colInfo, CTRowColFieldInfo rowInfo, CTAggFieldInfo aggInfo)**  
  This method inserts crosstab children into the crosstab.
* **insert(String parent, String name, String paperName, int charttype, String gName1, String gName2, String value, ChartLegendInfo chartLegendInfo, ChartLabelInfo chartLabelInfo)**  
  This method inserts a chart object and its children into the parent node.
* **insert (String parent, int type, String name, String topSection , String bottomSection)**  
  This method inserts a drawing object into the report and returns the handle of the new object.
* **insert(String parent, String name, GroupInfo groupInfo)**  
  This method inserts a group/sort into the parent node.
* **addDynamicFormula(String reportHandle, String datasetHandle, String formulaName, String expression, int useType, boolean isRawExpression)**   
  This method creates a dynamic formula in a report.
* **addDynamicAggregation(String reportHandle, String datasetHandle, String aggregationName, String basedFieldName, String function)**  
  This method creates a dynamic aggregation in a report.
* **modifyDynamicFormula(String formulaHandle, FormulaInfo formulaInfo, int useType, boolean isRawExpression)**   
  This method edits the definition of a dynamic formula according to the new information.
* **modifyDynamicAggregation(String aggHandle, BVAggregationInfo aggInfo)**  
  This method edits the definition or display name of a dynamic aggregation.
* **compileDynamicFormulas(String objHandle)**  
  This method compiles the dynamic formulas for an object. If the object is a report, the method complies all the dynamic formulas in the report.
* **public boolean changeZOrder(String objectHandle, int zorderType)**  
  This method changes the position of an object, for example, moves an object to front/back, or forward/backward.
* **delete(String handle)**  
  This method removes an object from its parent node.

## Getting and Setting Object Property Information

You can use the following methods to get the property values of different types and return the property value.

* getInt(String handle, String name)
* getLong(String handle, String name)
* getFloat(String handle, String name)
* getDouble(String handle, String name)
* getString(String handle, String name)
* getBool(String handle, String name)
* getColor(String handle, String name)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can use the *getControlFields(String handle, String name)* method to get fields that can control property values at runtime.

You can use the following methods to get the property name and type, and check property name.

* **getPropType(String handle, String name)**  
  This method gets and returns the property type defined in the Designer class.
* **getPropnames(String handle)**  
  This method gets property names and returns a name array.
* **containPropName(String handle, String name)**  
  This method checks whether the property name exists. If it exists, the method returns "true".

You can use the following methods to change the property values of different types. They return "true" if the value is changed.

* set(String handle, String name, Boolean value)
* set(String handle, String name, int value)
* set(String handle, String name, long value)
* set(String handle, String name, float value)
* set(String handle, String name, double value)
* set(String handle, String name, String value)
* set(String handle, String name, Color value)
* setReference(String handle, String name, String refHandle) - Changes the reference property value of an object.

You can use the following methods to get and set the property values using fields and formulas.

* **getControlField(String handle, String propertyName)**  
  This method gets the field or expression that controls the property value at runtime.
* **getControlFields(String handle, String propertyName)**  
  This method gets all available fields that you can use to control the property value at runtime.
* **setControlFields(String handle, String propertyName, String field)**  
  This method sets the field to control the property value at runtime.
* **getAvailableDynamicFormulas(String handle, String propertyName)**  
  This method gets all available dynamic formulas that you can use to control the value of a property for an object at runtime.
* **setControlledByDynamicFormula(String handle, String propertyName, String fmlDisplayName)**  
  This method sets the dynamic formula to control the property value at runtime.
* **setControlledByExpression(String handle, String propertyName, String expression)**  
  This method sets the expression to control the property value at runtime.
* **isPropertyControlledByOther(String handle, String propertyName)**  
  This method specifies whether the specified property value is controlled by the runtime value.

## Getting Report Metadata Information

You can use the *getDataSet()* method to get the dataset information. The method returns the dataset object. Then you can get the following report metadata information from the dataset: basic information, query information, business view information, and data buffer information.

You can use the following methods to get the basic information.

* **getName()**  
  This method returns the dataset name.
* **getDataSourceName()**  
  This method returns the name of the data resource used to build the data component.
* **getResourceType()**   
  This method returns the resource type. 1 means query, 2 means business view, and 3 means business/report cube.
* **getBlName()**  
  This method returns the information of the query, imported SQL, stored procedure, user-defined data source, business view, or business/report cube used to build the data component.
* **getMaxRecords()**  
  This method returns the maximum number of records you want to display for all of the data components using this dataset.
* **setMaxRecords(int maxRecords)**  
  This method sets the maximum number of records.
* **getDataDriver()**   
  This method returns the path of the cached query result file that is used as the data resource.
* **setDataDriver(String dataDriver)**  
  This method sets the path of the cached query result file.
* **getSecurityPolicyName()**  
  This method returns the security policy name that is applied to the data component.
* **setSecurityPolicyName(String securityPolicyName)**  
  This method sets the security policy name.

You can use the following methods to get information of the query, imported SQL, or other data objects that are used to create the dataset.

* **getQueriableName()**  
  This method returns the name of the query, imported SQL, stored procedure, or user-defined data source.
* **getDataFieldNames()**  
  This method returns a collection of data field mapping names that the dataset uses.

You can use the following methods to get the business view information that is used to create the dataset.

* **getBVName()**  
  This method returns the business view name.
* **getQueriableName()**  
  This method returns the name of the query, imported SQL, stored procedure, or user-defined data source that the business view uses.
* **getElementNames()**  
  This method returns a collection of the qualified names of the business view elements that the dataset uses.
* **getDisplayName(String qualifiedName)**  
  This method returns the display name of the business view element that has the qualified name.
* **getMappingName(String qualifiedName)**  
  This method returns the mapping name of the queriable object data field used to create business view element that has the qualified name.

You can use the following methods to get the data buffer information.

* **getMaxPageNumber()**   
  This method returns the maximum number of pages in the data buffer.
* **setMaxPageNumber(int maxPageNumber)**  
  This method sets the maximum number of pages.
* **getRecordsPerPage()**   
  This method returns the number of records in each page in the data buffer.
* **setRecordsPerPage(int recordsPerPage)**   
  This method sets the number of records in each page.

## Getting Objects and Object Information

You can use the following methods to get objects and object information.

* **getDBFields(String handle)**  
  This method gets DBFields that you can use in the report and returns a mapping name array.
* **getFormulae(String handle)**  
  This method gets formulas that you can use in the report and returns a mapping name array.
* **getSummaries(String handle)**  
  This method gets summaries that you can use in the report and returns a mapping name array.
* **getParameter()**  
  This method gets parameters in the catalog and returns a mapping name array.
* **getQueries()**  
  This method gets queries in the catalog and returns a mapping name array.
* **getQueryName(String handle)**  
  This method gets the query name of a report.
* **getProcedures()**  
  This method gets stored procedures in the catalog and returns a mapping name array.
* **getSections(String handle, boolean visible), getSections(String handle)**  
  This method gets handles of sections in a report.
* **getGroups(String handle)**  
  This method gets handles of groups in a report.
* **getGroupInfo(String handle)**  
  This method gets the group information in a report.
* **getReportSortInfo(String handle)**  
  This method gets the sort information of a report.
* **getSortInfo(java.lang.String handle)**  
  This method gets the sort information of a group.
* **getSQLs()**  
  This method gets the SQLs in the catalog.
* **getUDS()**  
  This method gets the UDSs in the catalog.
* **getViews()**   
  This method gets the viewss in the catalog.
* **getObjectType(String handle)**  
  This method gets the type information of an object.
* **getObjectInfo(String handle)**  
  This method gets the handle of an object in a report.
* **getInstanceName(String handle)**   
  This method gets the instance name of an object and returns the instance name. If the operation fails, the method returns null.
* **getClassType(String handle)**  
  This method gets the class type of an object and returns one of the class type values that are defined in the Designer class. If an error or a warning occurs, the method returns UNKNOWN.
* **getDataSetInfo(String objHandle)**  
  This method gets the dataset information of an object.
* **getDataSetInfos(String reportHandle)**  
  This method gets the dataset information of a report.
* **getAvailableDynamicFormulas(String handle)**  
  This method gets all available dynamic formulas for an object.
* **getDynamicFormulaInfo(String fmlHandle)**  
  This method gets the information of a dynamic formula.
* **getDynamicFormulaNames(String reportHandle, String datasetHandle)**   
  This method gets the display names of all dynamic formulas defined for a report and dataset.
* **getDynamicFormulaHandles(String reportHandle, String datasetHandle)**  
  This method gets the handles of all dynamic formulas defined for a report and dataset.
* **getDynamicAggregationInfo(String aggHandle)**   
  This method gets the information of a dynamic aggregation.
* **getDynamicAggregationNames(String reportHandle, String datasetHandle)**  
  This method gets the display names of all dynamic aggregations defined for a report and dataset.
* **getDynamicAggregationHandles(String reportHandle, String datasetHandle)**  
  This method gets the handles of all dynamic aggregations defined for a report and dataset.

## Setting, Getting, and Clearing Filters in a Report

You can use the following methods to set, get, and clear the filters that apply to the datasets and data components in a report.

* **public boolean setDatasetFilter(String datasetHandle, ExpressionNode filterInfo)**  
  This method sets the filters to be applied to the specified dataset of the report.
* **public ExpressionNode getDatasetFilter(String datasetHandle)**  
  This method gets the filters applied to the specified dataset of the report.
* **public void clearDatasetFilter(String datasetHandle)**  
  This method removes the filters applied to the specified dataset of the report.
* **public boolean setDataContainerFilter(String dataContainerHandle, ExpressionNode filterInfo)**  
  This method sets the filters to be applied to the specified data component in the report.
* **public ExpressionNode getDataContainerFilter(String dataContainerHandle)**  
  This method sets the filters applied to the specified data component in the report.
* **public void clearDataContainerFilter(String dataContainerHandle)**  
  This method removes the filters applied to the specified data component in the report.
* **public boolean setDatasetBLFilter(String datasetHandle, BLFilterInformation filterInfo)**  
  This method specifies the predefined filter of a business view to apply to the dataset that is based on the business view in the report.
* **public BLFilterInformation getDatasetBLFilter(String datasetHandle)**  
  This method gets the predefined filter of a business view applied to the dataset that is based on the business view in the report.
* **public boolean setBrowserFilter(String dataContainerHandle, ExpressionNode filterInfo)**  
  This method sets the filter to be applied to the specified data component in the report, which takes effect when you run the report on the Server.
* **public ExpressionNode getBrowserFilter(String dataContainerHandle)**  
  This method sets the filter to be applied to the specified data component in the report, which takes effect when you run the report on the Server.
* **public void clearBrowserFilter(String dataContainerHandle)**  
  This method removes the filter applied to the specified data component in the report, which takes effect when you run the report on the Web.

## Getting Editing Information

You can use the following methods to get editing information.

* **getWarning()**  
  This method gets and returns the warning message. If the operation is successful, the method returns null.
* **clearWarning()**  
  This method clears the warning message.
* **getError()**  
  This method gets and returns the error message. If the operation is successful, the method returns null.
* **clearError()**  
  This method clears the error message.
* **clearMsg()**  
  This method clears all warning and error messages.
* **setLog(OutputStream log, String encoding)**  
  This method sets the log to get error, debug, and other information.
* **writeLog(String msg)**  
  This method writes all messages to the log.
* **closeLog() throws IOException**  
  This method closes the log.

## Working with Library Components

The entry API for working with library components is *getLCEditor()*. All the following operations use it as the entry.

You can use the following methods to work with library components.

* **createLC(String titleText)**  
  This method creates a new library component.
* **addDataset(String name, String datasourceName, String BVName)**  
  This method creates a new dataset from a business view.
* **setDataset(String objHandle, String datasetHandle)**  
  This method applies an existing dataset used in the library component to the data component. It returns "true" if the dataset is bound to the data component successfully; otherwise, it returns "false".
* **insertTable(TableTemplateInfo info, boolean increasePanel)**  
  This method inserts a new table into the library component.
* **insertChart(ChartInfo info, String datasetName)**  
  This method inserts a new chart into the library component.
* **insertCrossTab(CrossTabInfo info)**  
  This method inserts a new crosstab into the library component.
* **insertImage(String imageName)**  
  This method inserts an image into the library component. The image must be in the same folder as the catalog.
* **insertLabel(String text)**  
  This method inserts a label into the library component.
* **insertSpecialField(int fieldType)**  
  This method inserts a special field into the library component.
* **saveLC(String lcFileName)**   
  This method saves the library component into the specified file (.lc).
* **loadLC(String lcFileName)**  
  This method loads the library component from the specified file (.lc).
* **close(String handle)**  
  This method closes the specified library component and clears all resources of the library component. It returns "true" if the library component is closed successfully; otherwise, it returns "false".
* **quit()**  
  This method quits from the library component editor and clears all resources of the editor.

## Exiting from the Editing Status

After finishing using the Design API each time, you need to call the following methods to exiting from the editing status.

* **exit()**  
  You can use this method to exit from the editing status, release all the resources, and save all reports and the catalog.

* **quit()**  
  You can use this method to quit the editing status without saving and release all resources. The method returns "false" if it fails; otherwise, it returns "true".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526762007-Getting-Started-Using-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735498221463-Running-the-Design-API-Samples)
