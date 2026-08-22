---
title: "User Defined Data Source Properties"
id: 28898451188109
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898451188109-User-Defined-Data-Source-Properties
updated_at: 2024-09-30T09:08:08Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
User Defined Data Source Properties

This topic describes the properties of a User Defined Data Source (UDS) object in a catalog.

| Property Name | Description |
| --- | --- |
| Class Name | Specifies the full name (including package name) of the class represented by the UDS. The class should actually exist and can be found by Designer, which means you should have already added the class to the class path of the system environment. Data type: String |
| Description | Specifies the description of the UDS. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the UDS runs, measured in seconds. By default, the property value is blank, meaning the time is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the UDS runs. By default, the property value is blank, meaning the number is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Name | Specifies the mapped name of the UDS in the catalog. Data type: String |
| Parameter | Specifies the value for the parameter of the UDS. Data type: String |
| Specify Metadata | Specifies whether to apply the column properties specified by users. Data type: Boolean |

Previous Topic  Next Topic
