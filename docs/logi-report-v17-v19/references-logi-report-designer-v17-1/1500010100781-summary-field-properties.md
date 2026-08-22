---
title: "Summary Field Properties"
id: 1500010100781
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100781-Summary-Field-Properties
updated_at: 2021-07-23T19:16:40Z
---

# Summary Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062402-Subreport-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100801-Table-Properties)

# Summary Field Properties

This topic lists the properties of a Summary Field object, which is supported only in page reports created using query resources.

| Property Name | Description |
| --- | --- |
| General | |
| Aggregate Function | Shows the function of the summary. This property is read only. |
| Field Type | Shows what kind of field it is. This property is read only. |
| Group By | Shows the group field that the summary is based on. If null, the summary is grouped based on the whole dataset. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Summary Name | Shows the name of the summary. This property is read only. |
| Summary On | Shows the name of the field on which to perform the summary function. This property is read only. |
| Geometry (not supported on summaries inside a heat map) | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Padding (not supported on summaries inside a heat map) | |
| Bottom Padding | Specifies the space between the text and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border (not supported on summaries inside a heat map) | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#PatternStyle) | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the object according to the contents. Not supported on summaries inside a heat map. Data type: Boolean |
| Auto Scale in Number | The property is available when the object is of the Number data type. It specifies whether to automatically scale the object values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.   The option "auto" means that the property setting follows that of the object's parent data container.  Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Convert HTML Tag | Specifies whether or not to parse the HTML tag elements that are included in the text of the object as the web browser translates them into HTML in the report result. There are the following limitations on the property:   * It takes effect only when the object's [Position](#Position) property is set to absolute. * It does not work when you view or export the report in the Page Report Result or Logi Report Result format.   Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#Format) | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  Note icon   * For the BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the Format property value. * For the Number data type and when the [Auto Scale in Number](#Scale) property is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with the Auto Scale in Number property, for example the values are displayed in percentage, then the Auto Scale in Number property is ignored. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Not supported on summaries inside a heat map. Data type: Enumeration |
| Ignore HTML Tag | Specifies whether or not to ignore the HTML tag elements that are included in the text of the object at runtime and in the HTML output of the report.  * **true** - Logi Report Engine does not parse the HTML tag elements so they display exactly as what they are. * **false** - Logi Report Engine transfers the HTML tag elements to the web browser so they are translated into HTML by the web browser.   **Note:** The property [Convert HTML Tag](#ConvertHTMLTag) has higher priority than Ignore HTML Tag.  Data type: Boolean |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Maximum Width | Specifies the maximum width of the text displayed. Type a numeric value to change the width. This property often works with the Auto Fit property. If Auto Fit is true and Maximum Width is not equal to 0, the text will extend until the width is this value.  Data type: Float |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Not supported on summaries inside a heat map. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Not supported on summaries inside a heat map. Data type: Boolean |
| Others | |
| Cache Value | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
| Column Name | Substitutes the current field with another field by selecting from the drop-down list. To make the property editable, clear **Forbid changing column** in the Options dialog box (**File** > **Options** > **Panel** > **Forbid changing column**).  Data type: String |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| Detail Report | Specifies the detail report that the object is linked to. Select the ellipsis button Ellipsis button in the value cell to set the detail report. For more information, see [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports#Detail). Data type: String |
| [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#DetailTargetFrame) | This property is supported on summary fields in the group header/footer panel of a banded object and enabled when [Go to Detail](#GoToDetail) is set to true. Specifies the target window or frame in which to display the detailed information. Choose an option from the drop-down list.  Data type: String |
| Display Null | Specifies the string to be displayed if the field value is null. Data type: String |
| Enable Hyperlink in Excel | Specifies whether to enable the link defined on the object in the Excel output of the report. Data type: Boolean |
| Enable Hyperlink in HTML | Specifies whether to enable the link defined on the object in the HTML output of the report. Data type: Boolean |
| Enable Hyperlink in PDF | Specifies whether to enable the link defined on the object in the PDF output of the report. Data type: Boolean |
| Export to CSV | Specifies whether to include the object in the CSV output of the report. If it is set to true, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| Export to Excel | Specifies whether to include the object in the Excel output of the report. If it is set to true, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output of the report. If it is set to true, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output of the report. If it is set to true, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output of the report. If it is set to true, only the string value will be included when the object is displayed as a text field, and only the text will be included when the object is displayed as a radio button or button. Data type: Boolean |
| Export to Text | Specifies whether to include the object in the Text output of the report. If it is set to true, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML output of the report. If it is set to true, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| [Filter Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#FilterOptions) | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. Data type: Integer |
| Go to Detail | This property is available only when the object is in the group header/footer panel of a banded object. Specifies whether to show the detailed information when you select the object in Page Report Studio. For more information, see [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010056722-Obtaining-Detailed-Information-from-a-Banded-Object).  Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select Ellipsis button in the value cell to set the link target. For more information, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports). Data type: String |
| Logic Column | This property is supported when the object is in a table. Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Choose an option from the drop-down list.  Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Specifies the position of the object. Choose an option from the drop-down list. Not supported on summaries inside a heat map. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#RecordLocation) | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Suppress When Null | If true and its value is null, the field will not be displayed. Data type: Boolean |
| Transfer Style | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Value Delimiter | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#TOC) (not supported on summaries inside a heat map) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External Dir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * **LTR** - Left-to-right text or table. * **RTL** - Right-to-left text or table.   Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Type an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
| Tag Name | It specifies the header tag name of the object used for labeling the heading order of the object in the PDF output for accessibility.  When setting the property, you should make sure that the headers are nested properly following the rules below so that the heading tag sequence can be accepted by Adobe.   * If any heading tags are used, H1 should be the first. * The descending sequence of the headers should follow the downward order of the objects in the Report Inspector. * The descending sequence of the headers should proceed in strict numerical order and should not skip an intervening heading level. *H1 H2 H3* is permissible, while *H1 H3* is not.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062402-Subreport-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100801-Table-Properties)
