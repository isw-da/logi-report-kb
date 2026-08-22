---
title: "Shape Map Properties"
id: 4405664670615
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664670615-Shape-Map-Properties
updated_at: 2022-01-27T20:38:21Z
---

# Shape Map Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661886231-Round-Box-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664672663-Special-Field-Properties)

# Shape Map Properties

This topic describes the properties of a [Shape Map object](https://devnet.logianalytics.com/hc/en-us/articles/4405664397975-Using-Shape-Maps) that you can use in query-based page reports only.

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Others | |
| Auto Scale in Number | Specifies whether to automatically scale the Number values in the object that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   Data type: Boolean |
| Default for Filter | Specifies whether to display the object as the default data component in the Apply To drop-down list of the Filter dialog box at runtime. Data type: Boolean  Note icon In the same report, you can only set one data component's Default for Filter property to "true". |
| Detail Target Frame | Designer displays this property when the object is in the group header/footer panel of a banded object, and enables it after you set [Go to Detail](#GoToDetail) of the object to "true". You can use it to specify the target window or frame to display the detail information. Choose an option from the drop-down list.  * **<Server Setting>** Select to load the detail information according to setting of the Pop up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Server. * **New Window** Select to load the detail information into a new window. The window is not named. * **Whole Window** Select to load the detail information into the full browser window. * **Same Frame** Select to load the detail information into the same frame as the object. * **Parent Frame** Select to load the detail information into the parent frame of the frame in which the object is. * **Other Frame** Select to load the detail information into some other specified frame. Type the name of the frame you have defined in the value cell. If the frame name does not exist, Server loads the detail information into a new window.   Data type: String |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML output. Data type: Boolean |
| Go to Detail | Designer displays this property when the object is in the group header/footer panel of a banded object. You can use it to specify whether to show the detail information about the group when users select the object in Page Report Studio. For more information, see [Obtaining the Group Details in a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661346583-Obtaining-the-Group-Details-in-a-Banded-Object). Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to display the object in the Apply To drop-down list of the Filter dialog box at runtime. Designer disables this property when you set [Default for Filter](#DFilter) of the object to "true". Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| Column Index | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Index | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab to "true" and Position of the object is not "static". Data type: Integer |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Map | |
| Alternate Content Type | Specifies the tip type of the areas that have data. The tip shows when you hover over the area in HTML output or in Page Report Studio. Choose an option from the drop-down list.  * **name** - If selected, names of the areas will be used as the area tips. * **value** - If selected, the summary values on the areas will be used as the area tips. If there is more than one value on an area, the summary values will be separated by comma. * **customized** - If selected, you can specify the tip for each area via the [Alternate Text](https://devnet.logianalytics.com/hc/en-us/articles/4405661645975-Shape-Map-Editor-Dialog-Box#Text) property of the area in the Shape Map Editor.   Data type: Enumeration |
| Column Name | Displays the mapping name of the field used as the image source. This property is read only. |
| Image Source | Specifies the source of the map image. Data type: String |
| Name | Specifies the name of the map. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) | |
| Anchor Display Value | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661886231-Round-Box-Shape-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664672663-Special-Field-Properties)
