---
title: "Format Area Dialog Box Properties"
id: 5741424380439
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741424380439-Format-Area-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:16Z
---

# Format Area Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741424370455-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741397252247-Format-Bar-Dialog-Box-Properties)

# Format Area Dialog Box Properties

You can use the Format Area dialog box to format the areas of an area chart. This topic describes the properties in the dialog box.

![Format Area dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905777224983/fmtarea.gif)

**Depth**

Specify the depth properties of the chart areas.

* **Use Depth**  
   Select to make the areas visually three-dimensional.
  + **Depth**  
     Specify the depth of the areas, in inches.
  + **Depth Direction**  
     Specify the angle of the axis along the depth of the areas, in degrees.

**Static Data Label**

Specify the properties of the static data labels on the areas. 3D area charts do not support this property.

* **Show Static Data Label**  
   Select **true** to show the static data labels on the areas. Only when it is true can the following static data label properties work.
* **Data Label Type**  
   Select the display type for data values in the static data labels.
  + **percent**  
     Select to display the percentage of each area node to the total.
  + **value**  
     Select to display the value for each area node.
  + **value and percent**  
     Select to display the value and the percentage for each area node.
* **Position**  
   Select the position of the static data labels on the areas.
  + **Autofit**  
     Select to display the static data labels automatically.
  + **Top Center**  
     Select to display the static data labels in the upper center of the nodes on the areas.
  + **Top Left**  
     Select to display the static data labels on the upper left of the nodes on the areas.
  + **Top Right**  
     Select to display the static data labels on the upper right of the nodes on the areas.
  + **Bottom Left**  
     Select to display the static data labels on the lower left of the nodes on the areas.
  + **Bottom Center**  
     Select to display the static data labels in the lower center of the nodes on the areas.
  + **Bottom Right**  
     Select to display the static data labels on the lower right of the nodes on the areas.
* **Auto Arrange**  
   Area charts do not support this property.
* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).

**Graph Border**

Specify the properties for the border of the areas.

* **Show Border**  
  Select to show the border and enable the border properties.
  + **Line Style**Select the line style of the border.
  + **Color**Specify the color of the border.
  + **Thickness**Specify the thickness of the border.
  + **Transparency**Specify the transparency for the border color.

**Hint**

Specify the data marker hint properties.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741424370455-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741397252247-Format-Bar-Dialog-Box-Properties)
