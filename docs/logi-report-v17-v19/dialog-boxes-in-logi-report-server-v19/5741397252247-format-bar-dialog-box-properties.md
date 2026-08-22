---
title: "Format Bar Dialog Box Properties"
id: 5741397252247
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741397252247-Format-Bar-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:16Z
---

# Format Bar Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741424380439-Format-Area-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741410633111-Format-Bar-Gauge-Dialog-Box-Properties)

# Format Bar Dialog Box Properties

You can use the Format Bar dialog box to format the bars of a bar chart or bench chart. This topic describes the properties in the dialog box.

![Format Bar dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905815932567/fmtbar.gif)

**Style**

Select the style of the bars in the chart.

* **Normal**  
   Select to make the bars be quadrate.
* **Cylinder**  
   Select to make the bars be columned. It takes effect only when you select **Use Depth** in the dialog box.
* **Vary Colors** Select to make each bar of the chart take a different color schema. It takes effect for clustered bar/bench types when the chart has no series field.

**Size**

Specify the size of the bars in the chart.

* **Bar Width**  
   Specify the bar width as a percentage of the unit width.

**Depth**

Specify the depth properties for the bars of the chart.

* **Use Depth**  
   Select **true** if you want to make the bars visually three-dimensional.
  + **Depth**  
     Specify the depth of the bars, in inches.
  + **Depth Direction**  
     Specify the angle of the axis along the depth of the bars, in degrees.

**Static Data Label**

Specify the properties of the static data labels on the bars. 3D bar/bench charts do not support this property.

* **Show Static Data Label**  
   Select **true** if you want to show the static data labels on the bars. Only when it is true can the following static data label properties work.
* **Data Label Type**  
   Select the display type for data values in the static data labels.
  + **percent**  
     Select to display the percentage of each bar to the total.
  + **value**  
     Select to display the value for each bar.
  + **value and percent**  
     Select to display the value and the percentage for each bar.
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
Server enables this property when you select **Inside Center**, **Inside Top**, or **Inside Bottom** as static data labels' position.
Select **true** if you want to display the static data labels that can completely show inside the bars.

+ **true**  
   Server displays the static data labels horizontally at the specified position if the bars have enough space horizontally, otherwise displays them vertically. If a bar does not have enough space both vertically and horizontally, Server does not display its static data label.
+ **false**  
   Server displays the static data labels at the specified position. If data labels overlap, Server does not display some of them.

* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).

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

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741424380439-Format-Area-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741410633111-Format-Bar-Gauge-Dialog-Box-Properties)
