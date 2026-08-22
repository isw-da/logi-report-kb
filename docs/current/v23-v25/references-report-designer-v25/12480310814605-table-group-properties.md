---
title: "Table Group Properties"
id: 12480310814605
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480310814605-Table-Group-Properties
updated_at: 2026-02-25T23:47:47Z
source_host: docs-report.zendesk.com
---
# 
Table Group Properties

This topic describes the properties of a Table Group Object.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Group By | Query Page Report | Shows the group-by field of the object. When this property value is null, the object is grouped based on the whole dataset. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Others |  |  |
| Current Block Index | Page Report, Web Report, Library Component | You can use Current Block Index and Items per Block together to control the data of the object you want to display in continuous page mode. Current Block Index specifies the index of the data block. 0 means the first block index, 1 means the second, and so on.Data type: Integer |
| Expand Detail Data | Page Report, Web Report, Library Component | Specifies whether to expand details of the group at runtime, if you add an Expand/Collapse Group web control for the group. Data type: Boolean This property takes effect only in continuous page mode. |
| Items per Block | Page Report, Web Report, Library Component | You can use Current Block Index and Items per Block together to control the data of the object you want to display in continuous page mode. Item per Block specifies the number of the records in each data block.Data type: Integer |
| Group Layout |  |  |
| Keep Group Together | Query Page Report | Specifies whether to keep the whole group together in the report. Data type: Boolean |
| TOC |  |  |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Security |  |  |
| Cascade | Query Page Report | Specifies whether to allow the users, groups, and roles defined in the following three properties to view details of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property.Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value, or edit an expression to control the property. Data type: String |

 Web Report Studio and JDashboard do not support any properties of the Table Group object at runtime.
