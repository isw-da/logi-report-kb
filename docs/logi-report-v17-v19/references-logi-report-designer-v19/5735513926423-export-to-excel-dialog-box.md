---
title: "Export to Excel Dialog Box"
id: 5735513926423
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735513926423-Export-to-Excel-Dialog-Box
updated_at: 2022-11-02T04:35:28Z
---

# Export to Excel Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529356567-Excel-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522811799-Export-to-Fax-Dialog-Box)

# Export to Excel Dialog Box

You can use the Export to Excel dialog box to [export a report to Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel). This topic describes the options in the dialog box.

Designer displays the Export to Excel dialog box when you navigate to File > Export > To Excel.

![Export to Excel dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477013911/expt2excl.gif)

Designer displays these options:

**Directory**

Specify the destination directory where you want to save the Excel file.

**File Name**

Specify the name of the Excel file.

**Browse**

Select to specify the directory and file name of the Excel file with File Explorer.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Use Custom File Extension**

Select to use the extension you want for the Excel file. By default, Designer uses .xls or .xlsx. Select this option and type your file name with any extension, or no extension.

**Select Report Tabs**

Designer displays this option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs into multiple sheets of the Excel file in the list order.
If the report has only one report tab, Designer selects the report tab by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified report tab higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified report tab lower in the list.

**Excel Version**

Select the Excel version to use: Excel 97-2003 Workbook (\*.xls) or Excel Workbook (\*.xlsx).

**Format**

Select the format of the Excel output.

* **Auto Format**  
  If you select this option, it is up to Designer to determine whether to apply Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Designer applies Column Format; otherwise, it is Report Format.
* **Report Format**  
  If you select this option, Designer attempts to make the formatting of the report in Excel match that in the report template. Usually, you should use this format if you just want to view the report in Excel.
* **Column Format**  
  If you select this option, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#Column) property of the report in the Report Inspector to decide the calculation method for all objects' row/column values in the Excel output.
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
  Select how you want to apply the Word Wrap property in the Excel output.
  + **All Keep Existing**  
    Select to keep all settings of each object's Word Wrap property as what you have specified in the report.
  + **All Disabled**  
    Select to disable the Word Wrap property for all objects, meaning, Designer applies "false" to the Word Wrap property of all objects.
  + **All Enabled**  
    Select to enable the Word Wrap property for all objects, meaning, Designer applies "true" to the Word Wrap property of all objects.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529347863-Enter-Values-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522811799-Export-to-Fax-Dialog-Box)
