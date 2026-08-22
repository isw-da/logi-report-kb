---
title: "PDF Option Dialog"
id: 1500009609522
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009609522-PDF-Option-Dialog
updated_at: 2021-07-24T16:04:18Z
---

# PDF Option Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609742-Parameter-Order-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609622-Pick-a-Color-Dialog)

# PDF Option Dialog

The PDF Option dialog helps you to specify the parameters for running a report in the PDF format. It appears when you set the Default Format for Viewing Report property of a report tab or a web report to PDF and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the value cell in the Report Inspector.

![PDF Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911689623/pdfoptn.gif)

The following are details about options in the dialog:

**No Margin**

Removes the margins you originally set while designing the report.

**TOC**

Generates the report result to PDF format with a Table of Contents.

**Drilldown**

Generates the report result to a PDF file with the Drilldown feature enabled. The Drilldown feature enables you to inspect certain items for further detailed data.

**Encrypt**

Specifies whether to encrypt the PDF result. Select the option and you can configure the encrypt settings in the [Encrypt](https://devnet.logianalytics.com/hc/en-us/articles/1500009631001-Encrypt-Dialog) dialog.

**Sign**

Specifies whether to add the digital sign to the PDF result. Select the option and you can configure the sign settings in the [Sign Digital ID](https://devnet.logianalytics.com/hc/en-us/articles/1500009633401-Sign-Digital-ID-Dialog) dialog.

**Accessible PDF**

Specifies to generate an accessible PDF result for the report. See [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500009628201-Accessibility) for more information.

**Compress Image**

Compresses the images in the report by the percentage you specify in the box.

**Generate charts and barcodes using images (recommended)**

When you run a report in PDF format, Logi Report will take the result of the whole report as a graphic to transform the report by the method of simulated printer and generate the report result in PDF format.

**Generate charts and barcodes using vector graphics**

The result of using Generate charts and barcodes using vector graphics is the same as with using Generate charts and barcodes using images (recommended). However, when you run a report in PDF format using Generate charts and barcodes using vector graphics, Logi Report will take the result of the whole report as a dataset to transform the report by sequence and to generate the report result in PDF format.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the PDF result. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**Clipping Area**

Specifies whether to cut the content that is beyond a specific area.

**![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")Zoom**

Specifies the zooming of the report content in the PDF result. You can select an item from the drop-down list or type a percentage in the text box. A valid percentage is greater than 0 and no larger than 6400% (you can type the value with or without the percent sign). Any invalid input will be treated as Default.

* **Default**  
  It means no zoom setting. After the PDF file is opened in the Adobe Acrobat, the zoom setting follows that in the Adobe.
* **Actual Size**  
  The report content remains its original size. It is same as 100%.
* **Fit Page**  
  The report content in a page is scaled to fit the entire page within the window both horizontally and vertically. If the required horizontal and vertical scale ratios are different, the smaller of the two is used.
* **Fit Width**  
  The report content in a page is scaled to fit the width of the page within the window.
* **Fit Height**  
  The report content in a page is scaled to fit the height of the page within the window.
* **Fit Visible** - The report content in a page is scaled to fit the width of its bounding box within the window.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609742-Parameter-Order-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009609622-Pick-a-Color-Dialog)
