---
title: "Export to Text Dialog"
id: 1500009608182
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608182-Export-to-Text-Dialog
updated_at: 2021-07-24T16:04:40Z
---

# Export to Text Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631141-Export-to-RTF-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608202-Export-to-XML-Dialog)

# Export to Text Dialog

The Export to Text dialog helps you to [export a report to a Text file](https://devnet.logianalytics.com/hc/en-us/articles/1500009611082-Exporting-to-Text). It appears when you select File > Export > To Text.

![Export to Text dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911669271/expt2txt.gif)

The following are details about options in the dialog:

**Export to**

Specifies the file name and destination directory where you want to store the exported Text file.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export to the Text file. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the specified report tab one step down.

**Delimited Format**

Specifies whether to use the delimited format to export the report result.

* **Format**  
   Specifies the delimiter to separate fields.
  + **CSV Format**   
     Fields in the exported Text file will be separated by a comma.
  + **Tab Delimited**  
     Fields in the exported Text file will be separated by a tab.
  + **Custom Delimited**  
     Fields in the exported Text file will be separated by a user defined delimiter. You can type your own delimiter in the Delimiter box (note that the delimiter should be only one character).
* **Use Quote mark**  
   Specifies whether the fields in the exported CSV Text will be marked with quotation marks.
* **Repeat Last Column Value If Null**  
   If the option is selected, when a cell in the exported CSV Text has no value, value of the previous cell in the same column will be used.

**User Defined Density**

Specifies whether to use user defined density to export the report result.

* **Horizontal Density**  
   Specifies the value for each unit of the horizontal density between columns.
* **Vertical Density**  
   Specifies the value for each unit of the vertical density between columns.

**Compress**

Specifies whether to generate the report result to Text format in a compressed size.

**Header and Footer**

If the option is selected, the exported file will contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer and Group Header/Footer. Otherwise, the exported file will only contain data in Detail panel.

**Windows End-of-line (CR-LF)**

Specifies whether to use CR-LF in Windows convention as the end-of-line character.

**Unix End-of-line (LF)**

Specifies whether to use LF in Unix convention as the end-of-line character.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported Text file.

**OK**

Applies all changes and exits the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631141-Export-to-RTF-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608202-Export-to-XML-Dialog)
