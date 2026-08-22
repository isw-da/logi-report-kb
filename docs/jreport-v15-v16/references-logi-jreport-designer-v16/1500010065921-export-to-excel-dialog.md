---
title: "Export to Excel Dialog"
id: 1500010065921
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065921-Export-to-Excel-Dialog
updated_at: 2021-07-24T10:38:54Z
---

# Export to Excel Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065861-Excel-Option-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030742-Export-to-Fax-Dialog)

# Export to Excel Dialog

The Export to Excel dialog helps you to [export a report to Microsoft Excel format](https://devnet.logianalytics.com/hc/en-us/articles/1500010033082-Exporting-to-Excel). It appears when you select File > Export > To Excel.

![Export to Excel dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909148823/expt2excl.gif)

The following are details about options in the dialog:

**Directory**

Specifies the destination directory where the exported Excel file will be placed.

**File Name**

Specifies the name of the exported Excel file. If you do not type the name, Logi JReport will use the report name as the Excel file name by default.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export to the Excel file. The selected report tabs will be exported into multiple sheets of the Excel file in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified report tab one step down.

**Excel Version**

Specifies the Excel version to be used.

* **Excel 97-2003 Workbook (\*.xls)**  
   Exports the file as .xls format.
* **Excel Workbook (\*.xlsx)**  
   Exports the file as .xlsx format.

**Format**

Specifies the format of the exported Excel file.

* **Auto Format**  
   If checked, it is up to Logi JReport to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Column Format will be used; otherwise it is Report Format. This option is selected by default.
* **Report Format**  
   If checked, Logi JReport will attempt to make the formatting of the report in Excel match the format as designed in the template. Usually this format is recommended if you just want to view the report in Excel.
* **Column Format**  
   If checked, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property value for the report in the Report Inspector to decide the calculation method used for all components' row/column values in the report when exporting.
* **Data Format**  
   If checked, only the report data will be exported without format. Available only for Excel 97-2003 Workbook (\*.xls).

**More/Less Options**

Select to show/hide the additional settings for exporting the report to Excel. When Data Format is selected, only Word Wrap and Run Linked Report are available here.

* **Include Shapes in Export**  
   Specifies whether to include the drawing objects in the exported Excel file, such as line, oval, and box.
* **Print Page Header**  
   Specifies the page header text for the printed file.
* **Print Page Footer**  
   Specifies the page footer text for the printed file.
* **Word Wrap**  
   Specifies the word wrap setting.
  + **All Keep Existing**  
     Keeps all settings of each component's Word Wrap property as specified in the report.
  + **All Disabled**  
     Disables the Word Wrap property for all components.
  + **All Enabled**  
     Enables the Word Wrap property for all components.
* **Print Gridlines**  
   Specifies whether to include gridlines when printing the exported Excel file.
* **Run Linked Report**  
   If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported Excel file.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030722-Enter-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030742-Export-to-Fax-Dialog)
