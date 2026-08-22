---
title: "Format KPI Label Dialog Box Properties"
id: 1500009772361
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772361-Format-KPI-Label-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:15Z
---

# Format KPI Label Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744442-Format-Label-Dialog-Box-Properties)

# Format KPI Label Dialog Box Properties

You can use the Format KPI Label dialog box to format the KPI value labels in a pie chart. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Format Tab Properties](#Format)

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

Specifies the general properties of the labels.

![Format KPI Label dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404880523799/fmtkpilbl_gnrl.gif)

**Option**

Specifies the size and position of the labels.

* **Width**  
   Specifies the width of the labels, in inches.
* **Height**  
   Specifies the height of the labels, in inches.
* **X**  
   Specifies the horizontal coordinate of the top left corner of the labels, relative to their parent container.
* **Y**  
   Specifies the vertical coordinate of the top left corner of the labels, relative to their parent container.
* **Alignment**  
   Specifies the alignment of the label text.
* **Word Wrap**  
   Specifies whether to enable the word wrap function for the label text.

**Fill**

Specifies the color and transparency of the labels.

* **Color**  
   Specifies the color to fill the labels. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.
* **Transparency**  
   Specifies the transparency to fill the labels.

**Border**

Specifies the properties for borders of the labels.

* **Line Style**  
   Specifies the line style to apply to the border.
* **Border Type**  
   Specifies the type of the border.
* **Color**  
   Specifies the color of the border. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Orientation**

* **Angle**  
   Specifies the rotation angle of the labels.

## Font Tab Properties

Specifies the properties for font of the label text.

![Format KPI Label dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404880524439/fmtkpilbl_font.gif)

**Font**

Lists all the available font faces that can be selected to apply to the text.

**Size**

Specifies the font size of the text.

**Fill Type**

Specifies the fill type of the text. It can be one of the following: none, color, texture, and gradient.

**Color**

Specifies the color of the text. It takes effect only when Fill Type in this tab is color.

**Font Style**

Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.

**Transparency**

Specifies the color transparency of the text.

## Format Tab Properties

Specifies the data format of the label text.

![Format KPI Label dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404880525079/fmtkpilbl_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009775121-Data-Format-Dialog-Box-Properties#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale). When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

**Sample**

Displays a preview sample of your selection.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the label.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772321-Format-Gauge-Label-Dialog-Box-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744442-Format-Label-Dialog-Box-Properties)
