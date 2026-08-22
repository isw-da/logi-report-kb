---
title: "Banded Object Properties"
id: 1500009777721
section: "Banded Object Properties"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777721-Banded-Object-Properties
updated_at: 2021-07-24T00:47:49Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749122-Web-Report-Object-Property-Reference)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777761-Banded-Footer-Properties)

# Banded Object Properties

This topic describes the properties of a Banded Object.

Select the following links to view the topics:

* [Banded Footer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777761-Banded-Footer-Properties)
* [Banded Header Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749162-Banded-Header-Properties)
* [Banded Page Footer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777821-Banded-Page-Footer-Properties)
* [Banded Page Header Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777841-Banded-Page-Header-Properties)
* [Banded Page Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749182-Banded-Page-Panel-Properties)
* [Detail Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777741-Detail-Panel-Properties)
* [Group Footer Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749142-Group-Footer-Panel-Properties)
* [Group Header Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777801-Group-Header-Panel-Properties)
* [Group Panel Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009777781-Group-Panel-Properties)

| Property Name | Description |
| --- | --- |
| General | |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Auto Fit | Specifies whether to automatically adjust the width of a vertical banded object or the height of a horizontal banded object according to the contents. Data type: Boolean |
| Height | Shows the height of the object, in inches. This property is read only. Data type: Float |
| Width | Specifies the width of the object, in inches. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
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
| Auto Scale in Number | Specifies whether to automatically scale the values that are of the Number data type when the values fall into the two ranges:   * When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.   Data type: Boolean |
| Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
| Enable Navigation | Specifies whether to enable page navigation on the banded object. If it is set to true, if the banded object contains more than one page, a page navigation bar specific for the banded object will be available right below it. You can use the bar to view the desired pages. When this property is set to true, you can further specify the height and width of the page for the banded object to display multiple pages, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). If you later resize the banded object, the two properties will be reset to the resized values.  Data type: Boolean |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include in Web Report Studio or when the report is opened in Web Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show or hide the object. All formulas and calculations will still be performed if the property is set to true. You can also [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Formula) whether to show the object. Data type: Boolean |
| Navigation Height | Specifies the height of the page for the banded object to display multiple pages. Type a numeric value to specify the height. If no value is given here, Logi Report will calculate the banded object page height. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| Navigation Width | Specifies the width of the page for the banded object to display multiple pages. Type a numeric value to specify the width. If no value is given here, Logi Report will calculate the banded object page width. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Position) | Specifies the position of the object. Available when the object is directly contained in the report body or a tabular cell.  * **absolute** - The object's position will be decided by its X and Y property values. * **static** - The object will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.   Data type: Enumeration |
| Record Location | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the report. All formulas and calculations will be skipped if the property is set to true. You can also use a formula to dynamically control whether to show the object. Data type: Boolean  Note iconWhen you set both the **Invisible** and **Suppress** properties of an object to **true**, Suppress has the higher priority. |
| Suppress When Empty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749122-Web-Report-Object-Property-Reference)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777761-Banded-Footer-Properties)
