---
title: "Format Area Dialog Box Properties"
id: 4405683822231
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683822231-Format-Area-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:17Z
---

# Format Area Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683821207-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683823255-Format-Bar-Dialog-Box-Properties)

# Format Area Dialog Box Properties

This topic describes how you can use the Format Area dialog box to format the areas of an area chart.

Server displays the dialog box when you right-click an area chart and select **Format Graph** from the shortcut menu.

![Format Area dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420461650967/fmtarea.gif)

**Depth**

Specify the depth properties of the chart areas.

* **Use Depth**  
   Select **true** if you want to make the areas visually three-dimensional.
  + **Depth**  
     Specify the depth of the areas, in inches.
  + **Direction**  
     Specify the angle of the axis along the depth of the areas, in degrees.

**Static Data Label**

Specify the properties of the static data labels on the areas.

* **Show Static Data Label**  
   Select **true** if you want to show the static data labels on the areas. Only when it is true can the following static data label properties work.
* **Style**  
   Select the display type for data values in the static data labels.
  + **Value**  
     Select to display the value for each area node.
  + **Percent**  
     Select to display the percentage of each area node to the total.
  + **Value and Percent**  
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

  The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

**Graph Border**

Specify the properties for the border of the areas.

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

  The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).
* **Customize Chart Value Names**  
  Select if you want to customize the names of the fields used as the values in the chart. Server uses the customized names in the data marker hint. Then select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4420453393175/btn_chsr2.gif) to open the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683804695-Customize-Chart-Value-Names-Dialog-Box-Properties).

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683821207-Format-Activity-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683823255-Format-Bar-Dialog-Box-Properties)
