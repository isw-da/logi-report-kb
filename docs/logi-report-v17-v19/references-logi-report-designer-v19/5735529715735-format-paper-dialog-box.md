---
title: "Format Paper Dialog Box"
id: 5735529715735
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735529715735-Format-Paper-Dialog-Box
updated_at: 2022-11-02T04:17:56Z
---

# Format Paper Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735509343767-Format-Line-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735542973719-Format-Pattern-Dialog-Box)

# Format Paper Dialog Box

You can use the Format Paper dialog box to [format the paper of a chart](https://devnet.logianalytics.com/hc/en-us/articles/5735564051223-Formatting-Chart-Paper). This topic describes the options in the dialog box.

Designer displays the Format Paper dialog box when you right-click any chart element and select Format Paper from the shortcut menu, or double-click the paper of a chart.

This dialog box contains the following tabs:

* [General Tab](#General) (for 2-D charts)
* [Rotation Tab](#Rotation) (for 3-D charts)
* [Fill Tab](#Fill)
* [Border Tab](#Border)

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

Designer displays the General tab when the chart is a 2-D chart. You can use it to specify general properties of the chart paper.

![Format Paper - General](https://devnet.logianalytics.com/hc/article_attachments/9898463203095/fmtpapr_gnrl.gif)

**Scale X**

Specify to scale up or down the display size of the chart along the X axis. You can either drag the slider to specify the scaling ratio or type the ratio in the text box.

**Scale Y**

Specify to scale up or down the display size of the chart along the Y axis. You can either drag the slider to specify the scaling ratio or type the ratio in the text box.

**Constraint Proportion**

Select to apply the same scaling ratio for both the X and Y axes.

## Rotation Tab

Designer displays the Rotation tab when the chart is a 3-D chart. You can use it to specify rotation properties for formatting the 3-D chart paper.

![Format Paper - Rotation](https://devnet.logianalytics.com/hc/article_attachments/9898463212439/fmtpapr_rotate.gif)

**Preview box**

This box displays a preview of your settings.

![No Rotation button](https://devnet.logianalytics.com/hc/article_attachments/9898480370967/btn_plot1.gif)

Select to rotate the chart on the basis of the X, Y, and Z axes.

![Angle X button](https://devnet.logianalytics.com/hc/article_attachments/9898480377367/btn_plot2.gif)

Select and type the rotation angle in the text box to rotate the chart just on the basis of the X axis.

![Angle Y button](https://devnet.logianalytics.com/hc/article_attachments/9898463234839/btn_plot3.gif)

Select and type the rotation angle in the text box to rotate the chart just on the basis of the Y axis.

![Angle Z button](https://devnet.logianalytics.com/hc/article_attachments/9898463256471/btn_plot4.gif)

Select and type the rotation angle in the text box to rotate the chart just on the basis of the Z axis.

**Width**

Specify the scaling ratio for the width of the paper. You can either drag the slider to specify the ratio or type the ratio in the text box.

**Height**

Specify the scaling ratio for the height of the paper. You can either drag the slider to specify the ratio or type the ratio in the text box.

**Depth**

Specify the scaling ratio for the depth of the paper. You can either drag the slider to specify the ratio or type the ratio in the text box.

**Constraint Proportion**

Select to apply the same scaling ratios for the width, height, and depth of the paper.

## Fill Tab

Use this tab to specify the fill pattern of the chart paper.

![Format Paper - Fill](https://devnet.logianalytics.com/hc/article_attachments/9898463265175/fmtpapr_fill.gif)

**Color**

Specify the color to fill the paper. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency of the paper.

**Sample**

This box displays a preview sample based on your selections.

## Border Tab

Use this tab to specify properties for the border of the chart paper.

![Format Paper - Border](https://devnet.logianalytics.com/hc/article_attachments/9898480410391/fmtpapr_brdr.gif)

**Border Type**

Select the type of the border.

* **none**  
  Select if you do not want to show the border.
* **raised**  
  Select to show 3-D border that appears as if it is raised off the page.
* **recess**  
  Select to show 3-D border that appears as if it is pressed into the page.
* **shadow**  
  Select to show two shadowed borders, beneath and to the right of the object.
* **solid**  
  Select to use single-line border.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the width of the border, in pixels.

**End Caps**

Select the ending style of the border.

* **butt**  
  Select to end unclosed subpaths and dash segments with no added decoration.
* **round**  
  Select to end unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the line width.
* **square**  
  Select to end unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Select the joint style of the border.

* **miter**  
  Select to join path segments by extending their outside edges until they meet.
* **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

This box displays a preview sample based on your selections.

**Path**

You can specify the fill pattern of the border in this box.

* **Outline Path**  
  Select to use outline path for the border.
* **Fill Path**  
  Select to use whole path for the border.

**Dash**

You can specify the dash size of the border
in this box if you select a dash line style for the border.

* **Auto Adjust Dash**  
  Select to adjust the dash size automatically.
* **Fixed Dash Size**  
  Select to use fixed dash size.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735509343767-Format-Line-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735542973719-Format-Pattern-Dialog-Box)
