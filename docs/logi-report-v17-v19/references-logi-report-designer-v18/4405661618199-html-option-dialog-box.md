---
title: "HTML Option Dialog Box"
id: 4405661618199
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661618199-HTML-Option-Dialog-Box
updated_at: 2022-01-27T20:35:48Z
---

# HTML Option Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661617175-Horizontal-Banded-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661619223-Image-Button-Dialog-Box)

# HTML Option Dialog Box

You can use the HTML Option dialog box to predefine the options for directly running a report in HTML on Server. This topic describes the options in the dialog box.

Designer displays the HTML Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "HTML" and then select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif) in the value cell in the Report Inspector.

![HTML Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410700055/htmloptn.gif)

You see the following options in the dialog box:

**No Margin**

Select to remove the margins that you set when designing the report
in the HTML output.

**Multiple Files**

Select to generate the report to multiple HTML files. Server designates a serial number for each HTML page at runtime. For example, if you named a 3-page report as "sales", Server creates three files called sales\_1.html, sales\_2.html, and sales\_3.html.

* **Embedded CSS**  
  Select to embed the cascading style sheet (CSS) in the HTML output; otherwise, Server generates the .css file individually at runtime.

**Single File**

Select to generate the report to a single HTML file.

* **No Hyperlink**  
  Select if you do not want to include the hyperlinks for navigating previous and Next Topics on the navigation bar of the HTML output.
* **No Page Number**  
  Select if you do not want to include the page number information that shows the current page number and total page number on the navigation bar of the HTML output.

**Drilldown**

Select if you want to generate the drill-down files for the HTML output, which enable users to drill down on the summaries in grouped banded objects.

**Section 508 Compliant Output**

Select to export the accessibility attributes that you define for the report elements in the Report Inspector to HTML which is Section 508 compliant at runtime. For more information, see [Exporting Reports to Accessible HTML and PDF](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF).

When you select Section 508 Compliant Output, Designer automatically selects the Use HTML Data Table and Relative Font Size options and disables them. The HTML report output is then Section 508 compliant including HTML data table, accessible attributes, and relative font feature.

**Use HTML Data Table**

Select to generate the table and crosstab components as table objects in the HTML output.

**Absolute Font Size**

Select to generate the report using an absolute font size, which means the font size is fixed and cannot be adjusted according to the font size settings in the web browser.

**Relative Font Size**

Select to generate the report using a relative font size, which means the font size can be adjusted according to the font size settings in the web browser.

**Image Chart**

Select the image format using which to convert charts in the report: Auto Select, GIF, JPG (JPEG), or PNG.

If you select "Auto Select", it is up to Server to detect the image format to JPG or GIF automatically at runtime: if the image colors are less than 256 colors, Server applies GIF; otherwise, it is JPG.

**Resolution**

Specify the resolution of the HTML output to zoom in/out, in DPI. Designer obtains the default value from your operation system, which is the resolution of your monitor, for example, 72 DPI on UNIX or 96 on Windows. You can set higher/lower value to zoom in/out at runtime.

**Web Browser**

Select the web browser for which the HTML output adapts.

**Text Overflow**

Specify whether the text overflow is visible or hidden.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports) in the HTML output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661617175-Horizontal-Banded-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661619223-Image-Button-Dialog-Box)
