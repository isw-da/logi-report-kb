---
title: "Export to Text Dialog Box"
id: 1500010096741
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096741-Export-to-Text-Dialog-Box
updated_at: 2021-07-23T19:15:23Z
---

# Export to Text Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059022-Export-to-RTF-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096761-Export-to-XML-Dialog-Box)

# Export to Text Dialog Box

You can use the Export to Text dialog box to [export a report to a Text file](https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text). This topic describes the options in the dialog box.

Designer displays the Export to Text dialog box when you select File > Export > To Text.

![Export to Text dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848472855/expt2txt.gif)

You see the following options in the dialog box:

**Export to**

Specify the file name and destination directory where to save the Text file. Select the Browse button to specify the file name and directory.

**Select Report Tabs**

Designer displays the option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. If the report has only one report tab, Designer selects the report tab by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified report tab higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified report tab lower in the list.

**Delimited Format**

Select to use the delimited format to export the report result.

* **Format**  
   Select the delimiter to separate fields.
  + **CSV Format**  
    Select to separate fields in the Text output by a comma.
  + **Tab Delimited**  
    Select to separate fields in the Text output by a tab.
  + **Custom Delimited**  
    Select to separate fields in the Text output by a user-defined delimiter. Type your own delimiter in the Delimiter box (the delimiter should be only one character).
* **Use Quote mark**  
  Select to mark the fields in the CSV Text output with quotation marks.
* **Repeat Last Column Value If Null**  
  Select to apply the value of the previous cell in the same column when a cell in the CSV Text output has no value.

**User Defined Density**

Select to use user-defined density to export the report result.

* **Horizontal Density**  
  Specify the value for each unit of the horizontal density between columns.
* **Vertical Density**  
  Specify the value for each unit of the vertical density between columns.

**Compress**

Select to generate the report result to Text in a compressed size.

**Header and Footer**

Select to include all headers and footers in the report, including report header/footer, page header/footer, and group header/footer in the Text output; otherwise, the Text output contains only data in the detail panel.

**Windows End-of-line (CR-LF)**

Select to use "CR-LF" in Windows convention as the end-of-line character.

**Unix End-of-line (LF)**

Select to use "LF" in Unix convention as the end-of-line character.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports)

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059022-Export-to-RTF-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096761-Export-to-XML-Dialog-Box)
