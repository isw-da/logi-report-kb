---
title: "User Defined Data Source Properties"
id: 5735516825495
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735516825495-User-Defined-Data-Source-Properties
updated_at: 2022-11-02T08:09:55Z
---

# User Defined Data Source Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735554133527-Table-View-Synonym-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735545814039-UDS-Column-Properties)

# User Defined Data Source Properties

This topic describes the properties of a [User Defined Data Source (UDS) object](https://devnet.logianalytics.com/hc/en-us/articles/5735521621399-Using-User-Defined-Data-Sources) in a catalog.

| Property Name | Description |
| --- | --- |
| Class Name | Specifies the full name (including package name) of the class represented by the UDS. The class should actually exist and can be found by Designer, which means you should have already added the class to the class path of the system environment. Data type: String |
| Description | Specifies the description of the UDS. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the UDS runs, measured in seconds. By default, the property value is blank, meaning the time is unlimited. For more information, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/5735555374103-Managing-the-Data-Retrieval-of-Queries#Limit). Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the UDS runs. By default, the property value is blank, meaning the number is unlimited. For more information, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/5735555374103-Managing-the-Data-Retrieval-of-Queries#Limit). Data type: Integer |
| Name | Specifies the mapped name of the UDS in the catalog. Data type: String |
| Parameter | Specifies the value for the parameter of the UDS. Data type: String |
| Specify Metadata | Specifies whether to apply the column properties specified by users. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735554133527-Table-View-Synonym-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735545814039-UDS-Column-Properties)
