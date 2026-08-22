---
title: "Geographic Map Properties"
id: 4405661859479
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661859479-Geographic-Map-Properties
updated_at: 2022-01-27T20:35:39Z
---

# Geographic Map Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661858455-Geo-Marker-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661860503-GMarker-Properties)

# Geographic Map Properties

This topic describes the properties of a [Geographic Map object](https://devnet.logianalytics.com/hc/en-us/articles/4405661386007-Using-Geographic-Maps), that is, the geographic map in a query-based page report.

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Shows the class type of the object. This property is read only. |
| Data Inherit | Shows whether the object inherits dataset from another object. This property is read only. |
| Dataset | Shows the dataset the object applies. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Others | |
| Auto Scale in Number | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   Data type: Boolean |
| Default for Filter | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean  Note icon In the same report, you can only set one data component's Default for Filter property to "true". |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set [Default for Filter](#DFilter) of the object to "true". Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| Column Index | Specifies the X coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab to "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Specifies the Y coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab to "true" and Position of the object is not "static". Data type: Integer |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | |
| Anchor Display Value | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661858455-Geo-Marker-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661860503-GMarker-Properties)
