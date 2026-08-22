---
title: "Format Surface Dialog Box Properties"
id: 1500009772461
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772461-Format-Surface-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:12Z
---

# Format Surface Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772481-Format-Stock-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772501-Format-Target-Label-Dialog-Box-Properties)

# Format Surface Dialog Box Properties

You can use the Format Surface dialog box to format the surface in a surface chart. This topic describes the options in the dialog box.

![Format Surface dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885569047/fmtsrfc.gif)

**Graph Border**

Specifies the properties for the border of the surface.

* **Show Border**  
  Specifies whether to show the border of the surface. When it is selected, the following border properties are enabled.
  + **Line Style**Specifies the line style to apply to the border.
  + **Color**Specifies the color of the border.
  + **Thickness**Specifies the thickness of the border, in inches.
  + **Transparency**Specifies the transparency for color of the border.

**Hint**

Specifies properties of the data marker hint.

* **Show Category and Series**Specifies whether to include the category and series values in the data marker hint.
* **Auto Scale in Number**

  Specifies whether to
  automatically scale the values that are of the Number data type when the values fall into the two ranges:

  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772481-Format-Stock-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772501-Format-Target-Label-Dialog-Box-Properties)
