---
title: "Format Bullet Dialog (for Library Component)"
id: 1500009587101
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587101-Format-Bullet-Dialog-for-Library-Component
updated_at: 2021-07-24T05:55:15Z
---

# Format Bullet Dialog (for Library Component)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587081-Format-Bubble-Gauge-Dialog-for-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565782-Format-Bullet-Dialog-for-Report-)

# Format Bullet Dialog (for Library Component)

The Format Bullet dialog for library component appears when you double-click a bullet of a chart in a library component, or right-click it and select Format Bullet from the shortcut menu. It helps you to [format the bullets of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563022-Formatting-the-Bullets), and consists of the four following tabs:

* [General](#General)
* [Fill](#Fill)
* [Border](#Border)
* [Data Label](#Data)
* [Behaviors](#Behaviors)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the bullet chart. [See the tab](javascript:%20void(null)).

![Format Bullet for Library Component - General](https://devnet.logianalytics.com/hc/article_attachments/4404893907863/fmtbult_gnrl_lc.gif)

**Size**

Specifies the size of the bullets in the chart.

**Featured Measure Width**

Specifies the featured measure width as a percentage of the unit width.

**Comparative Measure Width**

Specifies the comparative measure width as a percentage of the unit width.

**Qualitative Ranges Width**

Specifies the qualitative ranges width as a percentage of the unit width.

## Fill

Specifies the fill properties. [See the tab](javascript:%20void(null)).

![Format Bullet for Library Component - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893908119/fmtbult_fill_lc.gif)

**Featured Measure Color List**

Specifies the featured measure properties.

* **Color**  
   Specifies the color schema for the featured measures.
  To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Vary Colors by Color List**  
   Specifies whether or not to make colors for the featured measures vary. If checked, you can specify the color for each featured measure respectively.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for each featured measure.

**Comparative Measure Color List**

Specifies the comparative measure properties.

* **Color**  
   Specifies the color schema for the selected comparative measures in the same data series.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for comparative measures in the same data series respectively.

**Qualitative Ranges Color List**

Specifies the qualitative range properties.

* **Color**  
   Specifies the color schema for the selected qualitative ranges in the same data series.
* **Transparency**  
   Specifies the transparency of the color schema.
* **Color List**  
   Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009564822-Color-List-Dialog) dialog to modify color pattern for qualitative ranges in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies the properties for the borders of the bullets, which take effect only when the [Border](https://devnet.logianalytics.com/hc/en-us/articles/1500009591241-Properties-of-Chart-Paper-in-Page-Report#Border) property on chart paper is set to true in the Report Inspector. [See the tab](javascript:%20void(null)).

![Format Bullet for Library Component - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889355543/fmtbult_border_lc.gif)

**Border Type**

Displays the type for border of the bullets. The default value is solid, and cannot be changed.

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

* **Auto Adjusted Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data Label

Specifies properties for data labels displayed on the bullets. [See the tab](javascript:%20void(null)).

![Format Bullet for Library Component - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893908375/fmtbult_data_lc.gif)

**Static Data Label**

Specifies properties of the static data labels. Not supported on bullet chart.

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

## Behaviors

Specifies some web behaviors to the bullets. [See the tab](javascript:%20void(null)).

![Format Bullet for Library Component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404889355799/fmtbult_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587081-Format-Bubble-Gauge-Dialog-for-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565782-Format-Bullet-Dialog-for-Report-)
