---
title: "Properties of Table Group in Web Report"
id: 1500009570502
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570502-Properties-of-Table-Group-in-Web-Report
updated_at: 2021-07-24T05:53:57Z
---

# Properties of Table Group in Web Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570542-Properties-of-Table-Header-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592361-Properties-of-Table-Group-Header-in-Web-Report)

# Properties of Table Group in Web Report

A table group may contain the following child objects: [Table Group Header](https://devnet.logianalytics.com/hc/en-us/articles/1500009592361-Properties-of-Table-Group-Header-in-Web-Report), [Table Detail](https://devnet.logianalytics.com/hc/en-us/articles/1500009570522-Properties-of-Table-Detail-in-Web-Report)  and [Table Group Footer](https://devnet.logianalytics.com/hc/en-us/articles/1500009592341-Properties-of-Table-Group-Footer-in-Web-Report).

The properties of a table group object in a web report are as follows:

| Property Name | Description |
| --- | --- |
| Others | |
| Current Block Index | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Current Block Index specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
| Expand Detail Data | Specifies whether to expand the groups to show the details when the report is opened in Web Report Studio. Only works in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Data type: Boolean |
| Items per Block | The two properties, Current Block Index and Items per Block, work together to control the data of the object to be displayed in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode). Item per Block specifies the number of records in each data block.  Data type: Integer |
| Group Layout | |
| Keep Group Together | Specifies whether to keep the whole group together. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. A Boolean type value. |

**Note:** All these table group properties are not supported in Web Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570542-Properties-of-Table-Header-in-Web-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592361-Properties-of-Table-Group-Header-in-Web-Report)
