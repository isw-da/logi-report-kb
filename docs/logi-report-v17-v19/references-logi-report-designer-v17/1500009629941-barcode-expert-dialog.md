---
title: "Barcode Expert Dialog"
id: 1500009629941
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629941-Barcode-Expert-Dialog
updated_at: 2021-07-24T16:05:00Z
---

# Barcode Expert Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629921-Banded-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607302-Bind-Data-Dialog)

# Barcode Expert Dialog

The Barcode Expert dialog helps you create and edit a [barcode object](https://devnet.logianalytics.com/hc/en-us/articles/1500009605522-Barcodes) and then insert it in a report. It appears when you select Insert > Barcode.

![Barcode Expert dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904391831/brcd.gif)

The following are details about options in the dialog:

**Barcode Resources**

Lists the data resources that can be used for the barcode. The data source of a barcode can be database fields, formulas, summaries or parameters.

**Symbology**

Specifies the barcode type. You can choose from the following: UPC-A, UPC-E, EAN-13, EAN-8, Code39, Code128 and Codabar.

**Scale Mode**

Specifies the unit for values of Quiet Zone, Narrow Width, Supplement, Height, and Ratio. Can be Mils (0.001 inch), Metric (0.01 millimeter), and Points (1/72 inch).

**Quiet Zone**

Specifies the space around the barcode where there are no dark marks. Most of symbology requires a quiet zone which precedes the following barcode.

**Narrow Width**

Specifies the barcode bar width.

**Supplement**

Specifies the supplement. Some barcode types, such as CODE39, CODE128 and Codabar, do not have supplements.

**Height**

Specifies the height of the barcode.

**Ratio**

Specifies the width ratio of the thick bar to the thin bar in the CODE39/ Codabar barcode. The ratio box can have only 2 effective values, 2.0 and 3.0. Any ratio values that are not equal to 2.0 or 3.0 will be regarded as 2.0. Enabled only for CODE39 and Codabar.

**Default Message**

Specifies the default value for the barcode, which will be used for the barcode in design mode.

**Enable Checking Digits**

Specifies whether the checking digits will be enabled.

**Display HR**

Specifies whether to display the barcode numbers together with the barcode. Enabled only for CODE39, CODE128, and Codabar.

**Enable Length Optimization**

Specifies whether to enable optimizing the length of the barcode in the report result. Available to Code 128 only.

**Insert**

Accepts the changes and inserts the barcode into your report.

**Cancel**

Does not retain the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629921-Banded-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607302-Bind-Data-Dialog)
