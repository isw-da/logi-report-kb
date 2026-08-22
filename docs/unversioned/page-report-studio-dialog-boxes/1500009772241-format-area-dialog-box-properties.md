---
title: "Format Area Dialog Box Properties"
id: 1500009772241
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772241-Format-Area-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:15Z
---

# Format Area Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744342-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744362-Format-Bar-Dialog-Box-Properties)

# Format Area Dialog Box Properties

You can use the Format Area dialog box to format the areas of an area chart. This topic describes the options in the dialog box.

![Format Area dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880536983/fmtarea.gif)

**Depth**

Specifies the depth properties for areas of the chart.

* **Use Depth**  
   Specifies whether to make the areas visually three-dimensional.
  + **Depth**  
     Specifies the depth of the areas, in inches.
  + **Depth Direction**  
     Specifies the angle of the axis along the depth of the areas, in degrees.

**Static Data Label**

Specifies the properties of the static data labels on the areas. Not supported on 3-D area charts.

* **Show Static Data Label**  
   Specifies whether to show the static data labels on the areas. Only when it is true can the following static data label related properties work.
* **Data Label Type**  
   Specifies in which way to display the data values in the static data labels.
  + **percent**  
     Shows the percentage of each area node to the total.
  + **value**  
     Shows the value for each area node.
  + **value and percent**  
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

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

**Graph Border**

Specifies the properties for the border of the areas.

* **Show Border**  
  Specifies whether to show the border of the areas. When the option is selected, the other border properties will be enabled.
  + **Line Style**  
     Specifies the line style to apply to the border.
  + **Color**  
     Specifies the color of the border.
  + **Thickness**  
     Specifies the thickness of the border.
  + **Transparency**  
     Specifies the transparency for color of the border.

**Hint**

Specifies the data marker hint properties.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744342-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744362-Format-Bar-Dialog-Box-Properties)
