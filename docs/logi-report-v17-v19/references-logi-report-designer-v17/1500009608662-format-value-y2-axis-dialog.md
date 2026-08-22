---
title: "Format Value(Y2) Axis Dialog"
id: 1500009608662
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608662-Format-Value-Y2-Axis-Dialog
updated_at: 2021-07-24T16:04:32Z
---

# Format Value(Y2) Axis Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631721-Format-Value-Y-Gridline-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608682-Format-Value-Y2-Gridline-Dialog)

# Format Value (Y2) Axis Dialog

The Format Value (Y2) Axis dialog helps you to [format the value (Y2) axis of a combo chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605762-Formatting-the-Axes#Value). It appears when you right-click a combo chart and select Format Axes > Format Value (Y2) Axis from the shortcut menu, or double-click the Y2 axis of a combo chart.

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

![Format Value (Y2) Axis - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404904283799/fmtvalueaxis2_axis.gif)

**Option**

Specifies the options for the axis.

* **Minimum Value**  
   Specifies the minimum value that is to be displayed on the axis.
* **Maximum Value**  
   Specifies the maximum value that is to be displayed on the axis.
* **Increment**  
   Specifies the distance between two adjacent values on the axis.
* **Number of Tick Marks**  
   Specifies how many tick marks to be displayed on the axis.
* **Show Gridlines**  
   Specifies whether to show gridlines on the axis.
* **Show Percent**  
   Specifies whether to show the value labels on the axis in percent. Only applies to bar/bench, line and area chart that are not 100% stacked type.

**Line**

Specifies the line style for the axis.

* **Color**  
  Specifies the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Style**  
  Specifies the style of the axis.
* **Transparency**  
   Specifies the transparency for the color of the axis.
* **Thickness**  
  Specifies the thickness of the axis, in pixels.

**Label**

Specifies the label properties for the labels on the axis.

* **Label Axis Gap**  
  Specifies the distance between the label and the axis, in pixels.
* **Best Effect**   
   Specifies whether to adjust the labels on the axis automatically to make them placed best.

## Tick Mark

The tab consists of two sub tabs: [Major Tick Mark](#Majortm), and [Minor Tick Mark](#Minortm).

### Major Tick Mark

Specifies properties of the major tick marks on the axis.

![Format Value (Y2) Axis - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904284055/fmtvalueaxis2_mark_major.gif)

**Type**

Specifies the type of the major tick marks on the axis.

* **None**  
   If selected, major tick marks will not be shown on the axis and it will be meaningless to specify all the other major tick mark related properties.
* **Inside**  
   If selected, major tick marks will be inside the chart.
* **Outside**  
   If selected, major tick marks will be outside the chart.
* **Cross**  
   If selected, major tick marks will be across the axis.

**Line**

Specifies the line properties of the major tick marks on the axis.

* **Correlate with Axis**  
   If the option is selected, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the major tick marks.
  + **Style**  
     Specifies the type of the major tick marks.
  + **Thickness**  
     Specifies the thickness of the major tick marks, in pixels.
* **Tick Mark Length**  
   Specifies the length of the major tick marks, in pixels.

**Option**

Specifies the other properties of the major tick mark labels on the axis.

* **Show Major Tick Mark Labels**  
   Specifies whether to display the labels of the major tick marks on the axis. If the option is selected, the following three properties will be enabled.
* **Label Every N Major Tick Marks**  
   Specifies the frequency at which the major tick marks will be labeled.
* **Show Axis Label Tips**  
   Specifies whether to display the complete label text when the mouse pointer points at a label on the axis.
* **Number of Major Labels**  
   Specifies how many major tick mark labels to be displayed on the axis.
  + **Auto**  
     If the option is selected, all major tick mark labels will be shown.
  + **Fixed**  
     If the option is selected, you can specify the number of the major tick mark labels to be displayed on the axis.

### Minor Tick Mark

Specifies properties of the minor tick marks on the axis.

![Format Value (Y2) Axis - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904284311/fmtvalueaxis2_mark_minor.gif)

**Type**

Specifies the type of the minor tick marks on the axis.

* **None**  
   If selected, minor tick marks will not be shown on the axis and it will be meaningless to specify all the other minor tick mark related properties.
* **Inside**  
   If selected, minor tick marks will be inside the chart.
* **Outside**  
   If selected, minor tick marks will be outside the chart.
* **Cross**  
   If selected, minor tick marks will be across the axis.

**Line**

Specifies the line properties of the minor tick marks on the axis.

* **Correlate with Axis**  
   If the option is selected, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the minor tick marks.
  + **Style**  
     Specifies the type of the minor tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the minor tick marks.
  + **Thickness**  
     Specifies the thickness of the minor tick marks, in pixels.
* **Tick Mark Length**  
   Specifies the length of the minor tick marks, in pixels.

## Font

Specifies the font format for text in the major tick mark labels on the axis.

![Format Value (Y2) Axis - Font](https://devnet.logianalytics.com/hc/article_attachments/4404904284567/fmtvalueaxis2_font.gif)

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

Specifies the rotation angle of the major tick mark labels on the axis.

![Format Value (Y2) Axis - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404904285079/fmtvalueaxis2_orntatn.gif)

**Automatic**

Specifies whether to adjust the rotation angle of the label text on the axis automatically according to the length of the label text, in degrees.

When this option is selected by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the label text on the axis. When you change the rotation angle in the text box, the red line in the spin box will change correspondingly, and vice versa.

## Format

Specifies the data format of the major tick mark labels on the axis.

![Format Value (Y2) Axis - Format](https://devnet.logianalytics.com/hc/article_attachments/4404904285335/fmtvalueaxis2_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Lists all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example, the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631721-Format-Value-Y-Gridline-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608682-Format-Value-Y2-Gridline-Dialog)
