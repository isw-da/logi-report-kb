---
title: "Tabular Cell Properties"
id: 1500009635741
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009635741-Tabular-Cell-Properties
updated_at: 2021-07-24T16:03:29Z
---

# Tabular Cell Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612782-Tabular-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612822-Tabular-Row-Group-Properties)

# Tabular Cell Properties

This topic lists the properties of a Tabular Cell object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties#ReportType): Query Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Query Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Query Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Query Page Report, Web Report | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. Type a numeric value to change the position. Data type: Float |
| Y | Query Page Report, Web Report | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. Type a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Query Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Query Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Query Page Report, Web Report | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | | |
| Export to CSV | Query Page Report, Web Report | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Query Page Report, Web Report | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Query Page Report, Web Report | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Query Page Report, Web Report | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Query Page Report, Web Report | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Query Page Report, Web Report | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio. Data type: Boolean |
| Export to RTF | Query Page Report, Web Report | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Query Page Report, Web Report | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Query Page Report, Web Report | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Horizontal Alignment | Query Page Report, Web Report | Specifies the horizontal justification of the contents in the tabular cell. Choose an option from the drop-down list. Data type: Enumeration |
| Repeat Content | Query Page Report, Web Report | A cell may be extended to new pages for being affected by other cells even though it can be wholly put in the current page. In this case, if the property value is true, then its contents will appear on the new pages again. Data type: Boolean  **Note:** If there are two or more cells that will be affected in the same row group and the values of the property for these cells are true, then only the contents of the last one will be repeated. |
| Vertical Alignment | Web Report | Specifies the vertical justification of the contents in the tabular cell. Applied only when the web report runs in Web Report Studio. Choose an option from the drop-down list. Data type: Enumeration |
| Excel | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | Query Page Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index) | Query Page Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Border | | |
| Border Color | Query Page Report | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Query Page Report | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Query Page Report | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Query Page Report | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Query Page Report | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Query Page Report | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Query Page Report, Web Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Query Page Report, Web Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612782-Tabular-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612822-Tabular-Row-Group-Properties)
