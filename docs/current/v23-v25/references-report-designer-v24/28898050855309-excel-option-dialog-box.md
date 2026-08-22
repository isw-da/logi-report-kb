---
title: "Excel Option Dialog Box"
id: 28898050855309
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898050855309-Excel-Option-Dialog-Box
updated_at: 2024-09-30T09:09:23Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Excel Option Dialog Box

You can use the Excel Option dialog box to predefine the options for directly running a report in Excel on Server. This topic describes the options in the dialog box.
    

Designer displays the Excel Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "Excel" and then select the ellipsis  in the value cell in the Report Inspector.

Designer displays these options:

Excel Version

Select the Excel version to use: Excel 97-2003 Workbook (*.xls) or Excel Workbook (*.xlsx).

Format

Select the format of the Excel output.

- 
Auto Format
If you select this option, it is up to Server to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Server applies Column Format; otherwise, it is Report Format.

- 
Report Format
If you select this option, Server attempts to make the formatting of the report in Excel match that in the report template. Usually, you should use this format if you just want to view the report in Excel.

- 
Column Format
If you select this option, you can set the Columned property of the report in the Report Inspector to decide the calculation method for all component's row/column values in the Excel output.

- 
Data Format
Designer displays this option for the Excel version of Excel 97-2003 Workbook (*.xls) only. Select it when you only want the report data without any formatting in the Excel output. 

More Options/Less Options

Select to show or hide the additional settings for running the report to Excel. When you select Data Format, Designer only enables Word Wrap and Run Linked Report here.

- 
Include Shapes in Export
Select to include the drawing objects in the Excel output, such as Line, Oval, and Box.

- 
Overflow to Next Cell
Select to overflow the content of a cell to the next cell in the Excel output. The overflow occurs when all these prerequisites are met:				
- Corresponding fields of both cells are Text format.

- Text in the cell is not wrapped.

- Text length in the next cell is 0.

- None of the two cells is merged with other cells.

- 
Print Page Header
Specify the page header text for the printed file.

- 
Print Page Footer
Specify the page footer text for the printed file.

- 
Word Wrap
- 
All Keep Existing
Select to keep all settings of each component's Word Wrap property as specified in the report.

- 
All Disabled
Select to disable the Word Wrap property for all components, meaning, Designer applies "false" to the Word Wrap property of all components.

- 
All Enabled
Select to enable the Word Wrap property for all components, meaning, Designer applies "true" to the Word Wrap property of all components.

- 
Print Gridlines
Select to include the gridlines when printing the Excel output.

- 
Retain Formatted Values
If you select this option, when you select the cell of a value that applies format you specify in Designer in the Excel output, its corresponding value in the Excel formula bar also displays in the customized format.

- 
Generate Excel Formula
Select to generate Excel formula for the summary fields in table/banded object in the Excel output when the fields the summaries calculate are also detail fields in the table/banded object.

- 
Run Linked Report
Select to generate the reports that you link with the report (not including the detail reports) in the Excel output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
