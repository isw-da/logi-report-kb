---
title: "Banded Page Header"
id: 1500009723702
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723702-Banded-Page-Header
updated_at: 2021-07-25T07:18:49Z
---

# Banded Page Header

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723682-Banded-Page-Footer)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723662-Banded-Page-Panel)

# Banded Page Header

The properties of a Banded Page Header object are:

| Property Name | Description |
| --- | --- |
| General | |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Shows the height of the object, in inches. This property is read only. Data type: Float |
| Width | Specifies the width of the object, in inches. Type a numeric value to change the width. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Others | |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include in Web Report Studio or when the report is opened in Web Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show or hide the object. All formulas and calculations will still be performed if the property is set to true. You can also [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Formula) whether or not to show the object. Data type: Boolean |
| Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| [Merge to Next Panel](#Panel) | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
| Record Location | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Remove Blank Row](#Panel) | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
| [Repeat in Detail Panel](#Panel) | Specifies whether to make the objects in the panel repeated in the detail panel in the exported Excel file. Data type: Boolean |
| Suppress | Specifies whether to show the object in the report. All formulas and calculations will be skipped if the property is set to true. You can also use a formula to dynamically control whether or not to show the object. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress Blank Panel | Specifies whether a panel with no data is included in the report. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |

## Merge to Next Panel, Repeat in Detail Panel, Remove Blank Row

You can control panels of a banded object in the exported Excel file by settings the three properties:

* Merge to Next Panel controls whether to merge current panel to the next panel. It applies to the banded header, banded page header, group header, and group footer panels.
* Repeat in Detail Panel controls whether to repeat certain panel with the detail panel. It applies to the group header and banded page header panels.
* Remove Blank Row controls whether to remove blank rows in the panel. It applies to the banded page header, group header, and detail panels.

The three properties take effect only when the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009751061-Web-Report) property of the web report is set to true, and there is an operation order when those three properties work together: Merge to Next Panel > Repeat in Detail Panel > Remove Blank Row.

**Notes:**

* Do not set Merge to Next Panel to true for the last group footer panel, because it will make the exported Excel file incorrect.
* Do not set Merge to Next Panel to true for the panel that contains crosstab or subreport.
* When you specify to repeat a group header panel, if there is a chart in the panel, the chart cannot be repeated.
* If a banded object contains more than one group-by fields, that is to say, it has several group header panels, when you specify to repeat the first group header panel in the detail panel, it will be repeated in the second group header panel as well.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723682-Banded-Page-Footer)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723662-Banded-Page-Panel)
