---
title: "User-Defined Data Source (UDS) Properties"
id: 1500010061622
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061622-User-Defined-Data-Source-UDS-Properties
updated_at: 2021-07-23T19:16:26Z
---

# User-Defined Data Source (UDS) Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061582-Table-View-Synonym-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100141-UDS-Column-Properties)

# User-Defined Data Source (UDS) Properties

This topic lists the properties of a User-Defined Data Source (UDS) object in a catalog.

| Property Name | Description |
| --- | --- |
| Class Name | Specifies the full name (including package name) of the class represented by the UDS. The class you entered should actually exist and can be found by Designer, which means the class should be in the class path of the system environment. Data type: String |
| Description | Specifies the description of the UDS. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the UDS runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the UDS runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries#Limit).  Data type: Integer |
| Name | Specifies the name of the UDS. Data type: String |
| Parameter | Specifies the value of the UDS's parameter. Data type: String |
| Specify Metadata | Specifies whether or not to apply the column properties specified by users. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061582-Table-View-Synonym-Column-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100141-UDS-Column-Properties)
