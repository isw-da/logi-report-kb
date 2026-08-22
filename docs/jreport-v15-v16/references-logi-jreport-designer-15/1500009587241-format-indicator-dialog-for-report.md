---
title: "Format Indicator Dialog (for Report)"
id: 1500009587241
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587241-Format-Indicator-Dialog-for-Report
updated_at: 2021-07-24T05:55:14Z
---

# Format Indicator Dialog (for Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587221-Format-Indicator-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565882-Format-Label-Dialog)

# Format Indicator Dialog (for Report)

The Format Indicator dialog for page/web report appears when you double-click an indicator of a chart in a page report or web report, or right-click it and then select Format Indicator from the shortcut menu. It enables you to [format the indicators in an indicator chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563082-Formatting-the-Indicators), and consists of the following tabs:

* [General](#General)
* [Border](#Border)
* [Data Label](#Data)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

The options in the tab differ with value types of the indicator chart: [Boolean type](#Boolean), or [String/Numeric type](#String).

### General tab for Boolean type values

Specifies the general properties of the indicators. [See the tab](javascript:%20void(null)).

![Format Indicator dialog - General - Boolean](https://devnet.logianalytics.com/hc/article_attachments/4404893898263/fmtindctr_gnrl_boln.gif)

**Option**

* **Left Margin**  
   Specifies the gap between the left labels and the left indicators, in pixels.
* **Top Margin**  
   Specifies the gap between the top labels and the top indicators, in pixels.
* **Range Radius**  
   Specifies the relative size of an indicator in a percentage of the total indicator size.

**Color Range**

Specifies different colors or images to fill the indicators.

* **Show Image**  
   Specifies whether to use images instead of colors to represent the values. If checked, you can select an image to represent a specified value, and the color setting in the Color column will be ignored.
* **Value**  
  Lists the value for the indicator chart.
* **Color**  
   Specifies the color schema for the value. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette).
* **Image**  
   Specifies the image to represent the value.
* **Name**  
   Specifies the name of the value.

**Show Category Label**

Specifies whether to show the category labels for the indicators. The label displays the category value each indicator represents.

### General tab for String/Numeric type values

Specifies the general properties of the indicators. [See the tab](javascript:%20void(null)).

![Format Indicator dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404889349143/fmtindctr_gnrl_numeric.gif)

**Option**

Specifies the options for the indicators.

* **Left Margin**  
   Specifies the gap between the left labels and the left indicators, in pixels.
* **Top Margin**  
   Specifies the gap between the top labels and the top indicators, in pixels.
* **Range Radius**  
   Specifies the relative size of an indicator in a percentage of the total indicator size.

**Value**

Specifies the maximum and minimum values displayed on the chart. Not supported on indicator chart.

**Color Range**

Specifies different colors or images to fill the indicators.

* **Show Image**   
   Specifies whether to use images instead of colors to represent the value ranges. If checked, the color setting in the Color column will be ignored.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new value range.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected value range.

* **Minimum**  
   Specifies the minimum value of the range.
* **Maximum**  
   Specifies the maximum value of the range.
* **Color**  
   Specifies the color schema of the value range. Select in the color cell to customize the color on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette).
* **Image**  
   Specifies the image to represent the value range.
* **Name**  
   Specifies the name of the value range.
* **Others**  
   Specifies the properties for values that do not fall into any of the ranges you have defined.
  + **Name**  
     Specifies the name for the values.
  + **Color**  
     Specifies the color for the values. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
  + **Image**  
     Specifies the image to represent the values.

**Show Category Label**

Specifies whether to show the category labels for the indicators. The label displays the category value each indicator represents.

## Border

Specifies the properties for border of the indicators, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector and the indicators are not represented by images. [See the tab](javascript:%20void(null)).

![Format Indicator dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889349399/fmtindctr_brdr.gif)

**Style**

Specifies the style of the indicators.

**Line Style**

Specifies the line style to apply to the border.

**Thickness**

Specifies the thickness of the border, in pixels.

**Color**

Specifies the color of the border.

**Transparency**

Specifies the transparency for color of the border.

**Sample**

Displays a preview sample of your selection.

## Data Label

Specifies the properties for data labels on the indicators. [See the tab](javascript:%20void(null)).

![Format Indicator dialog - Format Indicator dialog - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404889349655/fmtindctr_dtlbl.gif)

**Static Data Label**

Specifies properties of the static data labels. Not supported on indicator chart.

**Font**

Specifies the font format of text in the data labels.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**  
   Specifies the font color of the text.
* **Transparency**  
  Specifies the transparency of the text.
* **Rotation**  
   Specifies the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
   Specifies the gradient of the text.

**Effects**

Specifies the special effects of text in the data labels.

* **Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
   Specifies the style of the horizontal line with which the text is struck through. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned.
* **Superscript**  
   Raises the text above the baseline and changes the text to a smaller font size, if a smaller size is available.
* **Embossed**  
   Makes the text appear to be raised off the page in relief.
* **Outlined**  
   Displays the inner and outer borders of each character.
* **Subscript**  
   Lowers the text below the baseline and changes the text to a smaller font size, if a smaller size is available.
* **Engraved**  
   Makes the text appear to be imprinted or pressed into the page.
* **Shadowed**  
   Adds a shadow beneath and to the right of the text.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587221-Format-Indicator-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565882-Format-Label-Dialog)
