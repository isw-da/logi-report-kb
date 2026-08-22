---
title: "Button Properties"
id: 1500009612502
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612502-Button-Properties
updated_at: 2021-07-24T16:03:33Z
---

# Button Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612462-Navigation-Control-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635521-OLE-Object-Multimedia-Object-Properties)

# Button Properties

This topic lists the properties of a Button object in a navigation control. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500009611922-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Text Format | | |
| Auto Fit | Page Report, Web Report, Library Component | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
| Bold | Page Report, Web Report, Library Component | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Page Report, Web Report, Library Component | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Page Report, Web Report, Library Component | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Page Report, Web Report, Library Component | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Text | Page Report, Web Report, Library Component | Specifies the text in the object. Type a string to display as the object text. Data type: String |
| Underline | Page Report, Web Report, Library Component | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Page Report, Web Report, Library Component | Specifies whether to wrap the text to the width. Data type: Boolean |
| Color | | |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. For page report, you can also use a formula or edit an expression that returns a color. Data type: String |
| Others | | |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Padding | | |
| Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border | | |
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
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties#PatternStyle) | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612462-Navigation-Control-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009635521-OLE-Object-Multimedia-Object-Properties)
