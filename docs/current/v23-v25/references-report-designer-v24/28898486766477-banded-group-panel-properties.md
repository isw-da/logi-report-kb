---
title: "Banded Group Panel Properties"
id: 28898486766477
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898486766477-Banded-Group-Panel-Properties
updated_at: 2024-09-30T09:10:58Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Banded Group Panel Properties

This topic describes the properties of a Group Panel object in a banded object.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Group By | Query Page Report | Shows the group-by field of the object. When this property value is null, the object is grouped based on the whole dataset. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Others |  |  |
| Current Block Index | Page Report, Web Report | You can use Current Block Index and Items per Block together to control the data of the object you want to display in continuous page mode. Current Block Index specifies the index of the data block. 0 means the first block index, 1 means the second, and so on.Data type: Integer |
| Expand Detail Data | Page Report | Specifies whether to expand details of the group when users run the report in Page Report Studio, if you add an Expand/Collapse Group web control for the group. Data type: Boolean This property takes effect only in continuous page mode. |
| Items per Block | Page Report, Web Report | You can use Current Block Index and Items per Block together to control the data of the object you want to display in continuous page mode. Item per Block specifies the number of the records in each data block.Data type: Integer |
| Shrink Footer | Page Report | Specifies whether to hide the group footer panel when users collapse details of the group in Page Report Studio, if you add an Expand/Collapse Group web control for the group. Data type: Boolean This property takes effect only in continuous page mode. |
| Group Layout |  |  |
| Keep Group Together | Page Report, Web Report | Specifies whether to keep the whole group together in the report. The whole group includes the header, detail, and footer panels of the group, and the subgroups (including their header, detail, and footer panels) of the group. When you set this property to "true", if a page is not blank and it cannot contain the whole group, Designer displays the group from the next page. By keeping the whole group together, you can always view the header of the group together with the group details in the same page, without having any group header display at the bottom of a page.Data type: Boolean |
| Repeat While Group Footer | Page Report, Web Report | Specifies whether to repeat the group header in the report when a page break occurs on the group footer, if you specify to repeat the group header. Data type: Boolean |
| TOC |  |  |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Security |  |  |
| Cascade | Query Page Report | Specifies whether to allow the users, groups, and roles defined in the following three properties to view details of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property.Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property.Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property.Data type: String |

Previous Topic  Next Topic
