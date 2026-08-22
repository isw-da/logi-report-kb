---
title: "Format Paper Dialog Box Properties"
id: 4405683645975
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683645975-Format-Paper-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:40Z
---

# Format Paper Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683644951-Format-Line-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683646999-Format-Pie-Dialog-Box-Properties)

# Format Paper Dialog Box Properties

You can use the Format Paper dialog box to format the paper of a chart. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Coordinate Tab Properties](#Coordinate)
* [Threshold Line Tab Properties](#ThresholdLine)
* [Axis Z Tab Properties](#AxisZ)
* [Bullet Tab Properties](#Bullet)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) Some tabs may not be applicable for certain chart types.

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the chart paper.

![Format Paper dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420461706647/fmtpapr_gnrl.gif)

**Name**

Specify the display name of the chart paper.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**X**

Specify the X coordinate of the chart paper.

**Y**

Specify the Y coordinate of the chart paper.

**Width**

Specify the width of the chart paper.

**Height**

Specify the height of the chart paper.

**Fill Type**

Select the type for filling the chart paper.

**Color**

Specify the background color of the chart paper.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Transparency**

Specify the transparency of the chart paper background color.

**Show Tips**

Select **true** to show the corresponding data information when you hover over a target in the chart paper.

**Show Wall**

Select **true** to show the chart wall.

**Show Floor**

Select **true** to show the chart floor.

## Border Tab Properties

Specify the border properties of the chart paper.

![Format Paper dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420447317655/fmtpapr_border.gif)

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

## Coordinate Tab Properties

You can use this tab to view and configure properties of the coordinates.

![Format Paper dialog box - Coordinate tab](https://devnet.logianalytics.com/hc/article_attachments/4420453639447/fmtpapr_crdnt.gif)

**Scale X**

Specify the scaling ratio for the X axis.

**Scale Y**

Specify the scaling ratio for the Y axis.

**Scale Z**

Specify the scaling ratio for the Z axis.

**Angle X**

Specify the rotation angle around the X axis. This property applies to 3D charts and pie charts.

**Angle Y**

Specify the rotation angle around the Y axis. This property applies to 3D charts and pie charts.

**Angle Z**

Specify the rotation angle around the Z axis. This property applies to 3D charts and pie charts.

**Perspective**

Type an integer to specify the perspective effect of the chart.

**Interactive**

Select **true** to make the chart interactive.

## Threshold Line Tab Properties

You can use this tab to view and configure properties of the threshold lines.

![Format Paper dialog box - Threshold Line tab](https://devnet.logianalytics.com/hc/article_attachments/4420447317911/fmtpapr_thrshdln.gif)

**Show Threshold Line1**

Select **true** to show the first threshold line.

**Threshold Value1**

Specify the value of the first threshold line.

**Threshold Line Color1**

Specify the color of the first threshold line.

**Show Threshold Line2**

Select **true** to show the second threshold line.

**Threshold Value2**

Specify the value of the second threshold line.

**Threshold Line Color2**

Specify the color of the second threshold line.

**Transparency**

Specify the color transparency of the threshold lines.

## Axis Z Tab Properties

You can use this tab to view and configure properties of the Z axis.

![Format Paper dialog box - Axis Z tab](https://devnet.logianalytics.com/hc/article_attachments/4420453639703/fmtpapr_axisz.gif)

**Show Axis Z**

Select **true** to show the Z axis.

**Placement**

Specify the position of the axis.

**Show Axis Label Tips**

Select **true** to display the complete label text when you hover over a label on the axis.

**Label Font Automatic Orientation**

Select **true** to adjust the rotation angle of the label text on the axis automatically according to the length of the label text, in degrees.

* If the text can completely display horizontally, the default rotation angle will be 0.
* If the text cannot completely display horizontally, the default rotation angle will be 30 anticlockwise. Server displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name.

**Angle**

Specify the rotation angle of the label text on the axis. This property takes effect when you select the Label Font Automatic Orientation property of false.

## Bullet Tab Properties

You can use this tab to view and configure properties of the bullets in a chart.

![Format Paper dialog box - Bullet tab](https://devnet.logianalytics.com/hc/article_attachments/4420453639959/fmtpapr_bullet.gif)

**Featured Measure Width**

Specify the width of the featured measures, measured in a percentage of the unit width. Type a numeric value to change the width.

**Comparative Measure Width**

Specify the width of the comparative measures, measured in a percentage of the unit width. Type a numeric value to change the width.

**Qualitative Ranges Width**

Specify the width of the qualitative ranges, measured in a percentage of the unit width. Type a numeric value to change the width.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683644951-Format-Line-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683646999-Format-Pie-Dialog-Box-Properties)
