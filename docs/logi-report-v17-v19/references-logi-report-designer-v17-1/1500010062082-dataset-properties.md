---
title: "Dataset Properties"
id: 1500010062082
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062082-Dataset-Properties
updated_at: 2021-07-23T19:16:33Z
---

# Dataset Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100361-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062102-Refresh-Object-Properties)

# Dataset Properties

This topic lists the properties of a Dataset object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Query Page Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report, Library Component | Indicates the class type of the object. This property is read only. |
| Data Name | Query Page Report, Library Component | Shows the name of the query or business view on which the dataset is based. It can be null. When it is null, the available resources for the dataset are parameters and constant level formulas in the current catalog data source. |
| Data Source Name | Library Component | Shows the name of the catalog data source in which the business view is created. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Is Query | Query Page Report, Library Component | It is true when the dataset is based on a query or false when based on a business view. |
| Others | | |
| Data Driver | Query Page Report, Library Component | Specifies the cached query result file as the data resource instead of the database for running the report. Usually used for support purpose. For more information, see [Applying Cached Query Results](https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results#Apply). Data type: String |
| Data Source Name | Query Page Report | Specifies the name of the catalog data source that contains the query you want to use for the specified data component. Data type: String |
| Maximum Records | Query Page Report, Library Component | Specifies the maximum number of records you want to display for all of the data components using this dataset. The default is to display all the records. Data type: Integer |
| Query Editor | Query Page Report | Edits the dataset if it is based on a query. Select the ellipsis button Ellipsis button in the value cell to display the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box) to edit the query as required. |
| Security | | |
| Function | Query Page Report | Specifies a formula to control the [Record Level Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094241-Applying-RLS-at-Report-Scope). Data type: String |
| Record Security | Query Page Report | Specifies the record level security policy for the dataset. Select Ellipsis button to open the [Record Level Security Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098461-Record-Level-Security-Information-Dialog-Box) to set the security settings. |
| Security Policy Name | Query Page Report, Library Component | Specifies the name of the [data source security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094221-Working-with-RLS-and-CLS-at-Data-Source-Scope) imported from the catalog. Choose a security policy from the value drop-down list. Data type: String  Note icon Column Level Security (CLS) is not supported in library components at present, so for a library component, only the data source security policies which have not been defined with CLS will be available in the value list. |
| [Data Buffer](#DataBuffer) | | |
| Maximum Page Number | Query Page Report, Library Component | Specifies the maximum number of pages in the data buffer. Data type: Integer |
| Records per Page | Query Page Report, Library Component | Specifies the number of records in each page in the data buffer. Data type: Integer |

## Data Buffer

You can improve report performance by setting data buffer size. By default, the size of one data buffer is 2M. When data exceeds the default size, they will be written on the disk, which will slow down the data processing. However, you may have enough memory which is much larger than the default buffer size, so that you can use the memory resource efficiently to achieve better performance. Logi Report enables you to set the data buffer size by specifying the two properties: Records per Page and Maximum Page Number.

When a buffer is defined, Logi Report Engine divides it into many pages and allocates records to be stored in the pages. Data will be transferred with the unit of page. The data buffer size is determined by values of maximum number of pages in the buffer and the number of records in every page. The default maximum page number in the data buffer is 2048, page size is 1k (1024 bytes).

The value of Maximum Page Number should be changed with different datasets. Generally speaking, it can be 1 ~ 50.

To view the data buffer information of a report and its subreports, select **View** > **Data Buffer Information**. For more information, see the [Data Buffer Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058522-Data-Buffer-Information-Dialog-Box).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* The properties should be set according to different databases, namely, different databases may have different configurations of data buffer.
* If the report runs in a different environment, the properties should be specified again.
* If the report contains subreports, the data buffer for subreports should also be configured to improve performance.
* As tested, if enough physical memory is available, and you know the total number of records in the dataset, then you can set Records per Page approximate to the total number of records to achieve better performance. Maximum Page Number is related to the report, and should not be very large.
* The size of data buffer should be less than the available physical memory.
* The Heap Size should be set when the data buffer is quite large.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100361-Column-Compound-Group-Row-Compound-Group-Summary-Area-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062102-Refresh-Object-Properties)
