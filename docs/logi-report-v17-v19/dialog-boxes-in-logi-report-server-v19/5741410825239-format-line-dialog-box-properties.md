---
title: "Format Line Dialog Box Properties"
id: 5741410825239
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741410825239-Format-Line-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:20Z
---

# Format Line Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741397489431-Format-Legend-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741397528087-Format-Paper-Dialog-Box-Properties)

# Format Line Dialog Box Properties

You can use the Format Line dialog box to format the lines of a line chart. This topic describes the properties in the dialog box.

![Format Line dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905814510103/fmtln.gif)

**Depth**

Specify the depth properties of the chart lines.

* **Use Depth**  
   Select to make the lines visually three-dimensional.
  + **Depth**  
     Specify the depth of the lines, in inches.
  + **Depth Direction**  
     Specify the angle of the axis along the depth of the lines, in degrees.

**Static Data Label**

Specify the properties of the static data labels on the lines. 3D line charts do not support this property.

* **Show Static Data Label**  
   Select **true** to show the static data labels on the lines. Only when it is true can the following static data label properties work.
* **Data Label Type**  
   Select the display type for data values in the static data labels.
  + **percent**  
     Select to display the percentage of each line node to the total.
  + **value**  
     Select to display the value for each line node.
  + **value and percent**  
     Select to display the value and the percentage for each line node.
* **Position**  
   Specify the position of the static data labels on the lines.
  + **Autofit**  
     Select to display the static data labels automatically.
  + **Top Center**  
     Select to display the static data labels on the upper center of the line nodes.
  + **Top Left**  
     Select to display the static data labels on the upper left of the line nodes.
  + **Top Right**  
     Select to display the static data labels on the upper right of the line nodes.
  + **Bottom Left**  
     Select to display the static data labels at the lower left of the line nodes.
  + **Bottom Center**  
     Select to display the static data labels at the lower center of the line nodes.
  + **Bottom Right**  
     Select to display the static data labels at the lower right of the line nodes.
* **Auto Arrange**  
   Line charts do not support this property.
* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741397489431-Format-Legend-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741397528087-Format-Paper-Dialog-Box-Properties)
