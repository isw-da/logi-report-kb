---
title: "Hierarchical Data Source Properties"
id: 12480288583181
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480288583181-Hierarchical-Data-Source-Properties
updated_at: 2026-02-25T23:48:15Z
source_host: docs-report.zendesk.com
---
# 
Hierarchical Data Source  Properties

This topic describes the properties of a Hierarchical Data Source (HDS) object in a catalog.

| Property Name | Description |
| --- | --- |
| Attributes | Specifies whether to allow using columns of this HDS to group by. When you set this property to "true", you cannot use the columns to group by. Data type: Boolean |
| Class Name | Shows the name of the class that Report provides for implementing hierarchical data sources. Read only. |
| Description | Specifies the description of the HDS. Data type: String |
| Full Name | Shows the full path name of the HDS that Designer generates automatically. Read only. |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the HDS runs, measured in seconds. By default, the property value is blank, meaning the time is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the HDS runs. By default, the property value is blank, meaning the number is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Name | Specifies the mapped name of the HDS in the catalog. Data type: String |
| Parameter | Specifies the value for the parameter of the HDS. Data type: String |
| Root Name | Specifies the name of the root node in the XML file. Data type: String |
| URI | Specifies the URI of the XML file. Data type: String |
| Version | Shows the version number of the HDS API. Read only. |
| XSD URI | Specifies the URI of the XSD file. Data type: String |
