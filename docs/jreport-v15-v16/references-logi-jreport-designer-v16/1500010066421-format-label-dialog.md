---
title: "Format Label Dialog"
id: 1500010066421
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066421-Format-Label-Dialog
updated_at: 2021-07-24T10:38:47Z
---

# Format Label Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030982-Format-KPI-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031022-Format-Legend-Dialog)

# Format Label Dialog

The Format Label dialog helps you to [format the titles of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063461-Formatting-the-Labels). It appears when you right-click a label of a chart and select Format Label from the shortcut menu, or double-click a label in a chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Border](#Border), [Font](#Font) and [Orientation](#Orientation).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the label.

![Format Label - General](https://devnet.logianalytics.com/hc/article_attachments/4404909207575/fmtlabel_gnrl.gif)

**Text**

Specifies the text of the label.

**Icon**

Specifies the icon formats.

* **Style**  
  Specifies the style for the icon that will be used in the label. If you don't want to show any icon in the label, you can choose No Icon from the drop-down list.
* **Icon Text Gap**  
   Specifies the distance between the icon and the label text.
* **Fill**  
   Specifies the color to fill the selected icon. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Transparency**  
   Specifies the transparency of the color that is used to fill the selected icon.
* **Width**  
   Specifies the width of the icon, in pixels.
* **Height**  
   Specifies the height of the icon, in pixels.

**Alignment**

Specifies the alignment format for text and icons in the label.

* **Text**  
   Specifies the alignment format for text in the label.
* **Icon**  
   Specifies the alignment format for icons in the label.

## Fill

Specifies the color schema to fill the title of the label.

![Format Label - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404901231383/fmtlabel_fill.gif)

**Color**

Specifies the color to fill the label.

**Transparency**

Specifies the transparency of the color.

**Sample**

Displays the specified color and transparency effects.

## Border

Specifies properties of the label border.

![Format Label - Border](https://devnet.logianalytics.com/hc/article_attachments/4404901231639/fmtlabel_brdr.gif)

**Border Style**

Specifies the type for border of the label.

* **none**  
   The object has no visible border lines.
* **raised**  
   The object has 3D borders that appear as if they are raised off the page.
* **recess**  
   The object has 3D borders that appear as if they are pressed into the page.
* **shadow**  
   The object has two shadowed borders, beneath and to the right of the object.
* **solid**  
   The object has single-line borders.

**Color**

Specifies the color for border of the label.

**Line Style**

Specifies the line style to apply to the label border.

**Thickness**

Specifies the thickness of the label border, in pixels.

**Transparency**

Specifies the transparency for the color of the label border.

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

**Path**

Specifies the fill pattern of the border line.

* **Outline Path**  
   Specify the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specify the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of the border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Font

Specifies the font format of the label text.

![Format Label - Font](https://devnet.logianalytics.com/hc/article_attachments/4404901231895/fmtlabel_font.gif)

**Font**

Specifies the font format of label text.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**  
   Specifies the font color of the text.
* **Transparency**  
  Specifies the color transparency of the text.
* **Rotation**  
   Specifies the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
   Specifies the gradient of the text.

**Effects**

Specifies the special effects of the label text.

* **Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
   Specifies the style of the horizontal line with which the text is struck through. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When patterned line or bold patterned is selected, a line or bold line in the pattern of the text will be drawn.

  **Note:** Web Report Studio and JDashboard do not support underlining chart text so this property will be ignored when the chart runs in Web Report Studio or is used in a dashboard.
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

**Sample**

Displays the specified font and any text effects.

## Orientation

This tab allows you to set the alignment format of the label text and the icon.

![Format Label - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404901232151/fmtlabel_orntatn.gif)

**Orientation**

Drag the pointer in the box to specify the alignment format of the label text and the icon.

**Angle**

Specify the alignment format of the label text and the icon.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030982-Format-KPI-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031022-Format-Legend-Dialog)
