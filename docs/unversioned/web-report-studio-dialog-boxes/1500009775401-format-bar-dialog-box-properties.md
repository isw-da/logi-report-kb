---
title: "Format Bar Dialog Box Properties"
id: 1500009775401
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775401-Format-Bar-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:27Z
---

# Format Bar Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775381-Format-Area-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747162-Format-Bar-Gauge-Dialog-Box-Properties)

# Format Bar Dialog Box Properties

This topic describes how you can use the Format Bar dialog box to format the bars of a bar chart. Server displays the dialog box when you right-click a bar chart and select **Format Graph** from the shortcut menu.

![Format Bar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885482775/fmtbar.gif)

**Style**

Specifies the style of the bars in the chart.

* **Normal**  
   Specifies to make the bars be quadrate.
* **Cylinder**  
   Specifies to make the bars be columned. It takes effect only when the property Use Depth is selected below.
* **Vary Colors**Specifies whether to make each bar of the chart take a different color schema. It takes effect only for clustered bar types and when the chart has no series field.

**Size**

Specifies the size of the bars in the chart.

* **Width**  
   Specifies the bar width as a percentage of the unit width.

**Depth**

Specifies the depth properties for bars of the chart.

* **Use Depth**  
   Specifies whether to make the bars visually three-dimensional.
  + **Depth**  
     Specifies the depth of the bars, in inches.
  + **Direction**  
     Specifies the angle of the axis along the depth of the bars, in degrees.

**Static Data Label**

Specifies the properties of the static data labels on the bars.

* **Show Static Data Label**  
   Specifies whether to show the static data labels on the bars. Only when it is true can the following static data label related properties work.
* **Style**  
   Specifies the display type for data values in the static data labels.
  + **Value**  
    Shows the value for each bar.
  + **Percent**  
     Shows the percentage of each bar to the total.
  + **Value and Percent**  
     Shows the value and the percentage for each bar.
* **Position**  
   Specifies the position of the static data labels on the bars.
  + **Autofit**  
     If selected, the static data labels will be displayed automatically.
  + **Outside Top**   
     If selected, the static data labels will be displayed on the outside top of the bars.
  + **Inside Top**  
     If selected, the static data labels will be displayed on the inside top of the bars.
  + **Inside Center**  
     If selected, the static data labels will be displayed at the inside center of the bars.
  + **Inside Bottom**  
     If selected, the static data labels will be displayed at the inside bottom of the bars.
* **Auto Arrange**  
  Specifies whether to display the static data labels inside the bars at the best position. Available only when the static data label's position is set to one of the following: Inside Center, Inside Top and Inside Bottom.
  + **true**  
     The static data labels will be displayed horizontally at the specified position if the bar has enough room horizontally, otherwise, will be displayed vertically. If a bar does not have enough room both vertically and horizontally, its static data label will not be displayed.
  + **false**  
     The static data labels will be displayed at the specified position, and if the labels get overlapping, some of them will not be displayed.
* **Auto Scale in Number**  

  Specifies whether to
  automatically scale the values that are of the Number data type when the values fall into the two ranges:

  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The value **auto** means the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009777861-Chart-Properties#AutoScale).

**Graph Border**

Specifies the properties for the border of the bars.

* **Show Border**  
  Specifies whether to show the border of the bars. When it is selected, the other border properties will be enabled.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775381-Format-Area-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747162-Format-Bar-Gauge-Dialog-Box-Properties)
