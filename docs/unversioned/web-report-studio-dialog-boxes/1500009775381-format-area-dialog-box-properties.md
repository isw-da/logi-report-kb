---
title: "Format Area Dialog Box Properties"
id: 1500009775381
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775381-Format-Area-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:27Z
---

# Format Area Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747142-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775401-Format-Bar-Dialog-Box-Properties)

# Format Area Dialog Box Properties

This topic describes how you can use the Format Area dialog box to format the areas of an area chart. Server displays the dialog box when you right-click an area chart and select **Format Graph** from the shortcut menu.

![Format Area dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880385431/fmtarea.gif)

**Depth**

Specifies the depth properties for areas of the chart.

* **Use Depth**  
   Specifies whether to make the areas visually three-dimensional.
  + **Depth**  
     Specifies the depth of the areas, in inches.
  + **Direction**  
     Specifies the angle of the axis along the depth of the areas, in degrees.

**Static Data Label**

Specifies the properties of the static data labels on the areas.

* **Show Static Data Label**  
   Specifies whether to show the static data labels on the areas. Only when it is true can the following static data label related properties work.
* **Style**  
   Specifies the display type for data values in the static data labels.
  + **Value**  
    Shows the value for each area node.
  + **Percent**  
     Shows the percentage of each area node to the total.
  + **Value and Percent**  
     Shows the value and the percentage for each area node.
* **Position**  
   Specifies the position of the static data labels on the areas.
  + **Autofit**  
     If selected, the static data labels will be displayed automatically.
  + **Top Center**  
     If selected, the static data labels will be displayed in the top center of the nodes on the areas.
  + **Top Left**  
     If selected, the static data labels will be displayed on the top left of the nodes on the areas.
  + **Top Right**  
     If selected, the static data labels will be displayed on the top right of the nodes on the areas.
  + **Bottom Left**  
     If selected, the static data labels will be displayed on the bottom left of the nodes on the areas.
  + **Bottom Center**  
     If selected, the static data labels will be displayed in the bottom center of the nodes on the areas.
  + **Bottom Right**  
     If selected, the static data labels will be displayed on the bottom right of the nodes on the areas.
* **Auto Arrange**  
   Not supported on area charts.
* **Auto Scale in Number**  

  Specifies whether to
  automatically scale the values that are of the Number data type when the values fall into the two ranges:

  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The value **auto** means the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties#AutoScale).

**Graph Border**

Specifies the properties for the border of the areas.

* **Show Border**  
  Specifies whether to show the border of the areas. When it is selected, the other border properties will be enabled.
  + **Line Style**Specifies the line style to apply to the border.
  + **Color**Specifies the color of the border.
  + **Thickness**Specifies the thickness of the border.
  + **Transparency**Specifies the transparency for color of the border.

**Hint**

Specifies the properties of the data marker hint.

* **Show Category and Series**Specifies whether to include the category and series values in the data marker hint.
* **Auto Scale in Number**

  Specifies whether to
  automatically scale the values that are of the Number data type when the values fall into the two ranges:

  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The value **auto** means the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties#AutoScale).

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747142-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775401-Format-Bar-Dialog-Box-Properties)
