---
title: "Format KPI Label Dialog"
id: 1500010030982
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030982-Format-KPI-Label-Dialog
updated_at: 2021-07-24T10:38:48Z
---

# Format KPI Label Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030962-Format-Indicator-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066421-Format-Label-Dialog)

# Format KPI Label Dialog

The Format KPI Label dialog helps you to [format the KPI value label](https://devnet.logianalytics.com/hc/en-us/articles/1500010063521-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart#KPIValue). It appears when you right-click the KPI value for a pie/donut and select Format KPI Label from the shortcut menu, or double-click the KPI value for a pie/donut.

The dialog contains the following tabs: [General](#General), [Font](#Font) and [Format](#Format).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the labels.

![Format KPI Label - General](https://devnet.logianalytics.com/hc/article_attachments/4404909207831/fmtkpilbl_gnrl.gif)

**Size**

Specifies the size and position of the labels.

* **Width**  
   Specifies the width of the labels, in pixels.
* **Height**  
   Specifies the height of the labels, in pixels.
* **X**  
   Specifies the horizontal coordinate of the top left corner of the labels, relative to their parent container.
* **Y**  
   Specifies the vertical coordinate of the top left corner of the labels, relative to their parent container.
* **Alignment**  
   Specifies the alignment of the label text.
* **Word Wrap**  
   Specifies whether to enable the word wrap function for the label text.

**Fill**

Specifies the color and transparency of the labels.

* **Fill**  
   Specifies the color to fill the labels.
* **Transparency**  
   Specifies the transparency to fill the labels.

**Border**

Specifies the properties for borders of the labels.

* **Border Type**  
   Specifies the type of the border.
* **Color**  
   Specifies the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Line Style**  
   Specifies the line style to apply to the border.
* **Transparency**  
   Specifies the color transparency for the border.
* **Thickness**  
   Specifies the thickness of the border, in pixels.
* **End Caps**  
   Specifies the ending style of the border line.

+ **butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
+ **round**  
   Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
+ **square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

* **Line Joint**  
   Specifies the line joint style for the border line.
  + **miter**  
     Joins path segments by extending their outside edges until they meet.
  + **round**  
     Joins path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
     Joins path segments by connecting the outer corners of their wide outlines with a straight segment.
  + **joint round**  
     Joins path segments by rounding off the corner at the specified radius.
* **Path**  
   Specifies the fill pattern of the border line.

  + **Outline Path**  
     Specifies the fill pattern of the border line to be outline path.
  + **Fill Path**  
     Specifies the fill pattern of the border line to be whole path.
* **Dash**  
   Specifies the dash size of border line.
  + **Auto Adjust Dash**  
     If selected, the dash size will be adjusted automatically.
  + **Fixed Dash Size**  
     If selected, the dash size will be fixed size.

**Orientation**

Specifies the orientation properties of the labels.

* **Label Orientation**   
   Specifies the rotation angle of the labels.

**Sample**

Displays a preview sample of your selection.

## Font

Specifies the font format of the label text.

![Format KPI Label - Font](https://devnet.logianalytics.com/hc/article_attachments/4404901232407/fmtkpilbl_font.gif)

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
   Specifies the rotation angle of the text around its center, in degrees.
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

## Format

Specifies the data format of the label text.

![Format KPI Label - Format](https://devnet.logianalytics.com/hc/article_attachments/4404901232791/fmtkpilbl_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500010030282-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text field and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Enabled when the KPI values are of the Number data type. It specifies whether to
automatically scale the values that fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Sample**

Displays a preview sample of your selection.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the label.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030962-Format-Indicator-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066421-Format-Label-Dialog)
