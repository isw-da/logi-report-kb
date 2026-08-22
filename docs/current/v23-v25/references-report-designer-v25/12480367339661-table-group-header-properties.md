---
title: "Table Group Header Properties"
id: 12480367339661
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480367339661-Table-Group-Header-Properties
updated_at: 2026-02-25T23:47:47Z
source_host: docs-report.zendesk.com
---
# 
Table Group Header Properties

This topic describes the properties of a Table Group Header object.

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry |  |  |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Shows the width of the object. Read only. |
| Color |  |  |
| Background | Page Report, Web Report, Library Component | Specifies the background color or fill effect of the object. Choose a color from the drop-down list, or select Custom to customize a color in the color palette. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.Data type: String |
| CSS |  |  |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the report tab or web report, and there are styles in the style group that are applicable to the object. Data type: String |
| Others |  |  |
| Export to CSV | Page Report, Web Report, Library Component | Specifies whether to include the object in the CSV output. Data type: Boolean |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Export to Text | Page Report, Web Report, Library Component | Specifies whether to include the object in the Text output. Data type: Boolean |
| Export to XML | Page Report, Web Report, Library Component | Specifies whether to include the object in the XML output. Data type: Boolean |
| Fill Whole Page | Page Report, Web Report, Library Component | Specifies whether to extend the row to the page bottom in the report, so that the next row starts on a new page. Data type: Boolean |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Label | Page Report | Specifies the tool tip you want to display for the row when you point to the left edge of the row in the design area. Type a string to change the label. Data type: String |
| On New Page | Page Report, Web Report, Library Component | Specifies whether to start the row on a new page in the report. Default (the property being "false") is starting the row on a new page only when the previous page is filled. This property cannot take effect if you disable Page Layout for the report, meaning, the report is in continuous page mode. Data type: Boolean If you specify to start the group header row on a new page, each group displays from a new page. However, this also means you get no detail records on the first page because the detail row starts from the second page. If you want to start each group on a new page and at the same time display the detail records on the first page, you can use the Fill Whole Page property of the group footer row. |
| Record Location | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list. default Select to calculate values of the properties in the default location where the object is placed. page header Select to calculate values of the properties in the banded page header panel. page footer Select to calculate values of the properties in the banded page footer panel. See Example 2: Showing a Label on Every Page Except the Last. Data type: Enumeration |
| Repeat | Page Report, Web Report, Library Component | Specifies whether to display the group header on every page in the report. If the details of a group span a large space vertically to show on several pages, you can set this property to "true" to display the group header information on each page. Data type: Boolean If you set Repeat to "true" for both the outer and inner group headers, Report Engine treats the two group headers as a completely repeated object; in this case, when the page can only hold the group headers or has no enough space for the group headers, it does not duplicate either of the group headers. |
| Suppress | Page Report, Web Report, Library Component | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report, Library Component | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Border |  |  |
| Border Color | Page Report, Web Report, Library Component | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report, Library Component | Specifies the joint style for the border of the object. Choose an option from the drop-down list. miter Select to join path segments by extending their outside edges until they meet. round Select to join path segments by rounding off the corner at the specified radius. Data type: Enumeration |
| Border Thickness | Page Report, Web Report, Library Component | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report, Library Component | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report, Library Component | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report, Library Component | Specifies the radius of the joint, when you set Border Joint of the object to "round". Type a numeric value to change the radius.Data type: Integer |
| Right Line | Page Report, Web Report, Library Component | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report, Library Component | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Accessibility |  |  |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |
