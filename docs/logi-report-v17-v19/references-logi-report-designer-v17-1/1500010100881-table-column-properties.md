---
title: "Table Column Properties"
id: 1500010100881
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100881-Table-Column-Properties
updated_at: 2021-07-23T19:16:42Z
---

# Table Column Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062422-Table-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062442-Table-Footer-Properties)

# Table Column Properties

This topic lists the properties of Table Column objects. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

There are four types of columns in a table: Common Column, Detail Column, Group Column and Summary Column. All these table column objects have the same properties.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Others | | |
| Auto Fit | Page Report, Web Report, Library Component | Specifies whether to adjust the width of the object according to the contents. If the property is set to true, the width of the object will be adjusted automatically only when:   * The Position property for the field/label in this object is static or relative. * If the Position property for the field/label in this object is absolute, then the Auto Fit property for the field/label should be set to true.   Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062422-Table-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062442-Table-Footer-Properties)
