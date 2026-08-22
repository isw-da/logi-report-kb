---
title: "Properties of Label in Web Report Crosstab"
id: 1500009592061
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592061-Properties-of-Label-in-Web-Report-Crosstab
updated_at: 2021-07-24T05:54:01Z
---

# Properties of Label in Web Report Crosstab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592041-Properties-of-Formula-Field-in-Web-Report-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570162-Properties-of-DBField-in-Web-Report)

# Properties of Label in Web Report Crosstab

The header of a total row or column, the display name of a column or row field, and the display name of an aggregate field are represented as labels in the report structure tree in the Report Inspector. Their class types are CTTextField, CTDBTitleField, and CTLabelField, respectively.

The properties of a label in a web report crosstab are:

| Property Name | Description |
| --- | --- |
| Text Format | |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Text | Specifies the text in the label. Enter a string to display as the label text. Data type: String |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| **Padding** | |
| Bottom Padding | Specifies the space between the text and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the object. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the object. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: Enumeration |
| Others | |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to CSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Export to Text | Specifies whether to include the object when exporting the report to Text. Data type: Boolean |
| Export to XML | Specifies whether to include the object when exporting the report to XML. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Binding a Link to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label). Data type: String |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Transfer Style | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Accessibility | |
| Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
| Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
| Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
| Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592041-Properties-of-Formula-Field-in-Web-Report-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570162-Properties-of-DBField-in-Web-Report)
