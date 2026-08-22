---
title: "Excel Option Dialog Box"
id: 1500010096601
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096601-Excel-Option-Dialog-Box
updated_at: 2021-07-23T19:15:21Z
---

# Excel Option Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058922-Enter-Values-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058962-Export-to-Excel-Dialog-Box)

# Excel Option Dialog Box

You can use the Excel Option dialog box to predefine the options for directly running a report in Excel on Server. This topic describes the options in the dialog box.

Designer displays the Excel Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "Excel" and then select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the value cell in the Report Inspector.

![Excel Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856972567/exceloptn.gif)

You see the following options in the dialog box:

**Excel Version**

Select the Excel version to use.

* **Excel 97-2003 Workbook (\*.xls)**  
  Select to export the file as .xls format.
* **Excel Workbook (\*.xlsx)**  
  Select to export the file as .xlsx format.

**Format**

Select the format of the Excel output.

* **Auto Format**  
  If you select the option, it is up to Logi Report Engine to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Logi Report Engine applies Column Format; otherwise, it is Report Format. Designer selects this option by default.
* **Report Format**  
  If you select the option, Logi Report Engine attempts to make the formatting of the report in Excel match the format as designed in the template. Usually, this format is recommended if you just want to view the report in Excel.
* **Column Format**  
  If you select the option, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property value for the report in the Report Inspector to decide the calculation method used for all components' row/column values in the Excel output.
* **Data Format**  
  If you select the option, you get only the report data without format in the Excel output. Designer displays the option only for the Excel version of Excel 97-2003 Workbook (\*.xls).

**More Options**/**Less Options**

Select to show or hide the additional settings for running the report to Excel. When you select Data Format, Designer only enables Word Wrap and Run Linked Report here.

* **Include Shapes in Export**  
  Select to include the drawing objects in the Excel output, such as Line, Oval, and Box.
* **Print Page Header**  
  Specify the page header text for the printed file.
* **Print Page Footer**  
  Specify the page footer text for the printed file.
* **Word Wrap**
  + **All Keep Existing**  
    Select to keep all settings of each component's Word Wrap property as specified in the report.
  + **All Disabled**  
    Select to disable the Word Wrap property for all components, meaning, Designer takes the Word Wrap property for all components as false.
  + **All Enabled**  
    Select to enable the Word Wrap property for all components, meaning, Designer takes the Word Wrap property for all components as true.
* **Print Gridlines**  
  Select to include the gridlines when printing the Excel output.
* **Run Linked Report**  
  Select to generate the reports that you link with the report (not including the detail reports) in the Excel output.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058922-Enter-Values-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058962-Export-to-Excel-Dialog-Box)
