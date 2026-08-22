---
title: "Geographic Map Properties"
id: 28898524989197
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898524989197-Geographic-Map-Properties
updated_at: 2024-09-30T09:10:56Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Geographic Map Properties

This topic describes the properties of a Geographic Map object, that is, the geographic map in a query-based page report.

| Property Name | Description |
| --- | --- |
| General |  |
| Class Type | Shows the class type of the object. Read only. |
| Data Inherit | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Shows the dataset the object applies. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Geometry |  |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Others |  |
| Auto Scale in Number | Specifies whether to automatically scale the Number values in the object that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. Data type: Boolean |
| Default for Filter | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean In the same report, you can only set one data component's Default for Filter property to "true". |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set Default for Filter of the object to "true". Data type: Boolean |
| Position | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel |  |
| Column Index | Specifies the X coordinate of the object relative to its parent container in the Excel output, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| Row Index | Specifies the Y coordinate of the object relative to its parent container in the Excel output, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| TOC |  |
| Anchor Display Value | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Accessibility |  |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External ID | This property is mapped to the HTML attribute id, as specified by w3.org. Data type: String |
| External Style | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| Language | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |

Previous Topic  Next Topic
