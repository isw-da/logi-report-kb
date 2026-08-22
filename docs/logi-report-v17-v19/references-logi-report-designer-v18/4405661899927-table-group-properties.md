---
title: "Table Group Properties"
id: 4405661899927
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661899927-Table-Group-Properties
updated_at: 2022-01-27T20:35:08Z
---

# Table Group Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664676247-Table-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661901335-Table-Detail-Properties)

# Table Group Properties

This topic describes the properties of a Table Group Object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Group By | Query Page Report | Shows the group-by field of the object. If null, the object is grouped based on the whole dataset. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Others | | |
| Current Block Index | Page Report, Web Report, Library Component | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Current Block Index specifies the index of the data block. 0 means the first block index, 1 means the second, and so on. Data type: Integer |
| Expand Detail Data | Page Report, Web Report, Library Component | Specifies whether to expand the groups to show the details when the report or library component is opened in Page/Web Report Studio or JDashboard. Only works in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Data type: Boolean |
| Items per Block | Page Report, Web Report, Library Component | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Item per Block specifies the number of the records in each data block. Data type: Integer |
| Group Layout | | |
| Keep Group Together | Query Page Report | Specifies whether to keep the whole group together in the report. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Security](https://devnet.logianalytics.com/hc/en-us/articles/4405661339799-Applying-Cached-Report-Bursting) | | |
| Cascade | Query Page Report | Specifies whether to allow the users, groups, and roles specified in the following three properties to view the detailed data of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) All these table group properties are not supported in Web Report Studio and JDashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664676247-Table-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661901335-Table-Detail-Properties)
