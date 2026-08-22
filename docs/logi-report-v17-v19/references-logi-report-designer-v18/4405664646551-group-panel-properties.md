---
title: "Group Panel Properties"
id: 4405664646551
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664646551-Group-Panel-Properties
updated_at: 2022-01-27T20:35:55Z
---

# Group Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661839511-Banded-Page-Header-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664647447-Detail-Panel-Properties)

# Group Panel Properties

This topic describes the properties of a Group Panel object in a banded object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Group By | Query Page Report | Shows the group-by field of the object. If null, the object is grouped based on the whole dataset. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Others | | |
| Current Block Index | Page Report, Web Report | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Current Block Index specifies the index of the data block. 0 means the first block index, 1 means the second, and so on. Data type: Integer |
| Expand Detail Data | Page Report | Specifies whether to expand details of the group when users run the report in Page Report Studio, if you add an [Expand/Collapse Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Expand) web control for the group. This property takes effect only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Data type: Boolean |
| Items per Block | Page Report, Web Report | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Item per Block specifies the number of the records in each data block. Data type: Integer |
| [Shrink Footer](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Expand) | Page Report | Specifies whether to hide the group footer panel when users collapse details of the group in Page Report Studio, if you add an [Expand/Collapse Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Expand) web control for the group. This property takes effect only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Mode). Data type: Boolean |
| Group Layout | | |
| Keep Group Together | Query Page Report | Specifies whether to keep the whole group together in the report. Data type: Boolean |
| Repeat While Group Footer | Page Report, Web Report | Specifies whether to repeat the group header in the report when a page break occurs on the group footer, if you specify to repeat the group header. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Security](https://devnet.logianalytics.com/hc/en-us/articles/4405661339799-Applying-Cached-Report-Bursting) | | |
| Cascade | Query Page Report | Specifies whether to allow the users, groups, and roles specified in the following three properties to view the detailed data of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661839511-Banded-Page-Header-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664647447-Detail-Panel-Properties)
