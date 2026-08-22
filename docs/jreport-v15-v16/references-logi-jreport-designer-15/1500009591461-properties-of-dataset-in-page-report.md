---
title: "Properties of Dataset in Page Report"
id: 1500009591461
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report
updated_at: 2021-07-24T05:54:11Z
---

# Properties of Dataset in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591421-Properties-of-Label-in-Page-Report-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591441-Properties-of-DBField-in-Page-Report)

# Properties of Dataset in Page Report

The properties of a dataset object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Name | Shows the name of the query or business view in use. It can be null. When it is null, the available resources for the dataset are parameters and constant level formulas in the data source. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Is Query | It is true when the data set is based on a query or false when based on a business view. |
| Others | |
| [Data Driver](#DataDriver) | Specifies the cached query result file as the data resource. Usually used for support purpose. The input format for cached query result file is as follows: jrquery:/jet.universe.resultfile.UResultFileResultSet;*Fullpath\_of\_cached\_query\_result*  Data type: String |
| Data Source Name | Specifies the name of the data source. Data type: String |
| Maximum Records | Specifies the maximum number of records you want to display for all of the data components using this dataset. The default is to display all the records. Data type: Integer |
| Query Editor | Edits the dataset if it is based on a query. Select  to display the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) to edit the query as required. |
| Security | |
| Function | Specifies a formula to control the record level security. Data type: String |
| Record Security | Specifies the record level security for the dataset. Select  to open the [Record Level Security Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009567282-Record-Level-Security-Information-Dialog) dialog in which to set the security settings. |
| Security Policy Name | Specifies the name of the [data source security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope) imported from the catalog. Choose a security policy from the value drop-down list. Data type: String |
| [Data Buffer](#DataBuffer) | |
| Maximum Page Number | Specifies the maximum number of pages in the data buffer. Data type: Integer |
| Records per Page | Specifies the number of records in each page in the data buffer. Data type: Integer |

## Data Driver

This property is usually used for support purpose. When you have problems with your report, we need to run it and reproduce the problem so as to fix it. Sometimes, the database is too large to be sent. In this case, you can [generate a cached query result file](https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results) for the data resource on which your report is built and set this property correctly, then Logi JReport Engine will choose that query file to view the report instead of using JDBC driver or User Data Source to run the report.

The property should be set in the following format:

jrquery:/jet.universe.resultfile.UResultFileResultSet;*Fullpath\_of\_cached\_query\_result*

For example, if the cached query result has been saved to `C:\Logi JReport\Designer\Cached` with the file name test, the property value should be `jrquery:/jet.universe.resultfile.UResultFileResultSet;C:\Logi JReport\Designer\Cached\test`.

## Data Buffer

You can improve report performance by setting data buffer size. By default, the size of one data buffer is 2M. When data exceeds the default size, they will be written on the disk, which will slow down the data processing. However, you may have enough memory which is much larger than the default buffer size, so that you can use the memory resource efficiently to achieve better performance. Logi JReport enables you to set the data buffer size by specifying the two properties: Records per Page and Maximum Page Number.

When a buffer is defined, Logi JReport divides it into many pages and allocates records to be stored in the pages. Data will be transferred with the unit of page. The data buffer size is determined by values of maximum number of pages in the buffer and the number of records in every page. The default maximum page number in the data buffer is 2048, page size is 1k(1024 bytes).

The value of Maximum Page Number should be changed with different datasets. Generally speaking, it can be 1 ~ 50.

To view the data buffer information of a report and its subreports, select **View** > **Data Buffer Information**. For details, see [Data Buffer Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009565022-Data-Buffer-Information-Dialog) dialog.

**Notes:**

* The properties should be set according to different databases, namely, different databases may have different configurations of data buffer.
* If the report runs in a different environment, the properties should be specified again.
* If the report contains subreports, the data buffer for subreports should also be configured to improve performance.
* As tested, if enough physical memory is available, and you know the total number of records in the dataset, then you can set Records per Page approximate to the total number of records to achieve better performance. Maximum Page Number is related to the report, and should not be very large.
* The size of data buffer should be less than the available physical memory.
* The Heap Size should be set when the data buffer is quite large.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591421-Properties-of-Label-in-Page-Report-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591441-Properties-of-DBField-in-Page-Report)
