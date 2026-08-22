---
title: "Export to PDF Dialog"
id: 1500009586741
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586741-Export-to-PDF-Dialog
updated_at: 2021-07-24T05:55:20Z
---

# Export to PDF Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565562-Export-to-Mail-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586761-Export-to-PostScript-Dialog)

# Export to PDF Dialog

The Export to PDF dialog appears when you select File > Export > To PDF. It helps you to [export a report to PDF format](https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF). [See the dialog](javascript:%20void(null)).

![Export to PDF dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893840535/expt2pdf.gif)

The following are details about options in the dialog:

**Directory**

Specifies the destination directory where the exported PDF file will be placed.

**File Name**

Specifies the name of the exported PDF file. If you do not type a name, Logi JReport will use the report name as the PDF file name.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export to the PDF file. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified report tab one step down.

**No Margin**

Specifies whether to remove the margins originally set when the report was designed.

**TOC**

Specifies whether to include a Table of Contents (TOC) in the exported PDF file.

**Drilldown**

Specifies whether to generate the report result to a PDF file with the Drilldown feature enabled. The Drilldown feature enables you to inspect certain items for further detailed data.

**Encrypt**

Specifies whether to encrypt the PDF file. Select the Setting button to configure the encrypt settings in the [Encrypt](https://devnet.logianalytics.com/hc/en-us/articles/1500009586661-Encrypt-Dialog) dialog.

**Sign**

Specifies whether to add the digital sign to the PDF file. Select the Setting button to configure the sign settings in the [Sign Digital ID](https://devnet.logianalytics.com/hc/en-us/articles/1500009588621-Sign-Digital-ID-Dialog) dialog.

**Compress Image**

If checked, the size of the images or pictures in the report will be compressed to the specified proportion of its original size.

**Generate charts and barcodes using images (recommended)**

If selected, charts, UDOs and barcodes in the report will be exported to common pictures, which will look dimmed and the file size may be relatively large. However, when Compress Image and this option are both checked, the transparency property of the charts, UDOs and barcodes will not take effect.

**Generate charts and barcodes using vector graphics**

If selected, charts, UDOs and barcodes in the report will be exported to vector graphics, which will not be anamorphic when it is zoomed out or zoomed in.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported PDF file. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**Clipping Area**

Specifies whether to keep the clipping area of the report in the exported PDF file.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565562-Export-to-Mail-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586761-Export-to-PostScript-Dialog)
