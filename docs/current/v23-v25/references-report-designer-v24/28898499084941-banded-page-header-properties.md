---
title: "Banded Page Header Properties"
id: 28898499084941
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898499084941-Banded-Page-Header-Properties
updated_at: 2024-09-30T09:10:57Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Banded Page Header Properties

This topic describes the properties of a Banded Page Header object. 

Designer provides some properties only when you use the object in certain report types. You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General |  |  |
| Class Type | Query Page Report | Shows the class type of the object. Read only. |
| Data Inherit | Query Page Report | Shows whether the object inherits dataset from another object. Read only. |
| Dataset | Query Page Report | Shows the dataset the object applies. Read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. Read only. |
| Geometry |  |  |
| Height | Page Report, Web Report | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| Color |  |  |
| Background | Page Report, Web Report | Specifies the background color or fill effect of the object. Choose a color from the drop-down list, or select Custom to customize a color in the color palette. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color.Data type: String |
| CSS |  |  |
| Class | Page Report, Web Report | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, if you define the CSS file as follows: @charset "GBK"; TextField {Background: #ff0000} /*Style=LabelX*/ TextField[Style="LabelX"]{Background: #0000FF} /*ID=W*/ TextField#W{Background: #FFFF00} /*class=C*/ TextField.C{Background: #00FFFF} To apply the Class Selector in the file to the object, type C in the value cell. Data type: String |
| Style | Page Report, Web Report | Specifies the style you want to apply to the object. You can specify the style in two ways: Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies. For example, to apply the style in the preceding sample CSS file to the object, type LabelX in the value cell. Choose a style from the drop-down list when you have specified the Style Group property for the report tab or web report, and there are styles in the style group that are applicable to the object. Data type: String |
| Others |  |  |
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
| Label | Page Report, Web Report | Specifies the tool tip you want to display for the panel when you point to the left edge of the panel in the design area. Type a string to change the label. Data type: String |
| Merge to Next Panel | Page Report, Web Report | Specifies whether to merge the panel into the next panel in the Excel output. Data type: Boolean |
| Record Location | Page Report, Web Report | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list. default Select to calculate values of the properties in the default location where the object is placed. page header Select to calculate values of the properties in the banded page header panel. page footer Select to calculate values of the properties in the banded page footer panel. See Example 2: Showing a Label on Every Page Except the Last. Data type: Enumeration |
| Remove Blank Row | Page Report, Web Report | Specifies whether to remove the blank rows in the panel in the Excel output. Data type: Boolean |
| Repeat in Detail Panel | Page Report, Web Report | Specifies whether to duplicate the objects the panel contains in the detail panel in the Excel output. Data type: Boolean |
| Show Bottom Line | Query Page Report | Specifies whether to add a horizontal line at the bottom of the panel in the report. Data type: Boolean |
| Suppress | Page Report, Web Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress Blank Panel | Page Report, Web Report | Specifies whether to suppress the panel in the report when it contains no data. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Page Report, Web Report | Specifies whether to layer the panel beneath the next panel in the banded object. This property is read only for the banded page header panel, meaning, the panel cannot be underlaid. Data type: Boolean |
| Border |  |  |
| Border Color | Page Report, Web Report | Specifies the color for the border of the object. Choose a color from the drop-down list, or select Custom to customize a color in the Pick a Color dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border of the object. Choose an option from the drop-down list. miter Select to join path segments by extending their outside edges until they meet. round Select to join path segments by rounding off the corner at the specified radius. Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius of the joint, when you set Border Joint of the object to "round". Type a numeric value to change the radius.Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Accessibility |  |  |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output.Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute id, as specified by w3.org. Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute lang, as specified by w3.org. Data type: String |

## 
Merge to Next Panel, Remove Blank Row, Repeat in Detail Panel 

You can control panels of a banded object in the Excel output by settings the three properties:

- Merge to Next Panel controls whether to merge the current panel into the next panel. It applies to the banded header, banded page header, group header, and group footer panels.

- Remove Blank Row controls whether to remove the blank rows in the panel. It applies to the banded page header, group header, and detail panels.

- Repeat in Detail Panel controls whether to duplicate the objects in certain panel in the detail panel as well. It applies to the  banded page header and group header panels.

The three properties take effect when you set the Columned property of the page report tab or the web report containing the banded object to "true", and there is an operation order when those three properties work together: Merge to Next Panel > Repeat in Detail Panel > Remove Blank Row.

Suppose you have a banded object as follows:

Then you set the Columned property of the page report tab to "true" and Merge to Next Panel of the first group header panel to "true", and export the report to Excel using Column Format. In the Excel output, you can see that Report Engine merges the two group panels into one and places the fields in the two panel in one cell.

In order to improve the layout of the Excel output, you can specify the Column Index and Row Index properties of the objects as follows:

| Object | Column Index | Row Index |
| --- | --- | --- |
| A | 3 | 1 |
| B | 4 | 1 |
| C | 1 | 1 |
| D | 2 | 1 |
| E | 3 | 1 |
| F | 4 | 1 |

Then, fields in the Excel output can display more clearly.

- Do not set Merge to Next Panel to "true" for the last group footer panel, because this can make the Excel output incorrect.

- Do not set Merge to Next Panel to "true" for the panel that contains a crosstab or subreport.

- If a banded object contains more than one groups, meaning, it has several group header panels, when you specify to repeat the first group header panel in the detail panel, Report Engine also repeats it  in the second group header panel in the Excel output.

- When two or more objects in the to-be-merged panels have the same Column Index and Row Index property values, after Report Engine merges the panels, in the Excel output, it merges the objects  into one cell and places them  in the cell based on this rule: the object whose X/Y property value is smaller than others is put to front, and Y has higher priority than X.

- When the objects in the group header/banded page header panel have the same Row Index and Column Index property values with those in the detail panel, and you specify to repeat the group header/banded page header panel in the detail panel, in the Excel output, Report Engine places the repeated objects  in the same cells with the ones in the detail panel based on this rule: the object whose X/Y property value is smaller than others is put to front, and Y has higher priority than X.

Previous Topic  Next Topic
