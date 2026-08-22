---
title: "Properties of Shape Map in Page Report"
id: 1500009569662
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569662-Properties-of-Shape-Map-in-Page-Report
updated_at: 2021-07-24T05:54:10Z
---

# Properties of Shape Map in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569822-Properties-of-Round-Box-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map)

# Properties of Shape Map in Page Report

A shape map can have the following child objects: [Area](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map), [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009591561-Properties-of-Label-in-Page-Report-Shape-Map), [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009591581-Properties-of-Summary-Field-in-Page-Report-Shape-Map) and [Line](https://devnet.logianalytics.com/hc/en-us/articles/1500009569682-Properties-of-Line-in-Page-Report-Shape-Map).

The properties of a shape map object in a page report are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Others | |
| Default for Filter | Specifies whether to show the data component as the default component in the Apply to drop-down list of the Filter dialog in Page Report Studio. Data type: Boolean  **Note:** In a page report tab, only one data component’s Default for Filter property can be set to true. |
| Detail Target Frame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [Go To Detail](#GoToDetail) is set to true. Choose an option from the drop-down list.  * **<Server Setting>**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Page Report Studio tab of the Profile dialog in Logi JReport Server. * **New Window**  Loads the detailed information into a new window. The window is not named. * **Whole Window**  Loads the detailed information into the full browser window. * **Same Frame**  Loads the detailed information into the same frame as the object. * **Parent Frame**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If selected, you can also directly input the name of the frame you have defined in the text box. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Go to Detail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. For details about its usage, refer to [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009592841-Obtaining-Detailed-Information-from-a-Banded-Object). Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Invisible for Filter Dialogs | Specifies whether to show the data component in the Apply to drop-down list of the Filter dialog in Page Report Studio. This property cannot be edited when [Default for Filter](#DFilter) is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Map | |
| Alternate Content Type | Specifies the tip type of the areas that have data. The tip is displayed when you hover the mouse pointer over the area in HTML result or in Page Report Studio. Choose an option from the drop-down list.  * **name** - If selected, names of the areas will be used as the area tips. * **value** - If selected, the summary values on the areas will be used as the area tips. If there is more than one value on an area, the summary values will be separated by comma. * **customized** - If selected, you can specify the tip for each area via the [Alternate Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map#Text) property of the area.   Data type: Enumeration |
| Column Name | Displays the mapping name of the field used as the image source. This property is read only. |
| Image Source | Specifies the source of the map image. Data type: String |
| Name | Specifies the name of the map. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569822-Properties-of-Round-Box-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map)
