---
title: "Format Legend Dialog Box Properties"
id: 4405683643799
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683643799-Format-Legend-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:41Z
---

# Format Legend Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683642775-Format-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683644951-Format-Line-Dialog-Box-Properties)

# Format Legend Dialog Box Properties

You can use the Format Legend dialog box to format the legend of a chart. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Placement Tab Properties](#Placement)
* [Border Tab Properties](#Border)
* [Font Tab Properties](#Font)
* [Label Tab Properties](#Label)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the chart legend.

![Format Legend dialog box - General](https://devnet.logianalytics.com/hc/article_attachments/4420461706903/fmtlgnd_gnrl.gif)

**Name**

Specify the display name of the chart legend.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**X**

Specify the X coordinate of the chart legend. This property takes effect when you select the Placement property of customized on the Placement tab.

**Y**

Specify the Y coordinate of the chart legend. This property takes effect when you select the Placement property of customized on the Placement tab.

**Width**

Specify the width of the chart legend. This property takes effect when you select the Placement property of customized on the Placement tab.

**Height**

Specify the height of the chart legend. This property takes effect when you select the Placement property of customized on the Placement tab.

**Fill Type**

Select the type for filling the chart legend.

**Color**

Specify the background color of the chart legend.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Transparency**

Specify the transparency of the legend background color.

**Show Value**

Select **true** to show the value of each legend.

**Show Percent**

Select **true** to show the percentage of each legend.

**Show Tips**

Select **true** to show the corresponding data information when you hover over a target in the chart legend.

## Placement Tab Properties

Specify the position-related properties of the chart legend.

![Format Legend dialog box - Placement](https://devnet.logianalytics.com/hc/article_attachments/4420453640471/fmtlgnd_place.gif)

**Placement**

Specify the position of the legend to be left, right, top, bottom, or customized by dragging in the chart manually.

**Secondary Placement**

Specify the position of the legend based on the Placement property.

**Label Vertical Spacing**

Specify the vertical distance between two adjacent legend labels.

**Label Horizontal Spacing**

Specify the horizontal distance between two adjacent legend labels.

**Top Margin**

Specify the distance between the legend labels and the top border of the legend.

**Bottom Margin**

Specify the distance between the legend labels and the bottom border of the legend.

**Left Margin**

Specify the distance between the legend labels and the left border of the legend.

**Right Margin**

Specify the distance between the legend labels and the right border of the legend.

**Reverse Labels**

Select **true** to arrange the legend labels in a reverse order.

## Border Tab Properties

Specify the border properties of the chart legend.

![Format Legend dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420453640727/fmtlgnd_border.gif)

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

Specify the font properties of the chart legend labels. See [Font Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683642775-Format-Label-Dialog-Box-Properties#Font).

![Format Legend dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4420453640983/fmtlgnd_font.gif)

## Label Tab Properties

Specify the text of the legend entry labels. This tab is available when the legend entry labels show the values of the field that displays on the category/series axis of the chart.

![Format Legend dialog box - Label](https://devnet.logianalytics.com/hc/article_attachments/4420447318167/fmtlgnd_lbl.gif)

**Auto**

Select if you want the legend entry labels to display the values of the category/series field. You can clear it to customize the label text.

**Label Text**

Specify the text of the legend entry labels. Type the label text manually, or select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif) and select a field from the list to use its values as the label text.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/4405690506135-Format-Platform-Dialog-Box-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683642775-Format-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683644951-Format-Line-Dialog-Box-Properties)
