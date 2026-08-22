---
title: "Format Legend Dialog Box Properties"
id: 1500009772381
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772381-Format-Legend-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:13Z
---

# Format Legend Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744442-Format-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744462-Format-Line-Dialog-Box-Properties)

# Format Legend Dialog Box Properties

You can use the Format Legend dialog box to format the legend of a chart. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Placement Tab Properties](#Placement)
* [Border Tab Properties](#Border)
* [Font Tab Properties](#Font)
* [Label Tab Properties](#Label)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the chart legend.

![Format Legend dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4404880520087/fmtlgnd_gnrl.gif)

**Name**

Specifies the display name of the chart legend.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**X**

Specifies the X coordinate of the chart legend. Available only when the Placement option in the Placement tab is set to customized.

**Y**

Specifies the Y coordinate of the chart legend. Available only when the Placement option in the Placement tab is set to customized.

**Width**

Specifies the width of the chart legend. Available only when the Placement option in the Placement tab is set to customized.

**Height**

Specifies the height of the chart legend. Available only when the Placement option in the Placement tab is set to customized.

**Fill Type**

Specifies the type for filling the chart legend.

**Color**

Indicates the background color of the chart legend.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Transparency**

Specifies the transparency of the legend background color.

**Show Value**

Specifies whether to show the value of each legend.

**Show Percent**

Specifies whether to show the percentage of each legend.

**Show Tips**

Specifies whether to show the corresponding data information when the mouse pointer points at a target in the chart legend.

## Placement Tab Properties

This tab shows the position-related information of the chart legend.

![Format Legend dialog - Placement](https://devnet.logianalytics.com/hc/article_attachments/4404880520599/fmtlgnd_place.gif)

**Placement**

Specifies the position of the legend to be left, right, top, bottom or customized by dragging in the chart manually.

**Secondary Placement**

Specifies the position of the legend on the basis of the Placement property.

**Label Vertical Spacing**

Specifies the vertical distance between two adjacent legend labels.

**Label Horizontal Spacing**

Specifies the horizontal distance between two adjacent legend labels.

**Top Margin**

Specifies the distance between the legend labels and the top border of the legend.

**Bottom Margin**

Specifies the distance between the legend labels and the bottom border of the legend.

**Left Margin**

Specifies the distance between the legend labels and the left border of the legend.

**Right Margin**

Specifies the distance between the legend labels and the right border of the legend.

**Reverse Labels**

Specifies whether to arrange the legend labels in a reverse order.

## Border Tab Properties

This tab shows information about borders of the chart legend.

![Format Legend dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404880521111/fmtlgnd_border.gif)

**Line Style**

Specifies the line style of the legend borders.

**Border Type**

Specifies the type of the legend borders.

**Color**

Specifies the color of the legend borders.

**Transparency**

Specifies the color transparency of the legend borders.

**Thickness**

Specifies the thickness of the legend borders.

## Font Tab Properties

This tab shows the font-related information of the chart legend.

![Format Legend dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404880522391/fmtlgnd_font.gif)

**Font**

Specifies the font face of the legend labels.

**Size**

Specifies the font size of the legend labels.

**Fill Type**

Specifies the fill type of the legend labels.

**Color**

Specifies the color of the legend labels.

**Transparency**

Specifies the color transparency of the legend labels.

**Font Style**

Specifies the font style of the legend labels.

**Font Effect**

Specifies the font effect of the legend labels.

**Font Underline**

Specifies the style of the line under the legend labels.

**Font Strikeout**

Specifies whether to attach a strikeout line to the legend labels.

**Font Rotation**

Specifies the rotation angle of each legend label around its center, in degrees.

**Font Shearing**

Specifies the shearing transformation of each legend label around its center, in degrees.

**Word Wrap**

Specifies whether to enable word wrapping for the label text.

## Label Tab Properties

Specifies the text of the legend entry labels. This tab is available only when the legend entry labels show the values of the field displayed on the category or series axis of the chart.

![Format Legend dialog - Label](https://devnet.logianalytics.com/hc/article_attachments/4404880522775/fmtlgnd_lbl.gif)

**Auto**

If selected, the legend entry labels display values of the category/series field. You can clear it to customize the label text.

* **Label Text**  
   Specifies the text of the legend entry labels. Type the desired label text manually or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) to select a field from the drop-down list to use its values as the label text.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009772421-Format-Platform-Dialog-Box-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744442-Format-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744462-Format-Line-Dialog-Box-Properties)
