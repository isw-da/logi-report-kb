---
title: "Excel Option Dialog"
id: 1500009608082
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608082-Excel-Option-Dialog
updated_at: 2021-07-24T16:04:43Z
---

# Excel Option Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608062-Enter-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631081-Export-to-Excel-Dialog)

# Excel Option Dialog

The Excel Option dialog helps you to specify the options for running a report in Excel format. It appears when you set the Default Format for Viewing Report property of a report tab or a web report to Excel and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the value cell in the Report Inspector.

![Excel Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904342935/exceloptn.gif)

The following are details about options in the dialog:

**Excel Version**

Specifies the Excel version to be used.

* **Excel 97-2003 Workbook (\*.xls)**  
   Exports the file as .xls format.
* **Excel Workbook (\*.xlsx)**  
   Exports the file as .xlsx format.

**Format**

Specifies the format of the Excel result.

* **Auto Format**  
   If the option is selected, it is up to Logi Report to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Column Format will be used; otherwise it is Report Format. This option is selected by default.
* **Report Format**  
   If the option is selected, Logi Report will attempt to make the formatting of the report in Excel match the format as designed in the template. Usually this format is recommended if you just want to view the report in Excel.
* **Column Format**  
   If the option is selected, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property value for the report in the Report Inspector to decide the calculation method used for all components' row/column values in the Excel result.
* **Data Format**  
   If the option is selected, only the report data will be displayed without format in the Excel result. Available only for the Excel version of Excel 97-2003 Workbook (\*.xls).

**More/Less Options**

Select to show/hide the additional settings for running the report to Excel. When Data Format is selected, only Word Wrap and Run Linked Report are available here.

* **Include Shapes in Export**  
   Specifies whether to include the drawing objects in the Excel result, such as line, oval, and box.
* **Print Page Header**  
   Specifies the page header text for the printed file.
* **Print Page Footer**  
   Specifies the page footer text for the printed file.
* **Word Wrap**  
   Specifies the word-wrap settings.
  + **All Keep Existing**  
     Keeps all settings of each component's Word Wrap property as specified in the report.
  + **All Disabled**  
     Disables the Word Wrap property for all components. That is, the Word Wrap property is made false for all components.
  + **All Enabled**  
     Enables the Word Wrap property for all components. That is, the Word Wrap property will be made true for all components.
* **Print Gridlines**  
   Specifies whether to include gridlines when printing the Excel result.
* **Run Linked Report**  
   If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the Excel result. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608062-Enter-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631081-Export-to-Excel-Dialog)
