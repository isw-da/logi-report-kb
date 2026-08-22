---
title: "Format Bench Dialog Box Properties"
id: 4405683825559
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683825559-Format-Bench-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:18Z
---

# Format Bench Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683824279-Format-Bar-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683826711-Format-Bubble-Gauge-Dialog-Box-Properties)

# Format Bench Dialog Box Properties

This topic describes how you can use the Format Bench dialog box to format the bars of a bench chart. Server displays the dialog box when you right-click a bench chart and select **Format Graph** from the shortcut menu.

![Format Bench dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420453581335/fmtbnch.gif)

**Style**

Select the style of the bars in the chart.

* **Normal**  
   Select to make the bars be quadrate.
* **Cylinder**  
   Select to make the bars be columned. It takes effect only when you select **Use Depth** in the dialog box.
* **Vary Colors** Select to make each bar of the chart take a different color schema. It takes effect for clustered bar/bench types when the chart has no series field.

**Size**

Specify the size of the bars in the chart.

* **Width**  
   Specify the bar height as a percentage of the unit height.

**Depth**

Specify the depth properties for the bars of the chart.

* **Use Depth**  
   Select **true** if you want to make the bars visually three-dimensional.
  + **Depth**  
     Specify the depth of the bars, in inches.
  + **Depth Direction**  
     Specify the angle of the axis along the depth of the bars, in degrees.

**Static Data Label**

Specify the properties of the static data labels on the bars.

* **Show Static Data Label**  
   Select **true** if you want to show the static data labels on the bars. Only when it is true can the following static data label properties work.
* **Style**  
   Select the display type for data values in the static data labels.
  + **Value**  
    Server displays the value for each bar.
  + **Percent**  
     Server displays the percentage of each bar to the total.
  + **Value and Percent**  
     Server displays the value and the percentage for each bar.
* **Position**
Select the position of the static data labels on the bars.

+ **Autofit**  
   Select to display the static data labels automatically.
+ **Outside Top**   
   Select to display the static data labels on the outside top of the bars.
+ **Inside Top**  
   Select to display the static data labels on the inside top of the bars.
+ **Inside Center**  
   Select to display the static data labels at the inside center of the bars.
+ **Inside Bottom**  
   Select to display the static data labels at the inside bottom of the bars.

* **Auto Arrange**  
  For a bench chart, Server always displays the static data labels horizontally at the specified position, regardless of this property value.
* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

**Graph Border**

Specify the properties for the border of the bars.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683824279-Format-Bar-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683826711-Format-Bubble-Gauge-Dialog-Box-Properties)
