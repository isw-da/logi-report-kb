---
title: "Banded Group Panel Properties"
id: 9898557685143
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9898557685143-Banded-Group-Panel-Properties
updated_at: 2022-11-02T04:10:43Z
---

# Banded Group Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735568700695-Banded-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557732503-Banded-Group-Header-Panel-Properties)

# Banded Group Panel Properties

This topic describes the properties of a Group Panel object in a banded object.

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Group By | Query Page Report | Shows the group-by field of the object. When this property value is null, the object is grouped based on the whole dataset. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Others | | |
| Current Block Index | Page Report, Web Report | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). Current Block Index specifies the index of the data block. 0 means the first block index, 1 means the second, and so on. Data type: Integer |
| Expand Detail Data | Page Report | Specifies whether to expand details of the group when users run the report in Page Report Studio, if you add an [Expand/Collapse Group](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Expand) web control for the group. Data type: Boolean  Note icon This property takes effect only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). |
| Items per Block | Page Report, Web Report | You can use Current Block Index and Items per Block together to control the data of the object you want to display in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). Item per Block specifies the number of the records in each data block. Data type: Integer |
| [Shrink Footer](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Expand) | Page Report | Specifies whether to hide the group footer panel when users collapse details of the group in Page Report Studio, if you add an [Expand/Collapse Group](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Expand) web control for the group. Data type: Boolean  Note icon This property takes effect only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode). |
| Group Layout | | |
| Keep Group Together | Page Report, Web Report | Specifies whether to keep the whole group together in the report. The whole group includes the header, detail, and footer panels of the group, and the subgroups (including their header, detail, and footer panels) of the group. When you set this property to "true", if a page is not blank and it cannot contain the whole group, Designer displays the group from the next page. By keeping the whole group together, you can always view the header of the group together with the group details in the same page, without having any group header display at the bottom of a page. Data type: Boolean |
| Repeat While Group Footer | Page Report, Web Report | Specifies whether to repeat the group header in the report when a page break occurs on the group footer, if you specify to repeat the group header. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) | | |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Security](https://devnet.logianalytics.com/hc/en-us/articles/5735520407191-Applying-Cached-Report-Bursting) | | |
| Cascade | Query Page Report | Specifies whether to allow the users, groups, and roles defined in the following three properties to view details of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735568700695-Banded-Footer-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898557732503-Banded-Group-Header-Panel-Properties)
