---
title: "Group Panel Properties"
id: 1500010033882
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033882-Group-Panel-Properties
updated_at: 2021-07-24T10:38:00Z
---

# Group Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033902-Detail-Panel-Properties)

# Group Panel Properties

This topic lists the properties of a Group Panel object in a banded object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Group By | Query Page Report | Shows the group field that the object is based on. If null, the object is grouped based on the whole dataset. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Others | | |
| Current Block Index | Page Report, Web Report | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010070921-Designing-the-Report-Pages#Mode). Current Block Index specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
| [Expand Detail Data](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Expand) | Page Report, Web Report | Specifies whether to expand the groups to show the details when the report is opened in Page/Web Report Studio. Only works in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010070921-Designing-the-Report-Pages#Mode). Data type: Boolean |
| Items per Block | Page Report, Web Report | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010070921-Designing-the-Report-Pages#Mode). Item per Block specifies the number of records in each data block.  Data type: Integer |
| [Shrink Footer](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Expand) | Page Report, Web Report | Specifies whether to hide the group footer panel when collapsing a group in Page/Web Report Studio. Only works in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010070921-Designing-the-Report-Pages#Mode). Data type: Boolean |
| Group Layout | | |
| Keep Group Together | Query Page Report | Specifies whether to keep the whole group together. Data type: Boolean |
| Repeat While Group Footer | Page Report, Web Report | If the group header is set to be repeated, you can specify whether to repeat the group header when a page break occurs on the group footer. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Page Report, Web Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| [Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting) | | |
| Cascade | Query Page Report | Specifies whether to allow the users, groups and roles specified in the following three properties to view the detailed data of the specified groups at current group level, including the child groups of this group level. Data type: Boolean |
| Grant | Query Page Report | Specifies which groups of data can be viewed by which users. You can define the security policy in a formula and then select the formula as the property value. Data type: String |
| Groups | Query Page Report | Specifies which groups of data can be viewed by which groups of users. You can define the security policy in a formula and then select the formula as the property value. Data type: String |
| Roles | Query Page Report | Specifies which groups of data can be viewed by which roles. You can define the security policy in a formula and then select the formula as the property value. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033902-Detail-Panel-Properties)
