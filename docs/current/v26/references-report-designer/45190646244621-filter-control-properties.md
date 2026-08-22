---
title: "Filter Control Properties"
id: 45190646244621
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190646244621-Filter-Control-Properties
updated_at: 2026-04-30T15:10:07Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Filter Control Properties

This topic describes the properties of a Filter Control object.

Designer provides some properties only when you use the object in certain report types. The properties of the object also vary for different filter control types (Text List, Drop-down List, Single Value Slider, and Range Slider). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Control Type | Page Report, Web Report, Library Component | Shows the type of the filter control. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Slider |  |  |
| Font Face | Slider in Library Component | Specifies the font face of the tick mark label text on the slider. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Slider in Library Component | Specifies the font size of the tick mark label text on the slider. Type an integer value to change the size. Data type: Integer |
| Format | Slider in Library Component | Specifies the format in which you want to display values of the object in reports. Choose an option from the drop-down list or type the format by yourself. Data type: String If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. |
| Number Slider Unit Increment | Slider in Library Component | Specifies the increment between two pixels on the slider. Data type: Float |
| Geometry |  |  |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color |  |  |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Selection | Slider in Library Component | Specifies the color for the selected part on the slider bar. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String This property takes effect only when the type of the filter control is Range Slider. |
| Slider Bar | Slider in Library Component | Specifies the color of the slider bar. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String This property takes effect only when the type of the filter control is Range Slider. |
| CSS |  |  |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type W in the value cell.Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the report tab or web report, and there are styles in the style group that are applicable to the object. Data type: String |
| Others |  |  |
| Current Selects | Page Report, Web Report | Specifies the current select values for the filter control. Read only. Select the “…“ button to display the Enter Values dialog box, and maintain the current select values in the box. Data type: String |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Item Bottom Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Item Top Padding | Page Report, Web Report, Library Component | Specifies the space between the text and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Overflow | Text List in Web Report | This property is mapped to the overflow CSS property, as specified by w3.org. Report's default behavior is doing nothing for the overflow content. You can select how you want the web browser to handle overflow in the text list.Data type: Enumeration |
| Position | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Excel |  |  |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab or web report's Columned property to "true" and the object's Position property is not "static". |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab or web report's Columned property to "true" and the object's Position property is not "static". |
| Border |  |  |
| Border Color | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Text List and Drop-down List in Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Title |  |  |
| Background | Text List in Page Report, Web Report, and Library Component | Specifies the background color of the title. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Bold | Text List in Page Report, Web Report, and Library Component | Specifies whether to apply bold formatting to the title. Data type: Boolean |
| Font Face | Text List in Page Report, Web Report, and Library Component | Specifies the font face of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Text List in Page Report, Web Report, and Library Component | Specifies the font size of the title. Type an integer value to change the size. Data type: Integer |
| Foreground | Text List in Page Report, Web Report, and Library Component | Specifies the foreground color of the title. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Horizontal Alignment | Text List in Page Report, Web Report, and Library Component | Specifies the horizontal justification of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Text List in Page Report, Web Report, and Library Component | Specifies whether to italicize the title. Data type: Boolean |
| Map Name | Text List in Page Report, Web Report, and Library Component | Specifies whether to display the name of the DBField that you add to the filter control as its title. If you add more than one DBField to the filter control, Designer applies the name of the first displayed field you select in the field list as the title. Data type: Boolean |
| Show Title | Text List in Page Report, Web Report, and Library Component | Specifies whether to show the title of the filter control. It is meaningful to set all the other title properties when this property is "true". Data type: Boolean |
| Text | Text List in Page Report, Web Report, and Library Component | Designer enables this property when you set Map Name to "false". You can use it to specify the text you want to display as the title. Type a string to change the text. Data type: String When you add only one DBField to the text list filter control and insert the On-screen Filter special field in a data container that uses the same data resource as the DBField, Report also applies the text in the filter expression of the special field at runtime. |
| Title Height | Text List in Page Report, Web Report, and Library Component | Specifies the height of the title, to ensure larger font sizes display without being cut off. Type a numeric value to change the height. Data type: Float |
| Underline | Text List in Page Report, Web Report, and Library Component | Specifies whether to add a horizontal line under the title. Data type: Boolean |
| Title Border |  |  |
| Border Color | Text List in Page Report and Web Report | Specifies the color for the border of the title. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Text List in Page Report and Web Report | Specifies the width for the border of the title. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Text List in Page Report and Web Report | Specifies the line style for the bottom border of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Text List in Page Report and Web Report | Specifies the line style for the left border of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Text List in Page Report and Web Report | Specifies the line style for the right border of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Text List in Page Report and Web Report | Specifies the line style for the top border of the title. Choose an option from the drop-down list. Data type: Enumeration |
| Body |  |  |
| Background | Text List in Page Report and Web Report | Specifies the background color for the body of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Body Border |  |  |
| Border Color | Text List in Page Report and Web Report | Specifies the color for the border of the object's body. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Text List in Page Report and Web Report | Specifies the width for the border of the object's body. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Text List in Page Report and Web Report | Specifies the line style for the bottom border of the object's body. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Text List in Page Report and Web Report | Specifies the line style for the left border of the object's body. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Text List in Page Report and Web Report | Specifies the line style for the right border of the object's body. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Text List in Page Report and Web Report | Specifies the line style for the top border of the object's body. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format |  |  |
| Auto Scale in Number | Text List in Page Report, Web Report, and Library Component | Designer displays this property when the fields bound with the object are Number data type. You can use it to specify whether to automatically scale the Number values that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. The option "auto" means that the property setting follows that of the object's parent data component. Data type: Boolean |
| Bold | Text List in Page Report, Web Report, and Library Component | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Font Face | Text List in Page Report, Web Report, and Library Component | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Text List in Page Report, Web Report, and Library Component | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Text List in Page Report, Web Report, and Library Component | Specifies the format in which you want to display values of the object in the report. Choose an option from the drop-down list or type the format by yourself. Data type: String If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. If the object is Number data type and you set its Auto Scale in Number property to "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the Auto Scale in Number property (for example, the values display in percentage), Designer ignores the Auto Scale in Number property. |
| Italic | Text List in Page Report, Web Report, and Library Component | Specifies whether to italicize the text in the object. Data type: Boolean |
| Underline | Text List in Page Report, Web Report, and Library Component | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Padding |  |  |
| Bottom Padding | Page Report, Web Report | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border Radius |  |  |
| Bottom Left Radius | Page Report, Web Report | Specifies the radius for the bottom left joint of the borders. Type a numeric value to change the radius. Data type: Float |
| Bottom Right Radius | Page Report, Web Report | Specifies the radius for the bottom right joint of the borders. Type a numeric value to change the radius. Data type: Float |
| Top Left Radius | Page Report, Web Report | Specifies the radius for the top left joint of the borders. Type a numeric value to change the radius. Data type: Float |
| Top Right Radius | Page Report, Web Report | Specifies the radius for the top right joint of the borders. Type a numeric value to change the radius. Data type: Float |
| Accessibility |  |  |
| Artifact | Page Report, Web Report, Library Component | Specifies whether to add an artifact tag when exporting to PDF. Data type:Boolean. |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute id, as specified by w3.org. Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| External Title | Query Page Report | This property is mapped to the HTML attribute title, as specified by w3.org.Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |
