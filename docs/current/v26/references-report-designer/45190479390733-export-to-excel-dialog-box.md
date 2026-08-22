---
title: "Export to Excel Dialog Box"
id: 45190479390733
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190479390733-Export-to-Excel-Dialog-Box
updated_at: 2026-04-30T15:13:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Export to Excel Dialog Box

You can use the Export to Excel dialog box to export a report to Excel. This topic describes the options in the dialog box.
    

Designer displays the Export to Excel dialog box when you navigate to File > Export > To Excel.

Designer displays these options:

Directory

Specify the destination directory where you want to save the Excel file.

File Name

Specify the name of the Excel file.

Browse

Select to specify the directory and file name of the Excel file with File Explorer.

Use Custom File Extension

Select to use the extension you want for the Excel file. By default, Designer uses .xls or .xlsx. Select this option and type your file name with any extension, or no extension.

Select Report Tabs

Designer displays this option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs into multiple sheets of the Excel file in the list order.
  If the report has only one report tab, Designer selects the report tab by default.

Move Up button

Select to move the specified report tab higher in the list.

Move Down button

Select to move the specified report tab lower in the list.

Excel Version

Select the Excel version to use: Excel 97-2003 Workbook (*.xls) or Excel Workbook (*.xlsx).

Format

Select the format of the Excel output.

- 
Auto Format
If you select this option, it is up to Designer to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Designer applies Column Format; otherwise, it is Report Format.

- 
Report Format
If you select this option, Designer attempts to make the formatting of the report in Excel match that in the report template. Usually, you should use this format if you just want to view the report in Excel.

- 
Column Format
If you select this option, you can set the Columned property of the report in the Report Inspector to decide the calculation method for all objects' row/column values in the Excel output.

- 
Data Format
Designer displays this option for the Excel version of Excel 97-2003 Workbook (*.xls) only. Select it when you only want the report data without any formatting in the Excel output. 

More Options/Less Options

Select to show or hide the additional settings for exporting the report to Excel. When you select Data Format, Designer only enables Word Wrap and Run Linked Report here.

- 
Include Shapes in Export
Select  to include the drawing objects in the Excel output, such as Line, Oval, and Box.

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
Select how you want to apply the Word Wrap property in the Excel output.

- 
All Keep Existing
Select to keep all settings of each object's Word Wrap property as what you have specified in the report.

- 
All Disabled
Select to disable the Word Wrap property for all objects, meaning, Designer applies "false" to the Word Wrap property of all objects.

- 
All Enabled
Select to enable the Word Wrap property for all objects, meaning, Designer applies "true" to the Word Wrap property of all objects.

- 
Print Gridlines
Select  to include the gridlines when printing the Excel output.

- 
Retain Formatted Values
If you select this option, when you select the cell of a value that applies format you specify in Designer in the Excel output, its corresponding value in the Excel formula bar also displays in the customized format.

- 
Generate Excel Formula
Select to generate Excel formula for the summary fields in table/banded object in the Excel output when the fields the summaries  calculate are also detail fields in the table/banded object.

- 
Run Linked Report
Select to generate the reports that you link with the report (not including the detail reports) in the Excel output.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
