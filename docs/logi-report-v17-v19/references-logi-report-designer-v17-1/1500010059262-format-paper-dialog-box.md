---
title: "Format Paper Dialog Box"
id: 1500010059262
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059262-Format-Paper-Dialog-Box
updated_at: 2021-07-23T19:15:30Z
---

# Format Paper Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059242-Format-Line-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097161-Format-Pattern-Dialog-Box)

# Format Paper Dialog Box

You can use the Format Paper dialog box to [format the paper of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094541-Formatting-the-Paper). This topic describes the options in the dialog box.

Designer displays the Format Paper dialog box when you right-click any chart element and select Format Paper from the shortcut menu, or double-click the paper of a chart.

The dialog box contains the following tabs:

* [General Tab](#General) (for 2-D charts)
* [Rotation Tab](#Rotation) (for 3-D charts)
* [Fill Tab](#Fill)
* [Border Tab](#Border)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Designer displays the General tab if the chart is a 2-D chart. You can use it to specify the general properties of the chart paper.

![Format Paper - General](https://devnet.logianalytics.com/hc/article_attachments/4404848545943/fmtpapr_gnrl.gif)

**Scale X**

Specify to scale up or down the display size of the chart along the X axis. You can either drag the slider to specify the scaling ratio or input the ratio in the text box.

**Scale Y**

Specify to scale up or down the display size of the chart along the Y axis. You can either drag the slider to specify the scaling ratio or input the ratio in the text box.

**Constraint Proportion**

Select to apply the same scaling ratio for both the X and Y axes.

## Rotation Tab

Designer displays the Rotation tab if the chart is a 3-D chart. You can use it to specify the rotation properties for formatting the 3-D chart paper.

![Format Paper - Rotation](https://devnet.logianalytics.com/hc/article_attachments/4404856942231/fmtpapr_rotate.gif)

**Preview box**

The box displays a preview sample of your settings.

![No Rotation button](https://devnet.logianalytics.com/hc/article_attachments/4404856942487/btn_plot1.gif)

Select to rotate the chart on the basis of the X, Y, and Z axes.

![Angle X button](https://devnet.logianalytics.com/hc/article_attachments/4404856942871/btn_plot2.gif)

Select and input the rotation angle in the text box to rotate the chart just on the basis of the X axis.

![Angle Y button](https://devnet.logianalytics.com/hc/article_attachments/4404856943127/btn_plot3.gif)

Select and input the rotation angle in the text box to rotate the chart just on the basis of the Y axis.

![Angle Z button](https://devnet.logianalytics.com/hc/article_attachments/4404856943639/btn_plot4.gif)

Select and input the rotation angle in the text box to rotate the chart just on the basis of the Z axis.

**Width**

Specify the scaling ratio for the width of the paper. You can either drag the slider to specify the ratio or input the ratio in the text box.

**Height**

Specify the scaling ratio for the height of the paper. You can either drag the slider to specify the ratio or input the ratio in the text box.

**Depth**

Specify the scaling ratio for the depth of the paper. You can either drag the slider to specify the ratio or input the ratio in the text box.

**Constraint Proportion**

Select to apply the same scaling ratios for the width, height, and depth of the paper.

## Fill Tab

Use this tab to specify the color pattern to fill the chart paper.

![Format Paper - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404848546455/fmtpapr_fill.gif)

**Color**

Specify the color to fill the paper. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency of the color to fill the paper.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Use this tab to specify the properties for the border of the chart paper.

![Format Paper - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856944023/fmtpapr_brdr.gif)

**Border Type**

Select the type of the border.

* **none**  
  Select if you do not want to show the border.
* **raised**  
  Select to show 3-D border which appears as if it is raised off the page.
* **recess**  
  Select to show 3-D border which appears as if it is pressed into the page.
* **shadow**  
  Select to show two shadowed borders, beneath and to the right of the object.
* **solid**  
  Select to use single-line border.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency for the color of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the thickness of the border, in pixels.

**End Caps**

Select the ending style of the border line.

* **butt**  
  Select to end unclosed sub paths and dash segments with no added decoration.
* **round**  
  Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
  Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Select the joint style of the border line.

* **miter**  
  Select to join path segments by extending their outside edges until they meet.
* **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

The box displays a preview sample of your selection.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059242-Format-Line-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097161-Format-Pattern-Dialog-Box)
