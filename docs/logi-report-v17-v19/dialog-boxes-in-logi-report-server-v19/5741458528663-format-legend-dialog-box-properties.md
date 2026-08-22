---
title: "Format Legend Dialog Box Properties"
id: 5741458528663
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741458528663-Format-Legend-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:27Z
---

# Format Legend Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445112215-Format-KPI-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741458554903-Format-Line-Dialog-Box-Properties)

# Format Legend Dialog Box Properties

This topic describes how you can use the Format Legend dialog box to format the legend of a chart. Server displays the dialog box when you right-click a chart and select **Format Legend** (unavailable to org charts and gauge bubble charts) from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Placement Tab Properties](#Placement)
* [Border Tab Properties](#Border)
* [Font Tab Properties](#Font)
* [Label Tab Properties](#Label)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the chart legend.

![Format Legend dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/9905731937175/fmtlgnd_gnrl.gif)

**Name**

Specify the display name of the chart legend.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Width**

Specify the width of the chart legend.

**Height**

Specify the height of the chart legend.

**Fill Type**

Specify the type for filling the chart legend. It can be one of the following: None, Color, Texture, Gradient, and Image. If you select Gradient or Image, you can specify the gradient or image by the Fill Type property in the Background category of the chart legend in the Inspector.

**Color**

Specify the background color of the chart legend. It takes effect only when Fill Type in this tab is Color.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range.

**Transparency**

Specify the transparency of the legend background color.

**Show Value**

Select if you want to show the value of each legend.

**Show Percent**

Select if you want to show the percentage of each legend.

**Show Tips**

Select if you want to show the corresponding data information when you hover over a target in the chart legend.

**Show Scrollbar**

Select if you want to show a scroll bar on the legend to fully view the legend contents when the contents do not fit into the legend.

**Truncate**

Select if you want to truncate the legend entry label text when the text overflow the labels.

## Placement Tab Properties

Specify the position-related properties of the chart legend.

![Format Legend dialog box - Placement](https://devnet.logianalytics.com/hc/article_attachments/9905731954967/fmtlgnd_place.gif)

**Placement**

Specify the position of the legend in the platform.

**Secondary Placement**

Specify the position of the legend on the basis of the Placement property.

**Top Margin**

Specify the distance between the legend labels and the top border of the legend.

**Bottom Margin**

Specify the distance between the legend labels and the bottom border of the legend.

**Left Margin**

Specify the distance between the legend labels and the left border of the legend.

**Right Margin**

Specify the distance between the legend labels and the right border of the legend.

**Label Vertical Spacing**

Specify the vertical distance between two adjacent legend labels.

**Label Horizontal Spacing**

Specify the horizontal distance between two adjacent legend labels.

**Reverse Labels**

Select if you want to arrange the legend labels in a reverse order.

## Border Tab Properties

Specify the border properties of the chart legend.

![Format Legend dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/9905731982743/fmtlgnd_border.gif)

**Line Style**

Select the line style of the border.

**Border Type**

Select the type of the border.

**Color**

Specify the color of the border.

**Transparency**

Specify the transparency for the color of the border.

**Thickness**

Specify the thickness of the border, in inches.

## Font Tab Properties

Specify the font properties of the chart legend.

![Format Legend dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/9905720270743/fmtlgnd_font.gif)

**Font**

Specify the font face for the legend labels.

**Size**

Specify the font size for the legend labels.

**Fill Type**

Specify the fill type for the legend labels. It can be one of the following: None, Color, Texture, and Gradient. If you select Gradient, you can specify the gradient or image by the Fill Type property in the Label category of the chart legend in the Inspector.

**Color**

Specify the color for the legend labels. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specify the transparency for the legend labels, in percent.

**Font Style**

Specify the font style of the text. It can be one of the following: Plain, Bold, Italic, and Bold Italic.

**Font Rotation**

Specify the rotation angle of each legend label around its center, in degrees.

**Word Wrap**

Select if you want to enable word wrapping for the label text.

## Label Tab Properties

Specify the text of the legend entry labels. This tab is available only when the legend entry labels show the values of the field displayed on the category or series axis of the chart.

![Format Legend dialog box - Label](https://devnet.logianalytics.com/hc/article_attachments/9905720284567/fmtlgnd_lbl.gif)

**Auto**

Select if you want the legend entry labels to display the values of the category/series field. You can clear **Auto** if you want to customize the label text.

* **Label Text**  
   Specify the text of the legend entry labels. Type the label text manually, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905615792535/btn_wbrpt_fmla.gif) and then select a field from the drop-down list to use its values as the label text.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741445112215-Format-KPI-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741458554903-Format-Line-Dialog-Box-Properties)
