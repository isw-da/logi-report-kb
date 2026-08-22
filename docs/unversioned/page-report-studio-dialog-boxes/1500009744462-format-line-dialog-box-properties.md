---
title: "Format Line Dialog Box Properties"
id: 1500009744462
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744462-Format-Line-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:14Z
---

# Format Line Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772381-Format-Legend-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744482-Format-Paper-Dialog-Box-Properties)

# Format Line Dialog Box Properties

You can use the Format Line dialog box to format the lines of a line chart. This topic describes the options in the dialog box.

![Format Line dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880519575/fmtln.gif)

**Depth**

Specifies the depth properties for lines of the chart.

* **Use Depth**  
   Specifies whether to make the lines visually three-dimensional.
  + **Depth**  
     Specifies the depth of the lines, in inches.
  + **Depth Direction**  
     Specifies the angle of the axis along the depth of the lines, in degrees.

**Static Data Label**

Specifies the properties of the static data labels on the lines. Not supported on 3-D line charts.

* **Show Static Data Label**  
   Specifies whether to show the static data labels on the lines. Only when it is true can the following static data label related properties work.
* **Data Label Type**  
   Specifies in which way to display the data values in the static data labels.
  + **percent**  
     Shows the percentage of each line node to the total.
  + **value**  
     Shows the value for each line node.
  + **value and percent**  
     Shows the value and the percentage for each line node.
* **Position**  
   Specifies the position of the static data labels on the lines.
  + **Autofit**  
     If selected, the static data labels will be displayed automatically.
  + **Top Center**  
     If selected, the static data labels will be displayed on the top center of the line nodes.
  + **Top Left**  
     If selected, the static data labels will be displayed on the top left of the line nodes.
  + **Top Right**  
     If selected, the static data labels will be displayed on the top right of the line nodes.
  + **Bottom Left**  
     If selected, the static data labels will be displayed at the bottom left of the line nodes.
  + **Bottom Center**  
     If selected, the static data labels will be displayed at the bottom center of the line nodes.
  + **Bottom Right**  
     If selected, the static data labels will be displayed at the bottom right of the line nodes.
* **Auto Arrange**  
   Not supported in line charts.
* **Auto Scale in Number**

  Specifies whether to
  automatically scale the values that are of the Number data type when the values fall into the two ranges:

  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772381-Format-Legend-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744482-Format-Paper-Dialog-Box-Properties)
