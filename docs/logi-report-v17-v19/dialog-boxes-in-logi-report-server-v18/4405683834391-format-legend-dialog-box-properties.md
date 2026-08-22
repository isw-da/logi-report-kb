---
title: "Format Legend Dialog Box Properties"
id: 4405683834391
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683834391-Format-Legend-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:19Z
---

# Format Legend Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683833367-Format-KPI-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690582935-Format-Line-Dialog-Box-Properties)

# Format Legend Dialog Box Properties

This topic describes how you can use the Format Legend dialog box to format the legend of a chart. Server displays the dialog box when you right-click a chart and select **Format Legend** (unavailable to org chart and gauge bubble chart) from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Placement Tab Properties](#Placement)
* [Border Tab Properties](#Border)
* [Font Tab Properties](#Font)
* [Label Tab Properties](#Label)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the Format Legend dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the chart legend.

![Format Legend dialog - General](https://devnet.logianalytics.com/hc/article_attachments/4420447233303/fmtlgnd_gnrl.gif)

**Name**

Specifies the display name of the chart legend.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Width**

Specifies the width of the chart legend.

**Height**

Specifies the height of the chart legend.

**Fill Type**

Specifies the type for filling the chart legend. It can be one of the following: None, Color, Texture, Gradient and Image. If Gradient or Image is selected, you can specify the gradient or image by the property Fill Type in the Background category of the chart legend in the Inspector.

**Color**

Indicates the background color of the chart legend. It takes effect only when Fill Type in this tab is Color.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Transparency**

Specifies the transparency of the legend background color.

**Show Value**

Specifies whether to show the value of each legend.

**Show Percent**

Specifies whether to show the percentage of each legend.

**Show Tips**

Specifies whether to show the corresponding data information when the mouse pointer points at a target in the chart legend.

**Show Scrollbar**

Specifies whether to show a scrollbar on the legend to fully view the legend contents when the contents do not fit into the legend.

**Truncate**

Specifies whether to truncate the legend entry label text when the text overflow the labels.

## Placement Tab Properties

This tab shows the position-related information of the chart legend.

![Format Legend dialog - Placement](https://devnet.logianalytics.com/hc/article_attachments/4420461641367/fmtlgnd_place.gif)

**Placement**

Specifies the position of the legend in the platform.

**Secondary Placement**

Specifies the position of the legend on the basis of the Placement property.

**Top Margin**

Specifies the distance between the legend labels and the top border of the legend.

**Bottom Margin**

Specifies the distance between the legend labels and the bottom border of the legend.

**Left Margin**

Specifies the distance between the legend labels and the left border of the legend.

**Right Margin**

Specifies the distance between the legend labels and the right border of the legend.

**Label Vertical Spacing**

Specifies the vertical distance between two adjacent legend labels.

**Label Horizontal Spacing**

Specifies the horizontal distance between two adjacent legend labels.

**Reverse Labels**

Specifies whether to arrange the legend labels in a reverse order.

## Border Tab Properties

This tab shows information about borders of the chart legend.

![Format Legend dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4420461641623/fmtlgnd_border.gif)

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

Specify the font properties of the chart legend.

![Format Legend dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4420461641879/fmtlgnd_font.gif)

**Font**

Specifies the font face for the legend labels.

**Size**

Specifies the font size for the legend labels.

**Fill Type**

Specifies the fill type for the legend labels. It can be one of the following: None, Color, Texture, and Gradient. If Gradient is selected, you can specify the gradient or image by the property Fill Type in the Label category of the chart legend in the Inspector.

**Color**

Specifies the color for the legend labels. It takes effect only when Fill Type in this tab is Color.

**Transparency**

Specifies the transparency for the legend labels, in percent.

**Font Style**

Specifies the font style of the text. It can be one of the following: Plain, Bold, Italic and Bold Italic.

**Font Rotation**

Specifies the rotation angle of each legend label around its center, in degrees.

**Word Wrap**

Specifies whether to enable word wrapping for the label text.

## Label Tab Properties

Specifies the text of the legend entry labels. This tab is available only when the legend entry labels show the values of the field displayed on the category or series axis of the chart.

![Format Legend dialog - Label](https://devnet.logianalytics.com/hc/article_attachments/4420453571223/fmtlgnd_lbl.gif)

**Auto**

If selected, the legend entry labels display values of the category/series field. You can clear it to customize the label text.

* **Label Text**  
   Specifies the text of the legend entry labels. Type the desired label text manually or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif) to select a field from the drop-down list to use its values as the label text.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4411830859799-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683833367-Format-KPI-Label-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690582935-Format-Line-Dialog-Box-Properties)
