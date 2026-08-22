---
title: "Format Pie Dialog Box Properties"
id: 5741424579095
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741424579095-Format-Pie-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:18Z
---

# Format Pie Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741397528087-Format-Paper-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties)

# Format Pie Dialog Box Properties

You can use the Format Pie dialog box to format the pies of a pie chart. This topic describes the properties in the dialog box.

![Format Pie dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905814335383/fmtpie.gif)

**Static Data Label**

Specify the properties of the static data labels on the pies.

* **Show Static Data Label**  
   Select **true** to show the static data labels on the pies. Only when it is true can the following static data label properties work.
* **Data Label Type**  
   Select the display type for the data values in the static data labels.
  + **category name**  
     Select to display the category name for each pie section.
  + **category name, percent**   
     Select to display the category name and percentage for each pie section.
  + **category name, value**   
     Select to display the category name and value for each pie section.
  + **category name, value, percent**   
     Select to display the category name, value, and percentage for each pie section.
  + **percent**  
     Select to display the percentage of each pie section to the total.
  + **value**  
     Select to display the value for each pie section.
  + **value and percent**  
     Select to display the value and the percentage for each pie section.
* **Position**  
   Select the position of the static data labels on the pies.
  + **Autofit**  
     Select to display the static data labels automatically.
  + **Sticker**  
    Select to display the static data labels beside the pie sections.
  + **Slim Leg**  
     Select to display the static data labels beside the pie sections with thin lines.
    - **Line Color**  
      Specify the color of the thin lines that point to the static data labels.
  + **Best Fit**  
     Select to display the static data labels at the best fit position automatically.
  + **On Slices**  
     Select to display the static data labels on the pie sections (slices).
* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale).
* **Show Truncated Label**  
  Select to truncate labels that would go beyond the boundaries on a pie chart paper instead of them being hidden altogether - the default behavior. Logi Report displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name, when you enable this property. The truncated labels are also affected if you select the Position property of Best Fit (as seen above); where the label is cut off from the left or the right depending on the position of the label.
* **Show Pie Name**Specify **true** to show the names of the pies.

**KPI Value**

Specify the properties for the KPI values of the pies.

* **Show KPI Value**  
   Select to show KPI value for each pie and enable these properties:
  + **KPI Value**  
     Specify the KPI value to display on each pie. By default, Server uses the total value of each pie as the KPI value. If you want to customize the value, clear **Auto**. Then type a value in the text box, or select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905631361687/btn_fmla.gif) and select a formula or summary from the list to use its value as the KPI value.
  + **Position**  
     Specify the position of the KPI value at the center, top, or bottom of each pie, or select **customized** if you want to set the X and Y properties to change the position.

**Graph Border**

Specify the properties for the border of the pies.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741397528087-Format-Paper-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties)
