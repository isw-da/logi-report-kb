---
title: "Dataset Properties"
id: 4405664656919
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664656919-Dataset-Properties
updated_at: 2022-01-27T20:35:13Z
---

# Dataset Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664655767-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661852055-DBField-Properties)

# Dataset Properties

This topic describes the properties of a [Dataset object](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) that you can use in query-based page reports and library components.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report, Library Component | Shows the class type of the object. This property is read only. |
| Data Name | Query Page Report, Library Component | Shows the name of the query or business view on which you have created the dataset. This property is read only. |
| Data Source Name | Library Component | Shows the name of the catalog data source that contains the business view the dataset uses. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Is Query | Query Page Report, Library Component | Shows whether the dataset is based on a query. "false" means the dataset is based on a business view. This property is read only. |
| Others | | |
| Data Driver | Query Page Report, Library Component | Specifies the cached query result file as the data resource instead of the database for running the report. For more information, see [Applying Cached Query Results](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results#Apply). Data type: String |
| Data Source Name | Query Page Report | Specifies the name of the catalog data source that contains the query you want to use for the dataset. Choose a data source from the drop-down list. Data type: String |
| Maximum Records | Query Page Report, Library Component | Specifies the maximum number of records you want to display for all data components using the dataset. Default (the property value being empty) is to display all records. Data type: Integer |
| Query Editor | Query Page Report | Edits the query based on which you have created this dataset. Select the ellipsis Ellipsis button in the value cell to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661685015-Query-Editor-Dialog-Box). |
| Security | | |
| Function | Query Page Report | Specifies the formula that contains predefined security conditions to control the [record level security](https://devnet.logianalytics.com/hc/en-us/articles/4405661343639-Applying-RLS-at-Report-Scope) on the dataset. Choose a formula from the drop-down list. Data type: String |
| Record Security | Query Page Report | Specifies the record level security policy for the dataset. Select the ellipsis Ellipsis button in the value cell to edit the security settings in the [Record Level Security Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661692183-Record-Level-Security-Information-Dialog-Box). Data type: String |
| Security Policy Name | Query Page Report, Library Component | Specifies the [data source security entry](https://devnet.logianalytics.com/hc/en-us/articles/4405661342359-Working-with-RLS-and-CLS-at-Data-Source-Scope) you want to apply to the dataset. Choose a security entry from the drop-down list. Data type: String  Note icon Designer does not support Column Level Security (CLS) on library components at present, so for a library component, only the security entries which do not contain CLS are available in the value list. |
| [Data Buffer](#DataBuffer) | | |
| Maximum Page Number | Query Page Report, Library Component | Specifies the maximum number of pages in the data buffer. Type a numeric value to change the number. Data type: Integer |
| Records per Page | Query Page Report, Library Component | Specifies the number of records in each page in the data buffer. Type a numeric value to change the number. Data type: Integer |

## Data Buffer

You can improve report performance by setting the data buffer size via the two properties: Maximum Page Number and Records per Page. By default, the size of one data buffer is 2MB. When data exceeds the default size, Logi Report Engine writes them to the disk, which slows down data processing. However, you may have enough memory which is much larger than the default buffer size, so you can use the memory resource efficiently to achieve better performance.

When you specify a data buffer, Logi Report Engine divides it into many pages and allocates records to store in the pages. Logi Report Engine transfers data with the unit of page. The data buffer size is determined by values of maximum number of pages in the buffer and the number of records in every page. The default maximum page number in the data buffer is 2048, and page size is 1k (1024 bytes).

To view the data buffer information of a report and its subreports, select **View** > **Data Buffer Information**. For more information, see [Data Buffer Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661495575-Data-Buffer-Information-Dialog-Box).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* You should set the two properties according to different databases, namely, different databases may have different configurations of data buffer.
* If the report runs in a different environment, you need to specify the two properties again.
* If the report contains subreports, you should also configure the data buffer for the subreports to improve performance.
* If enough physical memory is available and you know the total number of records in the dataset, you can set Records per Page approximate to the total number of records to achieve better performance. Maximum Page Number is related to the report, and should not be very large.
* The size of data buffer should be less than the available physical memory.
* You should set the heap size when the data buffer is quite large.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664655767-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661852055-DBField-Properties)
