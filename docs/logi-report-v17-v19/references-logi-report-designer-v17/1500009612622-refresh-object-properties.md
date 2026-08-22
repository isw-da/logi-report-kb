---
title: "Refresh Object Properties"
id: 1500009612622
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612622-Refresh-Object-Properties
updated_at: 2021-05-21T07:53:54Z
---

# Refresh Object Properties

[![Back](https://logianalytics.zendesk.com/hc/article_attachments/1500015085241/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612602-Parameter-Form-Control-Properties) [Next Topic![Next](https://logianalytics.zendesk.com/hc/article_attachments/1500015085261/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635681-Report-Body-Properties)

# Refresh Object Properties

This topic lists the properties of a Refresh Object, which is supported in library components only.

| Property Name | Description |
| --- | --- |
| General | |
| Business View Name | Displays the name of the business view for which the refresh object is created. This property is read only. Data type: String |
| Data Source Name | Displays the name of the data source in which the business view is created. This property is read only. Data type: String |
| Name | Displays the name of the refresh object, which by default is the business view name. This property is read only. Data type: String |
| Query Name | Displays the name of the query on which the business view is created. Data type: String |
| Refresh | |
| Enable Auto Refresh | Specifies whether to make the data components that are created on the business view automatically refresh themselves at runtime based on a defined interval. Data type: Boolean |
| Incremental Fetch | Specifies whether to fetch incremental data only when an auto refresh takes place. Enabled when Enable Auto Refresh is set to true. If set to true, you can select  in the value cell to open the [Incremental Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009608802-Incremental-Condition-Dialog) dialog to specify conditions to filter the incremental data. This property does not work on crosstabs and real time charts. Data type: Boolean |
| Interval | Specifies the time interval between two auto refreshes. It ranges from 0 to 86400 seconds. Enabled when Enable Auto Refresh is set to true. Type a numeric value to change the interval. Data type: Integer |
| Unique Key | Specifies the unique key used to delete duplicated data from the incremental data filtered by incremental condition. Select  in the value cell to open the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009610762-Unique-Key-dialog-Dialog) dialog to specify the key. It is meaningful to specify the property when Incremental Fetch is set to true. Data type: Array |
| Value Number | Specifies the number of records that can be displayed in the data components. The earliest records will be removed when records exceed the specified number. Type a numeric value to change the number. It is meaningful to specify the property when Incremental Fetch is set to true. Data type: Integer |

[![](https://logianalytics.zendesk.com/hc/article_attachments/1500014747302/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://logianalytics.zendesk.com/hc/article_attachments/1500015085241/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612602-Parameter-Form-Control-Properties) [Next Topic![Next](https://logianalytics.zendesk.com/hc/article_attachments/1500015085261/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635681-Report-Body-Properties)
