---
title: "Export to Text Dialog"
id: 1500009565602
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565602-Export-to-Text-Dialog
updated_at: 2021-07-24T05:55:19Z
---

# Export to Text Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565582-Export-to-RTF-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565622-Export-to-XML-Dialog)

# Export to Text Dialog

The Export to Text dialog appears when you select File > Export > To Text. It helps you to [export a report to a Text file](https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text). [See the dialog](javascript:%20void(null)).

![Export to Text dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889309335/expt2txt.gif)

The following are details about options in the dialog:

**Export to**

Specifies the file name and destination directory where you want to store the exported Text file.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export to the Text file. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified report tab one step down.

**Delimited Format**

Specifies whether to use the delimited format to export the report result.

* **Format**  
   Specifies the delimiter to separate fields.
  + **CSV Delimited**  
     Fields in the exported Text file will be separated by a comma.
  + **Tab Delimited**  
     Fields in the exported Text file will be separated by a tab.
  + **Customize Delimited**  
     Fields in the exported Text file will be separated by a user defined delimiter. You can type your own delimiter in the Delimiter box (note that the delimiter should be only one character).
* **Use Quote mark**  
   Specifies whether the fields in the exported Text file will be marked with quotation marks.
* **Repeat Last Column Value If Null**  
   If checked, when a cell in the exported CSV Text has no value, value of the previous cell in the same column will be used.

**User Defined Density**

Specifies whether to use user defined density to export the report result.

* **Horizontal Density**  
   Specifies the value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns.
* **Vertical Density**  
   Specifies the value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns.

**Notes:**

* By exporting using user defined densities, if the densities are not set appropriately, the fields in the report may overlap each other, so you are not recommended to use this way to export the report result to Text.
* When setting the value of Horizontal/Vertical Density, you need to pay attention to the following:
  + The value of Horizontal/Vertical Density must be greater than the character's width/height of the smallest field in the report (smallest field is the field with the smallest font size), otherwise, the value you set will not be applied.
  + If the value of Vertical Density is greater than 0 and the value of Horizontal Density is less than 0, the value that you specify for the Vertical Density will be applied and the value of Horizontal Density will be specified by Logi JReport.
  + If the value of Vertical Density is less than 0 and the value of Horizontal Density is greater than 0, the value that you specify for the Horizontal Density will be applied and the value of Vertical Density will be specified by Logi JReport.
  + If the values of Vertical Density and Horizontal Density are both greater than 0 and the value of Horizontal Density is less than 11, the specified value of the two densities will be applied. Otherwise, they will be specified by Logi JReport.
  + If the values of Vertical Density and Horizontal Density are both less than 1, these densities will be specified by Logi JReport.

**Compress**

Specifies whether to generate the report result to Text format in a compressed size, that is to say, there will be no clearance between the columns.

**Header and Footer**

If checked, the exported file will contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer and Group Header/Footer. Otherwise, the exported file will only contain data in Detail panel.

**Windows End-of-line (CR-LF)**

Specifies whether to use the CR-LF in Windows convention as the end-of-line character.

**Unix End-of-line (LF)**

Specifies whether to use the LF in Unix convention as the end-of-line character.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported Text file.

**OK**

Applies all changes and exits the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565582-Export-to-RTF-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565622-Export-to-XML-Dialog)
