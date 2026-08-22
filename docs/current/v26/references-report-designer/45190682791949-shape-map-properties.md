---
title: "Shape Map Properties"
id: 45190682791949
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190682791949-Shape-Map-Properties
updated_at: 2026-04-30T15:15:50Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Shape Map Properties

This topic describes the properties of a Shape Map object that you can use in query-based page reports only. 

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
| Color |  |
| Background | Specifies the background color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Others |  |
| Auto Scale in Number | Specifies whether to automatically scale the Number values in the object that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. Data type: Boolean |
| Default for Filter | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean In the same report, you can only set one data component's Default for Filter property to "true". |
| Detail Target Frame | Designer displays this property when the object is in the group header/footer panel of a banded object, and enables it after you set Go to Detail of the object to "true". You can use it to specify the target window or frame to display the detail information. Choose an option from the drop-down list.  Select to load the detail information according to the Pop Up New Window for Links property in the Page Report Studio Profile dialog box on Server. New Window Select to load the detail information into a new window. The window is not named. Whole Window Select to load the detail information into the full browser window. Same Frame Select to load the detail information into the same frame as the object. Parent Frame Select to load the detail information into the parent frame of the frame in which the object is. Other Frame Select to load the detail information into some other specified frame. Type the name of the frame you have defined in the value cell. If the frame name does not exist, Server loads the detail information into a new window. Data type: String |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML output. Data type: Boolean |
| Go to Detail | Designer displays this property when the object is in the group header/footer panel of a banded object. You can use it to specify whether to show the detail information about the group when users select the object in Page Report Studio. See Obtaining the Group Details in a Banded Object. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set Default for Filter of the object to "true". Data type: Boolean |
| Position | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel |  |
| Column Index | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab or web report's Columned property to "true" and the object's Position property is not "static". |
| Row Index | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| Border |  |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Map |  |
| Alternate Content Type | Specifies what you want to display in the tip of the areas that have data. The tip shows when you point to the area in HTML output or in Page Report Studio. Choose an option from the drop-down list. name Select to display the area names in the tip. value Select to display summary values on the areas in the tip. When there is more than one summary value on an area, Report Engine separates them by comma in the tip. customized Select to display customized tip. You can specify the tip for each area via the Alternate Text property of the area in the Shape Map Editor. Data type: Enumeration |
| Column Name | Shows the mapping name of the field that you select to use as the image source. Read only. |
| Image Source | Specifies the source of the map image. Data type: String |
| Name | Specifies the name of the map. Data type: String |
| TOC |  |
| Anchor Display Value | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Accessibility |  |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External ID | This property is mapped to the HTML attribute id, as specified by w3.org. Data type: String |
| External Style | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| Language | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |
