---
title: "Export to PDF Dialog Box"
id: 1500010096721
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096721-Export-to-PDF-Dialog-Box
updated_at: 2021-07-23T19:15:23Z
---

# Export to PDF Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096701-Export-to-Mail-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058982-Export-to-PostScript-Dialog-Box)

# Export to PDF Dialog Box

You can use the Export to PDF dialog box to [export a report to PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF). This topic describes the options in the dialog box.

Designer displays the Export to PDF dialog box when you select File > Export > To PDF.

![Export to PDF dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848474007/expt2pdf.gif)

You see the following options in the dialog box:

**Directory**

Specify the destination directory where to save the PDF.

**File Name**

Specify the file name of the PDF.

**Select Report Tabs**

Designer displays the option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. If the report has only one report tab, Designer selects the report tab by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified report tab higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified report tab lower in the list.

**No Margin**

Select to remove the margins that you set when designing the report
in the PDF output.

**TOC**

Select to enable the TOC (Table of Contents) in the PDF output.

**Drilldown**

Select to generate the drilldown files when exporting the report, which enable you to drill down on the summaries in grouped banded objects in the PDF output.

**Encrypt**

Select to encrypt the PDF. Select the Setting button to configure the encrypt settings in the [Encrypt dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096561-Encrypt-Dialog-Box).

**Sign**

Select to add digital sign to the PDF. Select the Setting button to configure the sign settings in the [Sign Digital ID dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098641-Sign-Digital-ID-Dialog-Box).

**Accessible PDF**

Select to generate an accessible PDF for the report.

**Compress Image**

Select to compress the size of the images or pictures in the report to the specified proportion of its original size.

**Generate charts and barcodes using images (recommended)**

Select to export charts and barcodes as well as web controls and UDOs in the report to common pictures, which look dimmed and the file size may be relatively large. However, when you select Compress Image and this option at the same time, the transparency property of the charts, UDOs, and barcodes cannot take effect.

**Generate charts and barcodes using vector graphics**

Select to export charts and barcodes as well as web controls and UDOs in the report to vector graphics, which are not anamorphic when you zoom in or out.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports) in the PDF output.

**Clipping Area**

Select to cut the content that is beyond a specific area.

**Zoom**

Select the zooming of the report content in the PDF output.

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

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096701-Export-to-Mail-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058982-Export-to-PostScript-Dialog-Box)
