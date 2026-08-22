---
title: "Properties of Dataset in Library Component"
id: 1500009569142
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569142-Properties-of-Dataset-in-Library-Component
updated_at: 2021-07-24T05:54:20Z
---

# Properties of Dataset in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569122-Properties-of-Data-Source-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569162-Properties-of-Refresh-Object-in-Library-Component)

# Properties of Dataset in Library Component

The properties of a dataset object in a library component are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Name | Shows the name of the query or business view in use. It can be null. When it is null, the available resources for the dataset are parameters and constant level formulas in the data source. |
| Data Source Name | Specifies the name of the data source. This property is read only. |
| Is Query | It is true when the dataset is based on a query or false when based on a business view. |
| Others | |
| [Data Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataDriver) | Specifies the cached query result file as the data resource. Usually used for support purpose. The input format for cached query result file is as follows: jrquery:/jet.universe.resultfile.UResultFileResultSet;*Fullpath\_of\_cached\_query\_result*  Data type: String |
| Maximum Records | Specifies the maximum number of records you want to display for all of the data components using this dataset. The default is to display all the records. Data type: Integer |
| Security | |
| Security Policy Name | Specifies the name of the [data source security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope) imported from the catalog. Choose a security policy from the value drop-down list. Data type: String  **Note:** Column-level security (CLS) is not supported on library component at present, so for a library component, only the data source security policies which have not been defined with CLS will be available in the value list. |
| [Data Buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataBuffer) | |
| Maximum Page Number | Specifies the maximum number of pages in the data buffer. Data type: Integer |
| Records per Page | Specifies the number of records in each page in the data buffer. Data type: Integer |

**Notes:**

* The properties should be set according to different databases, namely, different databases may have different configurations of data buffer.
* If the library component runs in a different environment, the properties should be specified again.
* As tested, if enough physical memory is available, and you know the total number of records in the dataset, then you can set Records per Page approximate to the total number of records to achieve better performance. Maximum Page Number is related to the library component, and should not be very large.
* The size of data buffer should be less than the available physical memory.
* The Heap Size should be set when the data buffer is quite large.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569122-Properties-of-Data-Source-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569162-Properties-of-Refresh-Object-in-Library-Component)
