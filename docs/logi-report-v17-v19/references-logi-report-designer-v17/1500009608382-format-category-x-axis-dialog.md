---
title: "Format Category (X) Axis Dialog"
id: 1500009608382
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608382-Format-Category-X-Axis-Dialog
updated_at: 2021-07-24T16:04:36Z
---

# Format Category (X) Axis Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631321-Format-Bullet-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608402-Format-Category-X-Gridline-Dialog)

# Format Category (X) Axis Dialog

The Format Category X Axis dialog helps you to [format the category (X) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605762-Formatting-the-Axes#Category). It appears when you right-click any chart element and select Format Axes > Format Category (X) Axis from the shortcut menu, or double-click the category axis of a chart.

The dialog contains the following tabs: [Axis](#Axis), [Tick Mark](#Tick), [Font](#Font), [Orientation](#Orientation), [Format](#Format), [Range](#Range) and [Behaviors](#Behaviors) (some tabs are available to specific chart types only).

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

![Format Category (X) Axis dialog - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404916800663/fmtctgryaxis_axis.gif)

**Option**

Specifies the options for the axis.

* **Minimum Value**  
   Specifies the minimum value that is to be displayed on the axis. Available only to scatter charts and bubble charts which show different fields on the category axis and bubble X axis.
* **Maximum Value**  
   Specifies the maximum value that is to be displayed on the axis. Available only to scatter charts and bubble charts which show different fields on the category axis and bubble X axis.
* **Increment**  
   Specifies the distance between two adjacent values on the axis. Available only to scatter charts and bubble charts which show different fields on the category axis and bubble X axis.
* **Number of Tick Marks**  
   Specifies how many tick marks to be displayed on the axis. Available only to scatter charts and bubble charts which show different fields on the category axis and bubble X axis.
* **Show Gridlines**  
   Specifies whether to show gridlines on the axis.

**Line**

Specifies the line style for the axis.

* **Color**  
  Specifies the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Style**  
   Specifies the style for the line of the axis.
* **Transparency**  
  Specifies the transparency for the color of the axis.
* **Thickness**  
  Specifies the thickness for the line of the axis, in pixels.

**Label**

Specifies the label properties for the labels on the axis.

* **Label Axis Gap**   
  Specifies the distance between the label and the axis, in pixels.
* **Best Effect**  
  Specifies whether to adjust the labels automatically to make them placed best. If the option is selected, some labels will be hidden when they are overlapped.
* **Auto**  
  If the option is selected, the major tick mark labels on the axis are values of the field displayed on the axis. You can clear it to customize the label text.
  + **Label Text**  
    Specifies the text of the major tick mark labels on the axis. Select a field from the drop-down list to use its values as the label text or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904223383/btn_x.gif) to type in the desired label text manually.

## Tick Mark

The tab consists of three sub tabs: [Major Tick Mark](#Majortm), [Minor Tick Mark](#Minortm), and [Scale](#Scale).

### Major Tick Mark

Specifies properties of the major tick marks on the axis.

![Format Category (X) Axis dialog - Tick Mark - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904324247/fmtctgryaxis_mark_major.gif)

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
   Specifies whether to display the labels of the major tick marks on the axis. If the option is selected, the following properties will be enabled.
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

![Format Category (X) Axis dialog - Tick Mark - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404904324503/fmtctgryaxis_mark_minor.gif)

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

**Option**

Specifies the other properties of the minor tick marks on the axis.

* **Show Minor Tick Mark Labels**  
   Specifies whether to display the labels of the minor tick marks on the axis. It takes effect only when Use Constant Interval in the Scale sub tab of the Tick Mark tab is selected. If the option is selected, the following properties will be enabled.
* **Label Every N Minor Tick Marks**  
   Specifies the frequency at which the minor tick marks will be labeled.
* **Number of Minor Labels**  
   Specifies how many minor tick mark labels to be displayed on the axis.
  + **Auto**  
     If the option is selected, all minor tick mark labels will be shown.
  + **Fixed**  
     If the option is selected, you can specify the number of the minor tick mark labels to be displayed on the axis.

### Scale

Customizes the way in which to label the major and minor tick marks on the axis with constant interval. This sub tab is activated only when the field on the category axis is one of the following types: Number, Date, DateTime, and Time (for a bubble chart only when the category field is one of the above types and the Bubble X Axis uses the category field). The sub tab is not available to scatter charts.

![Format Category (X) Axis dialog - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4404916800919/fmtctgryaxis_mark_scale.gif)

**Use Constant Interval**

Specifies whether to use a constant interval to label the tick marks. If the option is selected, the values of the tick marks will be increased continually on the axis based on the following properties instead of just using the data values, and the [customized major tick mark labels](#LabelText) in the Axis tab are ignored.

**Minimum**

Specifies the minimum value which will be used to label the tick marks.

* **Auto**  
   If the option is selected, the minimum value will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the minimum value by inputting it in the text box directly, selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) to select a field, or selecting the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif) to select a value from the calendar if the field on the category axis is of Date, DateTime, or Time type.

**Maximum**

Specifies the maximum value which will be used to label the tick marks.

* **Auto**  
   If the option is selected, the maximum value will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the maximum value by inputting it in the text box directly, selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) to select a field, or selecting the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif) to select a value from the calendar if the field on the category axis is of Date, DateTime, or Time type.

**Major Unit**

Specifies the unit between two adjacent major tick marks.

* **Auto**  
   If the option is selected, the unit will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the unit as required. If the field on the category axis is of the Date, DateTime or Time type, you can also choose a unit from the drop-down list.

**Minor Unit**

Specifies the unit between two adjacent minor tick marks.

* **Auto**  
   If the option is selected, the unit will be defined by Logi Report automatically.
* **Fixed**  
   If the option is selected, you can define the unit as required. If the field on the category axis is of the Date, DateTime or Time type, you can also choose a unit from the drop-down list.

## Font

The tab consists of two sub tabs: [Major Label](#Majorft) and [Minor Label](#Minorft).

### Major Label

Specifies the font format of the major tick mark labels on the axis.

![Format Category (X) Axis dialog - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404904324759/fmtctgryaxis_font_major.gif)

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

Displays a sample of the specified font and any text effects.

### Minor Label

Specifies the font format of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog - Font - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404904325015/fmtctgryaxis_font_minor.gif)

**Correlate with Major Label**

If the option is selected, the font format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unselected can the font properties of the minor tick mark labels take effect.

**Font**

Specifies the font format of text in the minor tick mark labels.

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

Specifies the special effects of text in the minor tick mark labels.

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

Displays a sample of the specified font and any text effects.

## Orientation

The tab consists of two sub tabs: [Major Label](#Majorlb) and [Minor Label](#Minorlb).

### Major Label

Specifies the rotation angle of the major tick mark labels on the axis.

![Format Category (X) Axis dialog - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404904325271/fmtctgryaxis_orntatn_major.gif)

**Automatic**

Specifies to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is selected by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the major tick mark label text on the axis. When you change the rotation angle in the text box, the red line in the spin box will change correspondingly, and vice versa.

### Minor Label

Specifies the rotation angle of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog - Orientation - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404904325527/fmtctgryaxis_orntatn_minor.gif)

**Correlate with Major Label**

If the option is selected, the orientation setting of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unselected can the orientation properties of the minor tick mark labels take effect.

**Automatic**

Specifies to adjust the rotation angle of the minor tick mark label text on the axis automatically according to the length of the label text, in degrees.

When this option is selected by default:

* If the text can be completely displayed horizontally, the default rotation angle will be 0.
* If the text cannot be completely displayed horizontally, the default rotation angle will be 30 anticlockwise, and the cut off part will be shown as suspension points.

**Angle**

Specifies to customize the rotation angle of the minor tick mark label text on the axis. When you change the rotation angle in the text box, the red line in the spin box will change correspondingly, and vice versa.

## Format

The tab consists of two sub tabs: [Major Label](#Majorfmt) and [Minor Label](#Minorfmt).

### Major Label

Specifies the data format of the major tick mark labels on the axis.

![Format Category (X) Axis dialog - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404904325783/fmtctgryaxis_fmt_major.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Lists all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Enabled when the category field is of the Number data type. It specifies whether to automatically scale the tick mark labels when the label values fall into the two ranges:

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

**Truncate**

Specifies whether to truncate the label text when the text is more than 10 characters.

### Minor Label

Specifies the data format of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog -Format - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404904326039/fmtctgryaxis_fmt_minor.gif)

**Correlate with Major Label**

If the option is selected, the data format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unselected can the format properties of the minor tick mark labels take effect.

**Category**

Lists the category types. Select one to customize its format.

**Format**

Lists all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Enabled when the category field is of the Number data type. It specifies whether to [automatically scale big and small numbers](#AutoScale) in the tick mark labels.

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

The tab is available only when the chart is of the Bar, Bench, Line, or Area type and is created in a web report or library component. It helps you to divide the category values into different range groups and edit data labels for them, and consists of two sub tabs: [Properties](#Properties) and [Data Label](#Datalb).

### Properties

Specifies the properties of the range groups.

![Format Category (X) Axis dialog - Range - Properties](https://devnet.logianalytics.com/hc/article_attachments/4404904326295/fmtctgryaxis_range_prpty.gif)

**Enable Range**

Specifies whether to enable the range function.

* **Special Group**   
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) dialog to define how to group the category values.

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

Specifies the properties of the data labels in the range groups.

![Format Category (X) Axis dialog - Range - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404916801175/fmtctgryaxis_range_dtlb.gif)

**Show Data Labels**

Specifies whether to show data labels for the range groups. Available only when the option Enable Range in the Properties tab is selected and range groups are defined.

* **Edit Data Labels**  
   Opens the [Data Label Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009630481-Data-Label-Editor-Dialog) to edit data labels for the range groups.

**Data Label Type**

Specifies in which way to display the values in the data labels of each range group.

* **value**  
   Shows the value for each group range.
* **percent**  
   Shows the percentage of each group range to the total.
* **value and percent**  
   Shows the value and the percentage for each group range.

**Percent within Group**

Specifies whether to calculate the percent value within each range group or across all range groups. Available only when percent or value and percent is select from the Data Label Type drop-down list.

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

Specifies some web behaviors to the axis. This tab is only available to charts in library components.

![Format Category (X) Axis dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404904326807/fmtctgryaxis_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631321-Format-Bullet-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608402-Format-Category-X-Gridline-Dialog)
