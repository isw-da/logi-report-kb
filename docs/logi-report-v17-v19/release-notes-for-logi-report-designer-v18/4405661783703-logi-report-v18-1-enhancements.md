---
title: "Logi Report v18.1 Enhancements"
id: 4405661783703
section: "Release Notes for Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661783703-Logi-Report-v18-1-Enhancements
updated_at: 2022-09-29T19:14:34Z
---

# Logi Report v18.1 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661781399-Logi-Report-v18-1-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664606871-Logi-Report-v18-Release-Notes)

# Logi Reportv18.1 Enhancements

This topic introduces the significant features of the Logi Report v18.1 release.

* [Improved Report UI/UX](#ReportUI)
* [Enhanced Embedding Capabilities](#Embedding)
* [Pixel-Perfect Formatting](#Pixel)
* [Advanced Accessible PDF](#PDF)

## Improved Report UI/UX

* Logi Report now has a new report style called DefaultSequential. This is also the default report style, providing you with an enhanced and modern look for your new reports.

  ![Chart in DefaultSequential Style](https://devnet.logianalytics.com/hc/article_attachments/4420542092183/default-sequential.png)
* Logi Report has modernized the style of embedded components like Table, Chart, Crosstab, Banded Object, and Web Control, enhancing their look and feel by adjusting default values for the font, padding, and border properties.

  ![Enhanced Component UI](https://devnet.logianalytics.com/hc/article_attachments/4420550848535/enhanced-component-ui.png)

## Enhanced Embedding Capabilities

* You can now save web report files in XML in both Designer and Web Report Studio, and download web reports from Server to Designer as XML resources.

  ![Web Report in XML](https://devnet.logianalytics.com/hc/article_attachments/4420556114967/xml-web-report.png)
* Logi Report now supports OpenJDK 14, in addition to OpenJDK 8, 11, 12, and 13.

## Pixel-Perfect Formatting

* You now have the option to either remove or keep blank spaces at the beginning and end of field values in your text output. You can set the Trim Blank Spaces property in the following cases:
  + In the Export to Text dialog box in Designer.
  + In the Server Preferences.
  + When advanced running reports.
  + When scheduling tasks to run reports.
  + In the Export dialog box in Page Report Studio or Web Report Studio.

  ![Trim Blank Spaces](https://devnet.logianalytics.com/hc/article_attachments/4420542092439/trim-blank-spaces.png)
* You can now use the Merged Cell property of a table cell to specify whether the cell is also a merged cell in the Excel output of a report, when the cell displays with its sequential cells as a merged cell in the report.

  ![Excel Output When Merged Cell False](https://devnet.logianalytics.com/hc/article_attachments/4420550849303/merged-cell-false.png)

  ![Excel Output When Merged Cell True](https://devnet.logianalytics.com/hc/article_attachments/4420550849559/merged-cell-true.png)

## Advanced Accessible PDF

* You can now export tables and crosstabs to a tagged PDF to make finding content in the PDF easier.
* You can now adjust the order you want the screen reader to read the report objects in the accessible PDF, by editing their display sequence in the Report Inspector.

  ![Adjust Object Order in Accessible PDF.png](https://devnet.logianalytics.com/hc/article_attachments/4420556115223/object-order-in-accessible-pdf.png)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661781399-Logi-Report-v18-1-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664606871-Logi-Report-v18-Release-Notes)
