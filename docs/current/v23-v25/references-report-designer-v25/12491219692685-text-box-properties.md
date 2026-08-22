---
title: "Text Box Properties"
id: 12491219692685
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491219692685-Text-Box-Properties
updated_at: 2026-02-25T23:47:45Z
source_host: docs-report.zendesk.com
---
# 
Text Box Properties

This topic describes the properties of a Text Box object that you can use in page reports and web reports.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Text Format |  |  |
| Default Font Face | Page Report, Web Report | Specifies the default font face in the object, which Designer applies each time when you clear content in the object and type new text. Choose an option from the drop-down list. Data type: Enumeration |
| Default Font Size | Page Report, Web Report | Specifies the default font size in the object, which Designer applies each time when you clear content in the object and type new text. Type an integer value to change the size. Data type: Integer |
| Color |  |  |
| Background | Page Report, Web Report | Specifies the background color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Default Foreground | Page Report, Web Report | Specifies the default font color in the object, which Designer applies each time when you clear content in the object and type new text. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Geometry |  |  |
| Height | Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static position in the container. Type a numeric value to change the coordinate. Data type: Float |
| CSS |  |  |
| Class | Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| Style | Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the page report tab and there are styles in the style group that are applicable to the object. Data type: String |
| Others |  |  |
| Auto Scale in Number | Page Report, Web Report | Specifies whether to automatically scale the Number values in the object that fall into the two ranges: When 1000 = 10^15, Designer uses scientific notation to scale the values. Data type: Boolean |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Overflow | Web Report | This property is mapped to the overflow CSS property, as specified by w3.org. Report's default behavior is doing nothing for the overflow content. You can select how you want the web browser to handle overflow in the text box.Data type: Enumeration |
| Position | Page Report, Web Report | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Record Location | Page Report, Web Report | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list. default Select to calculate values of the properties in the default location where the object is placed. page header Select to calculate values of the properties in the banded page header panel. page footer Select to calculate values of the properties in the banded page footer panel. See Example 2: Showing a Label on Every Page Except the Last. Data type: Enumeration |
| Suppress | Page Report, Web Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report | Specifies the vertical justification of the content in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Vertical Auto Size | Page Report, Web Report | Specifies whether to automatically expand the height of the object according to the size of its content. Data type: Boolean |
| Excel |  |  |
| Column Index | Query Page Report | Specifies the X coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| Row Index | Query Page Report | Specifies the Y coordinate of the object relative to its parent container in the Excel and CSV outputs, measured in cells. Data type: Integer This property takes effect when you set the page report tab's Columned property to "true" and the object's Position property is not "static". |
| Border |  |  |
| Border Color | Page Report, Web Report | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Page Report, Web Report | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Page Report, Web Report | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Padding |  |  |
| Bottom Padding | Page Report, Web Report | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Page Report, Web Report | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Page Report, Web Report | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Page Report, Web Report | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Border Radius |  |  |
| Bottom Left Radius | Page Report, Web Report | Specifies the radius for the bottom left joint of the borders. Type a numeric value to change the radius. Data type: Float |
| Bottom Right Radius | Page Report, Web Report | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Left Radius | Page Report, Web Report | Specifies the radius for the top left joint of the borders. Type a numeric value to change the radius. Data type: Float |
| Top Right Radius | Page Report, Web Report | Specifies the radius for the top right joint of the borders. Type a numeric value to change the radius. Data type: Float |
| TOC |  |  |
| Anchor Display Value | Page Report, Web Report | Specifies the text you want to display as the object's TOC entry label, when you set the object's TOC Anchor property to "true". Data type: String |
| TOC Anchor | Page Report, Web Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| Accessibility |  |  |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
