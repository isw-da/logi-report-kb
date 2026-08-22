---
title: "User Defined Data Source Properties"
id: 1500010069481
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069481-User-Defined-Data-Source-Properties
updated_at: 2021-07-24T10:38:02Z
---

# User Defined Data Source Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069441-Table-View-Synonym-Column-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069501-UDS-Column-Properties)

# User Defined Data Source Properties

This topic lists the properties of a User Defined Data Source (UDS) object in a catalog.

| Property Name | Description |
| --- | --- |
| Class Name | Specifies the full name (including package name) of the class represented by the UDS. The class you entered should actually exist and can be found by Logi JReport Designer, which means the class should be in the class path of the system environment. Data type: String |
| Description | Specifies the description of the UDS. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the UDS runs, measured in seconds. If the value is set to zero or is blank, it means the time will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500010034662-Data-Manager#Limit).  Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows that will be fetched from the data source when the UDS runs. If the value is set to zero or is blank, it means the number will be unlimited. For usage about the property, see [Limiting the Query Run Time and Number of Records](https://devnet.logianalytics.com/hc/en-us/articles/1500010034662-Data-Manager#Limit).  Data type: Integer |
| Name | Specifies the name of the UDS. Data type: String |
| Parameter | Specifies the value of the UDS's parameter. Data type: String |
| Specify Metadata | Specifies whether or not to apply the column properties specified by users. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069441-Table-View-Synonym-Column-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069501-UDS-Column-Properties)
