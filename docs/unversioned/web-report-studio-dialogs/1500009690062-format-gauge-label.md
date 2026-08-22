---
title: "Format Gauge Label"
id: 1500009690062
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009690062-Format-Gauge-Label
updated_at: 2021-11-03T06:57:22Z
---

# Format Gauge Label

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690042-Format-Donut)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690082-Format-Indicator)

# Format Gauge Label

The Format Gauge Label dialog enables you to format the gauge group labels. This dialog appears when you right-click on a gauge chart (excluding bubble gauge) and then select Format Gauge Label from the shortcut menu.

The dialog contains the following tabs: [General](#General), [Font](#Font) and [Format](#Format).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## General

Specifies the general properties of the labels.

![Format Gauge Label - General](https://devnet.logianalytics.com/hc/article_attachments/4412112596375/fmtgaugelbl_gnrl.gif)

**Option**

Specifies the size and position of the labels.

* **Width**  
   Specifies the width of the labels, in inches.
* **Height**  
   Specifies the height of the labels, in inches.
* **X**  
   Specifies the horizontal coordinate of the top left corner of the labels, relative to their parent container. It takes effect when the Show Gauge Group Name option is checked and Position is set to customized in the Frame tab of the gauge's corresponding Format XXX Gauge dialog.
* **Y**  
   Specifies the vertical coordinate of the top left corner of the labels, relative to their parent container. It takes effect when the Show Gauge Group Name option is checked and Position is set to customized in the Frame tab of the gauge's corresponding Format XXX Gauge dialog.
* **Alignment**  
   Specifies the alignment of the label text.
* **Word Wrap**  
   Specifies whether to enable the word wrap function for the label text.

**Fill**

Specifies the color and transparency of the labels.

* **Color**  
   Specifies the color to fill the labels. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range.
* **Transparency**  
   Specifies the transparency to fill the labels.

**Border**

Specifies the properties for borders of the labels.

* **Line Style**  
  Specifies the line style to apply to the border.
* **Border Type**  
   Specifies the type of the border.
* **Color**  
   Specifies the color of the border. To change the color, select the color indicator to select a new color from the color palette, or select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range.
* **Transparency**  
  Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Orientation**

* **Angle**  
   Specifies the rotation angle of the labels.

## Font

Specifies properties for font of the label text.

![Format Gauge Label - Font](https://devnet.logianalytics.com/hc/article_attachments/4412131447447/fmtgaugelbl_font.gif)

**Font**

Lists all the available font faces that can be selected to apply to the text.

**Size**

Specifies the font size of the text.

**Fill Type**

Specifies the fill type of the text. It can be one of the following: none, color, texture and gradient.

**Color**

Specifies the color of the text. It takes effect only when Fill Type in this tab is color.

**Font Style**

Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.

**Transparency**

Specifies the color transparency of the text.

## Format

Specifies the data format of the labels.

![Format Gauge Label - Format](https://devnet.logianalytics.com/hc/article_attachments/4412139552535/fmtgaugelbl_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009689742-Data-Format#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Specifies whether to
automatically scale the group labels that are of the Number data type when the label values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009718301-Chart#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example, the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Sample**

Displays a preview sample of your selection.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690042-Format-Donut)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690082-Format-Indicator)
