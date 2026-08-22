---
title: "Designing Reports with the Design API"
id: 1500010056562
section: "Working with APIs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056562-Designing-Reports-with-the-Design-API
updated_at: 2021-07-23T19:14:29Z
---

# Designing Reports with the Design API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093861-Getting-Started-Using-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093841-Running-the-Design-API-Samples)

# Designing Reports with the Design API

This topic introduces how you can use the Design API to perform different tasks on reports.

The class API is the root of the class hierarchy of the Design API (Design API and Catalog API). It is an abstract class and provides a series of editing methods for users. The Design API class has an API as a super class.

Designer is the principal class that manipulates reports. The application creates a Designer instance and calls the Designer methods to create or modify a report. For more information about the summary of FIELD, CONSTRUCTOR, and METHOD, see the jet.api package in the Logi Report Javadoc.

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

When creating reports, you should create the reports based on an existing catalog file; otherwise, you get an error.

* createReportSet(String name) -
  Creates a new page report with the specified name.
* addReport(String reportsetHandle, String name) -
  Creates a new report tab with the specified name in the specified page report.
* createWebReportSet(String reportsetName, String reportTabName) -
  Creates a new web report with the specified name. Creating a web report creates a report tab in the web report automatically.
* open(String name) -
  Opens an existing report and returns the handle of the report.
* close(String handle) -
  Saves any changes and closes the open report tab in the current page report.
* closeReportSet() -
  Saves any changes and closes the current report.
* quit(String handle) -
  Closes an open report without saving any changes.
* deleteReport(java.lang.String name) -
  Deletes an existing report with the specified name, and returns true if it successfully removes the report.

**Parameters**

* name - The name of the report or page report tab that is to be created, opened, or deleted.
* reportsetHandle - The handle of the page report into which the report tab is to be added.
* reportsetName - The name of the web report that is to be created.
* reportTabName - The report tab name in the web report that is to be created. Optional.
* handle - Ancestor handle of the open report or report tab.

## Inserting, Creating, Moving, and Deleting an Object in a Report

To insert an object in a report, you can use the following methods:

* insert(String parent, int type, String name) -
  Inserts an object into the parent node.
* insert(String parent, int type, String name, String mapping) -
  Inserts a DBField, parameter, formula, or summary into the parent node.
* insertTable(String parent, TableTemplateInfo info, boolean increasePanel) -
  Inserts a table into the parent node.
* insert(String parent, String name, CTRowColFieldInfo colInfo[], CTRowColFieldInfo rowInfo[], CTAggFieldInfo aggInfo[]) -
  Insert a crosstab object and its children into the parent node.
* insert(String parent, CTRowColFieldInfo colInfo, CTRowColFieldInfo rowInfo, CTAggFieldInfo aggInfo) -
  Inserts crosstab children into the crosstab.
* insert(String parent, String name, String paperName, int charttype, String gName1, String gName2, String value, ChartLegendInfo chartLegendInfo, ChartLabelInfo chartLabelInfo) -
  Inserts a chart object and its children into the parent node.
* insert (String parent, int type, String name, String topSection , String bottomSection) -
  Inserts a drawing object into the report and returns the handle of the new object.
* insert(String parent, String name, GroupInfo groupInfo) -
  Inserts a group/sort into the parent node.

To create and modify dynamic resources in a report, use the following methods:

* addDynamicFormula(String reportHandle, String datasetHandle, String formulaName, String expression, int useType, boolean isRawExpression) - Creates a dynamic formula in a report.
* addDynamicAggregation(String reportHandle, String datasetHandle, String aggregationName, String basedFieldName, String function) - Creates a dynamic aggregation in a report.
* modifyDynamicFormula(String formulaHandle, FormulaInfo formulaInfo, int useType, boolean isRawExpression) - Changes the definition of a dynamic formula according to the new information.
* modifyDynamicAggregation(String aggHandle, BVAggregationInfo aggInfo) - Changes the definition or display name of a dynamic aggregation.
* compileDynamicFormulas(String objHandle) - Compiles the dynamic formulas for an object. If the object is a report, the method complies all the dynamic formulas in the report.

To change the position of an object, use the following method:

* public boolean changeZOrder(String objectHandle,
  int zorderType) - Moves an object to front/back, or forward/backward.

To delete an object from a report, use the following method:

* delete(String handle) -
  Deletes an object from its parent node.

**Parameters**

* parent - Parent handle node.
* type - Class type that you want to insert.
* name - Instance name of the new object.
* mapping - Mapping name of the database field, parameter, formula, or summary.
* info - The table information including the information of the data, group, or columns in the table.
* increasePanel - Indicates whether to increase the bounds when the table is out of the panel bounds. If the parameter is true, the corresponding method increases the page width according to the table's width and position; if it is false, the method adjusts the table and its columns' width to fit the page.
* colInfo - Field information array of the column.
* rowInfo - Field information array of the row.
* aggInfo - Field information array of the aggregate.
* paperName - Instance name of the ChartCoordinatepaper object.
* charttype - Type of the chart.
* group1 - Mapping name of the first group.
* group2- Mapping name of the second group. It can be null.
* value - Mapping name of a summary.
* chartLegendInfo - Field information array of the chart legend.
* chartLabelInfo - Field information array of the chart title and notes.
* topSection - Handle of the top section attached by the shape.
* bottomSection - Handle of the bottom section attached by the shape.
* groupInfo - The group information.
* reportHandle - The handle of a report.
* datasetHandle - The handle of a dataset.
* formulaName - The display name of a dynamic formula.
* expression - The expression and function in String format.
* useType - The element type that a dynamic formula is used as, which can be a detail, group, or an aggregation object.
* isRawExpression - Specifies whether to create an uncompiled formula or not. If the parameter is false, the corresponding method compiles the formula expression and starts a javac thread.
* aggregationName - The display name of a dynamic aggregation.
* basedFieldName - The qualified display name of a field.
* function - The function name of a dynamic aggregation.
* formulaHandle - The handle of a dynamic formula.
* formulaInfo - The new information of a dynamic formula.
* aggHandle - The handle of a dynamic aggregation.
* aggInfo - The new information of a dynamic aggregation.
* objHandle - The handle of an object.
* objectHandle - Handle of the object whose z-order is to be moved.
* zorderType - Direction to which to move the object.
* handle - Handle of the object that is to be deleted.

## Getting and Setting Object Property Information

You can use the following methods to get the property values of different types and return the property value:

* getInt(String handle, String name)
* getLong(String handle, String name)
* getFloat(String handle, String name)
* getDouble(String handle, String name)
* getString(String handle, String name)
* getBool(String handle, String name)
* getColor(String handle, String name)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can use the getControlFields(String handle, String name) method to get fields that can control property values at runtime.

You can use the following methods to get the property name and type, and check property name:

* getPropType(String handle, String name) -
  Gets and returns the property type defined in the Designer class.
* getPropnames(String handle) -
  Gets property names and returns a name array.
* containPropName(String handle, String name) -
  Checks whether the property name exists. If it exists, the method returns true.

You can use the following methods to change the property values of different types. They return true if the value is changed.

* set(String handle, String name, Boolean value)
* set(String handle, String name, int value)
* set(String handle, String name, long value)
* set(String handle, String name, float value)
* set(String handle, String name, double value)
* set(String handle, String name, String value)
* set(String handle, String name, Color value)
* setReference(String handle, String name, String refHandle) - Changes the reference property value of an object.

You can use the following methods to get and set the property values using fields and formulas.

* getControlField(String handle, String propertyName) - Gets the field or expression that controls the property value at runtime.
* getControlFields(String handle, String propertyName) -
  Gets all available fields that you can use to control the property value at runtime.
* setControlFields(String handle, String propertyName, String field) - Sets the field to control the property value at runtime.
* getAvailableDynamicFormulas(String handle, String propertyName) - Gets all available dynamic formulas that you can use to control the value of a property of an object at runtime.
* setControlledByDynamicFormula(String handle, String propertyName, String fmlDisplayName) - Sets the dynamic formula to control the property value at runtime.
* setControlledByExpression(String handle, String propertyName, String expression) - Sets the expression to control the property value at runtime.
* isPropertyControlledByOther(String handle, String propertyName) - Indicates whether or not the specified property value is controlled by the runtime value.

**Parameters**

* handle - Object handle.
* propertyName - The property name.
* value - Property value.
* refHandle - Referenced object handle.
* field - The mapping name of a DBField or qualified display name of a business view element.
* fmlDisplayName - The display name of a dynamic formula.
* expression - The expression statement.

## Getting Report Metadata Information

You can use the method
*getDataSet()* to get the dataset information. The method returns the dataset object. Then you can get the following report metadata information from the dataset: basic information, query information, business view information, and data buffer information.

You can use the following methods to get the basic information:

* getName() -
  Returns the dataset name.
* getDataSourceName() -
  Returns the name of the data resource used to build the data component.
* getResourceType() -
  Returns the resource type. 1 means query, 2 means business view, and 3 means business/report cube.
* getBlName() -
  Returns the information of the query, imported SQL, stored procedure, user-defined data source, business view, or business/report cube used to build the data component.
* getMaxRecords() -
  Returns the maximum number of records you want to display for all of the data components using this dataset.
* setMaxRecords(int maxRecords) -
  Sets the maximum number of records.
* getDataDriver() -
  Returns the path of the cached query result file that is used as the data resource.
* setDataDriver(String dataDriver) -
  Sets the path of the cached query result file.
* getSecurityPolicyName() -
  Returns the security policy name that is applied to the data component.
* setSecurityPolicyName(String securityPolicyName) -
  Sets the security policy name.

You can use the following methods to get information of the query, imported SQL, or other data objects that are used to create the dataset.

* getQueriableName() -
  Returns the name of the query, imported SQL, stored procedure, or user-defined data source.
* getDataFieldNames() -
  Returns a collection of data field mapping names that the dataset uses.

You can use the following methods to get the business view information that is used to create the dataset.

* getBVName() -
  Returns the business view name.
* getQueriableName() -
  Returns the name of the query, imported SQL, stored procedure, or user-defined data source that the business view uses.
* getElementNames() -
  Returns a collection of the qualified names of the business view elements that the dataset uses.
* getDisplayName(String qualifiedName) -
  Returns the display name of the business view element that has the qualified name.
* getMappingName(String qualifiedName) -
  Returns the mapping name of the queriable object data field used to create business view element that has the qualified name.

You can use the following methods to get the data buffer information:

* getMaxPageNumber() -
  Returns the maximum number of pages in the data buffer.
* setMaxPageNumber(int maxPageNumber) -
  Sets the maximum number of pages.
* getRecordsPerPage() -
  Returns the number of records in each page in the data buffer.
* setRecordsPerPage(int recordsPerPage) - Sets the number of records in each page.

## Getting Objects and Object Information

* getDBFields(String handle) -
  Gets DBFields that you can use in the report and returns a mapping name array.
* getFormulae(String handle) -
  Gets formulas that you can use in the report and returns a mapping name array.
* getSummaries(String handle) -
  Gets summaries that you can use in the report and returns a mapping name array.
* getParameter() -
  Gets parameters in the catalog and returns a mapping name array.
* getQueries() -
  Gets queries in the catalog and returns a mapping name array.
* getQueryName(String handle) -
  Gets the query name of a report.
* getProcedures() -
  Gets stored procedures in the catalog and returns a mapping name array.
* getSections(String handle, boolean visible), getSections(String handle) -
  Gets handles of sections in a report.
* getGroups(String handle) -
  Gets handles of groups in a report.
* getGroupInfo(String handle) -
  Gets the group information in a report.
* getReportSortInfo(String handle) -
  Gets the sort information of a report.
* getSortInfo(java.lang.String handle) -
  Gets the sort information of a group.
* getSQLs() -
  Gets the SQLs in the catalog.
* getUDS() -
  Gets the UDSs in the catalog.
* getViews() -
  Gets the viewss in the catalog.
* getObjectType(String handle) -
  Gets the type information of an object.
* getObjectInfo(String handle) -
  Gets the handle of an object in a report.
* getInstanceName(String handle) -
  Gets the instance name of an object and returns the instance name. If the operation fails, the method returns null.
* getClassType(String handle) - Gets the class type of an object and returns one of the class type values that are defined in the Designer class. If an error or a warning occurs, the method returns UNKNOWN.
* getDataSetInfo(String objHandle) - Gets the dataset information of an object.
* getDataSetInfos(String reportHandle) - Gets the dataset information of a report.
* getAvailableDynamicFormulas(String handle) - Gets all available dynamic formulas for an object.
* getDynamicFormulaInfo(String fmlHandle) - Gets the information of a dynamic formula.
* getDynamicFormulaNames(String reportHandle, String datasetHandle) - Gets the display names of all dynamic formulas defined for a report and dataset.
* getDynamicFormulaHandles(String reportHandle, String datasetHandle) - Gets the handles of all dynamic formulas defined for a report and dataset.
* getDynamicAggregationInfo(String aggHandle) - Gets the information of a dynamic aggregation.
* getDynamicAggregationNames(String reportHandle, String datasetHandle) - Gets the display names of all dynamic aggregations defined for a report and dataset.
* getDynamicAggregationHandles(String reportHandle, String datasetHandle) - Gets the handles of all dynamic aggregations defined for a report and dataset.

**Parameters**

* handle/objHandle - Object handle.
* visible - A Boolean type parameter which specifies that the section is visible.
* reportHandle - The handle of a report.
* fmlHandle - The handle of a dynamic formula.
* datasetHandle - The handle of a dataset.
* aggHandle - The handle of a dynamic aggregation.

## Marks content and feature updates for Logi Report v17.1. New feature new content.Setting, Getting, and Clearing Filters in a Report

You can use the following methods to set, get, and clear the filters that apply to the datasets and data components in a report.

* public boolean setDatasetFilter(String datasetHandle, ExpressionNode filterInfo) - Sets the filters to be applied to the specified dataset of the report.
* public ExpressionNode getDatasetFilter(String datasetHandle) - Gets the filters applied to the specified dataset of the report.
* public void clearDatasetFilter(String datasetHandle) - Removes the filters applied to the specified dataset of the report.
* public boolean setDataContainerFilter(String dataContainerHandle, ExpressionNode filterInfo) - Sets the filters to be applied to the specified data component in the report.
* public ExpressionNode getDataContainerFilter(String dataContainerHandle) - Gets the filters applied to the specified data component in the report.
* public void clearDataContainerFilter(String dataContainerHandle) - Removes the filters applied to the specified data component in the report.
* public boolean setDatasetBLFilter(String datasetHandle, BLFilterInformation filterInfo) - Specifies the predefined filter of a business view to apply to the dataset that is based on the business view in the report.
* public BLFilterInformation getDatasetBLFilter(String datasetHandle) - Gets the predefined filter of a business view applied to the dataset that is based on the business view in the report.
* public boolean setBrowserFilter(String dataContainerHandle, ExpressionNode filterInfo) - Sets the filter to be applied to the specified data component in the report, which takes effect when you run the report on the Web.
* public ExpressionNode getBrowserFilter(String dataContainerHandle)
  - Gets the filter applied to the specified data component in the report, which takes effect when you run the report on the Web.
* public void clearBrowserFilter(String dataContainerHandle) - Removes the filter applied to the specified data component in the report, which takes effect when you run the report on the Web.

Parameters

* datasetHandle - The handle of the dataset.
* ExpressionNode filterInfo - The filter information which defines an abstract node for Expression and Expression Group.
* dataContainerHandle - The handle of the data component, such as a table, crosstab, and chart.
* BLFilterInformation filterInfo - The predefined filter information of the business view, which contains the filter information and the filter expression.

## Getting Editing Information

* getWarning() -
  Gets and returns the warning message. If the operation is successful, the method returns null.
* clearWarning() -
  Clears the warning message.
* getError() -
  Gets and returns the error message. If the operation is successful, the method returns null.
* clearError() -
  Clears the error message.
* clearMsg() -
  Clears all warning and error messages.
* setLog(OutputStream log, String encoding) -
  Sets the log to get error, debug, and other information.
* writeLog(String msg) -
  Writes all messages to the log.
* closeLog() throws IOException -
  Closes the log.

## Working with Library Components

The entry API for working with library components is *getLCEditor()*. All the following operations use it as the entry.

* createLC(String titleText) -
  Creates a new library component.
* addDataset(String name, String datasourceName, String BVName) -
  Creates a new dataset from a business view.
* setDataset(String objHandle, String datasetHandle) -
  Applies an existing dataset used in the library component to the data component. It returns true if the dataset is bound to the data component successfully; otherwise false.
* insertTable(TableTemplateInfo info, boolean increasePanel) -
  Inserts a new table into the library component.
* insertChart(ChartInfo info, String datasetName) -
  Inserts a new chart into the library component.
* insertCrossTab(CrossTabInfo info) -
  Inserts a new crosstab into the library component.
* insertImage(String imageName) -
  Inserts an image into the library component. The image must be in the same folder as the catalog.
* insertLabel(String text) -
  Inserts a label into the library component.
* insertSpecialField(int fieldType) -
  Inserts a special field into the library component.
* saveLC(String lcFileName) -
  Saves the library component into the specified file (.lc).
* loadLC(String lcFileName) -
  Loads the library component from the specified file (.lc).
* close(String handle) -
  Closes the specified library component and clears all resources of the library component. It returns true if the library component is closed successfully; otherwise false.
* quit() -
  Quits from the library component editor and clears all resources of the editor.

**Parameters**

* titleText - The title of the library component to be created.
* name - The dataset's instance name.
* datasourceName - The name of the data source that the required query belongs to.
* BVName - The name of the business view that the dataset is based on.
* objHandle - The handler string of the data component.
* datasetHandle - The handler string of the existing dataset.
* info - The class that defines the information of the table, chart, or crosstab, such as its data, properties, columns, rows, groups, aggregations, and their properties.
* increasePanel - Indicates whether to increase the bounds when the table is out of the panel bounds. If the parameter is true, the corresponding method increases the page width according to the table's width and position; if it is false, the method adjusts the table and its columns' width to fit the page.
* datasetName - The dataset's instance name.
* imageName - The name of the image to be inserted.
* text - The text of the label to be inserted.
* fieldType - The int value of the field type. The constants can be:
  + USERNAME
  + PRINTDATE
  + PRINTTIME
  + FETCHDATE
  + FETCHTIME
  + MODIFIEDDATE
  + MODIFIEDTIME
  + RECORDNUMBER
  + GROUPNAME
  + GROUPNUMBER
  + GROUPNUMBERS
  + PAGENUMBER
  + PAGENUMBERS
  + SQLSTATMENT
* lcFileName - The library component file name (.lc) with full path.
* handle - The handle of the library component object.

## Exiting from the Editing Status

After finishing using the Design API each time, you need to call the following methods to exiting from the editing status.

* exit() -
  Exits from the editing status, releases all the resources, and saves all reports and the catalog.

* quit() -
  Quits the editing status without saving and releases all resources. The method returns false if it fails; otherwise true.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093861-Getting-Started-Using-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093841-Running-the-Design-API-Samples)
