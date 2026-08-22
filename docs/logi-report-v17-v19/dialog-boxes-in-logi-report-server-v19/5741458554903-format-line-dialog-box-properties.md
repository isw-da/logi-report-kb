---
title: "Format Line Dialog Box Properties"
id: 5741458554903
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741458554903-Format-Line-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:29Z
---

# Format Line Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741458528663-Format-Legend-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741450401175-Format-Org-Line-Dialog-Box-Properties)

# Format Line Dialog Box Properties

This topic describes how you can use the Format Line dialog box to format the lines of a line chart. Server displays the dialog box when you right-click a line chart and select **Format Graph** from the shortcut menu.

![Format Line dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905720154263/fmtln.gif)

**Depth**

Specify the depth properties of the chart lines.

* **Use Depth**  
   Select **true** if you want to make the lines visually three-dimensional.
  + **Depth**  
     Specify the depth of the lines, in inches.
  + **Direction**  
     Specify the angle of the axis along the depth of the lines, in degrees.

**Static Data Label**

Specify the properties of the static data labels on the lines.

* **Show Static Data Label**  
   Select **true** if you want to show the static data labels on the lines. Only when it is true can the following static data label properties work.
* **Style**  
   Select the display type for data values in the static data labels.
  + **Value**  
    Select to display the value for each line node.
  + **Percent**  
     Select to display the percentage of each line node to the total.
  + **Value and Percent**  
     Select to display the value and the percentage for each line node.
* **Position**  
   Select the position of the static data labels on the lines.
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

  The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

**Hint**

Specify the data marker hint properties.

* **Show Category and Series**
Select to include the category and series values in the data marker hint.* **Auto Scale in Number**  
  Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:
  + When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

  The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).
* **Customize Chart Value Names**  
  Select if you want to customize the names of the fields used as the values in the chart. Server uses the customized names in the data marker hint. Then select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) to open the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457709079-Customize-Chart-Value-Names-Dialog-Box-Properties).

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741458528663-Format-Legend-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741450401175-Format-Org-Line-Dialog-Box-Properties)
