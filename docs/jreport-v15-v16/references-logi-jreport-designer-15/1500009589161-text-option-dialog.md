---
title: "Text Option Dialog"
id: 1500009589161
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589161-Text-Option-Dialog
updated_at: 2021-07-24T05:54:45Z
---

# Text Option Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589141-Tabular-Wizard-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567782-Time-Zone-and-Locale-Options-Dialog)

# Text Option Dialog

The Text Option dialog appears when you set the Default Format for Viewing Report property of a report tab or a web report to Text and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell in the Report Inspector. It helps you to specify the parameters for running a report in Text format. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893846039/txtoptn.gif)

The following are details about options in the dialog:

**Delimited Format**

Specifies whether to use the delimited format for the Text result.

* **Format**  
   Specifies the delimiter to separate fields.
  + **CSV Format**  
     Fields in the Text result will be separated by a comma.
  + **Tab Delimited**  
     Fields in the Text result will be separated by a tab.
  + **Custom Defined**   
     Fields in the Text result will be separated by a user defined delimiter. You can type your own delimiter in the Delimiter box (note that the delimiter should be only one character).
* **Use Quote mark**  
   Specifies whether the fields in the Text result will be marked with quotation marks.
* **Repeat Last Column Value If Null**  
   If checked, when a cell in the Text result has no value, value of the previous cell in the same column will be used.

**User Defined Density**

Specifies whether to use user defined density for the Text result.

* **Horizontal Density**  
   Specifies the value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns.
* **Vertical Density**  
   Specifies the value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns.

**Notes:**

* When using user defined densities, if the densities are not set appropriately, the fields in the report may overlap each other, so you are not recommended to use this way.
* When setting the value of Horizontal/Vertical Density, you need to pay attention to the following:
  + The value of Horizontal/Vertical Density must be greater than the character's width/height of the smallest field in the report (smallest field is the field with the smallest font size), otherwise, the value you set will not be applied.
  + If the value of Vertical Density is greater than 0 and the value of Horizontal Density is less than 0, the value that you specify for the Vertical Density will be applied and the value of Horizontal Density will be specified by Logi JReport.
  + If the value of Vertical Density is less than 0 and the value of Horizontal Density is greater than 0, the value that you specify for the Horizontal Density will be applied and the value of Vertical Density will be specified by Logi JReport.
  + If the values of Vertical Density and Horizontal Density are both greater than 0 and the value of Horizontal Density is less than 11, the specified value of the two densities will be applied. Otherwise, they will be specified by Logi JReport.
  + If the values of Vertical Density and Horizontal Density are both less than 1, these densities will be specified by Logi JReport.

**Compress**

Specifies whether to generate the Text result in a compressed size, that is to say, there will be no clearance between the columns.

**Header and Footer**

If checked, the Text result will contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer and Group Header/Footer. Otherwise, the Text result will only contain data in Detail panel.

**Windows End-of-line (CR-LF)**

Specifies to use Windows end-of-line characters to indicate the start of a new line. If checked, two characters <cr> and <lf> will be used at the end of the line.

**Unix End-of-line (LF)**

Specifies to use Unix End-of-line characters to indicate the start of a new line. If checked, only the Unix End-of-line character <lf> will be used.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the Text result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589141-Tabular-Wizard-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567782-Time-Zone-and-Locale-Options-Dialog)
