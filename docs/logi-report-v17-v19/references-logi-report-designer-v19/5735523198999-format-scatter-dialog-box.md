---
title: "Format Scatter Dialog Box"
id: 5735523198999
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735523198999-Format-Scatter-Dialog-Box
updated_at: 2022-11-02T04:18:01Z
---

# Format Scatter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529772183-Format-Rectangle-Title-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735529792151-Format-Series-Z-Axis-Dialog-Box)

# Format Scatter Dialog Box

You can use the Format Scatter dialog box to [format the scatter in a scatter chart](https://devnet.logianalytics.com/hc/en-us/articles/5735527353239-Formatting-Scatter-Chart). This topic describes the options in the dialog box.

Designer display the Format Scatter dialog box when you right-click a marker in a scatter chart and select Format Scatter from the shortcut menu, or double-click a marker in a scatter chart.

This dialog box contains the following tabs:

* [General Tab](#General)
* [Fill Tab](#Fill)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify general properties of the scatter chart.

![Format Scatter - General](https://devnet.logianalytics.com/hc/article_attachments/9898480099351/fmtsctr_gnrl.gif)

**Layout**

You can specify the layout of the scatter in this box.

* **No line**  
  Select if you do not want to use lines to connect the markers in the scatter chart.
* **Straight Line**  
  Select to use straight lines to connect the markers in the scatter chart.
* **Curved Line**  
  Select to use curved lines to connect the markers in the scatter chart.

**Line**

You can specify the property of the lines that connect the markers in the scatter chart in this box.

* **Thickness**  
   Specify the thickness of the lines, in pixels.

**Node**

You can specify properties of the markers in the scatter chart in this box.

* **Style**  
  Select the style of the markers.
* **Width**  
  Specify the width of the markers, in pixels.
* **Height**  
  Specify the height of the markers, in pixels.

## Fill Tab

Use this tab to specify the fill pattern of the scatter markers.

![Format Scatter - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898463018135/fmtsctr_fill.gif)

**Color**

Specify the color of the selected scatter markers in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency of the color.

**Self Settings**

Select to apply the color pattern to the scatter markers themselves only. When this option is cleared, Designer synchronizes the color pattern that you specify here with the [Pattern List](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#Pattern) property of the chart in the Report Inspector, which data markers of other subtypes can also apply if the chart is a combo chart.

**Color List**

Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522093463-Color-List-Dialog-Box) to modify the color pattern for scatter markers in the same data series respectively.

**Sample**

This box displays a preview sample based on your selections.

## Data Label Tab

Designer does not support displaying data labels in scatter charts, so you can skip this tab.

![Format Scatter - Data Panel](https://devnet.logianalytics.com/hc/article_attachments/9898463022871/fmtsctr_data.gif)

## Hint Tab

Use this tab to specify properties for the hint of the scatter markers.

![Format Scatter - Hint](https://devnet.logianalytics.com/hc/article_attachments/9898463028887/fmtsctr_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint that fall into the two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/5735545992599-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Customize Chart Value Names**

Select to customize the names of the fields on the value axis which you want to display in the hint. By default, Designer applies the display names of the fields in the hint to label the values which may be not intuitive to users. You can select the option and select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to customize the names in the [Customize Chart Value Names dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565355927-Customize-Chart-Value-Names-Dialog-Box) to help users better understand the values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735529772183-Format-Rectangle-Title-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735529792151-Format-Series-Z-Axis-Dialog-Box)
