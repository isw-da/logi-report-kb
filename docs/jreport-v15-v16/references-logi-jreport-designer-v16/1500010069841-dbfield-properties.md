---
title: "DBField Properties"
id: 1500010069841
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties
updated_at: 2021-07-24T10:37:56Z
---

# DBField Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069881-Refresh-Object-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034102-Filter-Control-Properties)

# DBField Properties

This topic lists the properties of a DBField object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Column | Query Page Report | Shows the column name of the field in the raw database. This property is read only. |
| Data Type | Query Page Report | Shows the data type of the field. This property is read only. |
| DBField Name | Page Report, Web Report, Library Component | Shows the mapping name of the field in the catalog. This property is read only. |
| Field Type | Query Page Report | Shows what kind of field it is. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Query | Query Page Report | Shows the query/UDS name. This property is read only. |
| Table | Query Page Report | Shows the table name of the field in the raw database. This property is read only. |
| Geometry (not supported on DBFields used as crosstab column/row fields or DBFields inside a heat map) | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. This property is read only for DBFields that are used to summarize data in a crosstab.  Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. This property is read only for DBFields that are used to summarize data in a crosstab.  Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies the identifier of the object, which must be unique in the report. The ID property value can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Excel (not supported on DBFields inside a crosstab) | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Padding (not supported on DBFields inside a heat map) | | |
| Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the left border of the object. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the right border of the object. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| Border (not supported on DBFields inside a heat map) | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Page Report, Web Report, Library Component | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Page Report, Web Report, Library Component | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | | |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| [Pattern Style](#PatternStyle) | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | | |
| Auto Fit | Page Report, Web Report, Library Component | Specifies whether to adjust the width and height of the object according to the contents. Not supported on DBFields inside a heat map. Data type: Boolean |
| Auto Scale in Number | Page Report, Web Report, Library Component | The property is available when the object is of the Number data type. It specifies whether to automatically scale the object values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   The option "auto" means that the property setting follows that of the object's parent data container.  Data type: Boolean |
| Bold | Page Report, Web Report, Library Component | Specifies whether to make the text bold. Data type: Boolean |
| Convert HTML Tag | Query Page Report | Specifies whether or not to parse the HTML tag elements that are written in the text of the object in the report result.  * **true** - Logi JReport Engine will parse the HTML tag elements in the report result. * **false** - HTML tag elements will not be parsed in the report result.   This property takes effect when the object's [Position](#Position) property is set to absolute. It is not supported on DBFields inside a crosstab.  **Note:** The property does not work when viewing or exporting the report in the Page Report Result or JReport Result format.  Data type: Boolean |
| Font Face | Page Report, Web Report, Library Component | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| [Format](#Format) | Page Report, Web Report, Library Component | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Notes:**   * For the BigDecimal data type, to avoid precision loss, you should enter a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with the Auto Scale in Number property, for example the values are displayed in percentage, then the Auto Scale in Number property is ignored. |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. This property is not supported on DBFields inside a heat map.  Data type: Enumeration |
| Ignore HTML Tag | Query Page Report | Specifies whether or not to ignore the HTML tag elements that are written in the text of the object in the HTML result of the report.  * **true** - HTML tag elements in the text will not be parsed. * **false** - HTML tag elements in the text will be transferred as they are translated into HTML by the web browser.   Data type: Boolean |
| Italic | Page Report, Web Report, Library Component | Specifies whether to make the text italic. Data type: Boolean |
| Maximum Width | Page Report, Web Report, Library Component | Specifies the maximum width of the text displayed. Enter a numeric value to change the width. This property often works with the Auto Fit property. If Auto Fit = true and Maximum Width is not equal to 0, the text will extend until the width is this value.  Data type: Float |
| Strikethrough | Page Report, Web Report, Library Component | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Page Report, Web Report, Library Component | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. This property is not supported on DBFields inside a heat map.  Data type: Enumeration |
| Word Wrap | Page Report, Web Report, Library Component | Specifies whether to wrap the text to the width. Not supported on DBFields inside a heat map. Data type: Boolean |
| Others | | |
| Cache Value | Query Page Report | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
| Column Name | Query Page Report | Substitutes the current field with another field by selecting from the drop-down list. To make the property editable, uncheck Forbid changing column in the Options dialog (File > Options > Panel > Forbid changing column).  Data type: String |
| Data Mapping File | Page Report, Web Report, Library Component | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010033362-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| Detail Report | Query Page Report | Specifies the detail report that the object is linked to. Select  in the value cell to set the detail report. For details, refer to [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports#Detail). This property is not supported on DBFields that are inside a crosstab.  Data type: String |
| [Detail Target Frame](#DetailTargetFrame) | Page Report | This property is supported on DBFields in the group header/footer panel of a banded object and enabled when [Go to Detail](#GoToDetail) is set to true. Specifies the target window or frame in which to display the detailed information. Choose an option from the drop-down list.  Data type: String |
| Display Null | Page Report， Web Report, Library Component | Specifies the string to be displayed if the field value is null. Data type: String |
| Enable Hyperlink in Excel | Page Report, Web Report, Library Component | Specifies whether to enable the link defined on the object in the Excel result of the report. Not supported on DBFields that are inside a crosstab in a web report/library component. Data type: Boolean |
| Enable Hyperlink in HTML | Page Report, Web Report, Library Component | Specifies whether to enable the link defined on the object in the HTML result of the report. Not supported on DBFields that are inside a crosstab in a web report/library component. Data type: Boolean |
| Enable Hyperlink in PDF | Page Report, Web Report, Library Component | Specifies whether to enable the link defined on the object in the PDF result of the report. Not supported on DBFields that are inside a crosstab in a web report/library component. Data type: Boolean |
| [Expand Data](https://devnet.logianalytics.com/hc/en-us/articles/1500010034082-Crosstab-Properties#Expand) | Page Report | This property is supported on DBFields that are used as column/row fields in a crosstab only. It specifies whether to allow Page Report Studio users to expand and collapse the details of the column/row group generated by the field in a crosstab. This property works only when the [Expand Data](https://devnet.logianalytics.com/hc/en-us/articles/1500010034082-Crosstab-Properties#ExpandData) property of the crosstab is set to true.  Data type: Boolean |
| [Expand Detail Data](https://devnet.logianalytics.com/hc/en-us/articles/1500010034082-Crosstab-Properties#Expand) | Page Report | This property is supported on DBFields that are used as column/row fields in a crosstab only. It specifies whether the details of the column/row group generated by the field in a crosstab is expanded by default in Page Report Studio. It is meaningful to enable the property only when the field's Expand Data property is set to true.  Data type: Boolean |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Not available when the object is displayed as a rank, image or image button in page report. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field, and only the text will be included when the object is displayed as a radio button or button. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML result of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| [Filter Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#FilterOptions) | Query Page Report | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. Data type: Integer |
| Go to Detail | Query Page Report | This property is available only when the object is in the group header/footer panel of a banded object. Specifies whether to show the detailed information when you select the object in Page Report Studio. For details about its usage, refer to [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010028622-Obtaining-Detailed-Information-from-a-Banded-Object).  Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Not supported on DBFields that are inside a crosstab. Data type: Boolean |
| Link | Page Report, Web Report, Library Component | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports). Data type: String |
| Logic Column | Page Report, Web Report, Library Component | This property is supported when the object is in a table. Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Choose an option from the drop-down list.  Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| Order By | Query Page Report | This property is supported on DBFields that are used as column/row fields in a crosstab only. It specifies the field by which to sort the data. Data type: String |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Not supported on DBFields that are inside a crosstab or heat map. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#RecordLocation) | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Query Page Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. For a DBField as a column or row header in a crosstab, setting Suppress to true will only hide the column or row header without affecting the calculation and the other part of the crosstab will remain the same in the report result. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Query Page Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Suppress When Null | Query Page Report | If true and its value is null, the field will not be displayed. Data type: Boolean |
| Transfer Style | Page Report, Web Report, Library Component | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Value Delimiter | Page Report, Web Report, Library Component | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#TOC) (only supported on DBFields in a banded object) | | |
| Anchor Display Value | Page Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| Abbr | Page Report, Web Report, Library Component | This property is supported on DBFields that are inside a crosstab only. It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content.  Data type: String |
| Axis | Page Report, Web Report, Library Component | This property is supported on DBFields that are inside a crosstab only. It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names.  Data type: String |
| External AccessKey | Query Page Report | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External Dir | Query Page Report | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * **LTR** - Left-to-right text or table. * **RTL** - Right-to-left text or table.   Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | Query Page Report | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | Query Page Report | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Headers | Page Report, Web Report, Library Component | This property is supported on DBFields that are inside a crosstab only. It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute.  Data type: String |
| HrefLang | Query Page Report | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | Query Page Report | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
| Scope | Page Report, Web Report, Library Component | This property is supported on DBFields that are inside a crosstab only. It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:   * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated in the HTML result   Data type: String |

**Note:** Only these DBField properties can be rendered in Web Report Studio and JDashboard:

* Data Mapping File
* Link
* Properties available to the DBField object in the Inspector panel of Web Report Studio.

## Pattern Style

The property can be set to one of the following:

* **none** - No pattern will be applied to the object.
* **50%** - The object will be filled in the Pattern Color of 50%-transparency.
* **horizontal** - The pattern will be made of horizontal lines of the Pattern Color.
* **vertical** - The pattern will be made of vertical lines of the Pattern Color.
* **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color.
* **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.

## Format

This property indicates what will be displayed in the report result. In other words, no matter in what kind of format the data is stored in the database, you can specify the format in which to display the result. For example, for a Number-type field about product price, we have the following formats for you to choose:

#,###  
#,###.##  
$#,##0.00  
...

You select $#,##0.00, and then a value displays as $6.05. You can enter manually as $#,##0.000, then the value is displayed as $6.050.

## Detail Target Frame

The property can be set to one of the following:

* **<Server Setting>** - Loads the detailed information according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server.
* **New Window** - Loads the detailed information into a new window. The window is not named.
* **Whole Window** - Loads the detailed information into the full browser window.
* **Same Frame** - Loads the detailed information into the same frame as the object.
* **Parent Frame** - Loads the detailed information into the parent frame of the frame in which the object is.
* **Other Frame** - Loads the detailed information into some other specified frame. If selected, you can also directly input the name of the frame you have defined in the text box. If the frame name does not exist, the detailed information will be loaded into a new window.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069881-Refresh-Object-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034102-Filter-Control-Properties)
