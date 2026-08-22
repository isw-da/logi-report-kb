---
title: "User-Defined Object (UDO) Properties"
id: 1500010062522
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062522-User-Defined-Object-UDO-Properties
updated_at: 2021-07-23T19:16:44Z
---

# User-Defined Object (UDO) Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100961-TOC-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100981-Web-Report-Properties)

# User-Defined Object (UDO) Properties

This topic lists the properties of a User-Defined Object (UDO).

A UDO is an object defined by users, which is supported only in page reports created using query resources. It has special properties defined by users. The properties listed in the Report Inspector correspond with the ones defined in your UDO programs. See the default properties below:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | |
| Export to CSV | Specifies whether to include the object in the CSV output of the report. If it is set to true, only the text value will be included. Data type: Boolean |
| Export to Excel | Specifies whether to include the object in the Excel output of the report. If it is set to true, only the text value will be included. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output of the report. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output of the report. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output of the report. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output of the report. Data type: Boolean |
| Export to Text | Specifies whether to include the object in the Text output of the report. If it is set to true, only the text value will be included. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML output of the report. If it is set to true, only the text value will be included. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports#Position) | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010100541-Label-Properties#RecordLocation) | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  Note icon When you set both the Invisible and Suppress properties of an object to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report result when no record is returned to its parent data container. Data type: Boolean |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Column Number | Specifies the number of columns which will be the object's width in the Excel output. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Row Number | Specifies the number of rows which will be the object's height in the Excel output. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Font | |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Logi Report UDO does not support RTF and PDF outputs. That is, when exporting to RTF and PDF, a report with a UDO may not be rendered correctly. However, there is no such problem for HTML and PostScript.

## Properties of the Built-in UDOs

Logi Report provides you with two built-in UDOs: [JHyperLink](#JHyperLink) and [JRotator](#JRotator), the properties of which are as follows

### JHyperLink

It operates in a similar way to the hyperlink in an HTML file (only for Windows NT). See its special properties below:

| Property Name | Description |
| --- | --- |
| Others | |
| Auto Fit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
| Display Value | Specifies the displayed text of the hyperlink. This property has lower priority than [Display Image](#DisplayImage). Data type: String |
| Enable Hyperlink in Excel | Specifies whether to enable the link defined on the object in the Excel output of the report. Data type: Boolean |
| Enable Hyperlink in HTML | Specifies whether to enable the link defined on the object in the HTML output of the report. Data type: Boolean |
| Enable Hyperlink in PDF | Specifies whether to enable the link defined on the object in the PDF output of the report. Data type: Boolean |
| Executer Class Name | If the specified URL is linked to a .rst file - the result file for the Logi Report Result export format, you should select jet.udos.RPTExecuter. For other links, use jet.udos.IEExecuter. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the content in the JHyperLink container. Choose an option from the drop-down list. Data type: Enumeration |
| HTML Style | Specifies the CSS style of the JHyperLink in HTML output and in Page Report Studio. The value is a String value containing only the body part of a CSS style definition. Make sure that you provide the right CSS style string. For Example, if a full style definition is:  `style="text-decoration:underline;color:#ffc800;font:italic small-caps bold 12pt serif;"`  you need only type the content in the quotation marks as the HTML Style value:  `text-decoration:underline;color:#ffc800;font:italic small-caps bold 12pt serif;`  Data type: String |
| Target | Specifies the window or frame at which to target contents. Choose an option from the drop-down list.  * **blank** - Loads the linked document into a new blank window. This window is not named. * **self** - Loads the linked document into the window in which the link is selected (the active window). * **parent** - Loads the linked document into the immediate parent window of the active window. If there is no parent window, the active window is used. * **top** - Loads the linked document into the topmost window.   Data type: Enumeration |
| Tooltips Text | Specifies the text that will be shown when you hover the mouse pointer over the JHyperLink in Designer view mode, in HTML output, or in Page Report Studio. Data type: String |
| URL | Specifies the URL for accessing the linked file or website page. Data type: String |
| Vertical Alignment | Specifies the vertical justification of the content in the JHyperLink container. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to enable the word wrap function of JHyperLink in the exported files. Data type: Boolean |
| Image | |
| Alternate Text | Specifies the text that will be displayed instead if the image cannot be displayed. Data type: String |
| Display Image | Specifies the local path of the image displayed for the hyperlink (like a hotspot in HTML). This property has higher priority than Display Value. Data type: String |
| Original | Specifies from where the image is fetched when viewing or running the report on Server. The property has following two options:   * **true** - If selected, the image will not be delivered when publishing the report to Server. Server will find the image from the local directory specified by the property Display Image when you view the report. * **false** - If selected, the image will be delivered when publishing the report to Server. Server will obtain the image from the Server side when you view or run the report.   Data type: Boolean |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |

**Example:**

Insert two JHyperLink UDOs, and specify the following:

* URL: `http://www.jinfonet.com`  
  Display Value: go here.
* URL: `C:\docword.txt`  
  Display Value: abc  
  Display Image: `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Demo\SampleReports\Coffee.jpg`

When you point your mouse at either UDO, a hand will show you that it is a hyperlink. By selecting it, you will be taken to the destination. The application launched to open it (the linked file) is from your Windows NT system. If Display Value and Display Image both have been specified, the image has the higher priority to be displayed.

### JRotator

It is a built-in UDO that can be rotated. Text and images can be held in JRotator. See its special properties below:

| Property Name | Description |
| --- | --- |
| Others | |
| Display Image | Specifies the local path of the image displayed in the JRotator. This property has higher priority than Display Value. Data type: String |
| Display Value | Specifies the text displayed in the JRotator. This property has lower priority than Display Image. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the text in the JRotator container. Choose an option from the drop-down list. Data type: Enumeration |
| Rotate | Specifies the angle at which to rotate the JRotator, in degrees.  * 0 - No rotation. * positive value - Rotates the JRotator clockwise. * negative value - Rotates the JRotator anticlockwise.   Data type: Integer |
| Vertical Alignment | Specifies the vertical justification of the text in the JRotator container. Choose an option from the drop-down list. Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010100961-TOC-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010100981-Web-Report-Properties)
