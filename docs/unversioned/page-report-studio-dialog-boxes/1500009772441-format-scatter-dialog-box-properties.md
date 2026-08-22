---
title: "Format Scatter Dialog Box Properties"
id: 1500009772441
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772441-Format-Scatter-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:14Z
---

# Format Scatter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744542-Format-Radar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744562-Format-Solid-Gauge-Dialog-Box-Properties)

# Format Scatter Dialog Box Properties

You can use the Format Scatter dialog box to format the scatter of a scatter chart. This topic describes the options in the dialog box.

![Format Scatter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880511383/fmtsctr.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint of the data markers.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744542-Format-Radar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744562-Format-Solid-Gauge-Dialog-Box-Properties)
