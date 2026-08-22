---
title: "Parameter Control Properties"
id: 45190715300877
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190715300877-Parameter-Control-Properties
updated_at: 2026-04-30T15:10:05Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Parameter Control Properties

This topic describes the properties of a Parameter Control object.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry |  |  |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color |  |  |
| Background | Page Report, Web Report, Library Component | Specifies the background color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Page Report, Web Report, Library Component | Specifies the foreground color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS |  |  |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type W in the value cell.Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the report tab or web report, and there are styles in the style group that are applicable to the object. Data type: String |
| Excel |  |  |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab or web report's Columned property to "true" and the object's Position property is not "static". |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab or web report's Columned property to "true" and the object's Position property is not "static". |
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
| Border |  |  |
| Border Color | Query Page Report, Web Report, Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Query Page Report, Web Report, Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Query Page Report, Web Report, Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Query Page Report, Web Report, Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Query Page Report, Web Report, Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Shadow | Query Page Report, Web Report, Library Component | Specifies whether to add a drop shadow effect to the border. Data type: Boolean |
| Shadow Color | Query Page Report, Web Report, Library Component | Specifies the color of the border shadow. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Query Page Report, Web Report, Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Pattern |  |  |
| Pattern Color | Page Report, Web Report, Library Component | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Page Report, Web Report, Library Component | Specifies the style of the pattern. Choose an option from the drop-down list. none Select if you do not want to apply a pattern to the object. 50% Select to fill the object using 50%-transparency of the specified pattern color. horizontal Select to fill the object with horizontal lines using the specified pattern color. vertical Select to fill the object with vertical lines using the specified pattern color. grid Select to fill the object with grids using the specified pattern color. diagonal Select to fill the object with diagonal lines using the specified pattern color. Data type: String |
| Text Format |  |  |
| Auto Scale in Number | Page Report, Web Report, Library Component | Designer displays this property when the parameter in the parameter control is Number data type. You can use it to specify whether to automatically scale the Number values that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. The option "auto" means that the property setting follows that of the object's parent data component. Data type: Boolean |
| Bold | Page Report, Web Report, Library Component | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Convert HTML Tag | Query Page Report | Specifies whether to parse the HTML tag elements that are included in the text of the object as the web browser translates them into HTML in the report. Data type: Boolean This property takes effect when you set the object's Position property to "absolute". This property does not work when you view or export the report in the Page Report Result or Report Result format. |
| Font Face | Page Report, Web Report, Library Component | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Page Report, Web Report, Library Component | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Page Report, Web Report, Library Component | Specifies the format in which you want to display values of the object in the report. Choose an option from the drop-down list or type the format by yourself. Data type: String If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. If the object is Number data type and you set its Auto Scale in Number property to "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the Auto Scale in Number property (for example, the values display in percentage), Designer ignores the Auto Scale in Number property. |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Page Report, Web Report, Library Component | Specifies whether to italicize the text in the object. Data type: Boolean |
| Underline | Page Report, Web Report, Library Component | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Others |  |  |
| Export as Text | Page Report, Web Report, Library Component | Specifies whether to export the parameter control as text. When this property is "true", depending on properties of the parameter in the parameter control, Report Engine exports it as follows: The selected values or text of the parameter are exported as text while the button for specifying the parameter value is not exported. When the parameter in the parameter control is Boolean data type, it displays as a checkbox in the parameter control, then when the checkbox is selected, it is exported as and if cleared, as . When this property is "false", Report Engine exports the parameter control as an image. Data Type: Boolean |
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
| Parameter | Page Report, Web Report, Library Component | Specifies the value of the parameter. Data type: String |
| Position | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Accessibility |  |  |
| Artifact | Page Report, Web Report, Library Component | Specifies whether to add an artifact tag when exporting to PDF. Data type:Boolean. |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| External Title | Query Page Report | This property is mapped to the HTML attribute title, as specified by w3.org.Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |
| Tag Name | Page Report, Web Report, Library Component | Specifies the header tag name of the object for labeling its heading order in the accessible PDF output. Choose an option from the drop-down list.When setting this property, you should nest the headers properly based on the following rules so that Adobe can accept the heading tag sequence. H1 should always be the first heading tag. The descending sequence of the headers should follow the downward order of the objects in the Report Inspector. The descending sequence of the headers should proceed in strict numerical order and should not skip an intervening heading level. H1 H2 H3 is permissible, while H1 H3 is not. Data type: Enumeration |
