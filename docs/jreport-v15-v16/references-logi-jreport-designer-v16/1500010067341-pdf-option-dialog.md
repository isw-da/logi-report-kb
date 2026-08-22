---
title: "PDF Option Dialog"
id: 1500010067341
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067341-PDF-Option-Dialog
updated_at: 2021-07-24T10:38:32Z
---

# PDF Option Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067421-Parameter-Order-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067401-Pick-a-Color-Dialog)

# PDF Option Dialog

The PDF Option dialog helps you to specify the parameters for running a report in the PDF format. It appears when you set the Default Format for Viewing Report property of a report tab or a web report to PDF and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the value cell in the Report Inspector.

![PDF Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909163159/pdfoptn.gif)

The following are details about options in the dialog:

**No Margin**

Removes the margins you originally set while designing the report.

**TOC**

Generates the report result to PDF format with a Table of Contents.

**Drilldown**

Generates the report result to a PDF file with the Drilldown feature enabled. The Drilldown feature enables you to inspect certain items for further detailed data.

**Encrypt**

Specifies whether to encrypt the PDF file. Select the option and you can configure the encrypt settings in the [Encrypt](https://devnet.logianalytics.com/hc/en-us/articles/1500010065821-Encrypt-Dialog) dialog.

**Sign**

Specifies whether to add the digital sign to the PDF file. Select the option and you can configure the sign settings in the [Sign Digital ID](https://devnet.logianalytics.com/hc/en-us/articles/1500010032442-Sign-Digital-ID-Dialog) dialog.

**Accessible PDF**

Specifies to generate an accessible PDF file for the report. See [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500010063081-Accessibility) for more information.

**Compress Image**

Compresses the images in the report by the percentage you specify in the box.

**Generate charts and barcodes using images (recommended)**

When you run a report in PDF format, Logi JReport will take the result of the whole report as a graphic to transform the report by the method of simulated printer and generate the report result in PDF format.

**Generate charts and barcodes using vector graphics**

The result of using Generate charts and barcodes using vector graphics is the same as with using Generate charts and barcodes using images (recommended). However, when you run a report in PDF format using Generate charts and barcodes using vector graphics, Logi JReport will take the result of the whole report as a dataset to transform the report by sequence and to generate the report result in PDF format.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the PDF result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067421-Parameter-Order-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067401-Pick-a-Color-Dialog)
