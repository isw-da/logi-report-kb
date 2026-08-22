---
title: "Format Donut Dialog Box Properties"
id: 1500009772301
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772301-Format-Donut-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:15Z
---

# Format Donut Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744422-Format-Dial-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties)

# Format Donut Dialog Box Properties

You can use the Format Donut dialog box to format the donuts of a donut chart. This topic describes the options in the dialog box.

![Format Donut dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885582743/fmtdnt.gif)

**Static Data Label**

Specifies the properties of the static data labels on the donuts.

* **Show Static Data Label**  
   Specifies whether to show the static data labels on the donuts. Only when it is true can the following static data label related properties work.
* **Data Label Type**  
   Specifies in which way to display the data values in the static data labels.
  + **category name**  
     Shows the category name for each donut section.
  + **category name, percent**   
     Shows the category name and percentage for each donut section.
  + **category name, value**   
     Shows the category name and value for each donut section.
  + **category name, value, percent**   
     Shows the category name, value, and percentage for each donut section.
  + **percent**  
     Shows the percentage of each donut section to the total.
  + **value**  
     Shows the value for each donut section.
  + **value and percent**  
     Shows the value and the percentage for each donut section.
* **Position**  
   Specifies the position of the static data labels on the donuts.
  + **Autofit**  
     If selected, the static data labels will be displayed automatically.
  + **Sticker**  
     If selected, the static data labels will be displayed beside the donut sections.
  + **Slim Leg**  
     If selected, the static data labels will be displayed beside the donut sections and pointed by thin lines.
    - **Line Color**  
       Specifies the color of the thin lines that are used to point to the static data labels.
  + **Best Fit**  
     If selected, the static data labels will be displayed at the best fit position automatically.
  + **On Slices**  
     If selected, the static data labels will be displayed on the donut sections (slices).
* **Auto Scale in Number**

  Specifies whether to
  automatically scale the values that are of the Number data type when the values fall into the two ranges:

  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).
* **Show Truncated Label**  
  Select this option to truncate labels that would go beyond the boundaries on a donut chart paper instead of them being hidden altogether - the default behavior. Logi Report displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name, when you select this option. The truncated labels are also affected if you select the Position option of Best Fit (as seen above); where the label is cut off from the left or the right depending on the position of the label.
* **Show Donut Name**  
   Specifies whether to show the names of the donuts.
* **Donut Hole**  
   Specifies the percentage the hole's thickness will take from the total radius of the pie circle.

**KPI Value**

Specifies the properties for the KPI values of the donuts.

* **Show KPI Value**  
   Specifies whether to show KPI value for each donut.
  + **KPI Value**  
     Specifies the KPI value to display on each donut. By default, the total value of each donut will be used as the KPI value. If you want to customize the value, clear Auto and type a value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880161431/btn_fmla.gif) and select a formula or summary from the drop-down list to use its value as the KPI value.
  + **Position**  
     Specifies the position of the KPI value at the center, top, bottom of each donut or customized which enables setting the X and Y properties to change the position.

**Graph Border**

Specifies the properties for the border of the donuts.

* **Show Border**  
   Specifies whether to show the border of the donuts. When it is selected, the other border properties will be enabled.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744422-Format-Dial-Gauge-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties)
