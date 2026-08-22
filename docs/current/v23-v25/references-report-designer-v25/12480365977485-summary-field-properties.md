---
title: "Summary Field Properties"
id: 12480365977485
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480365977485-Summary-Field-Properties
updated_at: 2026-02-25T23:51:12Z
source_host: docs-report.zendesk.com
---
# 
Summary Field Properties

This topic describes the properties of a Summary Field object that you can use in query-based page reports only.

| Property Name | Description |
| --- | --- |
| General |  |
| Aggregate Function | Shows the function of the summary. Read only. |
| Field Type | Shows what kind of field it is. Read only. |
| Group By | Shows the group-by field of the object. When this property value is null, the object is grouped based on the whole dataset. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Summary Name | Shows the name of the summary. Read only. |
| Summary On | Shows the name of the field on which to perform the summary function. Read only. |
| Geometry (not available when the summary field is in a heat map) |  |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color |  |
| Background | Specifies the background color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB or RGBA value (for example, 0x00ff11 or 0xff00ff11) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS |  |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| ID | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type W in the value cell.Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the page report tab and there are styles in the style group that are applicable to the object. Data type: String |
| Excel |  |
| Column Index | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| Row Index | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| Padding (not available when the summary field is in a heat map) |  |
| Bottom Padding | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border (not available when the summary field is in a heat map) |  |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to add a drop shadow effect to the border. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Pattern |  |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list. none Select if you do not want to apply a pattern to the object. 50% Select to fill the object using 50%-transparency of the specified pattern color. horizontal Select to fill the object with horizontal lines using the specified pattern color. vertical Select to fill the object with vertical lines using the specified pattern color. grid Select to fill the object with grids using the specified pattern color. diagonal Select to fill the object with diagonal lines using the specified pattern color. Data type: String |
| Text Format |  |
| Auto Fit | Specifies whether to automatically adjust the width and height of the object according to its content. Data type: Boolean Designer does not provide this property when the summary field is in a heat map. |
| Auto Scale in Number | Designer displays this property when the object is Number data type. You can use it to specify whether to automatically scale values of the object that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. The option "auto" means that the property setting follows that of the object's parent data component. Data type: Boolean |
| Bold | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Convert HTML Tag | Specifies whether to parse the HTML tag elements that are included in the text of the object as the web browser translates them into HTML in the report. Data type: Boolean This property has higher priority than the Ignore HTML Tag property. This property does not work when you view or export the report in the Page Report Result or Logi Report Result format. When the object is not in a table cell, this property takes effect only when you set its Position property to "absolute". |
| Font Face | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Specifies the format in which you want to display values of the object in the report. Choose an option from the drop-down list or type the format by yourself. Data type: String If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. If the object is Number data type and you set its Auto Scale in Number property to "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the Auto Scale in Number property (for example, the values display in percentage), Designer ignores the Auto Scale in Number property. |
| Format Locale | Specifies the locale for displaying and formatting values of the object when its data type is locale sensitive, such as the date and time formats, and number and currency formats. Default is the locale of your JVM or the language of the NLS report. Choose an option from the drop-down list if you want to change the locale. Data type: String When you use a formula or edit an expression to control the locale, the return value should be the two-letter language and country codes as defined by ISO-639 and ISO-3166 in the format language_country, for example, de_DE. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Ignore HTML Tag | Specifies whether to ignore the HTML tag elements that are included in the text of the object at runtime and in HTML output, so they display exactly as what they are. When you set this property to "false", Report Engine transfers the HTML tag elements to the web browser and they are translated into HTML by the web browser.Data type: Boolean |
| Italic | Specifies whether to italicize the text in the object. Data type: Boolean |
| Maximum Width | Specifies the maximum width of the text you want to display in the object. Type a numeric value to change the width. This property often works together with the Auto Fit property. When you set Auto Fit of the object to "true" and the value of Maximum Width is not equal to 0, the text extends in the object until the width is this value. Data type: Float |
| Reduce Width When Auto Fit | Specifies whether to reduce the width of the object according to its content when you specify to automatically adjust its width (set the object's Auto Fit property to "true") and the actual width of the content is smaller than that of the object. Data type: Boolean This property takes effect when you set the object's Position property to "absolute"; but, it does not work if you set the Word Wrap property of the object to "true". Designer does not provide this property when the object is in a heat map. |
| Strikethrough | Specifies whether to draw a line through the text in the object. Data type: Boolean |
| Underline | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text according to the width of the object. Data type: Boolean |
| Others |  |
| Cache Value | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
| Column Name | Designer enables this property when you have cleared "Forbid changing column" in the Panel category of the Options dialog box. You can use it to specify another field to substitute the current one. Choose the field from the drop-down list. Data type: String |
| Data Mapping File | Specifies the data mapping file (without the locale part) you want to apply to the object for NLS use. For example, if the data mapping file is Product_de_DE.properties, type Product in the value cell.Data type: String |
| Detail Report | Specifies the detail report that you want to link the object to. Select the ellipsis in the value cell to set the detail report. See Linking to a Detail Report. Data type: String |
| Detail Target Frame | Designer displays this property when the object is in the group header/footer panel of a banded object, and enables it after you set Go to Detail of the object to "true". You can use it to specify the target window or frame to display the detail information. Choose an option from the drop-down list.  Select to load the detail information according to the Pop Up New Window for Links property in the Page Report Studio Profile dialog box on Server. New Window Select to load the detail information into a new window. The window is not named. Whole Window Select to load the detail information into the full browser window. Same Frame Select to load the detail information into the same frame as the object. Parent Frame Select to load the detail information into the parent frame of the frame in which the object is. Other Frame Select to load the detail information into some other specified frame. Type the name of the frame you have defined in the value cell. If the frame name does not exist, Server loads the detail information into a new window. Data type: String |
| Display Null | Specifies the string you want to display when the field value is null. Data type: String |
| Enable Hyperlink in Excel | Specifies whether to enable the link that you have added on the object in the Excel output. Data type: Boolean |
| Enable Hyperlink in HTML | Specifies whether to enable the link that you have added on the object in the HTML output. Data type: Boolean |
| Enable Hyperlink in PDF | Specifies whether to enable the link that you have added on the object in the PDF output. Data type: Boolean |
| Export to CSV | Specifies whether to include the object in the CSV output. Data type: Boolean When you set this property to "true", if the summary field displays as a barcode or text field, Report Engine only includes the string value in the output; if it displays as a checkbox, radio button, or button, only the text. |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean When you set this property to "true", if the summary field displays as a text field, Report Engine only includes the string value in the output. |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean When you set this property to "true", if the summary field displays as a text field, Report Engine only includes the string value in the output. |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean When you set this property to "true", if the summary field displays as a text field, Report Engine only includes the string value in the output. |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean When you set this property to "true", if the summary field displays as a text field, Report Engine only includes the string value in the output; if it displays as a radio button or button, only the text. |
| Export to Text | Specifies whether to include the object in the Text output. Data type: Boolean When you set this property to "true", if the summary field displays as a barcode or text field, Report Engine only includes the string value in the output; if it displays as a checkbox, radio button, or button, only the text. |
| Export to XML | Specifies whether to include the object in the XML output. Data type: Boolean When you set this property to "true", if the summary field displays as a barcode or text field, Report Engine only includes the string value in the output; if it displays as a checkbox, radio button, or button, only the text. |
| Filter Options | Specifies the filter commands that you want to display on the object's shortcut menu in Page Report Studio. Select the ellipsis in the value cell to set the options. Data type: Integer |
| Go to Detail | Designer displays this property when the object is in the group header/footer panel of a banded object. You can use it to specify whether to show the detail information about the group when users select the object in Page Report Studio. See Obtaining the Group Details in a Banded Object. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Link | Specifies the target that you want to link the object to, which can be another report, a website, an email address, or a Blob data type field. Select the ellipsis in the value cell to set the link target. See Adding Links in Reports. Data type: String |
| Logic Column | Designer displays this property when the object is in a table. You can use it to specify whether to show the object in the next visible table cell in the same row when the column that holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. When you set this property for several objects in the same row to "next visible column", and the columns holding these objects are all hidden, only the object in the rightmost column shows in the next visible cell. |
| Position | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration Designer does not provide this property when the summary field is in a heat map. |
| Record Location | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list. default Select to calculate values of the properties in the default location where the object is placed. page header Select to calculate values of the properties in the banded page header panel. page footer Select to calculate values of the properties in the banded page footer panel. See Example 2: Showing a Label on Every Page Except the Last. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Suppress When Null | Specifies whether to suppress the field in the report when its value is null. Data type: Boolean |
| Transfer Style | Specifies whether to apply the style group of the primary report to the linked report, when the object is linked to another report. Data type: Boolean |
| Value Delimiter | Specifies the separator for DBArray data. By default, Designer displays the elements in a horizontal line and separates them by a space. Type the delimiter in the value cell. Data type: String |
| PDF |  |
| Annotation Background | Specifies the background color of the annotation. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Annotation Font Face | Specifies the font face of the annotation text. Choose an option from the drop-down list. Data type: Enumeration |
| Annotation Font Size | Specifies the font size of the annotation text. Type an integer value to change the size. Data type: Integer |
| Annotation Foreground | Specifies the foreground color of the annotation. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Annotation Height | Specifies the height of the annotation. Designer truncates the content that is beyond the defined annotation size. Type a numeric value to change the height. Data type: Float |
| Annotation Relative X | Specifies the horizontal coordinate of the annotation icon relative to the top right corner of the object from which the attachment is linked. Type a numeric value to change the coordinate. Data type: Float |
| Annotation Relative Y | Specifies the vertical coordinate of the annotation icon relative to the top right corner of the object from which the attachment is linked. Type a numeric value to change the coordinate. Data type: Float |
| Annotation Text | Specifies the annotation text you want to display for the attachment when you select the annotation type as Text.Data type: String |
| Annotation Text Strikethrough | Specifies whether to draw a line through the annotation text.Data type: Boolean |
| Annotation Text Underline | Specifies whether to add a horizontal line under the annotation text.Data type: Boolean |
| Annotation Tooltip | Specifies the tool tip of the annotation icon. Type a string to display as the annotation tip.Data type: String |
| Annotation Type | Specifies how you want to display the annotation for the attachment. Choose an option from the drop-down list. invisible Select to not display annotation for the attachment. Built-in Icon Select to display the annotation using the icon specified by the Predefined Annotation Icon property. Customized Icon Select to display the annotation using the icon specified by the Customized Annotation Icon property. Text Select to display the annotation in the text specified by the Annotation Text property. Data type: Enumeration |
| Annotation Width | Specifies the width of the annotation. Designer truncates the content that is beyond the defined annotation size. Type a numeric value to change the width. Data type: Float |
| Customized Annotation Icon | Specifies the annotation icon you want to display for the attachment when you select the annotation type as Customized Icon. The value of this property can be a valid physical path or URL. When you use a formula of Blob or Clob type to control the property, Designer embeds the byte stream into the PDF document as an icon.Data type: String |
| Ignore When No Attachment | Specifies whether to ignore the PDF attachment of the object when it cannot be found. When this property is "false" and Designer cannot load the file during exporting the report to a PDF/A compliant document, the export process will fail. Data type: Boolean |
| PDF Attachment | Specifies the file you want to add as attachment of the object in the PDF/A compliant output of the report. Select the ellipsis in the value cell to choose the file using the Select PDF Attachment dialog box. Data type: String |
| PDF Attachment Name | Specifies the name of the PDF attachment you add to the object. Data type: String |
| Predefined Annotation Icon | Specifies the annotation icon you want to display for the attachment when you select the annotation type as Built-in Icon. For compatibility with PDF/A-3, Designer embeds the predefined icons into the PDF document. Choose an option from the drop-down list.Data type: Enumeration |
| TOC (not available when the summary field is in a heat map) |  |
| Anchor Display Value | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Accessibility |  |
| Artifact | Specifies whether to add an artifact tag when exporting to PDF. Data type:Boolean. |
| External AccessKey | This property is mapped to the HTML attribute accesskey, as specified by w3.org.Data type: String |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External Dir | This property is mapped to the HTML attribute dir, as specified by w3.org.Data type: String |
| External ID | This property is mapped to the HTML attribute id, as specified by w3.org. Data type: String |
| External Style | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| External TabIndex | This property is mapped to the HTML attribute tabindex, as specified by w3.org.Data type: Integer |
| External Title | This property is mapped to the HTML attribute title, as specified by w3.org.Data type: String |
| HrefLang | This property is mapped to the HTML attribute hreflang, as specified by w3.org. You can use it to specify the base language of the resource designated by a link on the object, such as the target you define via the Link property. Data type: String |
| Language | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |
| LongDesc | This property is mapped to the HTML attribute longdesc, as specified by w3.org.Data type: String |
| Tag Name | Specifies the header tag name of the object for labeling its heading order in the accessible PDF output. Choose an option from the drop-down list.When setting this property, you should nest the headers properly based on the following rules so that Adobe can accept the heading tag sequence. H1 should always be the first heading tag. The descending sequence of the headers should follow the downward order of the objects in the Report Inspector. The descending sequence of the headers should proceed in strict numerical order and should not skip an intervening heading level. H1 H2 H3 is permissible, while H1 H3 is not. Data type: Enumeration |
