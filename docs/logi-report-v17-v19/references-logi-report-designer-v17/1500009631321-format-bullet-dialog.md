---
title: "Format Bullet Dialog"
id: 1500009631321
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631321-Format-Bullet-Dialog
updated_at: 2021-07-24T16:04:37Z
---

# Format Bullet Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608362-Format-Bubble-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608382-Format-Category-X-Axis-Dialog)

# Format Bullet Dialog

The Format Bullet dialog helps you to [format the bullets in a bullet chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605802-Formatting-the-Bullets-in-a-Bullet-Chart). It appears when you right-click a bullet of a bullet chart and select Format Bullet from the shortcut menu, or double-click a bullet of a bullet chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Border](#Border), [Data Label](#Data), [Hint](#Hint) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the bullet chart.

![Format Bullet - General](https://devnet.logianalytics.com/hc/article_attachments/4404916801687/fmtbult_gnrl.gif)

**Size**

Specifies the size of the bullets in the chart.

**Featured Measure Width**

Specifies the featured measure width as a percentage of the unit width.

**Comparative Measure Width**

Specifies the comparative measure width as a percentage of the unit width.

**Qualitative Ranges Width**

Specifies the qualitative ranges width as a percentage of the unit width.

## Fill

Specifies the fill properties.

![Format Bullet - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904327063/fmtbult_fill.gif)

**Featured Measure Color List**

Specifies the featured measure properties.

* **Color**  
  Specifies the color schema for the featured measures. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specifies the transparency of the color schema.
* **Self Settings**  
  Specifies whether to edit the color pattern for the featured measures themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
* **Color List**  
  Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for featured measures in the same data series respectively.
* **Vary Colors by Color List**  
  Specifies whether or not to make colors for the featured measures vary. If the option is selected, you can specify the color for each featured measure respectively.

**Comparative Measure Color List**

Specifies the comparative measure properties.

* **Color**  
   Specifies the color schema for the selected comparative measures in the same data series.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for comparative measures in the same data series respectively.

**Qualitative Ranges Color List**

Specifies the qualitative range properties.

* **Color**  
   Specifies the color schema for the selected qualitative ranges in the same data series.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for qualitative ranges in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies properties for the border of the bullets.

![Format Bullet - Border](https://devnet.logianalytics.com/hc/article_attachments/4404904327319/fmtbult_border.gif)

**Show Border**

Specifies whether to show the border of the bullets. When it is selected, the other border properties in the tab will be enabled.

**Color**

Specifies the color for border of the bullets.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to border of the bullets.

**Thickness**

Specifies the thickness of the border, in pixels.

**End Caps**

Specifies the ending style of the border line.

* **butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
* **round**  
   Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Specifies the line joint style for the border line.

* **miter**  
   Joins path segments by extending their outside edges until they meet.
* **round**  
   Joins path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
   Joins path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

Displays a preview sample of your selection.

**Path**

Specifies the fill pattern of the border line.

* **Outline Path**  
   Specifies the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specifies the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of the border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the chart. Not supported on bullet chart.

![Format Bullet - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404904327575/fmtbult_data.gif)

## Hint

Specifies properties for the hint of the bullets.

![Format Bullet - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904328087/fmtbult_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

## Behaviors

Specifies some web behaviors to the bullets. This tab is only available to charts in library components.

![Format Bullet - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904328343/fmtbult_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608362-Format-Bubble-Gauge-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608382-Format-Category-X-Axis-Dialog)
