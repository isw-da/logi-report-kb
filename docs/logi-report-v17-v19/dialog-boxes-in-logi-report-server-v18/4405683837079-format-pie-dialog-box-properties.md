---
title: "Format Pie Dialog Box Properties"
id: 4405683837079
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683837079-Format-Pie-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:20Z
---

# Format Pie Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690584727-Format-Paper-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690585751-Format-Platform-Dialog-Box-Properties)

# Format Pie Dialog Box Properties

This topic describes how you can use the Format Pie dialog box to format the pies of a pie chart. Server displays the dialog box when you right-click a pie chart and select **Format Graph** from the shortcut menu.

![Format Pie dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420447229207/fmtpie.gif)

**Pie**

Specify the properties of the pies.

* **Show Pie Name**Select **true** if you want to show the names of the pies.

**Static Data Label**

Specify the properties of the static data labels on the pies.

* **Show Static Data Label**  
   Select **true** if you want to show the static data labels on the pies. Only when it is true can the following static data label properties work.
* **Style**  
   Select the display type for data values in the static data labels.
  + **Value**  
    Select to display the value for each pie section.
  + **Category Name**  
    Select to display the category name for each pie section.
  + **Percent**  
     Select to display the percentage of each pie section to the total.
  + **Value and Percent**  
     Select to display the value and the percentage for each pie section.
  + **Category Name, Value**   
    Select to display the category name and value for each pie section.
  + **Category Name, Percent**   
     Select to display the category name and percentage for each pie section.
  + **Category Name, Value, Percent**   
    Select to display the category name, value, and percentage for each pie section.
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

  The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).
* **Show Truncated Label**  
  Select to truncate labels that would go beyond the boundaries on a pie chart paper instead of them being hidden altogether - the default behavior. Logi Report displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name, when you select this property. The truncated labels are also affected if you select the Position property of Best Fit (as seen above); where the label is cut off from the left or the right depending on the position of the label.

**KPI Value**

Specify the properties for the KPI values of the pies.

* **Show KPI Value**  
   Select to show KPI value for each pie and enable the two properties.
  + **KPI Value**  
     Specify the KPI value to display on each pie. By default, Server uses the total value of each pie as the KPI value. If you want to customize KPI the value, clear **Auto**, then type a value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447072407/btn_fmla.gif) and select a formula or summary from the value list to use its value as the KPI value.
  + **Position**  
     Select the position of the KPI value at the center, top, bottom of each pie or customized which enables setting the X and Y properties to change the position.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690584727-Format-Paper-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690585751-Format-Platform-Dialog-Box-Properties)
