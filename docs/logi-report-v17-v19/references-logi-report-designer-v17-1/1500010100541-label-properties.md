---
title: "Label Properties"
id: 1500010100541
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties
updated_at: 2021-07-23T19:16:36Z
---

# Label Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100521-KPI-Chart-Paper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100561-Line-Properties)

# Label Properties

This topic lists the properties of a Label object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Reference | Query Page Report | Shows the instance name of the field if the label is related to a field. This property is read only. |
| Text Format | | |
| [Auto Fit](#Autofit) | Page Report, Web Report, Library Component | Specifies whether to adjust the width and height of the object according to the contents. Not supported on labels that are inside a crosstab or heat map or on basic web controls. Data type: Boolean |
| Auto Map Field Name | Page Report, Web Report, Library Component | Enabled when the label is related to a field. It specifies whether to automatically map the label text to the dynamic display name of the field at runtime. If true, the text specified via the [Text](#Text) property will be ignored. You can customize the display names for fields [in query resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets#Customize) and [in business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Element). Data type: Boolean |
| Bold | Page Report, Web Report, Library Component | Specifies whether to make the text bold. Data type: Boolean |
| Convert HTML Tag | Query Page Report | Specifies whether or not to parse the HTML tag elements that are included in the text of the object as the web browser translates them into HTML in the report result. There are the following limitations on the property:   * It is not supported on labels inside a crosstab. * It takes effect only when the object's [Position](#Position) property is set to absolute. * It does not work when you view or export the report in the Page Report Result or Logi Report Result format.   Data type: Boolean |
| Font Face | Page Report, Web Report, Library Component | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Not supported on labels that are inside a heat map. Data type: Enumeration |
| Ignore HTML Tag | Page Report, Marks content and feature updates for Logi Report v17.1. New feature new content.Web Report, Library Component | Specifies whether or not to ignore the HTML tag elements that are included in the text of the object at runtime and in the HTML output of the report.  * **true** - Logi Report Engine does not parse the HTML tag elements so they display exactly as what they are. * **false** - Logi Report Engine transfers the HTML tag elements to the web browser so they are translated into HTML by the web browser.   **Note:** The property [Convert HTML Tag](#ConvertHTMLTag) has higher priority than Ignore HTML Tag.  Data type: Boolean |
| Italic | Page Report, Web Report, Library Component | Specifies whether to make the text italic. Data type: Boolean |
| [Maximum Width](#Autofit) | Query Page Report | Specifies the maximum width of the text displayed. Type a numeric value to change the width. This property often works with the Auto Fit property. If Auto Fit is true and Maximum Width is not equal to 0, the text will extend until the width is this value.  Data type: Float |
| Strikethrough | Page Report, Web Report, Library Component | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Text | Page Report, Web Report, Library Component | Specifies the text in the label. Type a string to display as the label text. Data type: String |
| Underline | Page Report, Web Report, Library Component | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Not supported on labels that are inside a heat map. Data type: Enumeration |
| [Word Wrap](#Autofit) | Page Report, Web Report, Library Component | Specifies whether to wrap the text to the width. Not supported on labels that are inside a heat map or on basic web controls. Data type: Boolean |
| Geometry (not supported on labels inside a crosstab or heat map) | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| CSS | | |
| [Class](#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](#CSS) | Page Report, Web Report, Library Component | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Excel (not supported on labels inside a crosstab) | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Padding (not supported on labels inside a heat map or on basic web controls) | | |
| Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border (not supported on labels inside a heat map) | | |
| Border Color | Page Report, Web Report, Library Component | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Page Report, Web Report, Library Component | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Page Report, Web Report, Library Component | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | | |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#PatternStyle) | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Others | | |
| Bind Column | Query Page Report, Web Report, Library Component | Specifies to bind the label with a field so that the report users can use the label's shortcut menu to filter and sort records of the bound field in Page/Web Report Studio and JDashboard. When a label is bound with a field, you can further set the label's [Filterable](#BindColumn) and [Sortable](#BindColumn) properties to true to display the corresponding buttons beside the label for easy filtering and sorting. This property is not supported on labels that are inside a crosstab.  Data type: String |
| Detail Report | Query Page Report | Specifies the detail report that the object is linked to. Select Ellipsis button in the value cell to set the detail report. For more information, see [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports#Detail). This property is not supported on labels that are inside a crosstab.  Data type: String |
| [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500010062062-DBField-Properties#DetailTargetFrame) | Page Report | This property is supported on labels in the group header/footer panel of a banded object and enabled when [Go to Detail](#GoToDetail) is set to true. Specifies the target window or frame in which to display the detailed information. Choose an option from the drop-down list.  Data type: String |
| Enable Hyperlink in Excel | Page Report, Web Report, Library Component | Specifies whether to enable the link defined on the object in the Excel output of the report. Not supported on labels that are inside a crosstab in a web report/library component. Data type: Boolean |
| Enable Hyperlink in HTML | Page Report, Web Report, Library Component | Specifies whether to enable the link defined on the object in the HTML output of the report. Not supported on labels that are inside a crosstab in a web report/library component. Data type: Boolean |
| Enable Hyperlink in PDF | Page Report, Web Report, Library Component | Specifies whether to enable the link defined on the object in the PDF output of the report. Not supported on labels that are inside a crosstab in a web report/library component. Data type: Boolean |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a text field, and only the text will be included when the object is displayed as a radio button or button. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output of the report. If it is set to true in page report, only the string value will be included when the object is displayed as a barcode or text field, and only the text will be included when the object is displayed as a checkbox, radio button or button. Data type: Boolean |
| [Filter Options](#FilterOptions) | Query Page Report, Web Report, Library Component | When the label has a [Bind Column](#BindColumn), you can set this property to specify the filter-related options that will be displayed on the Filter submenu when right-clicking the label in Page/Web Report Studio and JDashboard. Data type: Integer |
| [Filterable](#BindColumn) | Query Page Report, Web Report, Library Component | If true, a filter button appears beside the label when viewing the report or library component in Page/Web Report Studio or JDashboard. You can use the button to filter the records based on values of the field specified via the [Bind Column](#BindColumn) property. Data type: Boolean |
| Go to Detail | Query Page Report | This property is available only when the object is in the group header/footer panel of a banded object. Specifies whether to show the detailed information when you select the object in Page Report Studio. For more information, see [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010056722-Obtaining-Detailed-Information-from-a-Banded-Object).  Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Link | Page Report, Web Report, Library Component | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select Ellipsis button in the value cell to set the link target. For more information, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010101261-Adding-Links-in-Reports). Data type: String |
| Logic Column | Page Report, Web Report, Library Component | This property is supported when the object is in a table. Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Choose an option from the drop-down list.  Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Not supported on labels that are inside a crosstab or heat map. Data type: Enumeration |
| [Record Location](#RecordLocation) | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Sortable](#BindColumn) | Query Page Report, Web Report, Library Component | If true, a sort button appears beside the label when viewing the report or library component in Page/Web Report Studio or JDashboard. You can use the button to arrange the records of a specific field in ascending or descending order. The field is specified via the [Bind Column](#BindColumn) property. This property is not supported on labels that are inside a crosstab.  Data type: Boolean |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress Aggregate | Query Page Report | This property is supported on labels (excluding summary labels) that are inside a crosstab only. It specifies whether to hide the Total row or column. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to display the object in the results when no record is returned to its parent data component. Data type: Boolean |
| Transfer Style | Page Report, Web Report, Library Component | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#TOC) | | |
| Anchor Display Value | Query Page Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Query Page Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| Abbr | Page Report, Web Report, Library Component | This property is supported on labels that are inside a crosstab only. It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content.  Data type: String |
| Axis | Page Report, Web Report, Library Component | This property is supported on labels that are inside a crosstab only. It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names.  Data type: String |
| External AccessKey | Query Page Report | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External Dir | Query Page Report | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * **LTR** - Left-to-right text or table. * **RTL** - Right-to-left text or table.   Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | Query Page Report | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Type an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | Query Page Report | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Headers | Page Report, Web Report, Library Component | This property is supported on labels that are inside a crosstab only. It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute.  Data type: String |
| HrefLang | Query Page Report | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | Query Page Report | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
| Scope | Page Report, Web Report, Library Component | This property is supported on labels that are inside a crosstab only. It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:   * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated in the HTML output.   Data type: String |
| Tag Name | Page Report, Web Report, Library Component | This property is not supported on labels that are in a chart or map. It specifies the header tag name of the object used for labeling the heading order of the object in the PDF output for accessibility.  When setting the property, you should make sure that the headers are nested properly following the rules below so that the heading tag sequence can be accepted by Adobe.   * If any heading tags are used, H1 should be the first. * The descending sequence of the headers should follow the downward order of the objects in the Report Inspector. * The descending sequence of the headers should proceed in strict numerical order and should not skip an intervening heading level. *H1 H2 H3* is permissible, while *H1 H3* is not.   Data type: Enumeration |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) For labels in web reports and library component, only these properties can be rendered in Web Report Studio and JDashboard:

* Link
* Properties available to the Label object in the Inspector panel of Web Report Studio.

## Auto Fit , Maximum Width, Word Wrap

Here is a label:  
**Label product sales by region**

We want to show it as:  
**Label product  
sales by region**

We can set the following:

* Auto Fit: true
* Maximum Width: 1
* Word Wrap: true

Auto Fit=true enables the contents to grow horizontally but stop when the width becomes 1. Word Wrap=true enables the remaining contents to wrap downward if no space is left horizontally.

## Style, ID, Class

The following is an example of using the Style, ID, Class property values as style sheet selectors in a CSS style file:

NewCSSFile.css:

`@charset "GBK";  
 TextField {Background: #ff0000}  
 /*Style=LabelX*/  
 TextField[Style="LabelX"]{Background: #0000FF}  
 /*ID=W*/  
 TextField#W{Background: #FFFF00}   
 /*class=C*/  
 TextField.C{Background: #00FFFF}`

## Bind Column

By default, the Sort and Filter shortcut menu items are only available on fields (including DBField, formula and summary) in banded objects or tables. Logi Report provides you with the option to enable the two menu items on labels in the banded objects or tables by binding them with fields.

1. Select a label in a banded object or table.
2. In the Report Inspector, locate the Bind Column property. All the fields used in the banded object or table are listed in the property's value drop-down list. Select one to bind with the label.
3. If you want to display the sort and filter buttons beside the label at server runtime which provide another easy way for sorting and filtering, go on set the Sortable and Filterable properties of the label to true.
4. Save the report and publish it to Server.
5. Run the report and you can then right-click the label or the proper button beside the label to sort or filter the records of the bound field.

   ![Label Bind with Column](https://devnet.logianalytics.com/hc/article_attachments/4404856851351/prpty_rpt_lbl.htm.gif)

When a label in a page report is bound with a field, you can further specify the options that will be displayed on its Filter submenu at runtime with its [Filter Options](#FilterOptions) property.

## Filter Options

When you run a page report that is created using query resources in Page Report Studio, if you right-click a filterable label (a label with a [Bind Column](#BindColumn)) in a banded object or table, or a field (including DBField, formula and summary) in the report, you will find the Filter submenu. This submenu can list items such as Remove Filter, Top N, Bottom N, and More. With these menu items you can easily filter the records. While if you do not want to show some of the four items for a field or filterable label, you can set the filter options in Designer as follows.

1. Select the field or label and locate its Filter Options property in the Report Inspector.
2. Select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the value cell. Designer displays the Filter Options dialog box.

   ![Filter Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856851607/fltroptn.gif)
3. Select the items you want to show on the Filter submenu of the field in Page Report Studio, and then select **OK**.
4. The properties value will be generated, equal to sum of values of those selected items. The items and corresponding values when checked are as follows:

   Remove Filter: 1  
    Top N: 2  
    Bottom N: 4  
    More: 8  
    Default: 16
5. After saving the page report and publishing it to Server, you will see the effect.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) In the Filter Options dialog box, Designer enables the other four options only when you clear the Default checkbox. If you select Default, they are disabled, but their values still affect the Filter Options property value. If you select Default (Filter Options >= 16), which items are available on the Filter submenu in Page Report Studio is determined by settings in the Page Report Studio profile on Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).

## Record Location

This property is to specify the calculation point for the properties of the object that are controlled by formulas. Here is an example:

A report specifies to display the label "Continued on Next Topic" on every page that has another following it. If this label is inserted in the page header/page footer, then every page including the last page will contain the text. There is a way to use formulas that can resolve the problem.

1. Create three formulas as follows:

   **Continue1**:  
   `global boolean j=true;  
   j=false;`

   **Continue2**:  
   `pagenumber;  
   j=true;`

   **Continue3:**  
   `pagenumber;  
   return j;`
2. Insert Continue1 into the report header, Continue2 into the report footer. To track the calculation, you can insert Continue3 into the page footer.
3. Insert a label with the text "Continued on Next Topic" in the page header, and use Continue3 to control its Invisible property.
4. Set the property Record Location of the label to be Page Footer, so that Continue3 returns value which is calculated in the page footer instead of in the page header.

   PageNumber is included in the formula to force it to execute as a page level formula in the order the formula is encountered rather than at the end of a group or report. For more information, see [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100521-KPI-Chart-Paper-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100561-Line-Properties)
