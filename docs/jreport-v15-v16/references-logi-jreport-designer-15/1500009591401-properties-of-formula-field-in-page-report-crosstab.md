---
title: "Properties of Formula Field in Page Report Crosstab"
id: 1500009591401
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591401-Properties-of-Formula-Field-in-Page-Report-Crosstab
updated_at: 2021-07-24T05:54:12Z
---

# Properties of Formula Field in Page Report Crosstab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591381-Properties-of-DBField-in-Page-Report-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591421-Properties-of-Label-in-Page-Report-Crosstab)

# Properties of Formula Field in Page Report Crosstab

The properties of a formula field object in a crosstab of a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Data Type | Shows the data type of the formula. This property is read only. |
| Expression | Shows the expression of the formula. This property is read only. |
| Field Type | Shows what kind of field it is. This property is read only. |
| Formula Editor | Edits the formula. Select  to display the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog), in which you can edit the formula as required. |
| Formula Name | Shows the name of the formula. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry (only for aggregate field) | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Displays the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is read only. |
| Y | Displays the vertical coordinate of the top left corner of the object, relative to its parent container. This property is read only. |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
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
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: Enumeration |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width of the object according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should enter a prefix JRD when setting the format property value. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Ignore HTML Tag | Specifies whether or not to ignore the HTML tags when exporting the report results to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report results to HTML format.   This property is useful for exporting the report results to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: Boolean |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Maximum Width | Specifies the maximum width of the text displayed. Enter a numeric value to change the width. Data type: Float |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Others | |
| Cache Value | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
| Column Name | Substitutes the current field with another field by selecting from the drop-down list. To make the property editable, uncheck Forbid changing column in the Options dialog (**File** > **Options** > **Panel** > **Forbid changing column**).  Data type: String |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500009589921-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| Detail Target Frame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [Go To Detail](#GoToDetail) is set to true. Choose an option from the drop-down list.  * **<Server Setting>**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the detailed information into a new window. The window is not named. * **Whole Window**  Loads the detailed information into the full browser window. * **Same Frame**  Loads the detailed information into the same frame as the object. * **Parent Frame**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If selected, you can also directly input the name of the frame you have defined in the text box. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
| Display Null | Specifies the string to be displayed if the field value is null. Data type: String |
| Enable Hyperlink in Excel | Specifies whether to enable the link defined on the object when exporting the report to an Excel file. Data type: Boolean |
| Enable Hyperlink in HTML | Specifies whether to enable the link defined on the object when exporting the report to an HTML file. Data type: Boolean |
| Enable Hyperlink in PDF | Specifies whether to enable the link defined on the object when exporting the report to a PDF file. Data type: Boolean |
| [Expand Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab) | Specifies whether to enable Page Report Studio users to expand/collapse the details of the field which is as dimension (group level) in the crosstab. This property works only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode) and when the [Expand Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009591341-Properties-of-Crosstab-in-Page-Report#ExpandData) property of the crosstab is set to true. It is not available for aggregate field. Data type: Boolean |
| [Expand Detail Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab) | Specifies whether to display the details of the field by default in Page Report Studio. This property works only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Mode), and is not available for aggregate field. It is meaningful to enable the property only when the field's Expand Data property is set to true. Data type: Boolean |
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
| Filter Options | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. For more information, refer to [Setting Filter Options for an Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object). Data type: Integer |
| Go to Detail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. For details about its usage, refer to [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009592841-Obtaining-Detailed-Information-from-a-Banded-Object). Data type: Boolean |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Binding a Link to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label). Data type: String |
| Order By | Specifies the field by which to sort the data. Not available for aggregate field. Data type: String |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Suppress When Null | If true and its value is null, the field will not be displayed. Data type: Boolean |
| Transfer Style | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Value Delimiter | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
| Accessibility | |
| Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
| Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External Dir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
| Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591381-Properties-of-DBField-in-Page-Report-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591421-Properties-of-Label-in-Page-Report-Crosstab)
