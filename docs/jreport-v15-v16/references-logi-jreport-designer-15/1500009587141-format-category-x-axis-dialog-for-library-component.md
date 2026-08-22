---
title: "Format Category (X) Axis Dialog (for Library Component)"
id: 1500009587141
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587141-Format-Category-X-Axis-Dialog-for-Library-Component
updated_at: 2021-07-24T05:55:16Z
---

# Format Category (X) Axis Dialog (for Library Component)

![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic[Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565802-Format-Category-X-Axis-Dialog-for-Report-)

# Format Category (X) Axis Dialog (for Library Component)

The Format Category (X) Axis dialog for library component appears when you double-click the category (X) axis of a chart in a library component, or right-click it and then select Format Axes > Format Category (X) Axis from the shortcut menu. It helps you to [format the category (X) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009562982-Formatting-the-Axes#Category), and consists of the following tabs:

* [Axis](#Axis)
* [Tick Mark](#Tick)
* [Font](#Font)
* [Orientation](#Orientation)
* [Format](#Format)
* [Range](#Range)
* [Behaviors](#Behaviors)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Axis

Specifies the general properties for the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404889353623/fmtctgryaxis_axis_lc.gif)

**Option**

Specifies the options for the axis.

* **Minimum Value**  
   Specifies the minimum value that is to be displayed on the axis. Available only to bubble charts which use the axis to show numeric data and scatter charts.
* **Maximum Value**  
   Specifies the maximum value that is to be displayed on the axis. Available only to bubble charts which use the axis to show numeric data and scatter charts.
* **Increment**  
   Specifies the difference between two adjacent values on the axis. Available only to bubble charts which use the axis to show numeric data and scatter charts.
* **Number of Tick Marks**  
   Specifies how many tick marks to be displayed on the axis. Available only to bubble charts which use the axis to show numeric data and scatter charts.
* **Show Gridlines**  
   Specifies whether to show gridlines on the axis.

**Line**

Specifies the line style for the axis.

* **Color**  
   Specifies the color of the axis. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Style**  
   Specifies the style for the line of the axis.
* **Transparency**  
  Specifies the transparency for the color of the axis.
* **Thickness**  
   Specifies the thickness for the line of the axis, in pixels.

**Gap**

Specifies the gap properties for the labels on the axis.

* **Label Axis Gap**   
   Specifies the distance between the label and the axis, in pixels.
* **Best Effect**  
   Specifies whether to adjust the labels automatically to make them placed best.

## Tick Mark

The tab consists of three sub tabs: [Major Tick Mark](#Majortm), [Minor Tick Mark](#Minortm), and [Scale](#Scale).

### Major Tick Mark

Specifies properties of the major tick marks on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Tick Mark - Major](https://devnet.logianalytics.com/hc/article_attachments/4404893905047/fmtctgryaxis_mark_major_lc.gif)

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
   If checked, the line properties of the major tick marks will correlate with [that of the axis](#Line) automatically.
  + **Color**  
     Specifies the color of the major tick marks.
  + **Style**  
     Specifies the type of the major tick marks.
  + **Transparency**  
     Specifies the transparency for the color of the major tick marks.
  + **Thickness**  
     Specifies the thickness of the major tick marks, in pixels.
* **Tick Mark Length**  
   Specifies the length of the major tick marks, in pixels.

**Option**

Specifies the other properties of the major tick mark labels on the axis.

* **Show Major Tick Mark Labels**  
   Specifies whether to display the labels of the major tick marks on the axis. If checked, the following properties will be enabled.
* **Label Every N Major Tick Marks**  
   Specifies the frequency at which the major tick marks will be labeled.
* **Show Axis Label Tips**  
   Specifies whether to display the complete label text when the mouse pointer points at a label on the axis.
* **Number of Major Labels**  
   Specifies how many major tick mark labels to be displayed on the axis.
  + **Auto**  
     If checked, all major tick mark labels will be shown.
  + **Fixed**  
     If checked, you can specify the number of the major tick mark labels to be displayed on the axis.

### Minor Tick Mark

Specifies properties of the minor tick marks on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Tick Mark - Minor](https://devnet.logianalytics.com/hc/article_attachments/4404889353879/fmtctgryaxis_mark_minor_lc.gif)

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
   If checked, the line properties of the minor tick marks will correlate with [that of the axis](#Line) automatically.
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

**Option**

Specifies the other properties of the minor tick marks on the axis.

* **Show Minor Tick Mark Labels**  
   Specifies whether to display the labels of the minor tick marks on the axis. If checked, the following properties will be enabled.
* **Label Every N Minor Tick Marks**  
   Specifies the frequency at which the minor tick marks will be labeled.
* **Number of Minor Labels**  
   Specifies how many minor tick mark labels to be displayed on the axis.
  + **Auto**  
     If checked, all minor tick mark labels will be shown.
  + **Fixed**  
     If checked, you can specify the number of the minor tick mark labels to be displayed on the axis.

### Scale

Customizes the way in which to label the tick marks on the axis. Available only when the field on the category axis is one of the following types: Number, Date, DateTime, and Time, and not applied to scatter charts or when the category axis is used to show numeric data in bubble charts. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4404893905303/fmtctgryaxis_mark_scale_lc.gif)

**Use Constant Interval**

Specifies whether to use a constant interval to label the tick marks. If checked, the values of the tick marks will be increased continually on the axis based on the following properties, instead of just using the data values.

**Minimum**

Specifies the minimum value which will be used to label the tick marks.

* **Auto**  
   If checked, the minimum value will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the minimum value as required. Input the value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a field from the drop-down list or [use a formula to control it](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties). You can also specify it in the calendar if the field on the category axis is of Date, DateTime or Time type.

**Maximum**

Specifies the maximum value which will be used to label the tick marks.

* **Auto**  
   If checked, the maximum value will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the maximum value as required. Input the value in the text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a field from the drop-down list or [use a formula to control it](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties). You can also specify it in the calendar if the field on the category axis is of Date, DateTime or Time type.

**Major Unit**

Specifies the unit between two adjacent major tick marks.

* **Auto**  
   If checked, the unit will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the unit as required. If the field on the category axis is of the Date, DateTime or Time type, you can also choose a unit from the drop-down list.

**Minor Unit**

Specifies the unit between two adjacent minor tick marks.

* **Auto**  
   If checked, the unit will be defined by Logi JReport automatically.
* **Fixed**  
   If checked, you can define the unit as required. If the field on the category axis is of the Date, DateTime or Time type, you can also choose a unit from the drop-down list.

## Font

The tab consists of two sub tabs: [Major Label](#Majorft) and [Minor Label](#Minorft).

### Major Label

Specifies the font format of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404893905559/fmtctgryaxis_font_major_lc.gif)

**Font**

Specifies the font format of text in the major tick mark labels.

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

Specifies the special effects of text in the major tick mark labels.

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

**Sample**

Displays a sample of the specified font and any text effects.

### Minor Label

Specifies the font format of the minor tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Font - minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404893905815/fmtctgryaxis_font_minor_lc.gif)

**Correlate with Major Label**

If checked, the font format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the font properties of the minor tick mark labels take effect.

**Font**

Specifies the font format of text in the minor tick mark labels.

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

Specifies the special effects of text in the minor tick mark labels.

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

**Sample**

Displays a sample of the specified font and any text effects.

## Orientation

The tab consists of two sub tabs: [Major Label](#Majorlb) and [Minor Label](#Minorlb).

### Major Label

Specifies the rotation angle of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404889354263/fmtctgryaxis_orntatn_major_lc.gif)

**Automatic**

Specifies to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is checked by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the major tick mark label text on the axis. When you change the rotation angle in the text box, the red line in the spin box will change correspondingly, and vice versa.

### Minor Label

Specifies the rotation angle of the minor tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Orientation - Minnor Label](https://devnet.logianalytics.com/hc/article_attachments/4404893906071/fmtctgryaxis_orntatn_minor_lc.gif)

**Correlate with Major Label**

If checked, the orientation setting of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the orientation properties of the minor tick mark labels take effect.

**Automatic**

Specifies to adjust the rotation angle of the minor tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is checked by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the minor tick mark label text on the axis. When you change the rotation angle in the text box, the red line in the spin box will change correspondingly, and vice versa.

## Format

The tab consists of two sub tabs: [Major Label](#Majorfmt) and [Minor Label](#Minorfmt).

### Major Label

Specifies the data format of the major tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404893906327/fmtctgryaxis_fmt_major_lc.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the formats of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category. For more details about the formats, see [A Detailed Chart Property Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#DataFormat).

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text field and then select Add to add it as the format of the specified category.

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

### Minor Label

Specifies the data format of the minor tick mark labels on the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Format - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404893906583/fmtctgryaxis_fmt_minor_lc.gif)

**Correlate with Major Label**

If checked, the data format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the format properties of the minor tick mark labels take effect.

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the formats of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category. For more details about the formats, see [A Detailed Chart Property Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#DataFormat).

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text field and then select Add to add it as the format of the specified category.

**Sample**

Displays the selected format effects.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the minor tick mark labels.

## Range

The tab helps you to divide the catagory values into different range groups and edit data lables for them, and consists of two sub tabs: [properties](#Properties) and [data label](#Datalb).

### Properties

Specifies the properties of the range groups. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Range - Properties](https://devnet.logianalytics.com/hc/article_attachments/4404893906839/fmtctgryaxis_range_prpty_lc.gif)

**Enable Range**

Specifies whether to enable the range function.

* **Special Group**   
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define how to group your the category values.

**Gridline**

Specifies the style for the range separating lines.

* **Line Color**  
   Specifies the color of the range separating lines.
* **Line Style**  
   Specifies the style of the range separating lines.
* **Transparency**  
   Specifies the transparency for the color of the range separating lines.
* **Thickness**  
   Specifies the thickness of the range separating lines, in pixels.

**Fill**

Specifies the fill effects for each range group.

* **Group Name**   
   Shows the name of each range group.
* **Color**  
   Specifies the color to be applied to each range group.
* **Transparency**  
   Specifies the transparency for the color of each range group.

### Data Label

Specifies the properties of the data labels in the range groups. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Range - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404893907095/fmtctgryaxis_range_dtlb_lc.gif)

**Show Data Labels**

Specifies whether to show data labels for the range groups. Available only when the option Enable Range in the Properties tab is checked and range groups are defined.

* **Edit Data Labels**  
   Opens the [Data Label Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009565062-Data-Label-Editor-Dialog) to edit data labels for the range groups.

**Value Label Type**

Specifies the display type for data values in the value labels of each range group. It can be value, percent, value and percent.

**Percent within Group**

Specifies whether to calculate the percent value within each range group or across all range groups. Available only when percent or value and percent is select from the Value Label Type drop-down list.

**Alignment**

Specifies the alignment style for the data labels in each range group.

**Size**

Specifies the size of the data label area on the range groups.

* **Height**  
   Specifies the height of the data label area. It cannot exceed the maximum height.
* **Width**  
   Specifies the height of the data label area.
* **Maximum Height**   
   Specifies the maximum height of the data label area. It cannot exceed the height of the chart paper.

**Fill**

Specifies the fill effect for the data label area.

* **Color**  
   Specifies the color to fill the data label area.
* **Transparency**  
   Specifies the transparency of the color.

**Border**

Specifies the properties of the border line for the data label area.

* **Color**  
   Specifies the color of the border line.
* **Line Style**  
   Specifies the style of the border line.
* **Transparency**  
   Specifies the transparency for the color of the range separating lines.
* **End Caps**   
   Specifies the ending style of the border line.
  + **butt**  
     Ends unclosed sub paths and dash segments with no added decoration.
  + **round**  
     Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
  + **square**  
     Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.
* **Thickness**  
   Specifies the thickness of the border line, in pixels.
* **Line Joint**   
   Specifies the line joint style for the border line.
  + **miter**  
     Joins path segments by extending their outside edges until they meet.
  + **round**  
     Joins path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
     Joins path segments by connecting the outer corners of their wide outlines with a straight segment.

**Margin**

Specifies the distance between the edges and the borders.

* **Top**  
   Specifies the distance between the top edge and the top border.
* **Bottom**  
   Specifies the distance between the bottom edge and the bottom border.
* **Left**  
   Specifies the distance between the left edge and the left border.
* **Right**  
   Specifies the distance between the right edge and the right border.

**Padding**

Specifies the distance between the data labels and the borders.

* **Top**  
   Specifies the distance between the data labels and the top border.
* **Bottom**  
   Specifies the distance between the data labels and the bottom border.
* **Left**  
   Specifies the distance between the data labels and the left border.
* **Right**  
   Specifies the distance between the data labels and the right border.

## Behaviors

Specifies some web behaviors to the axis. [See the tab](javascript:%20void(null)).

![Format Category (X) Axis for Library Component - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404889354519/fmtctgryaxis_bhvr.gif)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565782-Format-Bullet-Dialog-for-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565802-Format-Category-X-Axis-Dialog-for-Report-)
