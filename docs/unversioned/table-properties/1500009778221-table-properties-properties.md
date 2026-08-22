---
title: "Table Properties Properties"
id: 1500009778221
section: "Table Properties"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778221-Table-Properties-Properties
updated_at: 2021-07-24T00:47:42Z
---

# Table Properties Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749422-Special-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778241-Table-Cell-Properties)

# Table Properties

This topic describes the properties of a Table object.

Select the following links to view the topics:

* [Table Cell Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778241-Table-Cell-Properties)
* [Table Column Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749442-Table-Column-Properties)
* [Table Detail Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749462-Table-Detail-Properties)
* [Table Header Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778301-Table-Header-Properties)
* [Table Footer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778261-Table-Footer-Properties)
* [Table Group Header Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009778281-Table-Group-Header-Properties)
* [Table Group Footer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749482-Table-Group-Footer-Properties)

| Property Name | Description |
| --- | --- |
| General | |
| Display Name | Specifies the display name of the object. Data type: String |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is unavailable if the [Position](#Position) property is set to static. Type a numeric value to change the position in inches. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Alternating Line Color | |
| Include Header and Footer | Specifies whether to apply alternating color to the footer, group headers and group footers of the table. By default, it is true and all table rows except the table header will use alternating color. When it is false, alternating color will be applied to the table detail rows only. Data type: Boolean |
| Pattern List | Specifies the color patterns of the alternating color for the table rows. Select Chooser button in the value cell to specify the patterns in the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009775061-Color-List-Dialog-Box-Properties) dialog box. Data type: String |
| Show | Specifies whether to enable alternating color for the table rows. Alternating color works as the background color and will overwrite the table rows' own background color. Only when it is set to true, the settings for the properties Include Header and Footer and Pattern List can take effect. Data type: Boolean  Note iconTo make alternating color work in merged cells in group tables, you also need to set the background color of the merged cells to that of the alternating color. |
| Others | |
| Auto Scale in Number | Specifies whether to automatically scale the values that are of the Number data type when the values fall into the two ranges:   * When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.   Data type: Boolean |
| Enable Navigation | Specifies whether to enable page navigation on the table. If it is set to true, if the table contains more than one page, a page navigation bar specific for the table will be available right below it. You can use the bar to view the desired pages. When this property is set to true, you can further specify the height and width of the page for the table to display multiple pages, by setting the two properties [Navigation Height](#NavigationHeight) and [Navigation Width](#NavigationWidth). If you later resize the table, the two properties will be reset to the resized values.  Data type: Boolean |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object in Web Report Studio or when the report is opened in Web Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show or hide the object. All formulas and calculations will still be performed if the property is set to true. You can [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Formula) whether to show the object. Data type: Boolean |
| Navigation Height | Specifies the height of the page for the table to display multiple pages. Type a numeric value to specify the height. If no value is given here, Logi Report will calculate the table page height. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| Navigation Width | Specifies the width of the page for the table to display multiple pages. Type a numeric value to specify the width. If no value is given here, Logi Report will calculate the table page width. This property takes effect when [Enable Navigation](#EnableNavigation) is set to true. Data type: Float |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Position) | Specifies the position of the object. Available when the object is directly contained in the report body or a tabular cell.  * **absolute** - The object's position will be decided by its X and Y property values. * **static** - The object will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.   Data type: Enumeration |
| Split Overflow Columns | Set this property to true to display a big table with many columns on multiple pages if one page cannot hold all the columns, instead of cutting the overflow columns off - the default behavior. When the property is true, the table object containing overflow columns on subsequent pages inherits the same Y value in its container, so that it keeps the same number of records as the table in the original page. However, its X value is reset to 0 for both static and absolute positions so as to show as many columns as possible. The height of each table row for overflow columns is the same as the corresponding row height in the original page.  Data type: Boolean |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border in inches. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749422-Special-Field-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778241-Table-Cell-Properties)
