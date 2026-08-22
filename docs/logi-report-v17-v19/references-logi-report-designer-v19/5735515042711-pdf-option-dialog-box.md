---
title: "PDF Option Dialog Box"
id: 5735515042711
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735515042711-PDF-Option-Dialog-Box
updated_at: 2022-11-02T07:53:16Z
---

# PDF Option Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544030999-Parameter-Order-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box)

# PDF Option Dialog Box

You can use the PDF Option dialog box to predefine the options for directly running a report in PDF on Server. This topic describes the options in the dialog box.

Designer displays the PDF Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "PDF" and then select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) in the value cell in the Report Inspector.

![PDF Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898461271447/pdfoptn.gif)

Designer displays these options:

**No Margin**

Select to remove the margins that you set when designing the report
in the PDF output.

**TOC**

Select to include the TOC tree of the report in the PDF output to display in the Table of Contents panel of the PDF browser.

**Drilldown**

Select to generate the drilldown files when exporting the report, which enable you to drill down on the summaries in grouped banded objects in the PDF output.

**Encrypt**

Select to encrypt the PDF. Select **Setting** to configure the encrypt settings in the [Encrypt dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522749847-Encrypt-Dialog-Box).

**Sign**

Select to add digital sign to the PDF. Select **Setting** to configure the sign settings in the [Sign Digital ID dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552629655-Sign-Digital-ID-Dialog-Box).

**Accessible PDF**

Select to generate an accessible PDF for the report. For more information, see [Exporting Reports to Accessible HTML and PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF).

**Compress Image**

Select to compress the size of the images or pictures in the report to the specified proportion of its original size.

**Generate charts and barcodes using images (recommended)**

When you run a report in PDF, Server takes the result of the whole report as a graphic to transform the report by the method of simulated printer and to generate the report in PDF.

**Generate charts and barcodes using vector graphics**

The result of using vector graphics is the same as with using images. However, when you run a report in PDF using vector graphics, Server takes the result of the whole report as a dataset to transform the report by sequence and to generate the report in PDF.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports) in the PDF output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

**Clipping Area**

Select to cut the content that is beyond a specific area.

**Zoom**

Select the zooming of the report content in the PDF output. You can select an item from the drop-down list or type a percentage in the text box. A valid percentage is greater than 0 and no larger than 6400% (you can type the value with or without the percent symbol). Designer treats any invalid input as "Default" (no zoom setting).

* **Default**  
  It means no zoom setting. After the PDF is opened in the Adobe Acrobat, the zoom setting follows that in the Adobe.
* **Actual Size**  
  Select to keep the report content in its original size. It is the same as 100%.
* **Fit Page**  
  Select to scale the report content in a page to fit the entire page within the window both horizontally and vertically. If the required horizontal and vertical scale ratios are different, the smaller of the two is used.
* **Fit Width**  
  Select to scale the report content in a page to fit the width of the page within the window.
* **Fit Height**  
  Select to scale the report content in a page to fit the height of the page within the window.
* **Fit Visible**  
  Select to scale the report content in a page to fit the width of its bounding box within the window.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735544030999-Parameter-Order-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box)
