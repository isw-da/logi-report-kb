---
title: "Format Radar Dialog Box Properties"
id: 1500009744542
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744542-Format-Radar-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:12Z
---

# Format Radar Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772441-Format-Scatter-Dialog-Box-Properties)

# Format Radar Dialog Box Properties

You can use the Format Radar dialog box to format the radar of a radar chart. This topic describes the options in the dialog box.

![Format Radar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885571991/fmtrdr.gif)

**Static Data Label**

Specifies the properties of the static data labels on the radar.

* **Show Static Data Label**  
   Specifies whether to show the static data labels on the radar. Only when it is true can the following static data label related properties work.
* **Data Label Type**  
   Specifies in which way to display the data values in the static data labels.
  + **percent**  
    Shows the percentage of each value node to the total.
  + **value**  
     Shows the value for each value node.
  + **value and percent**  
     Shows the value and the percentage for each value node.
* **Position**  
   The static data labels will be displayed automatically.
* **Auto Arrange**  
   Not supported on radar charts.
* **Auto Scale in Number**  
   Specifies whether to automatically scale the static data labels that are of the Number data type when the label values fall into the two ranges:
  + When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

**Graph Border**

Specifies the properties for the border of the radar.

* **Show Border**  
  Specifies whether to show the border of the radar. When it is selected, the other border properties will be enabled.
  + **Line Style**  
     Specifies the line style to apply to the border.
  + **Color**  
     Specifies the color of the border.
  + **Thickness**  
     Specifies the thickness of the border.
  + **Transparency**  
     Specifies the transparency for color of the border.

**Hint**

Specifies the properties of the data marker hint.

* **Show Category and Series**  
   Specifies whether to include the category and series values in the data marker hint.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744522-Format-Pointer-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772441-Format-Scatter-Dialog-Box-Properties)
