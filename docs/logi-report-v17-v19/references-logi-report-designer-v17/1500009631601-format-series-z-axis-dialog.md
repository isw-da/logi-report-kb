---
title: "Format Series(Z) Axis Dialog"
id: 1500009631601
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631601-Format-Series-Z-Axis-Dialog
updated_at: 2021-07-24T16:04:33Z
---

# Format Series(Z) Axis Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608582-Format-Scatter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608602-Format-Series-Z-Gridline-Dialog)

# Format Series (Z) Axis Dialog

The Format Series (Z) Axis dialog helps you to [format the series (Z) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605762-Formatting-the-Axes#Series). It appears when you right-click a chart and select Format Axes > Format Series (Z) Axis from the shortcut menu, or double-click the series axis of a chart.

The dialog contains the following tabs: [Axis](#Axis), [Tick Mark](#Tick), [Font](#Font), [Orientation](#Orientation) and [Format](#Format).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Axis

Specifies the general properties for the axis.

![Format Series (Z) Axis dialog - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404916790423/fmtseriesaxis_axis.gif)

**Option**

Specifies options for the axis.

* **Draw Axis Only**  
   Specifies whether to show the labels on the axis.
* **Show Axis Label Tips**  
   Specifies whether to display the complete label text when the mouse pointer points at a label on the axis. Available only when Draw Axis Only is unselected.
* **Show Gridlines**  
   Specifies whether to show gridlines on the axis.
* **Number of Labels**  
   Specifies how many labels to be displayed on the axis. Available only when Draw Axis Only is unselected.
* **Label Every N Tick Marks**  
   Specifies whether to display a label every N tick marks. Available only when Draw Axis Only is unselected.

**Line**

Specifies the line style for the axis.

* **Color**  
  Specifies the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specifies the transparency for the color of the axis.
* **Style**  
  Specifies the style of the axis.
* **Thickness**  
  Specifies the thickness of the axis.

**Label**

Specifies the label properties for the labels on the axis.

* **Label Axis Gap**   
  Specifies the distance between the label and the axis.
* **Best Effect**  
  Specifies whether to adjust the labels automatically to make them placed best.
* **Auto**  
  If the axis displays a field, by default the major tick mark labels on the axis are values of the field. You can clear it to customize the label text.
  + **Label Text**  
    Specifies the text of the major tick mark labels on the axis. Select a field from the drop-down list to use its values as the label text or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904223383/btn_x.gif) to type in the desired label text manually.

## Tick Mark

Specifies properties of the tick marks on the axis.

![Format Series (Z) Axis dialog - Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404916790679/fmtseriesaxis_mark.gif)

**Tick Mark**

Specifies the line properties of the tick marks.

* **Correlate with Axis**  
   If the option is selected, the line properties of the tick marks will correlate with [that of the axis](#Line) automatically. Only when it is unselected can the following four properties take effect.
* **Color**  
   Specifies the color of the tick marks.
* **Transparency**  
   Specifies the transparency for the color of the tick marks.
* **Style**  
   Specifies the type of the tick marks.
* **Thickness**  
   Specifies the thickness of the tick marks.

**Major Tick Mark**

Specifies properties of the major tick marks on the axis.

* **None**  
   If selected, major tick marks will not be shown on the axis and it will be meaningless to specify all the other major tick mark related properties.
* **Inside**  
   If selected, major tick marks will be inside the chart.
* **Outside**  
   If selected, major tick marks will be outside the chart.
* **Cross**  
   If selected, major tick marks will be across the axis.
* **Major Tick Length**  
   Specifies the length of the major tick marks on the axis.

**Minor Tick Mark**

Specifies properties of the minor tick marks on the axis.

* **None**  
   If selected, minor tick marks will not be shown on the axis and it will be meaningless to specify all the other minor tick mark related properties.
* **Inside**  
   If selected, minor tick marks will be inside the chart.
* **Outside**  
   If selected, minor tick marks will be outside the chart.
* **Cross**  
   If selected, minor tick marks will be across the chart.
* **Minor Tick Length**  
   Specifies the length of the minor tick marks on the axis.

## Font

Specifies the font format of text in the major tick mark labels on the axis.

![Format Series (Z) Axis dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404904294167/fmtseriesaxis_font.gif)

**Font**

Specifies the font format of text in the major tick mark labels.

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

Specifies the special effects of text in the major tick mark labels.

* **Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
   Specifies the style of the horizontal line with which the text is struck through. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When patterned line or bold patterned is selected, a line or bold line in the pattern of the text will be drawn.

  **Note:** JDashboard does not support underlining chart text so this property will be ignored when the chart is used in a dashboard.
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

Specifies the rotation angle of the major tick mark labels on the axis.

![Format Series (Z) Axis dialog - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404904294423/fmtseriesaxis_orntatn.gif)

**Automatic**

Specifies to adjust the rotation angle of the label text on the axis automatically according to the length of the label text, in degrees.

When this option is selected by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the label text on the axis. When you change the rotation angle in the text box, the red line in the spin box will change correspondingly, and vice versa.

## Format

Specifies the data format of the major tick mark labels on the axis.

![Format Series (Z) Axis dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404916790935/fmtseriesaxis_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Lists all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Enabled when the series field is of the Number data type. It specifies whether to automatically scale the major tick mark labels when the label values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Sample**

Displays the selected format effects.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the major tick mark labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608582-Format-Scatter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608602-Format-Series-Z-Gridline-Dialog)
