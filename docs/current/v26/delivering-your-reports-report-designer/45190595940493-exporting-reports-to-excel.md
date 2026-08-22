---
title: "Exporting Reports to Excel"
id: 45190595940493
section: "Delivering Your Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190595940493-Exporting-Reports-to-Excel
updated_at: 2026-07-30T22:55:24Z
source_host: logi-report-v26.insightsoftware.com
---
# 
 Exporting Reports to Excel

This topic describes how you can export a page or web report to an Excel file.

- Open the report that you want to export.

- Navigate to File > Export > To Excel. Designer displays the Export to Excel dialog box.
    

- By default, Designer saves the Excel file in the same folder and same name as the report file. You can type the destination directory and file name for the output in the Directory and File Name text boxes, or select Browse to specify the location and file name with File Explorer of your operating system. When the file name you specify does not contain the .xls or .xlsx extension, Designer automatically adds the extension to the output file. If you want to use your preferred extension (or to have no extension) for the file name of the output, select Use Custom File Extension, then you can type your file name with any extension or no extension.

- When you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. Designer exports the selected report tabs into multiple sheets of the Excel file in the list order. You can select a report tab and select Move Up or Move Down to change the order of the report tabs. 

- From the Excel Version drop-down list, select the version for the Excel file.

- 
Select the format of the Excel file from the Format drop-down list.
    
- To have Designer choose which format is the most appropriate, select Auto Format (the default behavior), then Designer determines whether to use Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Designer uses Column Format; otherwise, it uses Report Format. If you do not know which format is better,  select this option.

- To make the formatting of the Excel output match that in the report template, select Report Format, and then specify the available settings according to your requirements. Usually, you should use this format if you just want to view the report in Excel.

- To export the report to a general Excel file, select Column Format. Using this format, you can set the Columned property for the report tab or web report in the Report Inspector to specify the calculation method for the coordinates of the report objects in the Excel output (due to the particularity of mailing label report, do not set the Columned property to "true" if you want to export it to this format).

- To export only the report data without format, select Data Format. This option is only available for Excel 97-2003 Workbook (*.xls). When you select Data Format, Designer cannot support formulas, barcodes, images, hyperlink property, charts, and all drawing objects such as lines, ovals, and boxes in the report.

- Select More Options to customize other settings for the Excel file.

- If you have selected the format other than Data Format, select Include Shapes in Export to include the drawing objects in the Excel output, and specify the page header and footer text to display and whether to include gridlines when printing the exported Excel file.

- Clear Overflow to Next Cell if you do not want to overflow the content of a cell to the next cell in the Excel output. By default, Designer overflows the content of a cell to the next cell when		corresponding fields of both cells are Text format, text in the cell is not wrapped, text length in the next cell is 0, and none of the two cells is merged with other cells.

- From the Word Wrap drop-down list, specify how you want to apply the Word Wrap property of the report objects in the Excel output.
    
- 
All Keep Existing
Select  to  keep all settings of each object's Word Wrap property as what you have specified in the report.

- 
All Disabled
Select  to disable the Word Wrap property for all objects, meaning, Designer applies  "false" to the Word Wrap property of all objects.

- 
All Enabled
Select to enable the Word Wrap property for all objects, meaning, Designer applies "true" to the Word Wrap property of all objects.

- Select Print Gridlines to include gridlines  in the Excel output.

- Select Retain Formatted Values so when you select the cell of a value that applies format you specify in Designer in the Excel output, its corresponding value in the Excel formula bar also displays in the customized format.

- Clear Generate Excel Formula if you do not want to generate Excel formula for summary fields in the output.
By default, Designer generates Excel formula for the summary fields in table/banded object in the Excel output when the fields the summaries  calculate are also detail fields in the table/banded object.

- Select Run Linked Report if you want to generate the reports that you link with the report (not including the detail reports) in the Excel output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

- If you want to encrypt the Excel file to prevent users from opening and modifying it without authorization, select Encrypt, then in the Excel Encrypt dialog box:

If you want the exported Excel file to be read-only, select the Read-only checkbox.

In the Password to open text box, specify a password that users must enter to open the Excel file. Confirm the password in the Confirm Password to open text box. If a password to open is set, users who do not know the password will not be able to open the file at all.

If you want to use a separate password to restrict users from modifying the Excel file, specify the password in the Password to modify text box and confirm it in the Confirm Password to modify text box. The modify password should be different from the one used for opening the Excel file. Users who open the file without the modify password can still view the content in read-only mode if the Read-only option is also selected.

Select OK to finish configuring the encryption settings for the Excel file, or select Cancel to discard the changes.

 

- Select OK to start exporting.

 Designer also provides several properties that you can use to customize the Excel output of a report. You can specify them appropriately to make the Excel output best serve your requirements.
 These properties include:

- Column Width List, Full Fill and Border, No Page Break, Rows per Sheet, and Sheet Name on reports

- Column Index, Row Index, Column Number,  and Row Number that are available on several objects

- Bottom Attach Column, Bottom Attach Row, Top Attach Column, and Top Attach Row on drawing objects

- Merge to Next Panel, Repeat in Detail Panel, and Remove Blank Row on banded panels

- Merged Cell on tables

- On New Sheet, Sheet Name, Sheet Name Postfix, Customize Subreport Index Format, and the index format properties on subreports

The following are some tips for you when exporting a report to Excel:

- Designer can export multiple colors and languages in a report to an Excel file, but cannot export multiple pie charts and the Arc drawing object. For example, Excel only supports 56 kinds of colors; therefore, if there are more than 56 kinds of colors in a report, some colors are merged in the Excel output. 

- Designer exports paragraphs and texts in a report as objects.

- If the report contains the Drop-down List object, Designer only exports the value selected in the list.

- If you set an object's Export to Excel property to "false", Designer does not export the object and other objects contained in it.

- Designer exports gauge and surface charts in a report as bar chart, and stock chart  as image.

- Designer does not export the minor tick marks on a chart.

- If the data type of the field on the category axis of a chart is Date, Time, or DateTime whose format confirms to the Date format of Excel, Designer exports the axis  as a date axis, vice versa.

- When the field on the category axis of a chart is  Number data type and you use a constant interval to customize the tick marks on the axis, the settings cannot take effect.
