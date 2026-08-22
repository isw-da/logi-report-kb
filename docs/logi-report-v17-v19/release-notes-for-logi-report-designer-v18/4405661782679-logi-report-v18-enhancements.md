---
title: "Logi Report v18 Enhancements"
id: 4405661782679
section: "Release Notes for Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661782679-Logi-Report-v18-Enhancements
updated_at: 2022-01-27T20:34:48Z
---

# Logi Report v18 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664606871-Logi-Report-v18-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664317847-Logi-Report-Designer-Guide-v18-Overview)

# Logi Reportv18 Enhancements

This topic introduces the significant features of Logi Report v18.

* [Enhanced Embedding Capabilities](#Embedding)
* [Enhanced Pixel-Perfect Report](#Report)
* [Enhanced Performance](#Performance)
* [Enhanced UX](#UX)

## Enhanced Embedding Capabilities

* Report designers can now constrain the data sources that end users can apply at runtime, if they need to add more data components into the reports developed in Designer. This means you can create new data components without exposing out-of-scope data, and provides a much better experience with focused data views.

  ![Constrained Data](https://devnet.logianalytics.com/hc/article_attachments/4420410641431/constrained-data.png)
* Server administrators can now define business view security in a catalog, permitting users to access the business views.

  ![Define business view security](https://devnet.logianalytics.com/hc/article_attachments/4420402371863/define-bv-security.png)
* Server administrators can now customize business views for a report using the report properties dialog box, or for multiple reports at a time using the Administration menu.

  ![Customize business views for reports](https://devnet.logianalytics.com/hc/article_attachments/4420402372119/bv-for-report.png)
* Server administrators can now change the owner of a resource, to remove or update the resource if the current owner can no longer manage it.

  ![Change resource owner](https://devnet.logianalytics.com/hc/article_attachments/4420410641687/change-resource-owner.png)

## Enhanced Pixel-Perfect Report

* You can now specify whether to include or exclude specific table columns in your report output (PDF, Excel, HTML, and so on). This dynamic layout provides you different results in different formats. For example, you can show a full report in Web view, but display a summary without detail columns in PDF output.

  ![Table Column in Report Output](https://devnet.logianalytics.com/hc/article_attachments/4420410641943/export-table-column.png)
* You can now use formulas to control page properties such as width, height, and margins. With dynamic pagination, you can dynamically generate different report pages, different report layouts based on different users, and specific groups of data in different time zones.

  ![Dynamic Pagination](https://devnet.logianalytics.com/hc/article_attachments/4420402372375/dynamic-pagination.png)
* With enhanced Excel output of your reports, you can now specify whether to apply format to the empty cells in the Excel output, and customize the sheet name for a web report or business view-based page report tab.

  ![Enhanced Excel Output](https://devnet.logianalytics.com/hc/article_attachments/4420394701847/enhanced-excel-output.png)

## Enhanced Performance

* You can now reference parameters, formulas, and the special field "User Name" when specifying the information to connect to a MongoDB database, and use a parameter or formula to specify the database and collection from which to get data for an imported APE. With dynamic connections for MongoDB, different users from different organizations, tenants, or roles are able to share the same report template for different data sources.

  ![Dynamic MongoDB Data Source Connection](https://devnet.logianalytics.com/hc/article_attachments/4420394702103/dynamic-mongodb.png)
* Enhanced custom aggregations for group level calculations referenced by specific members of the groups, including the maximum and minimum members, enables picking a maximum value or a specific value from a group member, then simply showing them or comparing different values from different group members.

  ![Enhanced Custom Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4420402372759/enhanced-custom-aggregation.png)
* You can now configure the MongoDB connection in Logi Report Server or when running reports via URL, and create dynamic MongoDB connections.

  ![MongoDB Connection on Server](https://devnet.logianalytics.com/hc/article_attachments/4420394702359/mongodb-connection-server.png)

  ![Dynamic MongoDB Connection](https://devnet.logianalytics.com/hc/article_attachments/4420394702743/mongodb-connection-server1.png)
* Logi Report now just fetches necessary layout data when the report body contains only parameters, constant level formulas, or detail DBFields, to improve performance.
* You can now open the Public Reports folder quickly on the Server Console when the folder is big, and if many users and groups have complicated permissions on the folder.

## Enhanced UX

* You can now create horizontal tables in business view-based page reports and apply the Word Wrap property to horizontal table cells.

  ![Horizontal Table](https://devnet.logianalytics.com/hc/article_attachments/4420394703127/horizontal-table.png)
* You can now define the usage of a page report tab as subreport only, so that the report tab no longer displays in the Go To drop-down list in Page Report Studio.

  ![Report Tab Work as Subreport](https://devnet.logianalytics.com/hc/article_attachments/4420410642583/report-tab-as-subreport.png)
* You can now customize the names of the fields on the value axis of a chart in addition to the category and series names, which you want to display in the data marker hint of the chart, to provide users more meaningful information.

  ![Customizable Chart Value Names](https://devnet.logianalytics.com/hc/article_attachments/4420402375831/chart-value-name.png)
* With enhanced parameters, you can now use columns in queries or imported APEs as the Bind Column and Display Column of parameters, sort and search the DBFields when you specify the Bind Column and Display Column for a parameter, and sort the values of a parameter that is bound with a single column.

  ![Enhanced Parameter](https://devnet.logianalytics.com/hc/article_attachments/4420402376855/enhanced-parameter.png)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664606871-Logi-Report-v18-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664317847-Logi-Report-Designer-Guide-v18-Overview)
