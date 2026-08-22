---
title: "Format Gauge Label Dialog Box Properties"
id: 5741397400343
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741397400343-Format-Gauge-Label-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:17Z
---

# Format Gauge Label Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741402753303-Format-Donut-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741424509207-Format-KPI-Label-Dialog-Box-Properties)

# Format Gauge Label Dialog Box Properties

You can use the Format Gauge Label dialog box to format the group labels in a gauge chart (excluding bubble gauge chart). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Format Tab Properties](#Format)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the labels.

![Format Gauge Label dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9905776137239/fmtgaugelbl_gnrl.gif)

**Option**

Specify the size and position of the labels.

* **Width**  
   Specify the width of the labels, in inches.
* **Height**  
   Specify the height of the labels, in inches.
* **X**  
   Specify the horizontal coordinate of the upper-left corner of the labels, relative to their parent container. It takes effect when you have selected **Show Gauge Group Name** and set **Position** to **customized** on the Frame tab of the gauge's corresponding Format XXX Gauge dialog box.
* **Y**  
   Specify the vertical coordinate of the upper-left corner of the labels, relative to their parent container. It takes effect when you have selected **Show Gauge Group Name** and set **Position** to **customized** on the Frame tab of the gauge's corresponding Format XXX Gauge dialog box.
* **Alignment**  
   Select the alignment of the label text.
* **Word Wrap**  
   Select to enable the word wrap function for the label text.

**Fill**

Specify the color and transparency of the labels.

* **Color**  
   Specify the color to fill the labels. To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.
* **Transparency**  
   Specify the transparency of the color to fill the labels.

**Border**

Specify the properties for the borders of the labels.

* **Line Style**  
  Select the line style of the border.
* **Border Type**  
   Select the type of the border.
* **Color**  
   Specify the color of the border. To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.
* **Transparency**  
   Specify the transparency for the color of the border.
* **Thickness**  
   Specify the thickness of the border, in inches.

**Orientation**

* **Angle**  
   Specify the rotation angle of the labels.

## Font Tab Properties

Specify the font properties of the label text.

![Format Gauge Label dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/9905814937367/fmtgaugelbl_font.gif)

**Font**

Select the font face of the label text.

**Size**

Specify the font size of the label text.

**Fill Type**

Select the fill type of the label text: none, color, texture, or gradient.

**Color**

Specify the color of the label text. It takes effect when **Fill Type** on this tab is **color**.

**Transparency**

Specify the color transparency of the label text.

**Font Style**

Select the font style of the label text: plain, bold, italic, or bold italic.

## Format Tab Properties

Specify the data format of the labels.

![Format Gauge Label dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/9905776183831/fmtgaugelbl_fmt.gif)

**Category**

Select a category type to customize its format.

**Format**

Select a [format](https://devnet.logianalytics.com/hc/en-us/articles/5741457762839-Data-Format-Dialog-Box-Properties#DataFormat), and then select **Add** to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Server displays the properties of the format you select. If the formats listed in the **Format** box cannot meet your requirement, define the format in the **Properties** text box, and then select **Add** to add it as the format of the specified category.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/5741397555095-Format-Platform-Dialog-Box-Properties#AutoScale). When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Sample**

Server displays a preview sample of your settings.

**Stack**

Server displays all the formats you select for different categories.

**Add**

Select to add a format to the **Stack** box.

**Remove**

Select to remove a format from the **Stack** box.

**Apply**

Select to apply the specified format in the **Stack** box to the labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741402753303-Format-Donut-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741424509207-Format-KPI-Label-Dialog-Box-Properties)
