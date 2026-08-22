---
title: "Export to Excel Dialog Box"
id: 4405661541655
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661541655-Export-to-Excel-Dialog-Box
updated_at: 2022-01-27T20:38:12Z
---

# Export to Excel Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661538839-Excel-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661542679-Export-to-Fax-Dialog-Box)

# Export to Excel Dialog Box

You can use the Export to Excel dialog box to [export a report to Excel](https://devnet.logianalytics.com/hc/en-us/articles/4405661753751-Exporting-to-Excel). This topic describes the options in the dialog box.

Designer displays the Export to Excel dialog box when you navigate to File > Export > To Excel.

![Export to Excel dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420394711959/expt2excl.gif)

You see the following options in the dialog box:

**Directory**

Specify the destination directory where to place the Excel file. Select **Browse** to locate the directory.

**File Name**

Specify the name of the Excel file.

**Select Report Tabs**

Designer displays this option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs into multiple sheets of the Excel file in the list order.
If the report has only one report tab, Designer selects the report tab by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified report tab higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified report tab lower in the list.

**Excel Version**

Select the Excel version to use: Excel 97-2003 Workbook (\*.xls) or Excel Workbook (\*.xlsx).

**Format**

Select the format of the Excel output.

* **Auto Format**  
  If you select this option, it is up to Designer to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Designer applies Column Format; otherwise, it is Report Format.
* **Report Format**  
  If you select this option, Designer attempts to make the formatting of the report in Excel match the format as designed in the template. Usually, you should use this format if you just want to view the report in Excel.
* **Column Format**  
  If you select this option, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) property of the report in the Report Inspector to decide the calculation method for all components' row/column values in the Excel output.
* **Data Format**  
  Designer displays this option for the Excel version of Excel 97-2003 Workbook (\*.xls) only. Select it when you only want the report data without any formatting in the Excel output.

**More Options**/**Less Options**

Select to show or hide the additional settings for exporting the report to Excel. When you select Data Format, Designer only enables Word Wrap and Run Linked Report here.

* **Include Shapes in Export**  
  Select to include the drawing objects in the Excel output, such as Line, Oval, and Box.
* **Print Page Header**  
  Specify the page header text for the printed file.
* **Print Page Footer**  
  Specify the page footer text for the printed file.
* **Word Wrap**
  + **All Keep Existing**  
    Select to keep all settings of each component's Word Wrap property as what you have specified in the report.
  + **All Disabled**  
    Select to disable the Word Wrap property for all components, meaning, Designer applies "false" to the Word Wrap property of all components.
  + **All Enabled**  
    Select to enable the Word Wrap property for all components, meaning, Designer applies "true" to the Word Wrap property of all components.
* **Print Gridlines**  
  Select to include the gridlines when printing the Excel output.
* **Run Linked Report**  
  Select to generate the reports that you link with the report (not including the detail reports) in the Excel output.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661537687-Enter-Values-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661542679-Export-to-Fax-Dialog-Box)
