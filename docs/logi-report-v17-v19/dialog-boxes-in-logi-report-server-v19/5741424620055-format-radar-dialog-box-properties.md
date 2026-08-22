---
title: "Format Radar Dialog Box Properties"
id: 5741424620055
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741424620055-Format-Radar-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:20Z
---

# Format Radar Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741388608791-Format-Pointer-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741410929943-Format-Scatter-Dialog-Box-Properties)

# Format Radar Dialog Box Properties

You can use the Format Radar dialog box to format the radar of a radar chart. This topic describes the properties in the dialog box.

![Format Radar dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905775371159/fmtrdr.gif)

**Static Data Label**

Specify the properties of the static data labels on the radar.

* **Show Static Data Label**  
   Select **true** to show the static data labels on the radar. Only when it is true can the following static data label properties work.
* **Data Label Type**  
   Select the display type for the data values in the static data labels.
  + **percent**  
    Select to display the percentage of each value node to the total.
  + **value**  
     Select to display the value for each value node.
  + **value and percent**  
     Select to display the value and the percentage for each value node.
* **Position**  
   Server displays the static data labels automatically.
* **Auto Arrange**  
   Radar charts do not support this property.
* **Auto Scale in Number**  
   Select **true** if you want to automatically scale the static data labels that are of the Number data type when the label values fall into the two ranges:
  + When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).

**Graph Border**

Specify the border properties of the radar.

* **Show Border**  
  Select to show the border and enable the border properties.
  + **Line Style**Select the line style of the border.
  + **Color**Specify the color of the border.
  + **Thickness**Specify the thickness of the border.
  + **Transparency**Specify the transparency for the border color.

**Hint**

Specify the properties of the data marker hint.

* **Show Category and Series**
Select to include the category and series values in the data marker hint.* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741388608791-Format-Pointer-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741410929943-Format-Scatter-Dialog-Box-Properties)
