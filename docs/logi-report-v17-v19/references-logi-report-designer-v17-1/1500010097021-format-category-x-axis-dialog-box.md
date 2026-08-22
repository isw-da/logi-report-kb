---
title: "Format Category (X) Axis Dialog Box"
id: 1500010097021
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097021-Format-Category-X-Axis-Dialog-Box
updated_at: 2021-07-23T19:15:27Z
---

# Format Category (X) Axis Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097001-Format-Bullet-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059162-Format-Category-X-Gridline-Dialog-Box)

# Format Category (X) Axis Dialog Box

You can use the Format Category X Axis dialog box to [format the category (X) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094441-Formatting-the-Axes#Category). This topic describes the options in the dialog box.

Designer displays the Format Category X Axis dialog box when you right-click any chart element and select Format Axes > Format Category (X) Axis from the shortcut menu, or double-click the category axis of a chart.

The dialog box contains the following tabs (Designer displays some tabs only to specific chart types only, and the Behaviors tab only when the chart is in a library component):

* [Axis Tab](#Axis)
* [Tick Mark Tab](#Tick)
* [Font Tab](#Font)
* [Orientation Tab](#Orientation)
* [Format Tab](#Format)
* [Range Tab](#Range)
* [Behaviors Tab](#Behaviors)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Axis Tab

Use this tab to specify the general properties of the category axis.

![Format Category (X) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/4404856956951/fmtctgryaxis_axis.gif)

**Option**

You can specify the options for the axis in this box.

* **Show Gridlines**  
  Select to show gridlines on the axis.

  Designer displays the following four options only when the chart is a scatter chart, or a bubble chart which shows different fields on the category axis and the bubble X axis.

* **Minimum Value**  
  Specify the minimum value to display on the axis.
* **Maximum Value**  
  Specify the maximum value to display on the axis.
* **Increment**  
  Specify the distance between two adjacent values on the axis. Available only t
* **Number of Tick Marks**  
  Specify how many tick marks you want to display on the axis.

**Line**

You can specify the line style for the axis in this box.

* **Color**  
  Specify the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Style**  
  Select the line style for the axis.
* **Transparency**  
  Specify the transparency for the color of the axis.
* **Thickness**  
  Specify the thickness for the line of the axis, in pixels.

**Label**

You can specify the properties for the labels on the axis in this box.

* **Label Axis Gap**   
  Specify the distance between the labels and the axis, in pixels.
* **Best Effect**  
  Select to adjust the labels automatically to have them placed in the best way. If you select the option, Designer hides some labels when they overlap.
* **Auto**  
  Select to display the values of the field that you add to the axis as the major tick mark labels. Clear the option if you want to customize the label text.
  + **Label Text**  
    Specify the text of the major tick mark labels on the axis. Select a field from the drop-down list to use its values as the label text or select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848471319/btn_x.gif) to type the label text manually.

## Tick Mark Tab

You see the following sub tabs in the Tick Mark tab:

* [Major Tick Mark Sub Tab](#Majortm)
* [Minor Tick Mark Sub Tab](#Minortm)
* [Scale Sub Tab](#Scale)

### Major Tick Mark Sub Tab

Use this sub tab to specify the properties of the major tick marks on the category axis.

![Format Category (X) Axis dialog box - Tick Mark - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404856957207/fmtctgryaxis_mark_major.gif)

**Type**

You can specify the type of the major tick marks on the axis in this box.

* **None**  
  Select if you do not want to display major tick marks on the axis. It is meaningless to specify all the other major tick mark properties if you select this type.
* **Inside**  
  Select to display the major tick marks inside the axis.
* **Outside**  
  Select to display the major tick marks outside the axis.
* **Cross**  
  Select to display the major tick marks across the axis.

**Line**

You can specify the line properties of the major tick marks on the axis in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the major tick marks. If you clear the option, you can specify the line properties for the major tick marks separately using the following options:
  + **Color**  
    Specify the color of the major tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the major tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the major tick mark line.
  + **Thickness**  
    Specify the thickness of the major tick mark line, in pixels.
* **Tick Mark Length**  
  Specify the length of the major tick marks, in pixels.

**Option**

You can specify the other properties of the major tick mark labels on the axis in this box.

* **Show Major Tick Mark Labels**  
  Select to display the labels of the major tick marks on the axis. Designer enables the other options in the Options box when you select this option.
* **Label Every N Major Tick Marks**  
  Specify the frequency at which to label the major tick marks.
* **Show Axis Label Tips**  
  Select to display the complete label text when the mouse pointer points at a label on the axis.
* **Number of Major Labels**  
  Specify how many major tick mark labels to display on the axis.
  + **Auto**  
    Select to display all the major tick mark labels.
  + **Fixed**  
    Select and specify the number of the major tick mark labels you want to display.

### Minor Tick Mark Sub Tab

Use this sub tab to specify the properties of the minor tick marks on the category axis.

![Format Category (X) Axis dialog box - Tick Mark - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4404848561047/fmtctgryaxis_mark_minor.gif)

**Type**

You can specify the type of the minor tick marks on the axis in this box.

* **None**  
  Select if you do not want to display minor tick marks on the axis. It is meaningless to specify all the other minor tick mark properties if you select this type.
* **Inside**  
  Select to display the minor tick marks inside the axis.
* **Outside**  
  Select to display the minor tick marks outside the axis.
* **Cross**  
  Select to display the minor tick marks across the axis.

**Line**

You can specify the line properties of the minor tick marks on the axis in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the minor tick marks. If you clear the option, you can specify the line properties for the minor tick marks separately using the following options:
  + **Color**  
    Specify the color of the minor tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Style**  
    Select the style of the minor tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the minor tick mark line.
  + **Thickness**  
    Specify the thickness of the minor tick mark line, in pixels.
* **Tick Mark Length**  
  Specify the length of the minor tick marks, in pixels.

**Option**

You can specify the other properties of the minor tick mark labels on the axis in this box.

* **Show Minor Tick Mark Labels**  
  Select to display the labels of the minor tick marks on the axis. Designer enables the other options in the Options box when you select this option.
* **Label Every N Minor Tick Marks**  
  Specify the frequency at which to label the minor tick marks.
* **Number of Minor Labels**  
  Specify how many minor tick mark labels to display on the axis.
  + **Auto**  
    Select to display all the minor tick mark labels.
  + **Fixed**  
    Select and specify the number of the minor tick mark labels you want to display.

### Scale Sub Tab

Use this tab to customizes the way in which to label the major and minor tick marks on the category axis with constant interval. Designer enables the Scale sub tab only when the field on the category axis is one of the following types: Number, Date, Time, and DateTime (for a bubble chart only when the category field is one of the above types and the Bubble X Axis uses the category field), and does not display it for scatter charts.

![Format Category (X) Axis dialog box - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4404848561431/fmtctgryaxis_mark_scale.gif)

**Use Constant Interval**

Select to use a constant interval to label the tick marks. If you select the option, Designer increases the values of the tick marks continually on the axis based on the following properties instead of just using the data values, and ignores the [customized major tick mark labels](#LabelText) in the Axis tab.

**Minimum**

Specify the minimum value to label the tick marks.

* **Auto**  
  Select to let Designer calculate the minimum value automatically.
* **Fixed**  
  Select and specify the minimum value by inputting it in the text box directly, selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to select a field, or selecting the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to select a value from the calendar if the field on the category axis is of Date, Time, or DateTime type.

**Maximum**

Specify the maximum value to label the tick marks.

* **Auto**  
  Select to let Designer calculate the maximum value automatically.
* **Fixed**  
  Select and specify the maximum value by inputting it in the text box directly, selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) to select a field, or selecting ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to select a value from the calendar if the field on the category axis is of Date, Time, or DateTime type.

**Major Unit**

Specify the unit between two adjacent major tick marks.

* **Auto**  
  Select to let Designer define the unit automatically.
* **Fixed**  
  Select and input the unit in the text box. If the field on the category axis is of the Date, Time, or DateTime type, you can also choose a unit from the drop-down list.

**Minor Unit**

Specify the unit between two adjacent minor tick marks.

* **Auto**  
  Select to let Designer define the unit automatically.
* **Fixed**  
  Select and input the unit in the text box. If the field on the category axis is of the Date, Time, or DateTime type, you can also choose a unit from the drop-down list.

## Font Tab

You see the following sub tabs in the Font tab:

* [Major Label Sub Tab](#Majorft)
* [Minor Label Sub Tab](#Minorft)

### Major Label Sub Tab

Use this sub tab to specify the font format of the major tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404848561687/fmtctgryaxis_font_major.gif)

**Font**

You can specify the font format of the text in the major tick mark labels in this box.

* **Font list**  
  The drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects of the text in the major tick mark labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Web Report Studio and JDashboard do not support underlining chart text, therefore, Logi Report Engine ignores this property when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

The box displays a preview sample of your selection.

### Minor Label Sub Tab

Use this sub tab to specify the font format of the minor tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Font - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404856957847/fmtctgryaxis_font_minor.gif)

**Correlate with Major Label**

Select to apply the font properties that you define for the major tick mark labels in the Major Label sub tab to the minor tick mark labels.

**Font**

You can specify the font format of the text in the minor tick mark labels in this box.

* **Font list**  
  The drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects of the text in the minor tick mark labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Web Report Studio and JDashboard do not support underlining chart text, therefore, Logi Report Engine ignores this property when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

The box displays a preview sample of your selection.

## Orientation Tab

You see the following sub tabs in the Orientation tab:

* [Major Label Sub Tab](#Majorlb)
* [Minor Label Sub Tab](#Minorlb)

### Major Label Sub Tab

Use this sub tab to specify the rotation angle of the major tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404856958231/fmtctgryaxis_orntatn_major.gif)

**Automatic**

Select to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees.

**Angle**

Select and specify the rotation angle of the major tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

### Minor Label Sub Tab

Use this sub tab to specify the rotation angle of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog box - Orientation - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404848562199/fmtctgryaxis_orntatn_minor.gif)

**Correlate with Major Label**

Select to apply the rotation angle that you define for the major tick mark label text in the Major Label sub tab to the minor tick mark label text.

**Automatic**

Select to adjust the rotation angle of the minor tick mark label text on the axis automatically according to the length of the label text, in degrees.

**Angle**

Select and specify the rotation angle of the minor tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

You see the following sub tabs in the Format tab:

* [Major Label Sub Tab](#Majorfmt)
* [Minor Label Sub Tab](#Minorfmt)

### Major Label Sub Tab

Use this sub tab to specify the data format of the major tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4404856958487/fmtctgryaxis_fmt_major.gif)

**Category & Format**

The two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

**Properties**

The text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

The box displays a sample for the selected format.

**Stack**

The box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the major tick mark labels.

**Truncate**

Select to truncate the label text that is longer than 10 characters and only show the first 7 characters.

### Minor Label Sub Tab

Use this sub tab to specify the data format of the minor tick mark labels on the category axis.

![Format Category (X) Axis dialog box -Format - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4404848562711/fmtctgryaxis_fmt_minor.gif)

**Correlate with Major Label**

Select to apply the data format that you specify for the major tick mark labels in the Major Label sub tab to the minor tick mark labels.

**Category & Format**

The two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

**Properties**

The text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

The box displays a sample for the selected format.

**Stack**

The box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the minor tick mark labels.

## Range Tab

Designer displays the Range tab only when the chart is of the Bar, Bench, Line, or Area type and its value fields do not contain detail information. You can use it to divide the category values into different range groups and edit data labels for them.

You see the following sub tabs in the Range tab:

* [Properties Sub Tab](#Properties)
* [Data Label Sub Tab](#Datalb)

### Properties Sub Tab

Use this sub tab to specify the properties of the range groups on the category axis.

![Format Category (X) Axis dialog box - Range - Properties](https://devnet.logianalytics.com/hc/article_attachments/4404856958743/fmtctgryaxis_range_prpty.gif)

**Enable Range**

Select to enable the range function.

* **Special Group**   
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define how to group the category values.

**Gridline**

You can specify the style for the range separating lines in this box.

* **Line Color**  
  Specify the color of the range separating lines. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Line Style**  
  Select the style of the range separating lines.
* **Transparency**  
  Specify the transparency for the color of the range separating lines.
* **Thickness**  
  Specify the thickness of the range separating lines, in pixels.

**Fill**

You can specify the fill effects for each range group in this box.

* **Group Name**   
  The column shows the names of the ranges that you have added using the User Defined Group dialog box.
* **Color**  
  The column shows the colors that you specify for the range groups.
* **Transparency**  
  The column shows the transparency that you specify for the color of each range group.

### Data Label Sub Tab

Use this sub tab to specify the properties of the data labels in the range groups on the category axis.

![Format Category (X) Axis dialog box - Range - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404848562967/fmtctgryaxis_range_dtlb.gif)

**Show Data Labels**

Designer enables this option when you select Enable Range and have defined the range groups in the Properties sub tab. You can select it to show data labels for the range groups.

* **Edit Data Labels**  
  Select to open the [Data Label Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058562-Data-Label-Editor-Dialog-Box) to edit data labels for the range groups.

**Data Label Type**

Select in which way to display the values in the data labels of each range group.

* **value**  
  Select to show the value for each group range.
* **percent**  
  Select to show the percentage of each group range to the total.
* **value and percent**  
  Select to show the value and the percentage for each group range.

**Percent within Group**

Designer enables this option when you select "percent" or "value and percent" from the Data Label Type drop-down list. You can select it to calculate the percent value within each range group. When the option is unselected, the calculation is based on all the range groups.

**Alignment**

Select the alignment style for the data labels in each range group: left, center, or right.

**Size**

You can specify the size of the data label area on the range groups in this box.

* **Height**  
  Specify the height of the data label area. It cannot exceed the maximum height.
* **Width**  
  Specify the width of the data label area.
* **Maximum Height**  
  Specify the maximum height of the data label area. It cannot exceed the height of the chart paper.

**Fill**

You can specify the fill effect for the data label area in this box.

* **Color**  
  Specify the color to fill the data label area. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency of the color.

**Border**

You can specify the properties for the border of the data label area in this box.

* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Line Style**  
  Select the line style of the border.
* **Transparency**  
  Specify the transparency for the color of the border.
* **End Caps**  
  Select the ending style of the border line.

+ **butt**  
  Select to end unclosed sub paths and dash segments with no added decoration.
+ **round**  
  Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
+ **square**  
  Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

* **Thickness**  
  Specify the thickness of the border, in pixels.
* **Line Joint**  
  Select the joint style for the border line.

+ **miter**  
  Select to join path segments by extending their outside edges until they meet.
+ **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
+ **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Margin**

You can specify the distance between the edge and the border in this box.

* **Top**  
  Specify the distance between the top edge and the top border.
* **Bottom**  
  Specify the distance between the bottom edge and the bottom border.
* **Left**  
  Specify the distance between the left edge and the left border.
* **Right**  
  Specify the distance between the right edge and the right border.

**Padding**

You can specify the distance between the data labels and the border.

* **Top**  
  Specify the distance between the data labels and the top border.
* **Bottom**  
  Specify the distance between the data labels and the bottom border.
* **Left**  
  Specify the distance between the data labels and the left border.
* **Right**  
  Specify the distance between the data labels and the right border.

## Behaviors Tab

Designer displays the Behaviors tab only when the chart is in a library component. You can use it to specify web behaviors on the category axis of the chart.

![Format Category (X) Axis dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404848563223/fmtctgryaxis_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Down button**

Select to move the specified web behavior lower in the list.

**Events**

The column shows the events that you select to trigger the web actions.

**Actions**

The column shows the actions that you specify for the events to trigger. To bind a web action to an event, select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the action cell and Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box) for you to specify the web action.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097001-Format-Bullet-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059162-Format-Category-X-Gridline-Dialog-Box)
