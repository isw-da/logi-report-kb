---
title: "Text Option Dialog Box"
id: 5735531704087
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531704087-Text-Option-Dialog-Box
updated_at: 2022-11-02T08:23:41Z
---

# Text Option Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735515884439-Tabular-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525134999-Time-Zone-and-Locale-Options-Dialog-Box)

# Text Option Dialog Box

You can use the Text Option dialog box to predefine the options for directly running a report in Text on Server. This topic describes the options in the dialog box.

Designer displays the Text Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "Text" and then select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/7933674083095/btn_ellipsis1.gif) in the value cell in the Report Inspector.

![Text Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933680220311/txtoptn.gif)

Designer displays these options:

**Delimited Format**

Select to use the delimited format to generate the report.

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

Select to use user-defined density to generate the report.

* **Horizontal Density**  
  Specify the value for each unit of the horizontal density between columns.
* **Vertical Density**  
  Specify the value for each unit of the vertical density between columns.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/7933685587863/noteicon.jpg)

* When using user-defined densities, if you do not set the densities appropriately, the fields in the report may overlap each other.
* When you set the value of Horizontal/Vertical Density:
  + The value of Horizontal/Vertical Density must be greater than the character's width/height of the smallest field in the report (smallest field is the field with the smallest font size); otherwise, Server cannot apply the value you set at runtime.
  + If the value of Vertical Density is greater than 0 and the value of Horizontal Density is less than 0, Server applies the value that you specify for Vertical Density and specifies the value of Horizontal Density at runtime.
  + If the value of Vertical Density is less than 0 and the value of Horizontal Density is greater than 0, Server applies the value that you specify for Horizontal Density and specifies the value of Vertical Density at runtime.
  + If the values of Vertical Density and Horizontal Density are both greater than 0 and the value of Horizontal Density is less than 11, Server applies the values that you specify for the two densities; otherwise, Server specifies them at runtime.
  + If the values of Vertical Density and Horizontal Density are both less than 1, Server specifies these densities at runtime.

**Compress**

Select to generate the Text output in a compressed size, meaning there will be no clearance between the columns.

**Header and Footer**

Select to include all headers and footers in the report, including report header/footer, page header/footer, and group header/footer in the Text output; otherwise, the Text output contains only data in the detail panel.

**Windows End-of-line (CR-LF)**

Select to use "CR-LF" in Windows convention as the end-of-line character.

**Unix End-of-line (LF)**

Select to use "LF" in UNIX convention as the end-of-line character.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports) in the Text output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735515884439-Tabular-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525134999-Time-Zone-and-Locale-Options-Dialog-Box)
