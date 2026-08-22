---
title: "Excel Option Dialog"
id: 1500009565462
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565462-Excel-Option-Dialog
updated_at: 2021-07-24T05:55:21Z
---

# Excel Option Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565522-Export-to-Excel-Dialog)

# Excel Option Dialog

The Excel Option dialog appears when you set the Default Format for Viewing Report property of a report tab or a web report to Excel and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell in the Report Inspector. It helps you to specify the parameters for running the report in Excel format. [See the dialog](javascript:%20void(null)).

![Excel Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889364503/exceloptn.gif)

The following are details about options in the dialog:

**Excel Version**

Specifies the Excel version to be used.

* **Excel 97-2003 Workbook (\*.xls)**  
   Exports the file as .xls format.
* **Excel Workbook (\*.xlsx)**  
   Exports the file as .xlsx format.

**Format**

Specifies the format of the Excel result.

* **Report Format**  
   If checked, Logi JReport will attempt to make the formatting of the report in Excel match the format as designed in the template. Usually this format is recommended if you just want to view the report in Excel.
* **Column Format**  
   If checked, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property value for the report in the Report Inspector to decide the calculation method used for all components' row/column values in the Excel result.
* **Data Format**  
   If checked, only the report data will be displayed without format in the Excel result. Available only for the Excel version of Excel 97-2003 Workbook (\*.xls).

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
   If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the Excel result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565522-Export-to-Excel-Dialog)
