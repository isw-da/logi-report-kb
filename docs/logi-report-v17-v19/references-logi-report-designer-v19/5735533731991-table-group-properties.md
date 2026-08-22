---
title: "Table Group Properties"
id: 5735533731991
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735533731991-Table-Group-Properties
updated_at: 2022-11-02T08:17:32Z
---

# Table Group Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569437847-Table-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557836695-Table-Group-Header-Properties)

# Table Group Properties

This topic describes the properties of a Table Group Object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Group By | Query Page Report | Shows the group-by field of the object. When this property value is null, the object is grouped based on the whole dataset. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Others | | |
| Current Block Index | Page Report, Web Report, Library Component | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). Current Block Index specifies the index of the data block. 0 means the first block index, 1 means the second, and so on. Data type: Integer |
| Expand Detail Data | Page Report, Web Report, Library Component | Specifies whether to expand details of the group at runtime, if you add an [Expand/Collapse Group](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Expand) web control for the group. Data type: Boolean  Note icon This property takes effect only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). |
| Items per Block | Page Report, Web Report, Library Component | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). Item per Block specifies the number of the records in each data block. Data type: Integer |
| Group Layout | | |
| Keep Group Together | Query Page Report | Specifies whether to keep the whole group together in the report. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Security](https://devnet.logianalytics.com/hc/en-us/articles/5735520407191-Applying-Cached-Report-Bursting) | | |
| Cascade | Query Page Report | Specifies whether to allow the users, groups, and roles defined in the following three properties to view details of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Web Report Studio and JDashboard do not support any properties of the Table Group object at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569437847-Table-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557836695-Table-Group-Header-Properties)
