---
title: "Round Box Shape Properties"
id: 45190682661645
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190682661645-Round-Box-Shape-Properties
updated_at: 2026-04-30T15:15:51Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Round Box Shape Properties

This topic describes the properties of a Round Box Shape object that you can use in page reports only.

| Property Name | Description |
| --- | --- |
| General (available when the object is in a query-based page report) |  |
| Class Type | Shows the class type of the object. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Geometry |  |
| Bottom Attach Pos X | Specifies the horizontal coordinate for the bottom right point of the focus box in the involved banded panel. Data type: Float |
| Bottom Attach Pos Y | Specifies the vertical coordinate for the bottom right point of the focus box in the involved banded panel. Data type: Float |
| Top Attach Pos X | Specifies the horizontal coordinate for the top left point of the focus box in the involved banded panel. Data type: Float |
| Top Attach Pos Y | Specifies the vertical coordinate for the top left point of the focus box in the involved banded panel. Data type: Float |
| Color |  |
| Background | Specifies the background color of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS |  |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the page report tab and there are styles in the style group that are applicable to the object. Data type: String |
| Others |  |
| Export to Excel | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to RTF | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Record Location | Specifies the calculation point for the properties of the object that are controlled by formulas. Choose an option from the drop-down list. default Select to calculate values of the properties in the default location where the object is placed. page header Select to calculate values of the properties in the banded page header panel. page footer Select to calculate values of the properties in the banded page footer panel. See Example 2: Showing a Label on Every Page Except the Last. Data type: Enumeration |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Excel |  |
| Bottom Attach Column | Specifies the X coordinate for the lower right corner of the object in the Excel output, measured in cells. Data type: Float This property takes effect when you set the page report tab's Columned property to "true". |
| Bottom Attach Row | Specifies the Y coordinate for the lower right corner of the object in the Excel output, measured in cells. Data type: Float This property takes effect when you set the page report tab's Columned property to "true". |
| Top Attach Column | Specifies the X coordinate for the upper left corner of the object in the Excel output, measured in cells. Data type: Float This property takes effect when you set the page report tab's Columned property to "true". |
| Top Attach Row | Specifies the Y coordinate of the upper left corner of the object in the Excel output, measured in cells. Data type: Float This property takes effect when you set the page report tab's Columned property to "true". |
| Round Box Property |  |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Style | Specifies the line style for the border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Corner Factor | Specifies the relative radius for the corners of the round box. Data type: Float |
| Accessibility(available when the object is in a query-based page report) |  |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External ID | This property is mapped to the HTML attribute id, as specified by w3.org. Data type: String |
| External Style | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| External Title | This property is mapped to the HTML attribute style, as specified by w3.org. Data type: String |
| Language | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |
