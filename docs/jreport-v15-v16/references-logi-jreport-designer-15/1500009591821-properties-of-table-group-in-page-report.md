---
title: "Properties of Table Group in Page Report"
id: 1500009591821
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591821-Properties-of-Table-Group-in-Page-Report
updated_at: 2021-07-24T05:54:05Z
---

# Properties of Table Group in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591861-Properties-of-Table-Header-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591841-Properties-of-Table-Group-Header-in-Page-Report)

# Properties of Table Group in Page Report

A table group can contain the following child objects: [Table Group Header](https://devnet.logianalytics.com/hc/en-us/articles/1500009591841-Properties-of-Table-Group-Header-in-Page-Report), [Table Detail](https://devnet.logianalytics.com/hc/en-us/articles/1500009569942-Properties-of-Table-Detail-in-Page-Report)  and [Table Group Footer.](https://devnet.logianalytics.com/hc/en-us/articles/1500009569962-Properties-of-Table-Group-Footer-in-Page-Report)

The properties of a table group object in a page report are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Group By | Shows the group field that the object is based on. If null, the object is grouped based on the whole dataset. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Others | |
| Current Block Index | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Current Block Index specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
| Expand Detail Data | Specifies whether to expand the groups to show the details when the report is opened in Page Report Studio. Only works in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Data type: Boolean |
| Items per Block | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Item per Block specifies the number of records in each data block.  Data type: Integer |
| Group Layout | |
| Keep Group Together | Specifies whether to keep the whole group together. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. A Boolean type value. |
| [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009571202-Cached-Report-Bursting) | |
| Cascade | Specifies whether to allow the users, groups and roles specified in the following three properties to view the detailed data of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value. Data type: String |
| Groups | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value. Data type: String |
| Roles | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591861-Properties-of-Table-Header-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591841-Properties-of-Table-Group-Header-in-Page-Report)
