---
title: "Geo Map Properties"
id: 12480306492813
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480306492813-Geo-Map-Properties
updated_at: 2026-02-25T23:47:58Z
source_host: docs-report.zendesk.com
---
# 
Geo Map Properties

This topic describes the properties of a Geo Map object, that is, the geographic map object in a web report or library component.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table..

| Property Name | Available For | Description |
| --- | --- | --- |
| Geography |  |  |
| Display As | Web Report, Library Component | Specifies the display type of the map location. Choose an option from the drop-down list. Marker Select to display the map location as marker. Area Select to display the map location as area. Marker and Area Select to display the map location as marker and area. Data type: Enumeration |
| Geometry |  |  |
| Height | Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Others |  |  |
| Auto Scale in Number | Web Report, Library Component | Specifies whether to automatically scale the Number values in the object that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. Data type: Boolean |
| Default for Filter | Web Report | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean In the same report, you can only set one data component's Default for Filter property to "true". |
| Export to Excel | Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Web Report, Library Component | Specifies whether to include the object when you preview the report in Web Report Result in Designer, or when users run the report or use the library component at runtime. Data type: Boolean |
| Export to RTF | Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Invisible | Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Web Report | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set Default for Filter of the object to "true". Data type: Boolean |
| Position | Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Web Report, Library Component | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Web Report, Library Component | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| TOC |  |  |
| Anchor Display Value | Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
