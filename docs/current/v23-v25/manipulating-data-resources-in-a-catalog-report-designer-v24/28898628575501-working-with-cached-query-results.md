---
title: "Working with Cached Query Results"
id: 28898628575501
section: "Manipulating Data Resources in a Catalog - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898628575501-Working-with-Cached-Query-Results
updated_at: 2024-09-30T09:10:00Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Working with Cached Query Results

By default, when you run a report, Report Engine fetches data from the database for the report, thus if you are offline and do not have a database connection, you would not be able to load the report data. To help you avoid the inconvenience, Report provides the Cached Query Result feature, which enables you to create cached result files for queries (and also imported SQLs, stored procedures, user-defined data sources, and business views that function similarly as queries), save them somewhere in your machine, and apply them to your reports that use the queries. Then, when you view the reports, Report Engine fetches data from the files as opposed to the database. This is very useful for working on the design of a report while you are offline. It is also helpful when you have problems with your reports and need to send the reports with data resources to Logi Analytics for reproducing the problems. This topic describes how you can create cached query results, apply them to reports, and generate data source drivers for cached query results.

This topic contains the following sections:

- Creating Cached Query Results

- Applying Cached Query Results

- Generating Data Source Drivers for Cached Query Results

## 
Creating Cached Query Results

You can  create cached query results either in the Catalog Manager or in the Data panel.

- 
Creating a cached query result file in the Catalog Manager
- In the Catalog Manager, select the query for which you intend to create the cached query result file.

- Right-click the query, and select Create Cached Query Result from the shortcut menu. 

- In the Save Cached Query Result dialog box, specify the file name with or without an extension and the folder where you want to save the result file. You may want to use an extension such as .cqr to help you identify the files. Designer does not provide a default extension. 

- Select Save to save the cached query result file to the specified folder.

- 
Creating a cached query result file in the Data panel
- In the Data panel, right-click the query and select Create Cached Query Result from the shortcut menu.

- In the Save Cached Query Result dialog box, specify the file name with or without an extension and the folder where you want to save the result file and then select Save.

## 
Applying Cached Query Results

To run a library component or a query-based page report using cached query result, you can set the Data Driver property of the dataset appropriately in the Report Inspector. You can specify the property value by typing manually or selecting a predefined data source driver from the drop-down list. 

The input format is: jrquery:/jet.universe.resultfile.UResultFileResultSet;full_path_of_cached_query_result

For example, if you save the cached query result  to C:\LogiReport\Designer\Cached with the file name "test", the property value should be jrquery:/jet.universe.resultfile.UResultFileResultSet;C:\LogiReport\Designer\Cached\test.

However, the Data Driver property is not available to web reports and business view-based page reports . In order to apply cached query result to them, you can select the option Use cached query result in the Catalog category of the Options dialog box. Then whenever you preview a report in Designer, Designer displays a dialog box for you to choose a cached query result to run the report.

## 
Generating Data Source Drivers for Cached Query Results

When specifying the Data Driver property for a dataset, you may find it inconvenient to type a property value that is long and complicated. To help you with this,  Designer provides a tool for generating data source drivers for cached query results, and displays the drivers you generate in the Data Driver property's value drop-down list for selection. 

Assuming that you have created a cached query result file "orderstat_cached" for the query OrderStat in the catalog file SampleReports.cat and saved it in C:\LogiReport\Designer\Cached, to create a data source driver for the cached query result, take the following steps: 

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- In the Catalog Manager, select Data Source Drivers  on the toolbar. Designer displays the Data Source Drivers dialog box.
    

- Select New. Designer displays the Data Source Editor dialog box.
    

- Type a name for the driver in the Driver Name text box. Here, we name it OrderStat.

- Select URL and type the URL. The URL should be in the following format:
    jrquery:/jet.universe.resultfile.UResultFileResultSet;Fullpath_of_cached_query_result

In the example, the URL is jrquery:/jet.universe.resultfile.UResultFileResultSet;C:\LogiReport\Designer\Cached\orderstat_cached

 If you select Driver  to specify the driver, you need to specify the class name and parameter of the driver.      
- 
Class Name: jet.universe.resultfile.UResultFileResultSet

- 
Parameter: Full path of the cached query result (C:\LogiReport\Designer\Cached\orderstat_cached in this example)

Then, Designer generates a URL according to the information you specify.

- Select OK to add the driver.

- Select OK in the Data Source Drivers dialog box to close it.

- Now you can select the driver from the Data Driver property's value drop-down list, without having to type the long value manually.

Previous Topic  Next Topic
