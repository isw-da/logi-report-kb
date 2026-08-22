---
title: "Shape Map Properties"
id: 1500009612662
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612662-Shape-Map-Properties
updated_at: 2021-07-24T16:03:30Z
---

# Shape Map Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612642-Round-Box-Shape-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612722-Special-Field-Properties)

# Shape Map Properties

This topic lists the properties of a Shape Map object, which is supported only in page reports created using query resources.

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
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Others | |
| Auto Scale in Number | Specifies whether to automatically scale the values that are of the Number data type in the object when the values fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   Data type: Boolean |
| Default for Filter | Specifies whether to show the data component as the default component in the Apply To drop-down list of the Filter dialog in Page Report Studio. Data type: Boolean  **Note:** In a page report tab, only one data component's Default for Filter property can be set to true. |
| [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties#DetailTargetFrame) | Specifies the target window or frame in which to display the detailed information. Choose an option from the drop-down list. This property is supported on shape maps in the group header/footer panel of a banded object and enabled when [Go to Detail](#GoToDetail) is set to true. Data type: String |
| Export to Excel | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Go to Detail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. For details about its usage, refer to [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009605442-Obtaining-Detailed-Information-from-a-Banded-Object). Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to show the data component in the Apply To drop-down list of the Filter dialog in Page Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009613302-Editing-Reports#Position) | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Map | |
| Alternate Content Type | Specifies the tip type of the areas that have data. The tip is displayed when you hover the mouse pointer over the area in HTML result or in Page Report Studio. Choose an option from the drop-down list.  * **name** - If selected, names of the areas will be used as the area tips. * **value** - If selected, the summary values on the areas will be used as the area tips. If there is more than one value on an area, the summary values will be separated by comma. * **customized** - If selected, you can specify the tip for each area via the [Alternate Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009609082-Shape-Map-Editor-Dialog#Text) property of the area in the Shape Map Editor.   Data type: Enumeration |
| Column Name | Displays the mapping name of the field used as the image source. This property is read only. |
| Image Source | Specifies the source of the map image. Data type: String |
| Name | Specifies the name of the map. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612642-Round-Box-Shape-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612722-Special-Field-Properties)
